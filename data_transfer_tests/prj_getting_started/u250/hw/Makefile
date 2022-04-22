
all: app.exe emconfig.json vadd.xclbin
original: apporiginal.exe emconfig.json vadd.xclbin
1: app1.exe emconfig.json vadd.xclbin
2: app2.exe emconfig.json vadd.xclbin
4: app4.exe emconfig.json wide_vadd.xclbin
5: app5.exe emconfig.json wide_vadd.xclbin

apporiginal.exe: ../../src/host_original.cpp
	g++ -Wall -g -std=c++11 ../../src/host_original.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o apporiginal.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

app.exe: ../../src/host.cpp
	g++ -Wall -g -std=c++11 ../../src/host.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

app1.exe: ../../src/host_1.cpp
	g++ -Wall -g -std=c++11 ../../src/host_1.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app1.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

app2.exe: ../../src/host_2.cpp
	g++ -Wall -g -std=c++11 ../../src/host_2.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app2.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

app4.exe: ../../src/host_4.cpp
	g++ -Wall -g -std=c++11 ../../src/host_4.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app4.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++

app5.exe: ../../src/host_5.cpp
	g++ -Wall -g -std=c++11 ../../src/host_5.cpp ../../src/event_timer.cpp ../../src/xilinx_ocl_helper.cpp -o app5.exe \
		-I/home/kaxiotis/Vitis-Tutorials/Getting_Started/Vitis/example/src/ \
		-L${XILINX_XRT}/lib/ -lOpenCL -pthread -lrt -lstdc++
	
wide_vadd.xo: ../../src/wide_vadd.cpp
	v++ -c -t hw --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg -k wide_vadd -I../../src ../../src/wide_vadd.cpp -o wide_vadd.xo --hls.pre_tcl hls_config.tcl

wide_vadd.xclbin: ./wide_vadd.xo
	v++ -l -t hw --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg ./wide_vadd.xo -o wide_vadd.xclbin --hls.pre_tcl hls_config.tcl

vadd.xo: ../../src/vadd.cpp
	v++ -c -t hw --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg -k vadd -I../../src ../../src/vadd.cpp -o vadd.xo --hls.pre_tcl hls_config.tcl

vadd.xclbin: ./vadd.xo
	v++ -l -t hw --platform xilinx_u250_gen3x16_xdma_3_1_202020_1 --config ../../src/u250.cfg ./vadd.xo -o vadd.xclbin --hls.pre_tcl hls_config.tcl

emconfig.json:
	emconfigutil --platform  xilinx_u250_gen3x16_xdma_3_1_202020_1 --nd 1

clean:
	rm -rf wide_vadd* *.exe *json *csv *log *summary _x xilinx* .run .Xil .ipcache *.jou

# Unless specified, use the current directory name as the v++ build target
TARGET ?= $(notdir $(CURDIR))
