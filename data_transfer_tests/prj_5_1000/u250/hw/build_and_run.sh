#!/bin/bash

# Exit when any command fails
set -e

example="${1}"

make clean

# Make sure everything is up to date
make ${example} 

# Run the application in HW emulation mode
XCL_EMULATION_MODE=hw_emu ./app${example}.exe 

