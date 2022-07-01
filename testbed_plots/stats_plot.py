import os             
import sys
import csv
import numpy as np
import matplotlib.pyplot as plt

import argparse

from key_exe_times import *

path = "key_exe_times_csv/stat_param.csv"

csv_values = openclTrace()
csv_values.csv_reader(path)
csv_values.duration_calc()

csv_values.plot_distr_hist()
