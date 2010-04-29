from iocbuilder import AutoSubstitution, Device, ModuleBase, Call_TargetOS
from iocbuilder.arginfo import *

class _devIocStats(Device):
    LibFileList = ['devIocStats']
    DbdFileList = ['devIocStats']
    AutoInstantiate = True


class ioc(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'ioc.db'

class iocEnvVar(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'iocEnvVar.db'

class iocRTOS(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'iocRTOS.db'

class iocVxWorksOnly(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'iocVxWorksOnly.db'


## Create default Device IOC Stats definitions.
class defaultIocStats(ModuleBase):
    env_vars = [
        ('LOCATION'     , 'LOCATION'),
        ('ENGINEER'     , 'ENGINEER'),
    ]
    epics_vars = [
        ('CA_ADDR_LIST' , 'EPICS_CA_ADDR_LIST'),
        ('CA_CONN_TIME' , 'EPICS_CA_CONN_TMO'),
        ('CA_AUTO_ADDR' , 'EPICS_CA_AUTO_ADDR_LIST'),
        ('CA_RPTR_PORT' , 'EPICS_CA_REPEATER_PORT'),
        ('CA_SRVR_PORT' , 'EPICS_CA_SERVER_PORT'),
        ('CA_MAX_ARRAY' , 'EPICS_CA_MAX_ARRAY_BYTES'),
        ('CA_SRCH_TIME' , 'EPICS_CA_MAX_SEARCH_PERIOD'),
        ('CA_BEAC_TIME' , 'EPICS_CA_BEACON_PERIOD'),
        ('TIMEZONE'     , 'EPICS_TIMEZONE'),
        ('TS_NTP_INET'  , 'EPICS_TS_NTP_INET'),
        ('IOC_LOG_PORT' , 'EPICS_IOC_LOG_PORT'),
        ('IOC_LOG_INET' , 'EPICS_IOC_LOG_INET'),
    ]

    def __init__(self, ioc_name, name = ''):
        ioc(IOCNAME = ioc_name, name = name)
        for vars, var_type in [
                (self.env_vars, 'env'), (self.epics_vars, 'epics')]:
            for pv, var in vars:
                iocEnvVar(
                    IOCNAME = ioc_name, ENVNAME = pv, ENVVAR = var,
                    ENVTYPE = var_type)

        Call_TargetOS(self, 'extra', ioc_name)

    def extra_vxWorks(self, ioc_name):
        iocRTOS(IOCNAME = ioc_name, SYS_MBUF_FLNK = '')
        iocVxWorksOnly(IOCNAME = ioc_name, DAT_MBUF_FLNK = '')

    ArgInfo = makeArgInfo(__init__,
        ioc_name = Simple('IOC name'),
        name = Simple('GUI name, optional'))
