TOP=../..

include $(TOP)/configure/CONFIG


# ------------------------
# Build an IOC Application
# ------------------------

PROD_IOC = exampleVxWorks

DATA+=exampleVxWorksGUI

# exampleVxWorks.dbd will be installed into <top>/dbd
DBD += exampleVxWorks.dbd

# exampleVxWorks.dbd will be created from these files
exampleVxWorks_DBD += base.dbd
exampleVxWorks_DBD += devIocStats.dbd
exampleVxWorks_DBD += devVxStats.dbd

# exampleVxWorks_registerRecordDeviceDriver.cpp will be created
# exampleVxWorks.dbd
exampleVxWorks_SRCS += exampleVxWorks_registerRecordDeviceDriver.cpp

# These two lines are needed for non-vxWorks builds, such as Linux
exampleVxWorks_SRCS_DEFAULT += exampleVxWorksMain.cpp
exampleVxWorks_SRCS_vxWorks += -nil-

# Add locally compiled object code
#exampleVxWorks_SRCS +=

# The following adds object code from base/src/vxWorks
exampleVxWorks_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# This line says that this IOC Application depends on the
# xxx Support Module
exampleVxWorks_LIBS += devIocStats

# We need to link this IOC Application against the EPICS Base libraries
exampleVxWorks_LIBS += $(EPICS_BASE_IOC_LIBS)

# ---------------------------------------------------

# NOTE: To build SNL programs, SNCSEQ must be defined
# in the <top>/configure/RELEASE file
#
# The difference between a file with an "st" extension
# and one with an "stt" extension is:
# The "st" extension files get passed through the C preprocessor
# whereas the "stt" files do not.

#ifneq ($(SNCSEQ),)
    # This builds sncExample as a component of exampleVxWorks
#    exampleVxWorks_SNCFLAGS += +r
#    exampleVxWorks_DBD      += sncExample.dbd
#    exampleVxWorks_SRCS     += sncExample.stt
#    exampleVxWorks_LIBS     += seq pv

    # The following builds sncExample as a standalone application
#    PROD_HOST           += sncExample
#    sncExample_SNCFLAGS += +m
#    sncExample_SRCS     += sncExample.stt
#    sncExample_LIBS     += seq pv
    # Here, we need to specify the dependency on EPICS Base libraries
    # again because this is a standalone application and
    # not part of exampleVxWorks
#    sncExample_LIBS     += $(EPICS_BASE_HOST_LIBS)
#endif

include $(TOP)/configure/RULES
