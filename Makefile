ifneq ($(words $(CURDIR)),1)
 $(error Unsupported: GNU Make cannot build in directories containing spaces, build elsewhere: '$(CURDIR)')
endif


ifeq ($(VERILATOR_ROOT),)
VERILATOR = verilator
else
export VERILATOR_ROOT
VERILATOR = $(VERILATOR_ROOT)/bin/verilator
endif

VALUE = $(file < file_list.f)

TARGET=connection_test
INFO=info
default:
	@echo "-- Verilator hello-world simple example"
	@echo "-- VERILATE & BUILD --------"

	#@for src in $(VALUE); do echo $$src; done

	mkdir info

	@for src in $(VALUE); do \
		echo $$src; \
		$(VERILATOR) ./test_0_modify/$$src.v --xml-only --xml-output ./info/$$src.xml; \
		python3 read_xml.py ./info/$$src.xml; \
	done

	@echo "-- DONE --------------------"

maintainer-copy::
clean mostlyclean distclean maintainer-clean::
	-rm -rf obj_dir *.log *.dmp *.vpd core $(INFO).* *.json *.xml info
