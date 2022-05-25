import os             
import csv
import numpy as np
import matplotlib.pyplot as plt

class keyExeTimes:
    #def __init__ (self, ar_buff_size, ar_num_buff, ar_time_sw, ar_obj_migration, ar_wait_kernel, ar_time_hw):
    def __init__ (self):

#        #Setting buffer size array
#        if ar_buff_size is None:
#            self.ar_buff_size = []
#        elif isinstance(ar_buff_size, list):
#            self.ar_buff_size = ar_buff_size
#        else:
#            raise TypeError("Unsupported ar_buff_size type: ", ar_buff_size)
#
#        #Setting number of buffers array
#        if ar_num_buff is None:
#            self.ar_num_buff = []
#        elif isinstance(ar_num_buff, list):
#            self.ar_num_buff = ar_num_buff
#        else:
#            raise TypeError("Unsupported ar_num_buff type: ", ar_num_buff)
#        
#        #Setting software time execution array
#        if ar_time_sw is None:
#            self.ar_time_sw = []
#        elif isinstance(ar_time_sw, list):
#            self.ar_time_sw = ar_time_sw
#        else:
#            raise TypeError("Unsupported ar_time_sw type: ", ar_time_sw)
#
#        #Setting times for object migraiton array
#        if ar_obj_migration is None:
#            self.ar_obj_migration = []
#        elif isinstance(ar_obj_migration, list):
#            self.ar_obj_migration = ar_obj_migration
#        else:
#            raise TypeError("Unsupported ar_obj_migration type: ", ar_obj_migration)
#
#        #Setting times for kernel execution time array
#        if ar_wait_kernel is None:
#            self.ar_wait_kernel = []
#        elif isinstance(ar_wait_kernel, list):
#            self.ar_wait_kernel = ar_wait_kernel
#        else:
#            raise TypeError("Unsupported ar_wait_kernel type: ", ar_wait_kernel)
#
#        #Setting times for kernel execution time array
#        if ar_time_hw is None:
#            self.ar_time_hw = []

        self.ar_bs = []
        self.ar_buff_size = []
        self.ar_num_buff = []
        self.ar_time_sw = []
        self.ar_obj_migration = []
        self.ar_wait_kernel = []
        self.ar_time_hw = []
        self.ar_time_sw_sort = []
        self.ar_obj_migration_sort = []
        self.ar_wait_kernel_sort = []
        self.ar_time_hw_sort = []
 
    #Define interface funtions
    def get_ar_buff_size(self):     return self.ar_buff_size
    def get_ar_num_buff(self):      return self.ar_num_buff
    def get_ar_time_sw(self):       return self.ar_time_sw
    def get_ar_obj_migration(self): return self.ar_obj_migration
    def get_ar_wait_kernel(self):   return self.ar_wait_kernel
    def get_ar_time_hw(self):       return self.ar_time_hw

    #Defining csv reading functions

    #Reading csv file
    def csv_reader(self, directory, filename):
        with open (os.path.join(directory, filename), 'r') as f: 
            csvreader = csv.reader(f)
            header = next(csvreader)
            for values in csvreader:
                if values[0] == "Buffer size":
                    self.ar_bs.append(int(values[1]))
    
                if values[0] == "Software VADD run":
                    self.ar_time_sw.append(float(values[1]))
    
                if values[0] == "Memory object migration enqueue":
                    self.ar_obj_migration.append(float(values[1]))
    
                if values[0] == "Wait for kernels to complete":
                    self.ar_wait_kernel.append(float(values[1]))

    #Reads all the files in a given directory
    def csv_dir_reader(self, directory):
        for filename in os.listdir(directory):
            self.csv_reader(directory, filename)

        #Add "memory obj migration" and "wait for kernel" 
        self.ar_time_hw = [float(a) + float(b) for a, b in zip(self.ar_obj_migration, self.ar_wait_kernel)]  

        #Sort the lists according to buffer size
        self.ar_time_sw_sort = [x for _,x in sorted(zip(self.ar_bs, self.ar_time_sw))]
        self.ar_time_hw_sort = [x for _,x in sorted(zip(self.ar_bs, self.ar_time_hw))]
        self.ar_obj_migration_sort = [x for _,x in sorted(zip(self.ar_bs, self.ar_obj_migration))]
        self.ar_wait_kernel_sort = [x for _,x in sorted(zip(self.ar_bs, self.ar_wait_kernel))]

        #Sort buffer size
        self.ar_bs.sort()

    #Generating plots
    def plot_generator(self):
        plt.scatter(self.ar_bs, self.ar_time_sw_sort)
        plt.scatter(self.ar_bs, self.ar_obj_migration_sort)
        plt.scatter(self.ar_bs, self.ar_wait_kernel_sort)
        plt.scatter(self.ar_bs, self.ar_time_hw_sort)

        #Setting up axes
        plt.legend(["Software", "Object Migration", "Kernel Execution", "Hardware"], fontsize=20)
        plt.xlabel("Buffer Size [Integers]", fontsize=20)
        plt.ylabel("Execution Times [ms]", fontsize=20)

        plt.show()

if __name__ == "__main__":
    test_data = keyExeTimes()

    #Prints an empty list
    print(test_data.get_ar_time_hw())

    #Read data from a given directory
    test_data.csv_dir_reader("../key_exe_times_csv/5e3_1e6_b1/")

    #Prints the list that previously was empty
    print(test_data.get_ar_time_hw())

    #Plotting the data read
    test_data.plot_generator()

