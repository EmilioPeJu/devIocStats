TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

# Enable CPU monitoring via low priority spin 
# by setting SECONDS_TO_BURN > 0.  For vxWorks, SECONDS_TO_BURN will
# default to 5 if this is not defined.  For RTEMS, when SECONDS_TO_BURN
# is not defined, IDLE task usage is used. 
#USR_CFLAGS += -DSECONDS_TO_BURN=5

#=============================

# For DTYP="IOC stats"
DBD += devIocStats.dbd
# For DTYP="VX stats"
DBD += devVxStats.dbd

INC += devIocStatsOSD.h

#=============================

LIBRARY_IOC = devIocStats

# OSI parts
SRCS += devIocStatsAnalog.c
SRCS += devIocStatsString.c
SRCS += devIocStatsTest.c

# OSD parts
SRCS += osdCpuUsage.c
SRCS += osdFdUsage.c
SRCS += osdMemUsage.c
SRCS += osdClustInfo.c
SRCS += osdSuspTasks.c
SRCS += osdIFErrors.c
SRCS += osdBootInfo.c
SRCS += osdSystemInfo.c
SRCS += osdHostInfo.c

LIBS = $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

