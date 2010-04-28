#!/home/mp49/epics/support/devIocStats/iocs/exampleVxWorks/bin/linux-x86/exampleVxWorks

## You may have to change exampleVxWorks to something else
## everywhere it appears in this file

cd "/home/mp49/epics/support/devIocStats/iocs/exampleVxWorks"

# Load binaries on architectures that need to do so.
# VXWORKS_ONLY, LINUX_ONLY and RTEMS_ONLY are macros that resolve
# to a comment symbol on architectures that are not the current
# build architecture, so they can be used liberally to do architecture
# specific things. Alternatively, you can include an architecture
# specific file.
# Commented out VxWorks command:ld < bin/linux-x86/exampleVxWorks.munch

## This drvTS initializer is needed if the IOC has a hardware event system
#TSinit

## Register all support components
dbLoadDatabase("dbd/exampleVxWorks.dbd")
exampleVxWorks_registerRecordDeviceDriver(pdbbase)

## Load record instances
#dbLoadRecords("db/<filename>.db","<List of macros, e.g. user=xxx>")
dbLoadRecords("db/exampleVxWorks.db")

#Must be less than 40 chars
epicsEnvSet("ENGINEER","Flash Gorden")
epicsEnvSet("LOCATION","Earth")

## Set this to see messages from mySub
#mySubDebug 1

iocInit()

## Start any sequence programs
#seq sncExample,"user=xxx"
