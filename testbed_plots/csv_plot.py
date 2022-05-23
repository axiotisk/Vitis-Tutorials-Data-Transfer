import os             
import csv
import numpy as np
import matplotlib.pyplot as plt

#1 buffer


ar_wait_kernel = []
ar_obj_migration = []

ar_time_hw = []
ar_time_sw = []

ar_bs = []


for i, filename in enumerate(os.listdir("key_exe_times_csv/5e3_1e6_b1")):
    
    with open (os.path.join("key_exe_times_csv/5e3_1e6_b1", filename), 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for values in csvreader:
            #Reading buffer size
            if values[0] == "Buffer size":
                ar_bs.append(int(values[1]))

            #Reading software execution time
            if values[0] == "Software VADD run":
                ar_time_sw.append(float(values[1]))

            #Reading time to migrate values to buffer
            if values[0] == "Memory object migration enqueue":
                ar_obj_migration.append(float(values[1]))

            #Reading time to execute kernel
            if values[0] == "Wait for kernels to complete":
                ar_wait_kernel.append(float(values[1]))

ar_time_hw = [float(a) + float(b) for a, b in zip(ar_obj_migration, ar_wait_kernel)]  #Add "memory obj migration" and "wait for kernel"

ar_time_sw_sort = [x for _,x in sorted(zip(ar_bs, ar_time_sw))]
ar_time_hw_sort = [x for _,x in sorted(zip(ar_bs, ar_time_hw))]
ar_bs.sort()

#2 buffer

ar_wait_kernel_2 = []
ar_bs_2 = []
ar_obj_migration_2 = []
ar_time_hw_2 = []
ar_time_sw_2 = []

for i, filename in enumerate(os.listdir("key_exe_times_csv/5e3_1e6_b2")):
    
    with open (os.path.join("key_exe_times_csv/5e3_1e6_b2", filename), 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for values in csvreader:
            if values[0] == "Buffer size":
                ar_bs_2.append(int(values[1]))

            if values[0] == "Software VADD run":
                ar_time_sw_2.append(float(values[1]))

            if values[0] == "Memory object migration enqueue":
                ar_obj_migration_2.append(float(values[1]))

            if values[0] == "Wait for kernels to complete":
                ar_wait_kernel_2.append(float(values[1]))

ar_time_hw_2 = [float(a) + float(b) for a, b in zip(ar_obj_migration_2, ar_wait_kernel_2)]  #Add "memory obj migration" and "wait for kernel"

ar_time_sw_sort = [x for _,x in sorted(zip(ar_bs_2, ar_time_sw_2))]
ar_time_hw_sort_2 = [x for _,x in sorted(zip(ar_bs_2, ar_time_hw_2))]


#10 buffer

ar_wait_kernel_10 = []
ar_bs_10 = []
ar_obj_migration_10 = []
ar_time_hw_10 = []
ar_time_sw_10 = []

for i, filename in enumerate(os.listdir("key_exe_times_csv/5e3_1e6_b10")):
    
    with open (os.path.join("key_exe_times_csv/5e3_1e6_b10", filename), 'r') as f:
        csvreader = csv.reader(f)
        header = next(csvreader)
        for values in csvreader:
            if values[0] == "Buffer size":
                ar_bs_10.append(int(values[1]))

            if values[0] == "Software VADD run":
                ar_time_sw_10.append(float(values[1]))

            if values[0] == "Memory object migration enqueue":
                ar_obj_migration_10.append(float(values[1]))

            if values[0] == "Wait for kernels to complete":
                ar_wait_kernel_10.append(float(values[1]))

ar_time_hw_10 = [float(a) + float(b) for a, b in zip(ar_obj_migration_10, ar_wait_kernel_10)]  #Add "memory obj migration" and "wait for kernel"

ar_time_sw_sort = [x for _,x in sorted(zip(ar_bs_10, ar_time_sw_10))]
ar_time_hw_sort_10 = [x for _,x in sorted(zip(ar_bs_10, ar_time_hw_10))]







#Plot generation


plt.scatter(ar_bs, ar_time_sw_sort)
plt.scatter(ar_bs, ar_time_hw_sort)
plt.scatter(ar_bs, ar_time_hw_sort_2)
plt.scatter(ar_bs, ar_time_hw_sort_10)


#plt.legend(["Software", "Hardware NUMBUF 1", "Hardware NUMBUF 2", "Hardware NUMBUF 10"])
plt.legend(["Software", "Hardware NUMBUF 1", "Hardware NUMBUF 2", "Hardware NUMBUF 10"], fontsize=20)
plt.xlabel("Buffer Size [Integers]", fontsize=20)
plt.ylabel("Execution Times [ms]", fontsize=20)

#Linear fit buf 1
linear_model=np.polyfit(ar_bs,ar_time_hw_sort,1)
linear_model_fn=np.poly1d(linear_model)
ar_bs_s=np.arange(0,1e6)
plt.plot(ar_bs_s,linear_model_fn(ar_bs_s),color="orange")
m1,b1 = np.polyfit(ar_bs, ar_time_hw_sort, 1)
print(m1)

#Linear fit buf 2
linear_model=np.polyfit(ar_bs,ar_time_hw_sort_2,1)
linear_model_fn=np.poly1d(linear_model)
ar_bs_s=np.arange(0,1e6)
plt.plot(ar_bs_s,linear_model_fn(ar_bs_s),color="green")
m2,b2 = np.polyfit(ar_bs, ar_time_hw_sort_2, 1)
print(m2)


#Linear fit buf 10
linear_model=np.polyfit(ar_bs,ar_time_hw_sort_10,1)
linear_model_fn=np.poly1d(linear_model)
ar_bs_s=np.arange(0,1e6)
plt.plot(ar_bs_s,linear_model_fn(ar_bs_s),color="red")
m10,b10 = np.polyfit(ar_bs, ar_time_hw_sort_10, 1)
print(m10)

plt.ylim(0,4)

plt.show()
