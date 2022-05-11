
all: app.exe emconfig.json vadd.xclbin

app.exe: ../../src/host.cpp
	g++ -Wall -g -std=c++11 ../../src/host.cpp -o app.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

vadd.xo: ../../src/vadd.cpp
	v++ -c -t hw_emu --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg -k vadd -I../../src ../../src/vadd.cpp -o vadd.xo --hls.pre_tcl hls_config.tcl

vadd.xclbin: ./vadd.xo
	v++ -l -t hw_emu --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg ./vadd.xo -o vadd.xclbin --hls.pre_tcl hls_config.tcl

emconfig.json:
	emconfigutil --platform  xilinx_u250_gen3x16_xdma_3_1_202020_1 --nd 1

clean:
	rm -rf wide_vadd* *.exe *json *csv *log *summary _x xilinx* .run .Xil .ipcache *.jou

# Unless specified, use the current directory name as the v++ build target
TARGET ?= $(notdir $(CURDIR))
