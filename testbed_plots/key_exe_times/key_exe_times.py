class keyExeTimes:
    def __init__ (self, ar_buff_size, ar_num_buff, ar_time_sw, ar_obj_migration, ar_wait_kernel):

        #Setting buffer size array
        if ar_buff_size is None:
            self.ar_buff_size = []
        elif isinstance(ar_buff_size, list):
            self.ar_buff_size = ar_buff_size
        else:
            raise TypeError("Unsupported ar_buff_size type: ", ar_buff_size)

        #Setting number of buffers array
        if ar_num_buff is None:
            self.ar_num_buff = []
        elif isinstance(ar_num_buff, list):
            self.ar_num_buff = ar_num_buff
        else:
            raise TypeError("Unsupported ar_num_buff type: ", ar_num_buff)
        
        #Setting software time execution array
        if ar_time_sw is None:
            self.ar_time_sw = []
        elif isinstance(ar_time_sw, list):
            self.ar_time_sw = ar_time_sw
        else:
            raise TypeError("Unsupported ar_time_sw type: ", ar_time_sw)

        #Setting times for object migraiton array
        if ar_obj_migration is None:
            self.ar_obj_migration = []
        elif isinstance(ar_obj_migration, list):
            self.ar_obj_migration = ar_obj_migration
        else:
            raise TypeError("Unsupported ar_obj_migration type: ", ar_obj_migration)

        #Setting times for kernel execution time array
        if ar_wait_kernel is None:
            self.ar_wait_kernel = []
        elif isinstance(ar_wait_kernel, list):
            self.ar_wait_kernel = ar_wait_kernel
        else:
            raise TypeError("Unsupported ar_wait_kernel type: ", ar_wait_kernel)

        #Define interface funtions
        def get_ar_buff_size(self):     return self.ar_buff_size
        def get_ar_num_buff(self):      return self.ar_num_buff
        def get_ar_time_sw(self):       return self.ar_time_sw
        def get_ar_obj_migration(self): return self.ar_obj_migration
        def get_ar_wait_kernel(self):   return self.ar_wait_kernel
