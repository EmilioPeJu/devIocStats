TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

#----------------------------------------------------
#  Optimization of db files using dbst (DEFAULT: NO)
#DB_OPT = YES

#----------------------------------------------------
# In a Diamond IOC Application, build db files from
# template files like this
#
DB += exampleSoft.db

USES_TEMPLATE += $(DEVIOCSTATS)/db/ioc.db
USES_TEMPLATE += $(DEVIOCSTATS)/db/iocEnvVar.db

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
