from iocbuilder import AutoSubstitution, Device, ModuleBase, Call_TargetOS
from iocbuilder.arginfo import *

class _devIocStats(Device):
    LibFileList = ['devIocStats']
    DbdFileList = ['devIocStats']
    AutoInstantiate = True

class ioc(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'ioc.template'

class ioc_vxworks(ioc):
    TemplateFile = 'ioc_vxworks.template'

## Create default Device IOC Stats definitions.
class defaultIocStats(ModuleBase):
    def __init__(self, ioc_name, name = ''):
        Call_TargetOS(self, 'ioc')(IOCNAME = ioc_name, name = name)
        
    def ioc_linux(self):
        return ioc

    def ioc_vxWorks(self, **kargs):
        return ioc_vxworks

    ArgInfo = makeArgInfo(__init__,
        ioc_name = Simple('IOC name'),
        name = Simple('GUI name, optional'))
