#!/home/mp49/epics/support/devIocStats/iocs/exampleSoft/bin/vxWorks-ppc604_long/exampleSoft

## You may have to change exampleSoft to something else
## everywhere it appears in this file

cd "/home/mp49/epics/support/devIocStats/iocs/exampleSoft"

# Load binaries on architectures that need to do so.
# VXWORKS_ONLY, LINUX_ONLY and RTEMS_ONLY are macros that resolve
# to a comment symbol on architectures that are not the current
# build architecture, so they can be used liberally to do architecture
# specific things. Alternatively, you can include an architecture
# specific file.
ld < bin/vxWorks-ppc604_long/exampleSoft.munch

## This drvTS initializer is needed if the IOC has a hardware event system
#TSinit

## Register all support components
dbLoadDatabase("dbd/exampleSoft.dbd")
exampleSoft_registerRecordDeviceDriver(pdbbase)

## Load record instances
#dbLoadRecords("db/<filename>.db","<List of macros, e.g. user=xxx>")
dbLoadRecords("db/exampleSoft.db")

## Set this to see messages from mySub
#mySubDebug 1

iocInit()

## Start any sequence programs
#seq sncExample,"user=xxx"
