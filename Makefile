TOP = .
include $(TOP)/configure/CONFIG

DIRS += configure
DIRS += devIocStats
DIRS += iocAdmin
ifeq '$(MAKE_TEST_IOC_APP)' 'YES'
DIRS += testIocStatsApp
DIRS += iocBoot
# For LCLS
#DIRS += testIocAdminApp
endif
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard etc))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard op))
# Comment out the following line to disable building of example iocs
# DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard iocs))
include $(TOP)/configure/RULES_TOP
