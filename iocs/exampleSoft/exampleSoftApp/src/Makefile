TOP=../..

include $(TOP)/configure/CONFIG

# ------------------------
# Build an IOC Application
# ------------------------

PROD_IOC = exampleSoft

DATA+=exampleSoftGUI

# exampleSoft.dbd will be installed into <top>/dbd
DBD += exampleSoft.dbd

# exampleSoft.dbd will be created from these files
exampleSoft_DBD += base.dbd
exampleSoft_DBD += devIocStats.dbd

# exampleSoft_registerRecordDeviceDriver.cpp will be created
# exampleSoft.dbd
exampleSoft_SRCS += exampleSoft_registerRecordDeviceDriver.cpp

# These two lines are needed for non-vxWorks builds, such as Linux
exampleSoft_SRCS_DEFAULT += exampleSoftMain.cpp
exampleSoft_SRCS_vxWorks += -nil-

# Add locally compiled object code
#exampleSoft_SRCS +=

# The following adds object code from base/src/vxWorks
exampleSoft_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# This line says that this IOC Application depends on the
# xxx Support Module
exampleSoft_LIBS += devIocStats

# We need to link this IOC Application against the EPICS Base libraries
exampleSoft_LIBS += $(EPICS_BASE_IOC_LIBS)

# ---------------------------------------------------

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
#
# The difference between a file with an "st" extension
# and one with an "stt" extension is:
# The "st" extension files get passed through the C preprocessor
# whereas the "stt" files do not.

#ifneq ($(SNCSEQ),)
    # This builds sncExample as a component of exampleSoft
#    exampleSoft_SNCFLAGS += +r
#    exampleSoft_DBD      += sncExample.dbd
#    exampleSoft_SRCS     += sncExample.stt
#    exampleSoft_LIBS     += seq pv

    # The following builds sncExample as a standalone application
#    PROD_HOST           += sncExample
#    sncExample_SNCFLAGS += +m
#    sncExample_SRCS     += sncExample.stt
#    sncExample_LIBS     += seq pv
    # Here, we need to specify the dependency on EPICS Base libraries
    # again because this is a standalone application and
    # not part of exampleSoft
#    sncExample_LIBS     += $(EPICS_BASE_HOST_LIBS)
#endif

include $(TOP)/configure/RULES
