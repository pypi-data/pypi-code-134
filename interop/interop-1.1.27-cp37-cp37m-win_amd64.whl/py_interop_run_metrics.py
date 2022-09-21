# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _py_interop_run_metrics
else:
    import _py_interop_run_metrics

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class SwigPyIterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _py_interop_run_metrics.delete_SwigPyIterator

    def value(self):
        return _py_interop_run_metrics.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _py_interop_run_metrics.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _py_interop_run_metrics.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _py_interop_run_metrics.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _py_interop_run_metrics.SwigPyIterator_equal(self, x)

    def copy(self):
        return _py_interop_run_metrics.SwigPyIterator_copy(self)

    def next(self):
        return _py_interop_run_metrics.SwigPyIterator_next(self)

    def __next__(self):
        return _py_interop_run_metrics.SwigPyIterator___next__(self)

    def previous(self):
        return _py_interop_run_metrics.SwigPyIterator_previous(self)

    def advance(self, n):
        return _py_interop_run_metrics.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _py_interop_run_metrics.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _py_interop_run_metrics.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _py_interop_run_metrics.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _py_interop_run_metrics.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _py_interop_run_metrics.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _py_interop_run_metrics.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self

# Register SwigPyIterator in _py_interop_run_metrics:
_py_interop_run_metrics.SwigPyIterator_swigregister(SwigPyIterator)

import interop.py_interop_run
import interop.py_interop_comm
import interop.py_interop_metrics
class invalid_channel_exception(interop.py_interop_run.base_exception):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesg):
        _py_interop_run_metrics.invalid_channel_exception_swiginit(self, _py_interop_run_metrics.new_invalid_channel_exception(mesg))

    def __str__(self):
        return _py_interop_run_metrics.invalid_channel_exception___str__(self)
    __swig_destroy__ = _py_interop_run_metrics.delete_invalid_channel_exception

# Register invalid_channel_exception in _py_interop_run_metrics:
_py_interop_run_metrics.invalid_channel_exception_swigregister(invalid_channel_exception)

class invalid_metric_type(interop.py_interop_run.base_exception):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesg):
        _py_interop_run_metrics.invalid_metric_type_swiginit(self, _py_interop_run_metrics.new_invalid_metric_type(mesg))

    def __str__(self):
        return _py_interop_run_metrics.invalid_metric_type___str__(self)
    __swig_destroy__ = _py_interop_run_metrics.delete_invalid_metric_type

# Register invalid_metric_type in _py_interop_run_metrics:
_py_interop_run_metrics.invalid_metric_type_swigregister(invalid_metric_type)

class invalid_parameter(interop.py_interop_run.base_exception):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, mesg):
        _py_interop_run_metrics.invalid_parameter_swiginit(self, _py_interop_run_metrics.new_invalid_parameter(mesg))

    def __str__(self):
        return _py_interop_run_metrics.invalid_parameter___str__(self)
    __swig_destroy__ = _py_interop_run_metrics.delete_invalid_parameter

# Register invalid_parameter in _py_interop_run_metrics:
_py_interop_run_metrics.invalid_parameter_swigregister(invalid_parameter)


def copy_focus(metrics, focus_scores, channel, n):
    return _py_interop_run_metrics.copy_focus(metrics, focus_scores, channel, n)

def count_q_metric_bins(*args):
    return _py_interop_run_metrics.count_q_metric_bins(*args)

def populate_cumulative_distribution(*args):
    return _py_interop_run_metrics.populate_cumulative_distribution(*args)

def requires_legacy_bins(count):
    return _py_interop_run_metrics.requires_legacy_bins(count)

def compress_q_metrics(*args):
    return _py_interop_run_metrics.compress_q_metrics(*args)

def populate_legacy_q_score_bins(*args):
    return _py_interop_run_metrics.populate_legacy_q_score_bins(*args)

def count_qvals(*args):
    return _py_interop_run_metrics.count_qvals(*args)

def is_compressed(*args):
    return _py_interop_run_metrics.is_compressed(*args)

def max_qval(*args):
    return _py_interop_run_metrics.max_qval(*args)

def index_for_q_value(*args):
    return _py_interop_run_metrics.index_for_q_value(*args)

def create_collapse_q_metrics(metric_set, collapsed):
    return _py_interop_run_metrics.create_collapse_q_metrics(metric_set, collapsed)

def create_q_metrics_by_lane(metric_set, bylane, instrument):
    return _py_interop_run_metrics.create_q_metrics_by_lane(metric_set, bylane, instrument)

def to_group(type):
    return _py_interop_run_metrics.to_group(type)

def to_description(type):
    return _py_interop_run_metrics.to_description(type)

def list_descriptions(types):
    return _py_interop_run_metrics.list_descriptions(types)

def to_feature(type):
    return _py_interop_run_metrics.to_feature(type)

def to_group_feature(type):
    return _py_interop_run_metrics.to_group_feature(type)

def is_base_metric(type):
    return _py_interop_run_metrics.is_base_metric(type)

def is_channel_metric(type):
    return _py_interop_run_metrics.is_channel_metric(type)

def is_read_metric(type):
    return _py_interop_run_metrics.is_read_metric(type)

def is_cycle_metric(type):
    return _py_interop_run_metrics.is_cycle_metric(type)

def is_tile_metric(type):
    return _py_interop_run_metrics.is_tile_metric(type)

def list_metrics_to_load_metric_group(*args):
    return _py_interop_run_metrics.list_metrics_to_load_metric_group(*args)

def list_metrics_to_load_by_group(*args):
    return _py_interop_run_metrics.list_metrics_to_load_by_group(*args)

def list_metrics_to_load_by_type(*args):
    return _py_interop_run_metrics.list_metrics_to_load_by_type(*args)

def list_metrics_to_load_metric_groups(*args):
    return _py_interop_run_metrics.list_metrics_to_load_metric_groups(*args)

def list_metrics_to_load_by_groups(*args):
    return _py_interop_run_metrics.list_metrics_to_load_by_groups(*args)

def list_metrics_to_load_by_types(*args):
    return _py_interop_run_metrics.list_metrics_to_load_by_types(*args)

def list_metrics_to_load(*args):
    return _py_interop_run_metrics.list_metrics_to_load(*args)

def list_summary_metric_groups(*args):
    return _py_interop_run_metrics.list_summary_metric_groups(*args)

def list_index_summary_metric_groups(groups):
    return _py_interop_run_metrics.list_index_summary_metric_groups(groups)

def list_summary_metrics_to_load(*args):
    return _py_interop_run_metrics.list_summary_metrics_to_load(*args)

def list_index_metrics_to_load(valid_to_load):
    return _py_interop_run_metrics.list_index_metrics_to_load(valid_to_load)

def list_analysis_metrics_to_load(valid_to_load):
    return _py_interop_run_metrics.list_analysis_metrics_to_load(valid_to_load)
class run_metrics(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _py_interop_run_metrics.run_metrics_swiginit(self, _py_interop_run_metrics.new_run_metrics(*args))

    def read(self, *args):
        return _py_interop_run_metrics.run_metrics_read(self, *args)

    def read_xml(self, run_folder):
        return _py_interop_run_metrics.run_metrics_read_xml(self, run_folder)

    def read_run_info(self, run_folder):
        return _py_interop_run_metrics.run_metrics_read_run_info(self, run_folder)

    def read_run_parameters(self, run_folder, force_load=False):
        return _py_interop_run_metrics.run_metrics_read_run_parameters(self, run_folder, force_load)

    def finalize_after_load(self, *args):
        return _py_interop_run_metrics.run_metrics_finalize_after_load(self, *args)

    def empty(self):
        return _py_interop_run_metrics.run_metrics_empty(self)

    def legacy_channel_update(self, type):
        return _py_interop_run_metrics.run_metrics_legacy_channel_update(self, type)

    def set_naming_method(self, naming_method):
        return _py_interop_run_metrics.run_metrics_set_naming_method(self, naming_method)

    def count_legacy_bins(self, *args):
        return _py_interop_run_metrics.run_metrics_count_legacy_bins(self, *args)

    def is_run_parameters_required(self, *args):
        return _py_interop_run_metrics.run_metrics_is_run_parameters_required(self, *args)

    def run_info(self, *args):
        return _py_interop_run_metrics.run_metrics_run_info(self, *args)

    def run_parameters(self, *args):
        return _py_interop_run_metrics.run_metrics_run_parameters(self, *args)

    def list_filenames(self, *args):
        return _py_interop_run_metrics.run_metrics_list_filenames(self, *args)

    def copy_tile(self, metrics, tile_id):
        return _py_interop_run_metrics.run_metrics_copy_tile(self, metrics, tile_id)

    def append_tiles(self, metrics, tile_id):
        return _py_interop_run_metrics.run_metrics_append_tiles(self, metrics, tile_id)

    def check_for_data_sources(self, run_folder, last_cycle):
        return _py_interop_run_metrics.run_metrics_check_for_data_sources(self, run_folder, last_cycle)

    def read_metrics(self, *args):
        return _py_interop_run_metrics.run_metrics_read_metrics(self, *args)

    def write_metrics(self, run_folder, use_out=True):
        return _py_interop_run_metrics.run_metrics_write_metrics(self, run_folder, use_out)

    def read_metrics_from_buffer(self, group, buffer):
        return _py_interop_run_metrics.run_metrics_read_metrics_from_buffer(self, group, buffer)

    def write_metrics_to_buffer(self, group, buffer):
        return _py_interop_run_metrics.run_metrics_write_metrics_to_buffer(self, group, buffer)

    def calculate_buffer_size(self, group):
        return _py_interop_run_metrics.run_metrics_calculate_buffer_size(self, group)

    def validate(self):
        return _py_interop_run_metrics.run_metrics_validate(self)

    def is_group_empty(self, *args):
        return _py_interop_run_metrics.run_metrics_is_group_empty(self, *args)

    def populate_id_map(self, *args):
        return _py_interop_run_metrics.run_metrics_populate_id_map(self, *args)

    def sort(self):
        return _py_interop_run_metrics.run_metrics_sort(self)

    def clear(self):
        return _py_interop_run_metrics.run_metrics_clear(self)

    def set_corrected_intensity_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_corrected_intensity_metric_set(self, metrics)

    def corrected_intensity_metric_set(self):
        return _py_interop_run_metrics.run_metrics_corrected_intensity_metric_set(self)

    def set_error_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_error_metric_set(self, metrics)

    def error_metric_set(self):
        return _py_interop_run_metrics.run_metrics_error_metric_set(self)

    def set_extended_tile_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_extended_tile_metric_set(self, metrics)

    def extended_tile_metric_set(self):
        return _py_interop_run_metrics.run_metrics_extended_tile_metric_set(self)

    def set_extraction_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_extraction_metric_set(self, metrics)

    def extraction_metric_set(self):
        return _py_interop_run_metrics.run_metrics_extraction_metric_set(self)

    def set_image_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_image_metric_set(self, metrics)

    def image_metric_set(self):
        return _py_interop_run_metrics.run_metrics_image_metric_set(self)

    def set_q_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_q_metric_set(self, metrics)

    def q_metric_set(self):
        return _py_interop_run_metrics.run_metrics_q_metric_set(self)

    def set_tile_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_tile_metric_set(self, metrics)

    def tile_metric_set(self):
        return _py_interop_run_metrics.run_metrics_tile_metric_set(self)

    def set_index_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_index_metric_set(self, metrics)

    def index_metric_set(self):
        return _py_interop_run_metrics.run_metrics_index_metric_set(self)

    def set_q_collapsed_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_q_collapsed_metric_set(self, metrics)

    def q_collapsed_metric_set(self):
        return _py_interop_run_metrics.run_metrics_q_collapsed_metric_set(self)

    def set_q_by_lane_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_q_by_lane_metric_set(self, metrics)

    def q_by_lane_metric_set(self):
        return _py_interop_run_metrics.run_metrics_q_by_lane_metric_set(self)

    def set_summary_run_metric_set(self, metrics):
        return _py_interop_run_metrics.run_metrics_set_summary_run_metric_set(self, metrics)

    def summary_run_metric_set(self):
        return _py_interop_run_metrics.run_metrics_summary_run_metric_set(self)
    __swig_destroy__ = _py_interop_run_metrics.delete_run_metrics

# Register run_metrics in _py_interop_run_metrics:
_py_interop_run_metrics.run_metrics_swigregister(run_metrics)



