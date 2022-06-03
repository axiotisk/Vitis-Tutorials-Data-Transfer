import os             
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

import argparse

from key_exe_times import *
from os.path import exists

#Read argument list
if len(sys.argv) == 1:
    print("USAGE: %s --file_names <file_name_1> <file_name_2> ... --legends <legend_1> <legend_2> ..."%(sys.argv[0]))
    sys.exit(1)

print(sys.argv)


# defined command line options
# this also generates --help and error handling
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--file_names",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=str,
  default=[],  # default if nothing is provided
)
CLI.add_argument(
  "--legends",
  nargs="*",
  type=str,  # any type/callable can be used here
  default=[],
)

# parse the command line
args = CLI.parse_args()
# access CLI options
print("file_names: %r" % args.file_names)
print("legends: %r" % args.legends)


exe_times =[]
for i,j in enumerate(args.file_names):
    print(j, " ", args.legends[i])

    #Defining a list with the objects
    exe_times.append(keyExeTimes(str(j), args.legends))
    exe_times[-1].csv_dir_reader()

    print("File exists:", exists(str(j)))

#Setting up hw exe times
for i in exe_times:
    #Run on HW
    plt.scatter(exe_times[0].get_ar_bs(), i.get_ar_time_hw_sort())

    #Object Migration
    plt.scatter(exe_times[0].get_ar_bs(), i.get_ar_obj_migration_sort())

    #Kernel
    plt.scatter(exe_times[0].get_ar_bs(), i.get_ar_wait_kernel_sort())

#Setting up sofware exe time plot
#plt.scatter(exe_times[0].get_ar_bs(), exe_times[0].get_ar_time_sw_sort())
#args.legends.append("CPU")

#Setting legend
plt.legend(args.legends, fontsize=20)
plt.xlabel("Buffer Size [Integers]", fontsize=20)
plt.ylabel("Execution Times [ms]", fontsize=20)

plt.show()
