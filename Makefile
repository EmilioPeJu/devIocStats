TOP = .
include $(TOP)/configure/CONFIG

DIRS += configure
DIRS += devIocStats
DIRS += iocAdmin
#DIRS += testIocStatsApp
#DIRS += iocBoot
# For LCLS
#DIRS += testIocAdminApp

DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))
# Comment out the following line to disable building of example iocs
# DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))
include $(TOP)/configure/RULES_TOP
