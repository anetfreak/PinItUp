import sys
import getopt
import os
import zlib

path_py = os.path.abspath(os.path.join(os.path.dirname(__file__), '../lib'))
print path_py
if not path_py in sys.path:
	sys.path.insert(1,path_py)
del path_py

#Add path to python_citrusleaf
sys.path.append('../lib')

import citrusleaf as cl
import python_citrusleaf as pcl
from array import array
from python_citrusleaf import * 

class DBConn():
    def __init__(self):
        self.createConn()

    def createConn(self):
        # Initialize citrusleaf once
        import citrusleaf as cl
        cl.citrusleaf_init()
        # Create a cluster with a particular starting host
        self.asc = cl.citrusleaf_cluster_create()
        # Add host to the cluster
        return_value = cl.citrusleaf_cluster_add_host(self.asc, "127.0.0.1", 3000, 1000)


    def createKey_Obj(self,key):
        print 'DEBUG: In createKey_Obj for key:',key
        # set up the key. Create a stack object, set its value to a string
        key_obj = cl.cl_object()
        cl.citrusleaf_object_init_str(key_obj, key)
        return key_obj

    def createBins_general(self,bin_name,values,types,num):
        print 'DEBUG: In createBins_general for length:',num
        bins = cl.cl_bin_arr(num)
        print 'DEBUG Bins array created'
        for i in xrange(num):
            print 'DEBUG: creating bin for index: ',i
            b = bins[i]
            print 'DEBUG: bin name: ',bin_name[i] , ' value: ',values[i] , ' type: ',types[i]
            b.bin_name = bin_name[i]
            print 'DEBUG: bin name: ',bin_name[i] , ' value: ',values[i] , ' type: ',types[i]
            if types[i] == "string":
                cl.citrusleaf_object_init_str(b.object, values[i]);
                print 'DEBUG: string bin created'
            elif types[i] == "int":
                cl.citrusleaf_object_init_int(b.object, values[i]);
                print 'DEBUG: int bin created'
            else:
                print 'Wrong Type, use type as "string" or "int"'
            bins[i] = b
        return bins

    def createBins(self):
        # Declaring an array in this interface
        bins = cl.cl_bin_arr(4)
        # Provide values for those bins and then initialize them.
        # Initializing bin of type string
        b0 = bins[0]
        b0.bin_name = "boardName"
        cl.citrusleaf_object_init_str(b0.object, "Board Name");
        # Initializing bin of type string
        b1 = bins[1]
        b1.bin_name = "boardDesc"
        cl.citrusleaf_object_init_str(b1.object, "Board Description");
        # Initializing bin of type string
        b2 = bins[2]
        b2.bin_name = "category"
        cl.citrusleaf_object_init_str(b2.object, "Board category");
        # Initializing bin of type string
        b3 = bins[3]
        b3.bin_name = "isPrivate"
        cl.citrusleaf_object_init_str(b3.object, "Board isPrivate");
        # Assign the structure back to the "bins" variable
        bins[0] = b0
        bins[1] = b1
        bins[2] = b2
        bins[3] = b3
        return bins

    def writeToDB(self,set_name,key_obj,bins,num):
        print 'DEBUG: In writeToDB',num
        return_value = cl.citrusleaf_put(self.asc, "test", set_name, key_obj, bins, num, None);
        if return_value != cl.CITRUSLEAF_OK :
            print "Failure setting values %dn", return_value
            sys.exit(-1);
    
    def readFromDB(self,set_name,key_obj):
        print 'DEBUG: In readFromDB'
        size = cl.new_intp()
        generation = cl.new_intp()
        # Declare a reference pointer for cl_bin *
        bins_get_all = cl.new_cl_bin_p()
        rv = cl.citrusleaf_get_all(self.asc, "test", set_name, key_obj, bins_get_all , size, 100, generation);
        # Number of bins returned
        number_bins = cl.intp_value(size)
        print 'DEBUG: number of bins read is ',number_bins
        # Use helper function get_bins to get the bins from pointer bins_get_all and the number of bins
        bins = pcl.get_bins (bins_get_all, number_bins)
        # Printing value received
        
        result = []
        for i in xrange(number_bins):
            keyvalue = {}
            if(bins[i].object.type)==cl.CL_STR:
                print "Bin name: ",bins[i].bin_name,"Resulting string: ",bins[i].object.u.str
                keyvalue[bins[i].bin_name] = bins[i].object.u.str
            elif(bins[i].object.type)==cl.CL_INT:
                print "Bin name: ",bins[i].bin_name,"Resulting int: ",bins[i].object.u.i64
                keyvalue[bins[i].bin_name] = bins[i].object.u.i64
            elif bins[i].object.type == cl.CL_BLOB:
                binary_data = cl.cdata(bins[i].object.u.blob, bins[i].object.sz)
                print "Bin name: ",bins[i].bin_name,"Resulting decompressed blob: ",zlib.decompress(binary_data)
                keyvalue[bins[i].bin_name] = zlib.decompress(binary_data)
            else:
                print "Bin name: ",bins[i].bin_name,"Unknown bin type: ",bins[i].object.type
                keyvalue[bins[i].bin_name] = bins[i].object.type
            result.append(keyvalue)
        return result

    def cleanup(self):
        cl.citrusleaf_free_bins(bins, number_bins, bins_get_all)
        cl.delete_intp(size)
        cl.delete_intp(generation)
        cl.delete_cl_bin_p(bins_get_all)
