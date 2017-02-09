TOP = ..
include $(TOP)/configure/CONFIG
ifeq ($(EPICS_HOST_ARCH),linux-x86_64)
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard makeIocs))
DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard makeDocumentation))
endif
#DIRS := $(DIRS) $(filter-out $(DIRS), $(wildcard simulations))
include $(TOP)/configure/RULES_DIRS
