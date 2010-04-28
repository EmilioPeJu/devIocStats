TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

DB += exampleVxWorks.db

USES_TEMPLATE += $(DEVIOCSTATS)/db/ioc.db
USES_TEMPLATE += $(DEVIOCSTATS)/db/iocEnvVar.db
USES_TEMPLATE += $(DEVIOCSTATS)/db/iocRTOS.db
USES_TEMPLATE += $(DEVIOCSTATS)/db/iocVxWorksOnly.db


include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
