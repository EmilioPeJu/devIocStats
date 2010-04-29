TOP = .
include $(TOP)/configure/CONFIG

DIRS += configure
DIRS += devIocStats
DIRS += iocAdminLib
#DIRS += testIocStatsApp

DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))
# Comment out the following line to disable building of example iocs
# DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))
include $(TOP)/configure/RULES_TOP
