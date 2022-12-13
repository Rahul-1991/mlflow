# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2
from . import databricks_pb2 as databricks__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rservice.proto\x12\x06mlflow\x1a\x15scalapb/scalapb.proto\x1a\x10\x64\x61tabricks.proto\"H\n\x06Metric\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01\x12\x11\n\ttimestamp\x18\x03 \x01(\x03\x12\x0f\n\x04step\x18\x04 \x01(\x03:\x01\x30\"#\n\x05Param\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"C\n\x03Run\x12\x1d\n\x04info\x18\x01 \x01(\x0b\x32\x0f.mlflow.RunInfo\x12\x1d\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x0f.mlflow.RunData\"g\n\x07RunData\x12\x1f\n\x07metrics\x18\x01 \x03(\x0b\x32\x0e.mlflow.Metric\x12\x1d\n\x06params\x18\x02 \x03(\x0b\x32\r.mlflow.Param\x12\x1c\n\x04tags\x18\x03 \x03(\x0b\x32\x0e.mlflow.RunTag\"$\n\x06RunTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"+\n\rExperimentTag\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xdd\x01\n\x07RunInfo\x12\x0e\n\x06run_id\x18\x0f \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x10\n\x08run_name\x18\x03 \x01(\t\x12\x15\n\rexperiment_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x06 \x01(\t\x12!\n\x06status\x18\x07 \x01(\x0e\x32\x11.mlflow.RunStatus\x12\x12\n\nstart_time\x18\x08 \x01(\x03\x12\x10\n\x08\x65nd_time\x18\t \x01(\x03\x12\x14\n\x0c\x61rtifact_uri\x18\r \x01(\t\x12\x17\n\x0flifecycle_stage\x18\x0e \x01(\t\"\xbb\x01\n\nExperiment\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x19\n\x11\x61rtifact_location\x18\x03 \x01(\t\x12\x17\n\x0flifecycle_stage\x18\x04 \x01(\t\x12\x18\n\x10last_update_time\x18\x05 \x01(\x03\x12\x15\n\rcreation_time\x18\x06 \x01(\x03\x12#\n\x04tags\x18\x07 \x03(\x0b\x32\x15.mlflow.ExperimentTag\"\xb6\x01\n\x10\x43reateExperiment\x12\x12\n\x04name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x19\n\x11\x61rtifact_location\x18\x02 \x01(\t\x12#\n\x04tags\x18\x03 \x03(\x0b\x32\x15.mlflow.ExperimentTag\x1a!\n\x08Response\x12\x15\n\rexperiment_id\x18\x01 \x01(\t:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xfe\x01\n\x11SearchExperiments\x12\x13\n\x0bmax_results\x18\x01 \x01(\x03\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x0e\n\x06\x66ilter\x18\x03 \x01(\t\x12\x10\n\x08order_by\x18\x04 \x03(\t\x12#\n\tview_type\x18\x05 \x01(\x0e\x32\x10.mlflow.ViewType\x1aL\n\x08Response\x12\'\n\x0b\x65xperiments\x18\x01 \x03(\x0b\x32\x12.mlflow.Experiment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x8d\x01\n\rGetExperiment\x12\x1b\n\rexperiment_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\x32\n\x08Response\x12&\n\nexperiment\x18\x01 \x01(\x0b\x32\x12.mlflow.Experiment:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"h\n\x10\x44\x65leteExperiment\x12\x1b\n\rexperiment_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"i\n\x11RestoreExperiment\x12\x1b\n\rexperiment_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"z\n\x10UpdateExperiment\x12\x1b\n\rexperiment_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x10\n\x08new_name\x18\x02 \x01(\t\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xca\x01\n\tCreateRun\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x10\n\x08run_name\x18\x03 \x01(\t\x12\x12\n\nstart_time\x18\x07 \x01(\x03\x12\x1c\n\x04tags\x18\t \x03(\x0b\x32\x0e.mlflow.RunTag\x1a$\n\x08Response\x12\x18\n\x03run\x18\x01 \x01(\x0b\x32\x0b.mlflow.Run:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xd0\x01\n\tUpdateRun\x12\x0e\n\x06run_id\x18\x04 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12!\n\x06status\x18\x02 \x01(\x0e\x32\x11.mlflow.RunStatus\x12\x10\n\x08\x65nd_time\x18\x03 \x01(\x03\x12\x10\n\x08run_name\x18\x05 \x01(\t\x1a-\n\x08Response\x12!\n\x08run_info\x18\x01 \x01(\x0b\x32\x0f.mlflow.RunInfo:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"Z\n\tDeleteRun\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"[\n\nRestoreRun\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xb8\x01\n\tLogMetric\x12\x0e\n\x06run_id\x18\x06 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x11\n\x03key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05value\x18\x03 \x01(\x01\x42\x04\xf8\x86\x19\x01\x12\x17\n\ttimestamp\x18\x04 \x01(\x03\x42\x04\xf8\x86\x19\x01\x12\x0f\n\x04step\x18\x05 \x01(\x03:\x01\x30\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x8d\x01\n\x08LogParam\x12\x0e\n\x06run_id\x18\x04 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x11\n\x03key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05value\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x90\x01\n\x10SetExperimentTag\x12\x1b\n\rexperiment_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x11\n\x03key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05value\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x8b\x01\n\x06SetTag\x12\x0e\n\x06run_id\x18\x04 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x11\n\x03key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x12\x13\n\x05value\x18\x03 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"m\n\tDeleteTag\x12\x14\n\x06run_id\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x11\n\x03key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"}\n\x06GetRun\x12\x0e\n\x06run_id\x18\x02 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x1a$\n\x08Response\x12\x18\n\x03run\x18\x01 \x01(\x0b\x32\x0b.mlflow.Run:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x98\x02\n\nSearchRuns\x12\x16\n\x0e\x65xperiment_ids\x18\x01 \x03(\t\x12\x0e\n\x06\x66ilter\x18\x04 \x01(\t\x12\x34\n\rrun_view_type\x18\x03 \x01(\x0e\x32\x10.mlflow.ViewType:\x0b\x41\x43TIVE_ONLY\x12\x19\n\x0bmax_results\x18\x05 \x01(\x05:\x04\x31\x30\x30\x30\x12\x10\n\x08order_by\x18\x06 \x03(\t\x12\x12\n\npage_token\x18\x07 \x01(\t\x1a>\n\x08Response\x12\x19\n\x04runs\x18\x01 \x03(\x0b\x32\x0b.mlflow.Run\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xd8\x01\n\rListArtifacts\x12\x0e\n\x06run_id\x18\x03 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x0c\n\x04path\x18\x02 \x01(\t\x12\x12\n\npage_token\x18\x04 \x01(\t\x1aV\n\x08Response\x12\x10\n\x08root_uri\x18\x01 \x01(\t\x12\x1f\n\x05\x66iles\x18\x02 \x03(\x0b\x32\x10.mlflow.FileInfo\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\";\n\x08\x46ileInfo\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0e\n\x06is_dir\x18\x02 \x01(\x08\x12\x11\n\tfile_size\x18\x03 \x01(\x03\"\xa8\x01\n\x10GetMetricHistory\x12\x0e\n\x06run_id\x18\x03 \x01(\t\x12\x10\n\x08run_uuid\x18\x01 \x01(\t\x12\x18\n\nmetric_key\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x1a+\n\x08Response\x12\x1f\n\x07metrics\x18\x01 \x03(\x0b\x32\x0e.mlflow.Metric:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\xb1\x01\n\x08LogBatch\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x1f\n\x07metrics\x18\x02 \x03(\x0b\x32\x0e.mlflow.Metric\x12\x1d\n\x06params\x18\x03 \x03(\x0b\x32\r.mlflow.Param\x12\x1c\n\x04tags\x18\x04 \x03(\x0b\x32\x0e.mlflow.RunTag\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"g\n\x08LogModel\x12\x0e\n\x06run_id\x18\x01 \x01(\t\x12\x12\n\nmodel_json\x18\x02 \x01(\t\x1a\n\n\x08Response:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x95\x01\n\x13GetExperimentByName\x12\x1d\n\x0f\x65xperiment_name\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x1a\x32\n\x08Response\x12&\n\nexperiment\x18\x01 \x01(\x0b\x32\x12.mlflow.Experiment:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]\"\x8a\x01\n\x0cGetAuthToken\x12\x16\n\x08username\x18\x01 \x01(\tB\x04\xf8\x86\x19\x01\x12\x16\n\x08password\x18\x02 \x01(\tB\x04\xf8\x86\x19\x01\x1a\x1d\n\x08Response\x12\x11\n\tjwt_token\x18\x01 \x01(\t:+\xe2?(\n&com.databricks.rpc.RPC[$this.Response]*6\n\x08ViewType\x12\x0f\n\x0b\x41\x43TIVE_ONLY\x10\x01\x12\x10\n\x0c\x44\x45LETED_ONLY\x10\x02\x12\x07\n\x03\x41LL\x10\x03*I\n\nSourceType\x12\x0c\n\x08NOTEBOOK\x10\x01\x12\x07\n\x03JOB\x10\x02\x12\x0b\n\x07PROJECT\x10\x03\x12\t\n\x05LOCAL\x10\x04\x12\x0c\n\x07UNKNOWN\x10\xe8\x07*M\n\tRunStatus\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSCHEDULED\x10\x02\x12\x0c\n\x08\x46INISHED\x10\x03\x12\n\n\x06\x46\x41ILED\x10\x04\x12\n\n\x06KILLED\x10\x05\x32\xfa\x17\n\rMlflowService\x12\xa6\x01\n\x13getExperimentByName\x12\x1b.mlflow.GetExperimentByName\x1a$.mlflow.GetExperimentByName.Response\"L\xf2\x86\x19H\n,\n\x03GET\x12\x1f/mlflow/experiments/get-by-name\x1a\x04\x08\x02\x10\x00\x10\x01*\x16Get Experiment By Name\x12\x94\x01\n\x10\x63reateExperiment\x12\x18.mlflow.CreateExperiment\x1a!.mlflow.CreateExperiment.Response\"C\xf2\x86\x19?\n(\n\x04POST\x12\x1a/mlflow/experiments/create\x1a\x04\x08\x02\x10\x00\x10\x01*\x11\x43reate Experiment\x12\xc1\x01\n\x11searchExperiments\x12\x19.mlflow.SearchExperiments\x1a\".mlflow.SearchExperiments.Response\"m\xf2\x86\x19i\n(\n\x04POST\x12\x1a/mlflow/experiments/search\x1a\x04\x08\x02\x10\x00\n\'\n\x03GET\x12\x1a/mlflow/experiments/search\x1a\x04\x08\x02\x10\x00\x10\x01*\x12Search Experiments\x12\x84\x01\n\rgetExperiment\x12\x15.mlflow.GetExperiment\x1a\x1e.mlflow.GetExperiment.Response\"<\xf2\x86\x19\x38\n$\n\x03GET\x12\x17/mlflow/experiments/get\x1a\x04\x08\x02\x10\x00\x10\x01*\x0eGet Experiment\x12\x94\x01\n\x10\x64\x65leteExperiment\x12\x18.mlflow.DeleteExperiment\x1a!.mlflow.DeleteExperiment.Response\"C\xf2\x86\x19?\n(\n\x04POST\x12\x1a/mlflow/experiments/delete\x1a\x04\x08\x02\x10\x00\x10\x01*\x11\x44\x65lete Experiment\x12\x99\x01\n\x11restoreExperiment\x12\x19.mlflow.RestoreExperiment\x1a\".mlflow.RestoreExperiment.Response\"E\xf2\x86\x19\x41\n)\n\x04POST\x12\x1b/mlflow/experiments/restore\x1a\x04\x08\x02\x10\x00\x10\x01*\x12Restore Experiment\x12\x94\x01\n\x10updateExperiment\x12\x18.mlflow.UpdateExperiment\x1a!.mlflow.UpdateExperiment.Response\"C\xf2\x86\x19?\n(\n\x04POST\x12\x1a/mlflow/experiments/update\x1a\x04\x08\x02\x10\x00\x10\x01*\x11Update Experiment\x12q\n\tcreateRun\x12\x11.mlflow.CreateRun\x1a\x1a.mlflow.CreateRun.Response\"5\xf2\x86\x19\x31\n!\n\x04POST\x12\x13/mlflow/runs/create\x1a\x04\x08\x02\x10\x00\x10\x01*\nCreate Run\x12q\n\tupdateRun\x12\x11.mlflow.UpdateRun\x1a\x1a.mlflow.UpdateRun.Response\"5\xf2\x86\x19\x31\n!\n\x04POST\x12\x13/mlflow/runs/update\x1a\x04\x08\x02\x10\x00\x10\x01*\nUpdate Run\x12q\n\tdeleteRun\x12\x11.mlflow.DeleteRun\x1a\x1a.mlflow.DeleteRun.Response\"5\xf2\x86\x19\x31\n!\n\x04POST\x12\x13/mlflow/runs/delete\x1a\x04\x08\x02\x10\x00\x10\x01*\nDelete Run\x12v\n\nrestoreRun\x12\x12.mlflow.RestoreRun\x1a\x1b.mlflow.RestoreRun.Response\"7\xf2\x86\x19\x33\n\"\n\x04POST\x12\x14/mlflow/runs/restore\x1a\x04\x08\x02\x10\x00\x10\x01*\x0bRestore Run\x12u\n\tlogMetric\x12\x11.mlflow.LogMetric\x1a\x1a.mlflow.LogMetric.Response\"9\xf2\x86\x19\x35\n%\n\x04POST\x12\x17/mlflow/runs/log-metric\x1a\x04\x08\x02\x10\x00\x10\x01*\nLog Metric\x12t\n\x08logParam\x12\x10.mlflow.LogParam\x1a\x19.mlflow.LogParam.Response\";\xf2\x86\x19\x37\n(\n\x04POST\x12\x1a/mlflow/runs/log-parameter\x1a\x04\x08\x02\x10\x00\x10\x01*\tLog Param\x12\xa1\x01\n\x10setExperimentTag\x12\x18.mlflow.SetExperimentTag\x1a!.mlflow.SetExperimentTag.Response\"P\xf2\x86\x19L\n4\n\x04POST\x12&/mlflow/experiments/set-experiment-tag\x1a\x04\x08\x02\x10\x00\x10\x01*\x12Set Experiment Tag\x12\x66\n\x06setTag\x12\x0e.mlflow.SetTag\x1a\x17.mlflow.SetTag.Response\"3\xf2\x86\x19/\n\"\n\x04POST\x12\x14/mlflow/runs/set-tag\x1a\x04\x08\x02\x10\x00\x10\x01*\x07Set Tag\x12u\n\tdeleteTag\x12\x11.mlflow.DeleteTag\x1a\x1a.mlflow.DeleteTag.Response\"9\xf2\x86\x19\x35\n%\n\x04POST\x12\x17/mlflow/runs/delete-tag\x1a\x04\x08\x02\x10\x00\x10\x01*\nDelete Tag\x12\x61\n\x06getRun\x12\x0e.mlflow.GetRun\x1a\x17.mlflow.GetRun.Response\".\xf2\x86\x19*\n\x1d\n\x03GET\x12\x10/mlflow/runs/get\x1a\x04\x08\x02\x10\x00\x10\x01*\x07Get Run\x12u\n\nsearchRuns\x12\x12.mlflow.SearchRuns\x1a\x1b.mlflow.SearchRuns.Response\"6\xf2\x86\x19\x32\n!\n\x04POST\x12\x13/mlflow/runs/search\x1a\x04\x08\x02\x10\x00\x10\x01*\x0bSearch Runs\x12\x83\x01\n\rlistArtifacts\x12\x15.mlflow.ListArtifacts\x1a\x1e.mlflow.ListArtifacts.Response\";\xf2\x86\x19\x37\n#\n\x03GET\x12\x16/mlflow/artifacts/list\x1a\x04\x08\x02\x10\x00\x10\x01*\x0eList Artifacts\x12\x95\x01\n\x10getMetricHistory\x12\x18.mlflow.GetMetricHistory\x1a!.mlflow.GetMetricHistory.Response\"D\xf2\x86\x19@\n(\n\x03GET\x12\x1b/mlflow/metrics/get-history\x1a\x04\x08\x02\x10\x00\x10\x01*\x12Get Metric History\x12p\n\x08logBatch\x12\x10.mlflow.LogBatch\x1a\x19.mlflow.LogBatch.Response\"7\xf2\x86\x19\x33\n$\n\x04POST\x12\x16/mlflow/runs/log-batch\x1a\x04\x08\x02\x10\x00\x10\x01*\tLog Batch\x12p\n\x08logModel\x12\x10.mlflow.LogModel\x1a\x19.mlflow.LogModel.Response\"7\xf2\x86\x19\x33\n$\n\x04POST\x12\x16/mlflow/runs/log-model\x1a\x04\x08\x02\x10\x00\x10\x01*\tLog Model\x12w\n\x0cgetAuthToken\x12\x14.mlflow.GetAuthToken\x1a\x1d.mlflow.GetAuthToken.Response\"2\xf2\x86\x19.\n\x1a\n\x04POST\x12\x0c/mlflow/auth\x1a\x04\x08\x02\x10\x00\x10\x01*\x0eGet Auth TokenB\x1e\n\x14org.mlflow.api.proto\x90\x01\x01\xe2?\x02\x10\x01')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\024org.mlflow.api.proto\220\001\001\342?\002\020\001'
  _CREATEEXPERIMENT.fields_by_name['name']._options = None
  _CREATEEXPERIMENT.fields_by_name['name']._serialized_options = b'\370\206\031\001'
  _CREATEEXPERIMENT._options = None
  _CREATEEXPERIMENT._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _SEARCHEXPERIMENTS._options = None
  _SEARCHEXPERIMENTS._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _GETEXPERIMENT.fields_by_name['experiment_id']._options = None
  _GETEXPERIMENT.fields_by_name['experiment_id']._serialized_options = b'\370\206\031\001'
  _GETEXPERIMENT._options = None
  _GETEXPERIMENT._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _DELETEEXPERIMENT.fields_by_name['experiment_id']._options = None
  _DELETEEXPERIMENT.fields_by_name['experiment_id']._serialized_options = b'\370\206\031\001'
  _DELETEEXPERIMENT._options = None
  _DELETEEXPERIMENT._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _RESTOREEXPERIMENT.fields_by_name['experiment_id']._options = None
  _RESTOREEXPERIMENT.fields_by_name['experiment_id']._serialized_options = b'\370\206\031\001'
  _RESTOREEXPERIMENT._options = None
  _RESTOREEXPERIMENT._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _UPDATEEXPERIMENT.fields_by_name['experiment_id']._options = None
  _UPDATEEXPERIMENT.fields_by_name['experiment_id']._serialized_options = b'\370\206\031\001'
  _UPDATEEXPERIMENT._options = None
  _UPDATEEXPERIMENT._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _CREATERUN._options = None
  _CREATERUN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _UPDATERUN._options = None
  _UPDATERUN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _DELETERUN.fields_by_name['run_id']._options = None
  _DELETERUN.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _DELETERUN._options = None
  _DELETERUN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _RESTORERUN.fields_by_name['run_id']._options = None
  _RESTORERUN.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _RESTORERUN._options = None
  _RESTORERUN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _LOGMETRIC.fields_by_name['key']._options = None
  _LOGMETRIC.fields_by_name['key']._serialized_options = b'\370\206\031\001'
  _LOGMETRIC.fields_by_name['value']._options = None
  _LOGMETRIC.fields_by_name['value']._serialized_options = b'\370\206\031\001'
  _LOGMETRIC.fields_by_name['timestamp']._options = None
  _LOGMETRIC.fields_by_name['timestamp']._serialized_options = b'\370\206\031\001'
  _LOGMETRIC._options = None
  _LOGMETRIC._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _LOGPARAM.fields_by_name['key']._options = None
  _LOGPARAM.fields_by_name['key']._serialized_options = b'\370\206\031\001'
  _LOGPARAM.fields_by_name['value']._options = None
  _LOGPARAM.fields_by_name['value']._serialized_options = b'\370\206\031\001'
  _LOGPARAM._options = None
  _LOGPARAM._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _SETEXPERIMENTTAG.fields_by_name['experiment_id']._options = None
  _SETEXPERIMENTTAG.fields_by_name['experiment_id']._serialized_options = b'\370\206\031\001'
  _SETEXPERIMENTTAG.fields_by_name['key']._options = None
  _SETEXPERIMENTTAG.fields_by_name['key']._serialized_options = b'\370\206\031\001'
  _SETEXPERIMENTTAG.fields_by_name['value']._options = None
  _SETEXPERIMENTTAG.fields_by_name['value']._serialized_options = b'\370\206\031\001'
  _SETEXPERIMENTTAG._options = None
  _SETEXPERIMENTTAG._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _SETTAG.fields_by_name['key']._options = None
  _SETTAG.fields_by_name['key']._serialized_options = b'\370\206\031\001'
  _SETTAG.fields_by_name['value']._options = None
  _SETTAG.fields_by_name['value']._serialized_options = b'\370\206\031\001'
  _SETTAG._options = None
  _SETTAG._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _DELETETAG.fields_by_name['run_id']._options = None
  _DELETETAG.fields_by_name['run_id']._serialized_options = b'\370\206\031\001'
  _DELETETAG.fields_by_name['key']._options = None
  _DELETETAG.fields_by_name['key']._serialized_options = b'\370\206\031\001'
  _DELETETAG._options = None
  _DELETETAG._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _GETRUN._options = None
  _GETRUN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _SEARCHRUNS._options = None
  _SEARCHRUNS._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _LISTARTIFACTS._options = None
  _LISTARTIFACTS._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _GETMETRICHISTORY.fields_by_name['metric_key']._options = None
  _GETMETRICHISTORY.fields_by_name['metric_key']._serialized_options = b'\370\206\031\001'
  _GETMETRICHISTORY._options = None
  _GETMETRICHISTORY._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _LOGBATCH._options = None
  _LOGBATCH._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _LOGMODEL._options = None
  _LOGMODEL._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _GETEXPERIMENTBYNAME.fields_by_name['experiment_name']._options = None
  _GETEXPERIMENTBYNAME.fields_by_name['experiment_name']._serialized_options = b'\370\206\031\001'
  _GETEXPERIMENTBYNAME._options = None
  _GETEXPERIMENTBYNAME._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _GETAUTHTOKEN.fields_by_name['username']._options = None
  _GETAUTHTOKEN.fields_by_name['username']._serialized_options = b'\370\206\031\001'
  _GETAUTHTOKEN.fields_by_name['password']._options = None
  _GETAUTHTOKEN.fields_by_name['password']._serialized_options = b'\370\206\031\001'
  _GETAUTHTOKEN._options = None
  _GETAUTHTOKEN._serialized_options = b'\342?(\n&com.databricks.rpc.RPC[$this.Response]'
  _MLFLOWSERVICE.methods_by_name['getExperimentByName']._options = None
  _MLFLOWSERVICE.methods_by_name['getExperimentByName']._serialized_options = b'\362\206\031H\n,\n\003GET\022\037/mlflow/experiments/get-by-name\032\004\010\002\020\000\020\001*\026Get Experiment By Name'
  _MLFLOWSERVICE.methods_by_name['createExperiment']._options = None
  _MLFLOWSERVICE.methods_by_name['createExperiment']._serialized_options = b'\362\206\031?\n(\n\004POST\022\032/mlflow/experiments/create\032\004\010\002\020\000\020\001*\021Create Experiment'
  _MLFLOWSERVICE.methods_by_name['searchExperiments']._options = None
  _MLFLOWSERVICE.methods_by_name['searchExperiments']._serialized_options = b'\362\206\031i\n(\n\004POST\022\032/mlflow/experiments/search\032\004\010\002\020\000\n\'\n\003GET\022\032/mlflow/experiments/search\032\004\010\002\020\000\020\001*\022Search Experiments'
  _MLFLOWSERVICE.methods_by_name['getExperiment']._options = None
  _MLFLOWSERVICE.methods_by_name['getExperiment']._serialized_options = b'\362\206\0318\n$\n\003GET\022\027/mlflow/experiments/get\032\004\010\002\020\000\020\001*\016Get Experiment'
  _MLFLOWSERVICE.methods_by_name['deleteExperiment']._options = None
  _MLFLOWSERVICE.methods_by_name['deleteExperiment']._serialized_options = b'\362\206\031?\n(\n\004POST\022\032/mlflow/experiments/delete\032\004\010\002\020\000\020\001*\021Delete Experiment'
  _MLFLOWSERVICE.methods_by_name['restoreExperiment']._options = None
  _MLFLOWSERVICE.methods_by_name['restoreExperiment']._serialized_options = b'\362\206\031A\n)\n\004POST\022\033/mlflow/experiments/restore\032\004\010\002\020\000\020\001*\022Restore Experiment'
  _MLFLOWSERVICE.methods_by_name['updateExperiment']._options = None
  _MLFLOWSERVICE.methods_by_name['updateExperiment']._serialized_options = b'\362\206\031?\n(\n\004POST\022\032/mlflow/experiments/update\032\004\010\002\020\000\020\001*\021Update Experiment'
  _MLFLOWSERVICE.methods_by_name['createRun']._options = None
  _MLFLOWSERVICE.methods_by_name['createRun']._serialized_options = b'\362\206\0311\n!\n\004POST\022\023/mlflow/runs/create\032\004\010\002\020\000\020\001*\nCreate Run'
  _MLFLOWSERVICE.methods_by_name['updateRun']._options = None
  _MLFLOWSERVICE.methods_by_name['updateRun']._serialized_options = b'\362\206\0311\n!\n\004POST\022\023/mlflow/runs/update\032\004\010\002\020\000\020\001*\nUpdate Run'
  _MLFLOWSERVICE.methods_by_name['deleteRun']._options = None
  _MLFLOWSERVICE.methods_by_name['deleteRun']._serialized_options = b'\362\206\0311\n!\n\004POST\022\023/mlflow/runs/delete\032\004\010\002\020\000\020\001*\nDelete Run'
  _MLFLOWSERVICE.methods_by_name['restoreRun']._options = None
  _MLFLOWSERVICE.methods_by_name['restoreRun']._serialized_options = b'\362\206\0313\n\"\n\004POST\022\024/mlflow/runs/restore\032\004\010\002\020\000\020\001*\013Restore Run'
  _MLFLOWSERVICE.methods_by_name['logMetric']._options = None
  _MLFLOWSERVICE.methods_by_name['logMetric']._serialized_options = b'\362\206\0315\n%\n\004POST\022\027/mlflow/runs/log-metric\032\004\010\002\020\000\020\001*\nLog Metric'
  _MLFLOWSERVICE.methods_by_name['logParam']._options = None
  _MLFLOWSERVICE.methods_by_name['logParam']._serialized_options = b'\362\206\0317\n(\n\004POST\022\032/mlflow/runs/log-parameter\032\004\010\002\020\000\020\001*\tLog Param'
  _MLFLOWSERVICE.methods_by_name['setExperimentTag']._options = None
  _MLFLOWSERVICE.methods_by_name['setExperimentTag']._serialized_options = b'\362\206\031L\n4\n\004POST\022&/mlflow/experiments/set-experiment-tag\032\004\010\002\020\000\020\001*\022Set Experiment Tag'
  _MLFLOWSERVICE.methods_by_name['setTag']._options = None
  _MLFLOWSERVICE.methods_by_name['setTag']._serialized_options = b'\362\206\031/\n\"\n\004POST\022\024/mlflow/runs/set-tag\032\004\010\002\020\000\020\001*\007Set Tag'
  _MLFLOWSERVICE.methods_by_name['deleteTag']._options = None
  _MLFLOWSERVICE.methods_by_name['deleteTag']._serialized_options = b'\362\206\0315\n%\n\004POST\022\027/mlflow/runs/delete-tag\032\004\010\002\020\000\020\001*\nDelete Tag'
  _MLFLOWSERVICE.methods_by_name['getRun']._options = None
  _MLFLOWSERVICE.methods_by_name['getRun']._serialized_options = b'\362\206\031*\n\035\n\003GET\022\020/mlflow/runs/get\032\004\010\002\020\000\020\001*\007Get Run'
  _MLFLOWSERVICE.methods_by_name['searchRuns']._options = None
  _MLFLOWSERVICE.methods_by_name['searchRuns']._serialized_options = b'\362\206\0312\n!\n\004POST\022\023/mlflow/runs/search\032\004\010\002\020\000\020\001*\013Search Runs'
  _MLFLOWSERVICE.methods_by_name['listArtifacts']._options = None
  _MLFLOWSERVICE.methods_by_name['listArtifacts']._serialized_options = b'\362\206\0317\n#\n\003GET\022\026/mlflow/artifacts/list\032\004\010\002\020\000\020\001*\016List Artifacts'
  _MLFLOWSERVICE.methods_by_name['getMetricHistory']._options = None
  _MLFLOWSERVICE.methods_by_name['getMetricHistory']._serialized_options = b'\362\206\031@\n(\n\003GET\022\033/mlflow/metrics/get-history\032\004\010\002\020\000\020\001*\022Get Metric History'
  _MLFLOWSERVICE.methods_by_name['logBatch']._options = None
  _MLFLOWSERVICE.methods_by_name['logBatch']._serialized_options = b'\362\206\0313\n$\n\004POST\022\026/mlflow/runs/log-batch\032\004\010\002\020\000\020\001*\tLog Batch'
  _MLFLOWSERVICE.methods_by_name['logModel']._options = None
  _MLFLOWSERVICE.methods_by_name['logModel']._serialized_options = b'\362\206\0313\n$\n\004POST\022\026/mlflow/runs/log-model\032\004\010\002\020\000\020\001*\tLog Model'
  _MLFLOWSERVICE.methods_by_name['getAuthToken']._options = None
  _MLFLOWSERVICE.methods_by_name['getAuthToken']._serialized_options = b'\362\206\031.\n\032\n\004POST\022\014/mlflow/auth\032\004\010\002\020\000\020\001*\016Get Auth Token'
  _VIEWTYPE._serialized_start=4542
  _VIEWTYPE._serialized_end=4596
  _SOURCETYPE._serialized_start=4598
  _SOURCETYPE._serialized_end=4671
  _RUNSTATUS._serialized_start=4673
  _RUNSTATUS._serialized_end=4750
  _METRIC._serialized_start=66
  _METRIC._serialized_end=138
  _PARAM._serialized_start=140
  _PARAM._serialized_end=175
  _RUN._serialized_start=177
  _RUN._serialized_end=244
  _RUNDATA._serialized_start=246
  _RUNDATA._serialized_end=349
  _RUNTAG._serialized_start=351
  _RUNTAG._serialized_end=387
  _EXPERIMENTTAG._serialized_start=389
  _EXPERIMENTTAG._serialized_end=432
  _RUNINFO._serialized_start=435
  _RUNINFO._serialized_end=656
  _EXPERIMENT._serialized_start=659
  _EXPERIMENT._serialized_end=846
  _CREATEEXPERIMENT._serialized_start=849
  _CREATEEXPERIMENT._serialized_end=1031
  _CREATEEXPERIMENT_RESPONSE._serialized_start=953
  _CREATEEXPERIMENT_RESPONSE._serialized_end=986
  _SEARCHEXPERIMENTS._serialized_start=1034
  _SEARCHEXPERIMENTS._serialized_end=1288
  _SEARCHEXPERIMENTS_RESPONSE._serialized_start=1167
  _SEARCHEXPERIMENTS_RESPONSE._serialized_end=1243
  _GETEXPERIMENT._serialized_start=1291
  _GETEXPERIMENT._serialized_end=1432
  _GETEXPERIMENT_RESPONSE._serialized_start=1337
  _GETEXPERIMENT_RESPONSE._serialized_end=1387
  _DELETEEXPERIMENT._serialized_start=1434
  _DELETEEXPERIMENT._serialized_end=1538
  _DELETEEXPERIMENT_RESPONSE._serialized_start=953
  _DELETEEXPERIMENT_RESPONSE._serialized_end=963
  _RESTOREEXPERIMENT._serialized_start=1540
  _RESTOREEXPERIMENT._serialized_end=1645
  _RESTOREEXPERIMENT_RESPONSE._serialized_start=953
  _RESTOREEXPERIMENT_RESPONSE._serialized_end=963
  _UPDATEEXPERIMENT._serialized_start=1647
  _UPDATEEXPERIMENT._serialized_end=1769
  _UPDATEEXPERIMENT_RESPONSE._serialized_start=953
  _UPDATEEXPERIMENT_RESPONSE._serialized_end=963
  _CREATERUN._serialized_start=1772
  _CREATERUN._serialized_end=1974
  _CREATERUN_RESPONSE._serialized_start=1893
  _CREATERUN_RESPONSE._serialized_end=1929
  _UPDATERUN._serialized_start=1977
  _UPDATERUN._serialized_end=2185
  _UPDATERUN_RESPONSE._serialized_start=2095
  _UPDATERUN_RESPONSE._serialized_end=2140
  _DELETERUN._serialized_start=2187
  _DELETERUN._serialized_end=2277
  _DELETERUN_RESPONSE._serialized_start=953
  _DELETERUN_RESPONSE._serialized_end=963
  _RESTORERUN._serialized_start=2279
  _RESTORERUN._serialized_end=2370
  _RESTORERUN_RESPONSE._serialized_start=953
  _RESTORERUN_RESPONSE._serialized_end=963
  _LOGMETRIC._serialized_start=2373
  _LOGMETRIC._serialized_end=2557
  _LOGMETRIC_RESPONSE._serialized_start=953
  _LOGMETRIC_RESPONSE._serialized_end=963
  _LOGPARAM._serialized_start=2560
  _LOGPARAM._serialized_end=2701
  _LOGPARAM_RESPONSE._serialized_start=953
  _LOGPARAM_RESPONSE._serialized_end=963
  _SETEXPERIMENTTAG._serialized_start=2704
  _SETEXPERIMENTTAG._serialized_end=2848
  _SETEXPERIMENTTAG_RESPONSE._serialized_start=953
  _SETEXPERIMENTTAG_RESPONSE._serialized_end=963
  _SETTAG._serialized_start=2851
  _SETTAG._serialized_end=2990
  _SETTAG_RESPONSE._serialized_start=953
  _SETTAG_RESPONSE._serialized_end=963
  _DELETETAG._serialized_start=2992
  _DELETETAG._serialized_end=3101
  _DELETETAG_RESPONSE._serialized_start=953
  _DELETETAG_RESPONSE._serialized_end=963
  _GETRUN._serialized_start=3103
  _GETRUN._serialized_end=3228
  _GETRUN_RESPONSE._serialized_start=1893
  _GETRUN_RESPONSE._serialized_end=1929
  _SEARCHRUNS._serialized_start=3231
  _SEARCHRUNS._serialized_end=3511
  _SEARCHRUNS_RESPONSE._serialized_start=3404
  _SEARCHRUNS_RESPONSE._serialized_end=3466
  _LISTARTIFACTS._serialized_start=3514
  _LISTARTIFACTS._serialized_end=3730
  _LISTARTIFACTS_RESPONSE._serialized_start=3599
  _LISTARTIFACTS_RESPONSE._serialized_end=3685
  _FILEINFO._serialized_start=3732
  _FILEINFO._serialized_end=3791
  _GETMETRICHISTORY._serialized_start=3794
  _GETMETRICHISTORY._serialized_end=3962
  _GETMETRICHISTORY_RESPONSE._serialized_start=3874
  _GETMETRICHISTORY_RESPONSE._serialized_end=3917
  _LOGBATCH._serialized_start=3965
  _LOGBATCH._serialized_end=4142
  _LOGBATCH_RESPONSE._serialized_start=953
  _LOGBATCH_RESPONSE._serialized_end=963
  _LOGMODEL._serialized_start=4144
  _LOGMODEL._serialized_end=4247
  _LOGMODEL_RESPONSE._serialized_start=953
  _LOGMODEL_RESPONSE._serialized_end=963
  _GETEXPERIMENTBYNAME._serialized_start=4250
  _GETEXPERIMENTBYNAME._serialized_end=4399
  _GETEXPERIMENTBYNAME_RESPONSE._serialized_start=1337
  _GETEXPERIMENTBYNAME_RESPONSE._serialized_end=1387
  _GETAUTHTOKEN._serialized_start=4402
  _GETAUTHTOKEN._serialized_end=4540
  _GETAUTHTOKEN_RESPONSE._serialized_start=4466
  _GETAUTHTOKEN_RESPONSE._serialized_end=4495
  _MLFLOWSERVICE._serialized_start=4753
  _MLFLOWSERVICE._serialized_end=7819
_builder.BuildServices(DESCRIPTOR, 'service_pb2', globals())
# @@protoc_insertion_point(module_scope)
