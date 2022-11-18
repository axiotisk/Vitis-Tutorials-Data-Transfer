#!/bin/bash

#Set's up the environment variables to run the Vitis-Tutorial

source /opt/xilinx/xrt/setup.sh
source /home/xilinx/Vitis/2022.1/settings64.sh

PLATFORM_REPO_PATHS=/opt/xilinx/platforms/
LIBRARY_PATH=/usr/lib/x86_64-linux-gnu
CPATH=/usr/include/x86_64-linux-gnu

export PLATFORM_REPO_PATHS
export LIBRARY_PATH
export CPATH
