#!/bin/bash

# Exit when any command fails
set -e

#Set by the user
BUF_SIZE=100000
NUM_BUF=10

CSV_DIR=csv_files/
SUMMARY_DIR=summaries/
KEY_EXE_TIMES_DIR=key_exe_times/

TARGET_DIR=nb_${NUM_BUF}/

#Full paths to directory
KEY_EXE_TIMES_SAVING_DIR=${CSV_DIR}${KEY_EXE_TIMES_DIR}${TARGET_DIR}
SUMMARY_SAVING_DIR=${CSV_DIR}${SUMMARY_DIR}${TARGET_DIR}

#Deleting saving directories if they exist
if [ -d "$KEY_EXE_TIMES_SAVING_DIR" ]; then rm -Rf $KEY_EXE_TIMES_SAVING_DIR; fi
if [ -d "$SUMMARY_SAVING_DIR" ]; then rm -Rf $SUMMARY_SAVING_DIR; fi

#Creating the directories
mkdir -p $KEY_EXE_TIMES_SAVING_DIR
mkdir -p $SUMMARY_SAVING_DIR

#make clean
#
# Make sure everything is up to date
make -j

# Run the application in HW emulation mode
XCL_EMULATION_MODE=hw_emu ./app.exe ${KEY_EXE_TIMES_SAVING_DIR} ${BUF_SIZE}

cp summary.csv ${SUMMARY_SAVING_DIR}/bs_${BUF_SIZE}.csv
