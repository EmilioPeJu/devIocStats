TOP=../..
include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE

# Low-level stats displays
EDLS += ioc_stats.edl
EDLS += ioc_stats_clust.edl
EDLS += ioc_stats_epics_env.edl
EDLS += ioc_stats_limits.edl
EDLS += ioc_stats_reboot_confirm.edl
EDLS += ioc_stats_release.edl
EDLS += ioc_stats_soft.edl
EDLS += ioc_stats_vxworks.edl
EDLS += ioc_stats_scanmon.edl
EDLS += ioc_stats_softdls.edl

# Top level display for all BL GW IOCs
EDLS += BLGWStatus.edl
EDLS += ioc_embed.edl

DATA += $(EDLS)

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE
