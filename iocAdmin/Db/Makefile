TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_INSTALLS_OPT = YES

#----------------------------------------------------
# Create and install (or just install)
# databases, templates, substitutions like this
#
DB_INSTALLS += ioc.template
DB_INSTALLS += ioc_vxworks.template
DB_INSTALLS += iocRTOS.template
DB_INSTALLS += iocVxWorksOnly.template
DB_INSTALLS += iocRTEMSOnly.template
DB_INSTALLS += iocEnvVar.template
DB_INSTALLS += iocCluster.template
DB_INSTALLS += iocScanMon.template
DB_INSTALLS += iocScanMonSum.template
DB_INSTALLS += iocGeneralTime.template
DB_INSTALLS += access.db
#DB_INSTALLS += iocAdminVxWorks.template
#DB_INSTALLS += iocAdminSoft.template
#DB_INSTALLS += iocAdminRTEMS.template
#DB_INSTALLS += iocAdminScanMon.template
DB_INSTALLS += baseSecurity.acf
DB_INSTALLS += iocGui.db

#
#----------------------------------------------------
# If <anyname>.db template is not named <anyname>*.template add
# <anyname>_TEMPLATE = <templatename>

include $(TOP)/configure/RULES

#----------------------------------------
#  ADD RULES AFTER THIS LINE

include $(TOP)/configure/RULES.Db
