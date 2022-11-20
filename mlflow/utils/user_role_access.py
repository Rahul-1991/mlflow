PV_ROLE_ACCESS = ['get', 'search']
PC_ROLE_ACCESS = PV_ROLE_ACCESS + ['create']
PM_ROLE_ACCESS = PC_ROLE_ACCESS
SA_ROLE_ACCESS = PM_ROLE_ACCESS + ['delete', 'restore', 'rename']

role_access_map = {
    'PM': PM_ROLE_ACCESS, 'PC': PC_ROLE_ACCESS, 'PV': PV_ROLE_ACCESS, 'SA': SA_ROLE_ACCESS
}
