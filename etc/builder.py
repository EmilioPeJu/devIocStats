from iocbuilder import AutoSubstitution, Device
from iocbuilder.arginfo import *

class ioc(AutoSubstitution, Device):
    # Substitution attributes
    TemplateFile = 'ioc.db'
    
    # Device attributes    
    LibFileList = ['devIocStats']
    DbdFileList = ['iocAdmin']
