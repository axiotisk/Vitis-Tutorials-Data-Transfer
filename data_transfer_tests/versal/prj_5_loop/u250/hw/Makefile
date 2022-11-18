
all: app.exe emconfig.json wide_vadd.xclbin

app.exe: ../../src/host.cpp
	g++ -Wall -g -std=c++11 ../../src/host.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++
	
wide_vadd.xo: ../../src/wide_vadd.cpp
	v++ -c -t hw --config ../../src/u250.cfg -k wide_vadd -I../../src ../../src/wide_vadd.cpp -o wide_vadd.xo --hls.pre_tcl hls_config.tcl

wide_vadd.xsa: ./wide_vadd.xo
	v++ -l -t hw --config ../../src/u250.cfg ./wide_vadd.xo -o wide_vadd.xsa --hls.pre_tcl hls_config.tcl

wide_vadd.xclbin: ./wide_vadd.xsa
	v++ --package -t hw --config ../../src/u250.cfg ./wide_vadd.xsa -o wide_vadd.xclbin --hls.pre_tcl hls_config.tcl

emconfig.json:
	emconfigutil --platform  xilinx_vck5000_gen4x8_xdma_2_202210_1 --nd 1

clean:
	rm -rf wide_vadd* *.exe *json *csv *log *summary _x xilinx* .run .Xil .ipcache *.jou

# Unless specified, use the current directory name as the v++ build target
TARGET ?= $(notdir $(CURDIR))
