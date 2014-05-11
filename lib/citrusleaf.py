# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_citrusleaf', [dirname(__file__)])
        except ImportError:
            import _citrusleaf
            return _citrusleaf
        if fp is not None:
            try:
                _mod = imp.load_module('_citrusleaf', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _citrusleaf = swig_import_helper()
    del swig_import_helper
else:
    import _citrusleaf
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def cdata(*args):
  return _citrusleaf.cdata(*args)
cdata = _citrusleaf.cdata

def memmove(*args):
  return _citrusleaf.memmove(*args)
memmove = _citrusleaf.memmove
class cl_bin_arr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_bin_arr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_bin_arr, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _citrusleaf.new_cl_bin_arr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_bin_arr
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _citrusleaf.cl_bin_arr___getitem__(self, *args)
    def __setitem__(self, *args): return _citrusleaf.cl_bin_arr___setitem__(self, *args)
    def cast(self): return _citrusleaf.cl_bin_arr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _citrusleaf.cl_bin_arr_frompointer
    if _newclass:frompointer = staticmethod(_citrusleaf.cl_bin_arr_frompointer)
cl_bin_arr_swigregister = _citrusleaf.cl_bin_arr_swigregister
cl_bin_arr_swigregister(cl_bin_arr)

def cl_bin_arr_frompointer(*args):
  return _citrusleaf.cl_bin_arr_frompointer(*args)
cl_bin_arr_frompointer = _citrusleaf.cl_bin_arr_frompointer

class cf_digest_arr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cf_digest_arr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cf_digest_arr, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _citrusleaf.new_cf_digest_arr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cf_digest_arr
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _citrusleaf.cf_digest_arr___getitem__(self, *args)
    def __setitem__(self, *args): return _citrusleaf.cf_digest_arr___setitem__(self, *args)
    def cast(self): return _citrusleaf.cf_digest_arr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _citrusleaf.cf_digest_arr_frompointer
    if _newclass:frompointer = staticmethod(_citrusleaf.cf_digest_arr_frompointer)
cf_digest_arr_swigregister = _citrusleaf.cf_digest_arr_swigregister
cf_digest_arr_swigregister(cf_digest_arr)

def cf_digest_arr_frompointer(*args):
  return _citrusleaf.cf_digest_arr_frompointer(*args)
cf_digest_arr_frompointer = _citrusleaf.cf_digest_arr_frompointer

class cl_record_arr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_record_arr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_record_arr, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _citrusleaf.new_cl_record_arr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_record_arr
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _citrusleaf.cl_record_arr___getitem__(self, *args)
    def __setitem__(self, *args): return _citrusleaf.cl_record_arr___setitem__(self, *args)
    def cast(self): return _citrusleaf.cl_record_arr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _citrusleaf.cl_record_arr_frompointer
    if _newclass:frompointer = staticmethod(_citrusleaf.cl_record_arr_frompointer)
cl_record_arr_swigregister = _citrusleaf.cl_record_arr_swigregister
cl_record_arr_swigregister(cl_record_arr)

def cl_record_arr_frompointer(*args):
  return _citrusleaf.cl_record_arr_frompointer(*args)
cl_record_arr_frompointer = _citrusleaf.cl_record_arr_frompointer

class cl_op_arr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_op_arr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_op_arr, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _citrusleaf.new_cl_op_arr(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_op_arr
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _citrusleaf.cl_op_arr___getitem__(self, *args)
    def __setitem__(self, *args): return _citrusleaf.cl_op_arr___setitem__(self, *args)
    def cast(self): return _citrusleaf.cl_op_arr_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _citrusleaf.cl_op_arr_frompointer
    if _newclass:frompointer = staticmethod(_citrusleaf.cl_op_arr_frompointer)
cl_op_arr_swigregister = _citrusleaf.cl_op_arr_swigregister
cl_op_arr_swigregister(cl_op_arr)

def cl_op_arr_frompointer(*args):
  return _citrusleaf.cl_op_arr_frompointer(*args)
cl_op_arr_frompointer = _citrusleaf.cl_op_arr_frompointer


def new_intp():
  return _citrusleaf.new_intp()
new_intp = _citrusleaf.new_intp

def copy_intp(*args):
  return _citrusleaf.copy_intp(*args)
copy_intp = _citrusleaf.copy_intp

def delete_intp(*args):
  return _citrusleaf.delete_intp(*args)
delete_intp = _citrusleaf.delete_intp

def intp_assign(*args):
  return _citrusleaf.intp_assign(*args)
intp_assign = _citrusleaf.intp_assign

def intp_value(*args):
  return _citrusleaf.intp_value(*args)
intp_value = _citrusleaf.intp_value

def new_cl_bin_p():
  return _citrusleaf.new_cl_bin_p()
new_cl_bin_p = _citrusleaf.new_cl_bin_p

def copy_cl_bin_p(*args):
  return _citrusleaf.copy_cl_bin_p(*args)
copy_cl_bin_p = _citrusleaf.copy_cl_bin_p

def delete_cl_bin_p(*args):
  return _citrusleaf.delete_cl_bin_p(*args)
delete_cl_bin_p = _citrusleaf.delete_cl_bin_p

def cl_bin_p_assign(*args):
  return _citrusleaf.cl_bin_p_assign(*args)
cl_bin_p_assign = _citrusleaf.cl_bin_p_assign

def cl_bin_p_value(*args):
  return _citrusleaf.cl_bin_p_value(*args)
cl_bin_p_value = _citrusleaf.cl_bin_p_value

def new_charp():
  return _citrusleaf.new_charp()
new_charp = _citrusleaf.new_charp

def copy_charp(*args):
  return _citrusleaf.copy_charp(*args)
copy_charp = _citrusleaf.copy_charp

def delete_charp(*args):
  return _citrusleaf.delete_charp(*args)
delete_charp = _citrusleaf.delete_charp

def charp_assign(*args):
  return _citrusleaf.charp_assign(*args)
charp_assign = _citrusleaf.charp_assign

def charp_value(*args):
  return _citrusleaf.charp_value(*args)
charp_value = _citrusleaf.charp_value

def new_cf_digest_p():
  return _citrusleaf.new_cf_digest_p()
new_cf_digest_p = _citrusleaf.new_cf_digest_p

def copy_cf_digest_p(*args):
  return _citrusleaf.copy_cf_digest_p(*args)
copy_cf_digest_p = _citrusleaf.copy_cf_digest_p

def delete_cf_digest_p(*args):
  return _citrusleaf.delete_cf_digest_p(*args)
delete_cf_digest_p = _citrusleaf.delete_cf_digest_p

def cf_digest_p_assign(*args):
  return _citrusleaf.cf_digest_p_assign(*args)
cf_digest_p_assign = _citrusleaf.cf_digest_p_assign

def cf_digest_p_value(*args):
  return _citrusleaf.cf_digest_p_value(*args)
cf_digest_p_value = _citrusleaf.cf_digest_p_value
class cl_record(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_record, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_record, name)
    __repr__ = _swig_repr
    __swig_setmethods__["gen"] = _citrusleaf.cl_record_gen_set
    __swig_getmethods__["gen"] = _citrusleaf.cl_record_gen_get
    if _newclass:gen = _swig_property(_citrusleaf.cl_record_gen_get, _citrusleaf.cl_record_gen_set)
    __swig_setmethods__["bin"] = _citrusleaf.cl_record_bin_set
    __swig_getmethods__["bin"] = _citrusleaf.cl_record_bin_get
    if _newclass:bin = _swig_property(_citrusleaf.cl_record_bin_get, _citrusleaf.cl_record_bin_set)
    __swig_setmethods__["ns"] = _citrusleaf.cl_record_ns_set
    __swig_getmethods__["ns"] = _citrusleaf.cl_record_ns_get
    if _newclass:ns = _swig_property(_citrusleaf.cl_record_ns_get, _citrusleaf.cl_record_ns_set)
    __swig_setmethods__["set"] = _citrusleaf.cl_record_set_set
    __swig_getmethods__["set"] = _citrusleaf.cl_record_set_get
    if _newclass:set = _swig_property(_citrusleaf.cl_record_set_get, _citrusleaf.cl_record_set_set)
    __swig_setmethods__["record_ttl"] = _citrusleaf.cl_record_record_ttl_set
    __swig_getmethods__["record_ttl"] = _citrusleaf.cl_record_record_ttl_get
    if _newclass:record_ttl = _swig_property(_citrusleaf.cl_record_record_ttl_get, _citrusleaf.cl_record_record_ttl_set)
    __swig_setmethods__["n_bins"] = _citrusleaf.cl_record_n_bins_set
    __swig_getmethods__["n_bins"] = _citrusleaf.cl_record_n_bins_get
    if _newclass:n_bins = _swig_property(_citrusleaf.cl_record_n_bins_get, _citrusleaf.cl_record_n_bins_set)
    __swig_setmethods__["digest"] = _citrusleaf.cl_record_digest_set
    __swig_getmethods__["digest"] = _citrusleaf.cl_record_digest_get
    if _newclass:digest = _swig_property(_citrusleaf.cl_record_digest_get, _citrusleaf.cl_record_digest_set)
    def __init__(self): 
        this = _citrusleaf.new_cl_record()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_record
    __del__ = lambda self : None;
cl_record_swigregister = _citrusleaf.cl_record_swigregister
cl_record_swigregister(cl_record)

class BatchResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BatchResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BatchResult, name)
    __repr__ = _swig_repr
    __swig_setmethods__["records"] = _citrusleaf.BatchResult_records_set
    __swig_getmethods__["records"] = _citrusleaf.BatchResult_records_get
    if _newclass:records = _swig_property(_citrusleaf.BatchResult_records_get, _citrusleaf.BatchResult_records_set)
    __swig_setmethods__["index"] = _citrusleaf.BatchResult_index_set
    __swig_getmethods__["index"] = _citrusleaf.BatchResult_index_get
    if _newclass:index = _swig_property(_citrusleaf.BatchResult_index_get, _citrusleaf.BatchResult_index_set)
    __swig_setmethods__["rv"] = _citrusleaf.BatchResult_rv_set
    __swig_getmethods__["rv"] = _citrusleaf.BatchResult_rv_get
    if _newclass:rv = _swig_property(_citrusleaf.BatchResult_rv_get, _citrusleaf.BatchResult_rv_set)
    def __init__(self): 
        this = _citrusleaf.new_BatchResult()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_BatchResult
    __del__ = lambda self : None;
BatchResult_swigregister = _citrusleaf.BatchResult_swigregister
BatchResult_swigregister(BatchResult)

class cf_digest(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cf_digest, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cf_digest, name)
    __repr__ = _swig_repr
    __swig_setmethods__["digest"] = _citrusleaf.cf_digest_digest_set
    __swig_getmethods__["digest"] = _citrusleaf.cf_digest_digest_get
    if _newclass:digest = _swig_property(_citrusleaf.cf_digest_digest_get, _citrusleaf.cf_digest_digest_set)
    def __init__(self): 
        this = _citrusleaf.new_cf_digest()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cf_digest
    __del__ = lambda self : None;
cf_digest_swigregister = _citrusleaf.cf_digest_swigregister
cf_digest_swigregister(cf_digest)

class cl_bin(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_bin, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_bin, name)
    __repr__ = _swig_repr
    __swig_setmethods__["bin_name"] = _citrusleaf.cl_bin_bin_name_set
    __swig_getmethods__["bin_name"] = _citrusleaf.cl_bin_bin_name_get
    if _newclass:bin_name = _swig_property(_citrusleaf.cl_bin_bin_name_get, _citrusleaf.cl_bin_bin_name_set)
    __swig_setmethods__["object"] = _citrusleaf.cl_bin_object_set
    __swig_getmethods__["object"] = _citrusleaf.cl_bin_object_get
    if _newclass:object = _swig_property(_citrusleaf.cl_bin_object_get, _citrusleaf.cl_bin_object_set)
    def __init__(self): 
        this = _citrusleaf.new_cl_bin()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_bin
    __del__ = lambda self : None;
cl_bin_swigregister = _citrusleaf.cl_bin_swigregister
cl_bin_swigregister(cl_bin)

class cl_object(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_object, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_object, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _citrusleaf.cl_object_type_set
    __swig_getmethods__["type"] = _citrusleaf.cl_object_type_get
    if _newclass:type = _swig_property(_citrusleaf.cl_object_type_get, _citrusleaf.cl_object_type_set)
    __swig_setmethods__["sz"] = _citrusleaf.cl_object_sz_set
    __swig_getmethods__["sz"] = _citrusleaf.cl_object_sz_get
    if _newclass:sz = _swig_property(_citrusleaf.cl_object_sz_get, _citrusleaf.cl_object_sz_set)
    __swig_setmethods__["free"] = _citrusleaf.cl_object_free_set
    __swig_getmethods__["free"] = _citrusleaf.cl_object_free_get
    if _newclass:free = _swig_property(_citrusleaf.cl_object_free_get, _citrusleaf.cl_object_free_set)
    __swig_getmethods__["u"] = _citrusleaf.cl_object_u_get
    if _newclass:u = _swig_property(_citrusleaf.cl_object_u_get)
    def __init__(self): 
        this = _citrusleaf.new_cl_object()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_object
    __del__ = lambda self : None;
cl_object_swigregister = _citrusleaf.cl_object_swigregister
cl_object_swigregister(cl_object)

class cl_object_u(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_object_u, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_object_u, name)
    __repr__ = _swig_repr
    __swig_setmethods__["str"] = _citrusleaf.cl_object_u_str_set
    __swig_getmethods__["str"] = _citrusleaf.cl_object_u_str_get
    if _newclass:str = _swig_property(_citrusleaf.cl_object_u_str_get, _citrusleaf.cl_object_u_str_set)
    __swig_setmethods__["blob"] = _citrusleaf.cl_object_u_blob_set
    __swig_getmethods__["blob"] = _citrusleaf.cl_object_u_blob_get
    if _newclass:blob = _swig_property(_citrusleaf.cl_object_u_blob_get, _citrusleaf.cl_object_u_blob_set)
    __swig_setmethods__["i64"] = _citrusleaf.cl_object_u_i64_set
    __swig_getmethods__["i64"] = _citrusleaf.cl_object_u_i64_get
    if _newclass:i64 = _swig_property(_citrusleaf.cl_object_u_i64_get, _citrusleaf.cl_object_u_i64_set)
    def __init__(self): 
        this = _citrusleaf.new_cl_object_u()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_object_u
    __del__ = lambda self : None;
cl_object_u_swigregister = _citrusleaf.cl_object_u_swigregister
cl_object_u_swigregister(cl_object_u)

CL_NULL = _citrusleaf.CL_NULL
CL_INT = _citrusleaf.CL_INT
CL_FLOAT = _citrusleaf.CL_FLOAT
CL_STR = _citrusleaf.CL_STR
CL_BLOB = _citrusleaf.CL_BLOB
CL_TIMESTAMP = _citrusleaf.CL_TIMESTAMP
CL_DIGEST = _citrusleaf.CL_DIGEST
CL_JAVA_BLOB = _citrusleaf.CL_JAVA_BLOB
CL_CSHARP_BLOB = _citrusleaf.CL_CSHARP_BLOB
CL_PYTHON_BLOB = _citrusleaf.CL_PYTHON_BLOB
CL_RUBY_BLOB = _citrusleaf.CL_RUBY_BLOB
CL_PHP_BLOB = _citrusleaf.CL_PHP_BLOB
CL_UNKNOWN = _citrusleaf.CL_UNKNOWN
CITRUSLEAF_FAIL_ASYNCQ_FULL = _citrusleaf.CITRUSLEAF_FAIL_ASYNCQ_FULL
CITRUSLEAF_FAIL_TIMEOUT = _citrusleaf.CITRUSLEAF_FAIL_TIMEOUT
CITRUSLEAF_FAIL_CLIENT = _citrusleaf.CITRUSLEAF_FAIL_CLIENT
CITRUSLEAF_OK = _citrusleaf.CITRUSLEAF_OK
CITRUSLEAF_FAIL_UNKNOWN = _citrusleaf.CITRUSLEAF_FAIL_UNKNOWN
CITRUSLEAF_FAIL_NOTFOUND = _citrusleaf.CITRUSLEAF_FAIL_NOTFOUND
CITRUSLEAF_FAIL_GENERATION = _citrusleaf.CITRUSLEAF_FAIL_GENERATION
CITRUSLEAF_FAIL_PARAMETER = _citrusleaf.CITRUSLEAF_FAIL_PARAMETER
CITRUSLEAF_FAIL_KEY_EXISTS = _citrusleaf.CITRUSLEAF_FAIL_KEY_EXISTS
CITRUSLEAF_FAIL_BIN_EXISTS = _citrusleaf.CITRUSLEAF_FAIL_BIN_EXISTS
CITRUSLEAF_FAIL_CLUSTER_KEY_MISMATCH = _citrusleaf.CITRUSLEAF_FAIL_CLUSTER_KEY_MISMATCH
CITRUSLEAF_FAIL_PARTITION_OUT_OF_SPACE = _citrusleaf.CITRUSLEAF_FAIL_PARTITION_OUT_OF_SPACE
CITRUSLEAF_FAIL_SERVERSIDE_TIMEOUT = _citrusleaf.CITRUSLEAF_FAIL_SERVERSIDE_TIMEOUT
CITRUSLEAF_FAIL_NOXDS = _citrusleaf.CITRUSLEAF_FAIL_NOXDS
CITRUSLEAF_FAIL_UNAVAILABLE = _citrusleaf.CITRUSLEAF_FAIL_UNAVAILABLE
CITRUSLEAF_FAIL_INCOMPATIBLE_TYPE = _citrusleaf.CITRUSLEAF_FAIL_INCOMPATIBLE_TYPE
CITRUSLEAF_FAIL_RECORD_TOO_BIG = _citrusleaf.CITRUSLEAF_FAIL_RECORD_TOO_BIG
CITRUSLEAF_FAIL_KEY_BUSY = _citrusleaf.CITRUSLEAF_FAIL_KEY_BUSY
class cl_write_parameters(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_write_parameters, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_write_parameters, name)
    __repr__ = _swig_repr
    __swig_setmethods__["unique"] = _citrusleaf.cl_write_parameters_unique_set
    __swig_getmethods__["unique"] = _citrusleaf.cl_write_parameters_unique_get
    if _newclass:unique = _swig_property(_citrusleaf.cl_write_parameters_unique_get, _citrusleaf.cl_write_parameters_unique_set)
    __swig_setmethods__["unique_bin"] = _citrusleaf.cl_write_parameters_unique_bin_set
    __swig_getmethods__["unique_bin"] = _citrusleaf.cl_write_parameters_unique_bin_get
    if _newclass:unique_bin = _swig_property(_citrusleaf.cl_write_parameters_unique_bin_get, _citrusleaf.cl_write_parameters_unique_bin_set)
    __swig_setmethods__["use_generation"] = _citrusleaf.cl_write_parameters_use_generation_set
    __swig_getmethods__["use_generation"] = _citrusleaf.cl_write_parameters_use_generation_get
    if _newclass:use_generation = _swig_property(_citrusleaf.cl_write_parameters_use_generation_get, _citrusleaf.cl_write_parameters_use_generation_set)
    __swig_setmethods__["use_generation_gt"] = _citrusleaf.cl_write_parameters_use_generation_gt_set
    __swig_getmethods__["use_generation_gt"] = _citrusleaf.cl_write_parameters_use_generation_gt_get
    if _newclass:use_generation_gt = _swig_property(_citrusleaf.cl_write_parameters_use_generation_gt_get, _citrusleaf.cl_write_parameters_use_generation_gt_set)
    __swig_setmethods__["use_generation_dup"] = _citrusleaf.cl_write_parameters_use_generation_dup_set
    __swig_getmethods__["use_generation_dup"] = _citrusleaf.cl_write_parameters_use_generation_dup_get
    if _newclass:use_generation_dup = _swig_property(_citrusleaf.cl_write_parameters_use_generation_dup_get, _citrusleaf.cl_write_parameters_use_generation_dup_set)
    __swig_setmethods__["generation"] = _citrusleaf.cl_write_parameters_generation_set
    __swig_getmethods__["generation"] = _citrusleaf.cl_write_parameters_generation_get
    if _newclass:generation = _swig_property(_citrusleaf.cl_write_parameters_generation_get, _citrusleaf.cl_write_parameters_generation_set)
    __swig_setmethods__["timeout_ms"] = _citrusleaf.cl_write_parameters_timeout_ms_set
    __swig_getmethods__["timeout_ms"] = _citrusleaf.cl_write_parameters_timeout_ms_get
    if _newclass:timeout_ms = _swig_property(_citrusleaf.cl_write_parameters_timeout_ms_get, _citrusleaf.cl_write_parameters_timeout_ms_set)
    __swig_setmethods__["record_ttl"] = _citrusleaf.cl_write_parameters_record_ttl_set
    __swig_getmethods__["record_ttl"] = _citrusleaf.cl_write_parameters_record_ttl_get
    if _newclass:record_ttl = _swig_property(_citrusleaf.cl_write_parameters_record_ttl_get, _citrusleaf.cl_write_parameters_record_ttl_set)
    __swig_setmethods__["w_pol"] = _citrusleaf.cl_write_parameters_w_pol_set
    __swig_getmethods__["w_pol"] = _citrusleaf.cl_write_parameters_w_pol_get
    if _newclass:w_pol = _swig_property(_citrusleaf.cl_write_parameters_w_pol_get, _citrusleaf.cl_write_parameters_w_pol_set)
    def __init__(self): 
        this = _citrusleaf.new_cl_write_parameters()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_write_parameters
    __del__ = lambda self : None;
cl_write_parameters_swigregister = _citrusleaf.cl_write_parameters_swigregister
cl_write_parameters_swigregister(cl_write_parameters)

CL_OP_WRITE = _citrusleaf.CL_OP_WRITE
CL_OP_READ = _citrusleaf.CL_OP_READ
CL_OP_INCR = _citrusleaf.CL_OP_INCR
CL_OP_MC_INCR = _citrusleaf.CL_OP_MC_INCR
CL_OP_PREPEND = _citrusleaf.CL_OP_PREPEND
CL_OP_APPEND = _citrusleaf.CL_OP_APPEND
CL_OP_MC_PREPEND = _citrusleaf.CL_OP_MC_PREPEND
CL_OP_MC_APPEND = _citrusleaf.CL_OP_MC_APPEND
CL_OP_TOUCH = _citrusleaf.CL_OP_TOUCH
CL_OP_MC_TOUCH = _citrusleaf.CL_OP_MC_TOUCH
class cl_operation(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, cl_operation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, cl_operation, name)
    __repr__ = _swig_repr
    __swig_setmethods__["bin"] = _citrusleaf.cl_operation_bin_set
    __swig_getmethods__["bin"] = _citrusleaf.cl_operation_bin_get
    if _newclass:bin = _swig_property(_citrusleaf.cl_operation_bin_get, _citrusleaf.cl_operation_bin_set)
    __swig_setmethods__["op"] = _citrusleaf.cl_operation_op_set
    __swig_getmethods__["op"] = _citrusleaf.cl_operation_op_get
    if _newclass:op = _swig_property(_citrusleaf.cl_operation_op_get, _citrusleaf.cl_operation_op_set)
    def __init__(self): 
        this = _citrusleaf.new_cl_operation()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _citrusleaf.delete_cl_operation
    __del__ = lambda self : None;
cl_operation_swigregister = _citrusleaf.cl_operation_swigregister
cl_operation_swigregister(cl_operation)


def citrusleaf_init():
  return _citrusleaf.citrusleaf_init()
citrusleaf_init = _citrusleaf.citrusleaf_init

def citrusleaf_shutdown():
  return _citrusleaf.citrusleaf_shutdown()
citrusleaf_shutdown = _citrusleaf.citrusleaf_shutdown

def citrusleaf_cluster_create():
  return _citrusleaf.citrusleaf_cluster_create()
citrusleaf_cluster_create = _citrusleaf.citrusleaf_cluster_create

def citrusleaf_cluster_use_nbconnect(*args):
  return _citrusleaf.citrusleaf_cluster_use_nbconnect(*args)
citrusleaf_cluster_use_nbconnect = _citrusleaf.citrusleaf_cluster_use_nbconnect

def citrusleaf_cluster_add_host(*args):
  return _citrusleaf.citrusleaf_cluster_add_host(*args)
citrusleaf_cluster_add_host = _citrusleaf.citrusleaf_cluster_add_host

def citrusleaf_cluster_destroy(*args):
  return _citrusleaf.citrusleaf_cluster_destroy(*args)
citrusleaf_cluster_destroy = _citrusleaf.citrusleaf_cluster_destroy

def cl_write_parameters_set_default(*args):
  return _citrusleaf.cl_write_parameters_set_default(*args)
cl_write_parameters_set_default = _citrusleaf.cl_write_parameters_set_default

def citrusleaf_object_init(*args):
  return _citrusleaf.citrusleaf_object_init(*args)
citrusleaf_object_init = _citrusleaf.citrusleaf_object_init

def citrusleaf_object_init_str(*args):
  return _citrusleaf.citrusleaf_object_init_str(*args)
citrusleaf_object_init_str = _citrusleaf.citrusleaf_object_init_str

def citrusleaf_object_init_str2(*args):
  return _citrusleaf.citrusleaf_object_init_str2(*args)
citrusleaf_object_init_str2 = _citrusleaf.citrusleaf_object_init_str2

def citrusleaf_object_init_blob(*args):
  return _citrusleaf.citrusleaf_object_init_blob(*args)
citrusleaf_object_init_blob = _citrusleaf.citrusleaf_object_init_blob

def citrusleaf_object_init_blob2(*args):
  return _citrusleaf.citrusleaf_object_init_blob2(*args)
citrusleaf_object_init_blob2 = _citrusleaf.citrusleaf_object_init_blob2

def citrusleaf_object_init_int(*args):
  return _citrusleaf.citrusleaf_object_init_int(*args)
citrusleaf_object_init_int = _citrusleaf.citrusleaf_object_init_int

def citrusleaf_object_init_null(*args):
  return _citrusleaf.citrusleaf_object_init_null(*args)
citrusleaf_object_init_null = _citrusleaf.citrusleaf_object_init_null

def citrusleaf_put(*args):
  return _citrusleaf.citrusleaf_put(*args)
citrusleaf_put = _citrusleaf.citrusleaf_put

def citrusleaf_get(*args):
  return _citrusleaf.citrusleaf_get(*args)
citrusleaf_get = _citrusleaf.citrusleaf_get

def citrusleaf_get_all(*args):
  return _citrusleaf.citrusleaf_get_all(*args)
citrusleaf_get_all = _citrusleaf.citrusleaf_get_all

def citrusleaf_get_digest(*args):
  return _citrusleaf.citrusleaf_get_digest(*args)
citrusleaf_get_digest = _citrusleaf.citrusleaf_get_digest

def citrusleaf_put_digest(*args):
  return _citrusleaf.citrusleaf_put_digest(*args)
citrusleaf_put_digest = _citrusleaf.citrusleaf_put_digest

def citrusleaf_delete_digest(*args):
  return _citrusleaf.citrusleaf_delete_digest(*args)
citrusleaf_delete_digest = _citrusleaf.citrusleaf_delete_digest

def citrusleaf_delete(*args):
  return _citrusleaf.citrusleaf_delete(*args)
citrusleaf_delete = _citrusleaf.citrusleaf_delete

def get_name(*args):
  return _citrusleaf.get_name(*args)
get_name = _citrusleaf.get_name

def get_object(*args):
  return _citrusleaf.get_object(*args)
get_object = _citrusleaf.get_object

def citrusleaf_bins_free(*args):
  return _citrusleaf.citrusleaf_bins_free(*args)
citrusleaf_bins_free = _citrusleaf.citrusleaf_bins_free

def citrusleaf_batch_get(*args):
  return _citrusleaf.citrusleaf_batch_get(*args)
citrusleaf_batch_get = _citrusleaf.citrusleaf_batch_get

def citrusleaf_calculate_digest(*args):
  return _citrusleaf.citrusleaf_calculate_digest(*args)
citrusleaf_calculate_digest = _citrusleaf.citrusleaf_calculate_digest

def free(*args):
  return _citrusleaf.free(*args)
free = _citrusleaf.free

def citrusleaf_free_bins(*args):
  return _citrusleaf.citrusleaf_free_bins(*args)
citrusleaf_free_bins = _citrusleaf.citrusleaf_free_bins

def citrusleaf_operate(*args):
  return _citrusleaf.citrusleaf_operate(*args)
citrusleaf_operate = _citrusleaf.citrusleaf_operate

def citrusleaf_use_shm(*args):
  return _citrusleaf.citrusleaf_use_shm(*args)
citrusleaf_use_shm = _citrusleaf.citrusleaf_use_shm

def citrusleaf_async_initialize(*args):
  return _citrusleaf.citrusleaf_async_initialize(*args)
citrusleaf_async_initialize = _citrusleaf.citrusleaf_async_initialize

def citrusleaf_async_put_forget(*args):
  return _citrusleaf.citrusleaf_async_put_forget(*args)
citrusleaf_async_put_forget = _citrusleaf.citrusleaf_async_put_forget

def citrusleaf_async_put_digest_forget(*args):
  return _citrusleaf.citrusleaf_async_put_digest_forget(*args)
citrusleaf_async_put_digest_forget = _citrusleaf.citrusleaf_async_put_digest_forget
# This file is compatible with both classic and new-style classes.

