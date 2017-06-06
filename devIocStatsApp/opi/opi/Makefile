TOP = ../../..

ifeq (linux-x86_64, $(findstring linux-x86_64, $(EPICS_HOST_ARCH)))
INSTALL = runcss.sh
else
INSTALL =
endif

install: $(INSTALL)

clean:
	rm -f runcss.sh

runcss.sh:
	build_run_css -t $(TOP)

