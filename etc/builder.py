from iocbuilder import AutoSubstitution, Device, Architecture, ModuleBase
from iocbuilder.arginfo import *

class _devIocStats(Device):
    LibFileList = ['devIocStats']
    DbdFileList = ['devIocStats']
    AutoInstantiate = True

class iocAdminScanMon(AutoSubstitution):
    Dependencies = (_devIocStats,)
    TemplateFile = 'iocAdminScanMon.db'

class iocAdminVxWorks(AutoSubstitution):
    Dependencies = (_devIocStats,)    
    TemplateFile = 'iocAdminVxWorks.db'

class iocAdminSoft(AutoSubstitution):
    Dependencies = (_devIocStats, )
    TemplateFile = "iocAdminSoft.db"

class iocGui(AutoSubstitution):
    TemplateFile = "iocGui.db"
    
class devIocStatsHelper(ModuleBase):
    Dependencies = (_devIocStats,)
    def __init__(self, ioc, name='',
                 scanMonitor=True, guiTags=True,
                 screen="ioc_stats_softdls.edl"):
        self.name = name
        self.ioc = ioc
        if Architecture().startswith("linux") or Architecture().startswith("windows"):
            iocAdminSoft(IOC= ioc)
        elif Architecture().startswith("vxWorks"):
            iocAdminVxWorks(IOC= ioc)
        if scanMonitor:
            iocAdminScanMon(IOC= ioc)
        if guiTags:
            iocGui(IOC= ioc, name=name, EDM_FILE=screen)

    ArgInfo = makeArgInfo(
        __init__,
        ioc = Simple("ioc name", str),
        name = Simple("gui element name", str),
        scanMonitor = Simple("choice to include scan monitor", bool),
        guiTags = Simple("choice to include gui tags", bool),
        screen = Simple("edm file for gui tags", str)
    )
    
