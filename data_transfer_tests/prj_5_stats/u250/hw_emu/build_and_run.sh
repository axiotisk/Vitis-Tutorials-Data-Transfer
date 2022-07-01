#!/bin/bash

# Exit when any command fails
set -e

make clean

# Make sure everything is up to date
make

# Run the application in HW emulation mode
XCL_EMULATION_MODE=hw_emu ./app.exe 

