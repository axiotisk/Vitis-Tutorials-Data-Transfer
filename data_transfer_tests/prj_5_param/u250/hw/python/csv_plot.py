import os             
import csv
import numpy as np
import matplotlib.pyplot as plt

array_files = [[],[]]
array_csv = []

ar_wait_kernel = []
ar_obj_migration = []

ar_time_hw = []
ar_time_sw = []

ar_bs = []

for i, filename in enumerate(os.listdir("key_exe_times_csv")):
    
    with open (os.path.join("key_exe_times_csv", filename), 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for values in csvreader:
            if values[0] == "Buffer size":
                ar_bs.append(int(values[1]))

            if values[0] == "Software VADD run":
                ar_time_sw.append(float(values[1]))

            if values[0] == "Memory object migration enqueue":
                ar_obj_migration.append(float(values[1]))

            if values[0] == "Wait for kernels to complete":
                ar_wait_kernel.append(float(values[1]))

ar_time_hw = [float(a) + float(b) for a, b in zip(ar_obj_migration, ar_wait_kernel)]  #Add "memory obj migration" and "wait for kernel"

#print(ar_bs)
#print(ar_time_sw)
#print(ar_obj_migration)
#print(ar_wait_kernel)
#print(ar_time_hw)

ar_time_sw_sort = [x for _,x in sorted(zip(ar_bs, ar_time_sw))]
ar_time_hw_sort = [x for _,x in sorted(zip(ar_bs, ar_time_hw))]
ar_bs.sort()


#print(ar_bs)
#print(ar_time_sw_sort)
#print(ar_time_hw_sort)


plt.scatter(ar_bs, ar_time_sw_sort)
plt.scatter(ar_bs, ar_time_hw_sort)

plt.legend(["Software", "Hardware"])
plt.xlabel("Buffer size")
plt.ylabel("Time of exeution [ms]")

plt.show()
