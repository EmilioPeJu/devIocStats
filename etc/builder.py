from iocbuilder import AutoSubstitution, Device, ModuleBase, Call_TargetOS
from iocbuilder.arginfo import *

# This decorator provides the ability to create a template class
# that overrides another template.  Use this when a *.template file
# has an include statement.  This functionality will be moved into
# iocbuilder in the future
# Shamelessly stolen from ADCore 2-4dls2 - EW 14/06/16
def includesTemplates(*templates):
    def decorator(cls):
        arginfo = templates[0].ArgInfo
        arguments = list(templates[0].Arguments)
        defaults = templates[0].Defaults.copy()
        for template in templates[1:]:
            arginfo += template.ArgInfo
            arguments += [x for x in template.Arguments if x not in arguments]
            defaults.update(template.Defaults)
        cls.ArgInfo = arginfo + cls.ArgInfo
        cls.Arguments = list(cls.Arguments) + [x for x in arguments if x not in cls.Arguments]
        defaults.update(cls.Defaults)
        cls.Defaults = defaults
        return cls
    return decorator    

class _devIocStats(Device):
    LibFileList = ['devIocStats']
    DbdFileList = ['devIocStats']
    AutoInstantiate = True

class iocGui(AutoSubstitution):
    TemplateFile = 'iocGui.db'

@includesTemplates(iocGui)
class ioc(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'ioc.db'

class ioc_vxworks(ioc):
    TemplateFile = 'ioc_vxworks.db'

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
