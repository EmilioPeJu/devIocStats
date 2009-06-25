/* devIocStatsOSD.h - devIocStats.c Support for RTEMS - based on */
/* devVXStats.c - Device Support Routines for vxWorks statistics */
/*
 *	Author: Jim Kowalkowski
 *	Date:  2/1/96
 *
 *	Experimental Physics and Industrial Control System (EPICS)
 *
 *	Copyright 1991, the Regents of the University of California,
 *	and the University of Chicago Board of Governors.
 *
 *	This software was produced under  U.S. Government contracts:
 *	(W-7405-ENG-36) at the Los Alamos National Laboratory,
 *	and (W-31-109-ENG-38) at Argonne National Laboratory.
 *
 *	Initial development by:
 *		The Controls and Automation Group (AT-8)
 *		Ground Test Accelerator
 *		Accelerator Technology Division
 *		Los Alamos National Laboratory
 *
 *	Co-developed with
 *		The Controls and Computing Group
 *		Accelerator Systems Division
 *		Advanced Photon Source
 *		Argonne National Laboratory
 *
 * Modifications for LCLS/SPEAR at SLAC:
 * ----------------
 *  08-08-26    Till Straumann, ported to RTEMS.
 *
 *              RTEMS notes:
 *                - RTEMS also uses a 'workspace' memory
 *                  area which is independent of the malloc heap.
 *                  Some system-internal data structures are
 *                  allocated from the workspace area.
 *                  So far, support for monitoring the workspace area 
 *                  has not been implemented (although it would be
 *                  straightforward to do.
 *
 *              The RTEMS/BSD stack has only one pool of mbufs
 *              and only uses two sizes: MSIZE (128b) for 'ordinary'
 *              mbufs, and MCLBYTES (2048b) for 'mbuf clusters'.
 *                 Therefore, the 'data' pool is empty. However,
 *              the calculation of MinDataMBuf always shows usage
 *              info of 100% free (but 100% of 0 is still 0).
 *
 */
#define __RTEMS_VIOLATE_KERNEL_VISIBILITY__
#include <rtems.h>
#include <bsp.h>
#include <rtems/libcsupport.h>
#include <rtems/libio_.h>
#include <rtems/rtems_bsdnet.h>
#include <sys/mbuf.h>
#include <sys/socket.h>
#include <net/if.h>
#include <net/if_var.h>

#undef malloc
#undef free

#include <string.h>
#include <stdlib.h>

#define sysBootLine rtems_bsdnet_bootp_cmdline
/* Override default STARTUP environment variable to use INIT */
#undef  STARTUP
#define STARTUP "INIT"
#define CLUSTSIZES 2 /* only regular mbufs and clusters */

/* Heap implementation changed; we should use
 * malloc_free_space() which handles these changes
 * transparently but then we don't get the
 * 'bytesUsed' information.
 */
# if   (__RTEMS_MAJOR__ > 4) \
   || (__RTEMS_MAJOR__ == 4 && __RTEMS_MINOR__ > 7)
#define RTEMS_MALLOC_IS_HEAP
#include <rtems/score/protectedheap.h>
typedef char objName[13];
#define RTEMS_OBJ_GET_NAME(tc,name) rtems_object_get_name((tc)->Object.id, sizeof(name),(name))
#ifdef SSRLAPPSMISCUTILS
#define USE_SSRLAPPSMISCUTILS
extern int isnan();
#include <ssrlAppsMiscUtils.h>
#endif
# else
typedef char * objName;
#define RTEMS_OBJ_GET_NAME(tc,name) name = (tc)->Object.name
# endif

#ifdef RTEMS_BSP_PGM_EXEC_AFTER /* only defined on uC5282 */
#define reboot(x) bsp_reset(0)
#elif   (__RTEMS_MAJOR__ > 4) \
         || (__RTEMS_MAJOR__ == 4 && __RTEMS_MINOR__ > 9) \
         || (__RTEMS_MAJOR__ == 4 && __RTEMS_MINOR__ == 9 && __RTEMS_REVISION__ > 0)
#define reboot(x) bsp_reset()
#else
#define reboot(x) rtemsReboot()
#endif
/* Use alternate to cpuBurn if SECONDS_TO_BURN is not defined */
#ifndef  SECONDS_TO_BURN
#define SECONDS_TO_BURN 0
#endif
