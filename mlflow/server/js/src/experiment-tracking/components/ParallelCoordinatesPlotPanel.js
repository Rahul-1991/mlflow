import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import ParallelCoordinatesPlotView from './ParallelCoordinatesPlotView';
import { ParallelCoordinatesPlotControls } from './ParallelCoordinatesPlotControls';
import {
  getAllParamKeysByRunUuids,
  getAllMetricKeysByRunUuids,
  getSharedMetricKeysByRunUuids,
} from '../reducers/Reducers';
import _ from 'lodash';
import { CompareRunPlotContainer } from './CompareRunPlotContainer';
import { FormattedMessage } from 'react-intl';

export class ParallelCoordinatesPlotPanel extends React.Component {
  static propTypes = {
    runUuids: PropTypes.arrayOf(PropTypes.string).isRequired,
    // An array of all parameter keys across all runs
    allParamKeys: PropTypes.arrayOf(PropTypes.string).isRequired,
    // An array of all metric keys across all runs
    allMetricKeys: PropTypes.arrayOf(PropTypes.string).isRequired,
    // An array of metric keys for which all runs have values
    sharedMetricKeys: PropTypes.arrayOf(PropTypes.string).isRequired,
    // A subset of allParamKeys where the values, potentially undefined,
    // of the parameters differ between runs
    diffParamKeys: PropTypes.arrayOf(PropTypes.string).isRequired,
  };

  state = {
    // Default to select differing parameters. Sort alphabetically (to match
    // highlighted params in param table), then cap at first 3
    selectedParamKeys: this.props.diffParamKeys.sort().slice(0, 3),
    // Default to select the first metric key.
    // Note that there will be no color scaling if no metric is selected.
    selectedMetricKeys: this.props.sharedMetricKeys.slice(0, 1),
  };

  handleParamsSelectChange = (paramValues) => {
    this.setState({ selectedParamKeys: paramValues });
  };

  handleMetricsSelectChange = (metricValues) => {
    this.setState({ selectedMetricKeys: metricValues });
  };

  onClearAllSelect = () => {
    this.setState({ selectedParamKeys: [], selectedMetricKeys: [] });
  };

  render() {
    const { runUuids, allParamKeys, allMetricKeys } = this.props;
    const { selectedParamKeys, selectedMetricKeys } = this.state;
    return (
      <CompareRunPlotContainer
        controls={
          <ParallelCoordinatesPlotControls
            paramKeys={allParamKeys}
            metricKeys={allMetricKeys}
            selectedParamKeys={selectedParamKeys}
            selectedMetricKeys={selectedMetricKeys}
            handleMetricsSelectChange={this.handleMetricsSelectChange}
            handleParamsSelectChange={this.handleParamsSelectChange}
            onClearAllSelect={this.onClearAllSelect}
          />
        }
      >
        {!_.isEmpty(selectedParamKeys) || !_.isEmpty(selectedMetricKeys) ? (
          <ParallelCoordinatesPlotView
            runUuids={runUuids}
            paramKeys={selectedParamKeys}
            metricKeys={selectedMetricKeys}
          />
        ) : (
          <div css={styles.noValuesSelected} data-testid='no-values-selected'>
            <h2>
              <FormattedMessage
                defaultMessage='Nothing to compare!'
                // eslint-disable-next-line max-len
                description='Header displayed in the metrics and params compare plot when no values are selected'
              />
            </h2>
            <FormattedMessage
              defaultMessage='Please select parameters and/or metrics to display the comparison.'
              // eslint-disable-next-line max-len
              description='Explanation displayed in the metrics and params compare plot when no values are selected'
            />
          </div>
        )}
      </CompareRunPlotContainer>
    );
  }
}

export const getDiffParams = (allParamKeys, runUuids, paramsByRunUuid) => {
  const diffParamKeys = [];
  allParamKeys.forEach((param) => {
    // collect all values for this param
    const paramVals = runUuids.map(
      (runUuid) => paramsByRunUuid[runUuid][param] && paramsByRunUuid[runUuid][param].value,
    );
    if (!paramVals.every((x, i, arr) => x === arr[0])) diffParamKeys.push(param);
  });
  return diffParamKeys;
};

const mapStateToProps = (state, ownProps) => {
  const { runUuids } = ownProps;
  const allParamKeys = getAllParamKeysByRunUuids(runUuids, state);
  const allMetricKeys = getAllMetricKeysByRunUuids(runUuids, state);
  const sharedMetricKeys = getSharedMetricKeysByRunUuids(runUuids, state);
  const { paramsByRunUuid } = state.entities;
  const diffParamKeys = getDiffParams(allParamKeys, runUuids, paramsByRunUuid);

  return {
    allParamKeys,
    allMetricKeys,
    sharedMetricKeys,
    diffParamKeys,
  };
};

const styles = {
  noValuesSelected: (theme) => ({
    padding: theme.spacing.md,
    textAlign: 'center',
  }),
};

export default connect(mapStateToProps)(ParallelCoordinatesPlotPanel);
