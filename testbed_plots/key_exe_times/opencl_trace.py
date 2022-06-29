import csv
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

class opencl_trace:
    def __init__ (self, write_std_deviation = None, read_std_deviation = None, kernel_exe_std_deviation = None, write_mean = None, read_mean = None, kernel_exe_mean = None):

        self.read_start_time = []
        self.read_end_time = []
        self.write_start_time = []
        self.write_end_time = []
        self.kernel_start_exe_time = []
        self.kernel_end_exe_time = []
        self.write_time = []
        self.read_time = []
        self.kernel_exe_time = []
        self.write_std_deviation = write_std_deviation
        self.read_std_deviation = read_std_deviation
        self.kernel_exe_std_deviation = kernel_exe_std_deviation
        self.write_mean = write_mean
        self.read_mean = read_mean
        self.kernel_exe_mean = kernel_exe_mean

    #Define interface functions
    def get_read_start_time(self):            return self.read_start_time
    def get_read_end_time(self):              return self.read_end_time
    def get_write_start_time(self):           return self.write_start_time
    def get_write_end_time(self):             return self.write_end_time
    def get_kernel_start_exe_time(self):      return self.kernel_start_exe_time
    def get_kernel_end_exe_time(self):        return self.kernel_end_exe_time
    def get_write_time(self):                 return self.write_time
    def get_read_time(self):                  return self.read_time
    def get_kernel_exe_time(self):            return self.kernel_exe_time
    def get_write_std_deviation(self):        return self.write_std_deviation
    def get_read_std_deviation(self):         return self.read_std_deviation
    def get_kernel_exe_std_deviation(self):   return self.kernel_exe_std_deviation
    def get_write_mean(self):                 return self.write_mean
    def get_read_mean(self):                  return self.read_mean
    def get_kernel_exe_mean(self):            return self.kernel_exe_mean

    #Read csv file
    def csv_reader(self, filename):
        event_flag = False
        event_flag_flag = False
        with open (filename, 'r') as f:
            csvreader = csv.reader(f)
            header = next(csvreader)
            for values in csvreader:
                #Checks if values is not empty
                if values:
                    #Reads only what is between EVENTS and DEPENDENCIES
                    if event_flag == True:
                        event_flag_flag = True
                    if values[0] == "EVENTS":
                        event_flag = True
                    elif values[0] == "DEPENDENCIES":
                        event_flag = False
                        event_flag_flag = False

                    if event_flag_flag:
                        if values[4] == "WRITE_BUFFER":
                            if len(values) > 5:
                                self.write_start_time.append(values[2])
                            else:
                                self.write_end_time.append(values[2])
                        elif values[4] == "READ_BUFFER":
                            if len(values) > 5:
                                self.read_start_time.append(values[2])
                            else:
                                self.read_end_time.append(values[2])
                        elif values[4] == "KERNEL_ENQUEUE":
                            if values[7] == "1":
                                self.kernel_start_exe_time.append(values[2])
                            elif values[7] == "0":
                                self.kernel_end_exe_time.append(values[2])

    #Calculates the durations
    def duration_calc(self):
        self.write_time = [float(b) - float(a) for b,a  in zip (self.write_end_time, self.write_start_time)]
        self.read_time = [float(b) - float(a) for b,a  in zip (self.read_end_time, self.read_start_time)]
        self.kernel_exe_time = [float(b) - float(a) for b,a in zip (self.kernel_end_exe_time, self.kernel_start_exe_time)]

    #Calculates standard deviation
    def std_deviation(self):
        self.write_std_deviation = np.std(self.write_time)
        self.read_std_deviation = np.std(self.read_time)
        self.kernel_exe_std_deviation = np.std(self.kernel_exe_time)

    #Calculates mean value of duration
    def mean_calc(self):
        self.write_mean = np.mean(self.write_time)
        self.read_mean = np.mean(self.read_time)
        self.kernel_exe_mean = np.mean(self.kernel_exe_time)

    #Plots stadard deviation and mean
    def plot_std_deviation_mean(self):
        #Code from : "https://www.nbshare.io/notebook/42712841/Understanding-Standard-Deviation-With-Python/"
        values = ["Write", "Read", "Kernel Execution"]
        domain = np.linspace(-0.2, 0.5, 1000) # dividing the distance between -2 and 2 into 1000 points
	
        means = [self.write_mean, self.read_mean, self.kernel_exe_mean]
        std_values = [self.write_std_deviation, self.read_std_deviation, self.kernel_exe_std_deviation]
        
        plt.figure(figsize=(16, 9))
        for mu, std, values in zip(means, std_values, values):
            # pdf stands for Probability Density Function, which is the plot the probabilities of each range of values
            probabilities = norm.pdf(domain, mu, std)
            plt.plot(domain, probabilities, label=f"{values}\n$\mu={mu}$\n$\sigma={std}$\n")
        
        plt.legend(fontsize=8)
        plt.xlabel("Value", fontsize=15)
        plt.ylabel("Probability", fontsize=15)
        plt.show()
        
if __name__ == "__main__":
    csv_values = opencl_trace()
    csv_values.csv_reader("opencl_trace.csv")
    csv_values.duration_calc()
    csv_values.std_deviation()
    csv_values.mean_calc()
#    print("write_start_time: ", csv_values.get_write_start_time())
#    print("wrie_end_time: ", csv_values.get_write_end_time())
#    print("exe_start_time: ", csv_values.get_kernel_start_exe_time())
#    print("write_time: ", csv_values.get_write_time())
#    print("read_time: ", csv_values.get_read_time())
#    print("kernel_exe_time: ", csv_values.get_kernel_exe_time())
    print("write_deviation: ", csv_values.get_write_std_deviation())
    print("read_deviation: ", csv_values.get_read_std_deviation())
    print("kenrel_exe_deviation: ", csv_values.get_kernel_exe_std_deviation())
    print("write_mean: ", csv_values.get_write_mean())
    print("read_mean: ", csv_values.get_read_mean())
    print("kenrel_exe_mean: ", csv_values.get_kernel_exe_mean())

    csv_values.plot_std_deviation_mean()


