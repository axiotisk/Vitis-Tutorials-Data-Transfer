#!/bin/bash

# Exit when any command fails
set -e

make clean

# Make sure everything is up to date
make -j

# Run the application in HW emulation mode
## Check if XCL_EMULATION_MODE is set and if os then unset it before running
## the executatble
if [[ -z "${XCL_EMULATION_MODE}" ]]; then
  ./app.exe 
else
  unset XCL_EMULATION_MODE
  ./app.exe 
fi
