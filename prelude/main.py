#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xff1e998

# Compiled with Coconut version 3.1.0-post_dev7

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev7', '35', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == '__coconut__':
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and '__coconut_cache__' in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != '__coconut_cache__':
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

# Helpers:

#### Operators:


#### Imports:
import sys  #18 (line in Coconut source)
import fractions as _fractions  #19 (line in Coconut source)
import math as _math  #20 (line in Coconut source)
import ast as _ast  #21 (line in Coconut source)
from math import gcd as _gcd  #22 (line in Coconut source)

from prelude.util import *  # type: ignore  #24 (line in Coconut source)

#### Untyped built-ins:
_max = max  # type: _coconut.typing.Callable[..., T.Any]  #27 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #27 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #27 (line in Coconut source)
__annotations__["_max"] = '_coconut.typing.Callable[..., T.Any]'  #27 (line in Coconut source)
_min = min  # type: _coconut.typing.Callable[..., T.Any]  #28 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #28 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #28 (line in Coconut source)
__annotations__["_min"] = '_coconut.typing.Callable[..., T.Any]'  #28 (line in Coconut source)
_zip = zip  # type: _coconut.typing.Callable[..., T.Any]  #29 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #29 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #29 (line in Coconut source)
__annotations__["_zip"] = '_coconut.typing.Callable[..., T.Any]'  #29 (line in Coconut source)
_abs = abs  # type: _coconut.typing.Callable[..., T.Any]  #30 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #30 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #30 (line in Coconut source)
__annotations__["_abs"] = '_coconut.typing.Callable[..., T.Any]'  #30 (line in Coconut source)
_round = round  # type: _coconut.typing.Callable[..., T.Any]  #31 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #31 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #31 (line in Coconut source)
__annotations__["_round"] = '_coconut.typing.Callable[..., T.Any]'  #31 (line in Coconut source)
_fmap = fmap  # type: _coconut.typing.Callable[..., T.Any]  # type: ignore  #32 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #32 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #32 (line in Coconut source)
__annotations__["_fmap"] = '_coconut.typing.Callable[..., T.Any]'  # type: ignore  #32 (line in Coconut source)
_reduce = reduce  # type: _coconut.typing.Callable[..., T.Any]  #33 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #33 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #33 (line in Coconut source)
__annotations__["_reduce"] = '_coconut.typing.Callable[..., T.Any]'  #33 (line in Coconut source)
_all = all  # type: _coconut.typing.Callable[..., T.Any]  #34 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #34 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #34 (line in Coconut source)
__annotations__["_all"] = '_coconut.typing.Callable[..., T.Any]'  #34 (line in Coconut source)
_any = any  # type: _coconut.typing.Callable[..., T.Any]  #35 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #35 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #35 (line in Coconut source)
__annotations__["_any"] = '_coconut.typing.Callable[..., T.Any]'  #35 (line in Coconut source)
_map = map  # type: _coconut.typing.Callable[..., T.Any]  #36 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #36 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #36 (line in Coconut source)
__annotations__["_map"] = '_coconut.typing.Callable[..., T.Any]'  #36 (line in Coconut source)
_filter = filter  # type: _coconut.typing.Callable[..., T.Any]  #37 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #37 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #37 (line in Coconut source)
__annotations__["_filter"] = '_coconut.typing.Callable[..., T.Any]'  #37 (line in Coconut source)
_int = int  # type: _coconut.typing.Callable[..., T.Any]  #38 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #38 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #38 (line in Coconut source)
__annotations__["_int"] = '_coconut.typing.Callable[..., T.Any]'  #38 (line in Coconut source)
_sum = sum  # type: _coconut.typing.Callable[..., T.Any]  #39 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #39 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #39 (line in Coconut source)
__annotations__["_sum"] = '_coconut.typing.Callable[..., T.Any]'  #39 (line in Coconut source)
_reversed = reversed  # type: _coconut.typing.Callable[..., T.Any]  #40 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #40 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #40 (line in Coconut source)
__annotations__["_reversed"] = '_coconut.typing.Callable[..., T.Any]'  #40 (line in Coconut source)
_print = print  # type: _coconut.typing.Callable[..., T.Any]  #41 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #41 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #41 (line in Coconut source)
__annotations__["_print"] = '_coconut.typing.Callable[..., T.Any]'  #41 (line in Coconut source)
_cycle = cycle  # type: _coconut.typing.Callable[..., T.Any]  # type: ignore  #42 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #42 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #42 (line in Coconut source)
__annotations__["_cycle"] = '_coconut.typing.Callable[..., T.Any]'  # type: ignore  #42 (line in Coconut source)
_ceil = _math.ceil  # type: _coconut.typing.Callable[..., T.Any]  #43 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #43 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #43 (line in Coconut source)
__annotations__["_ceil"] = '_coconut.typing.Callable[..., T.Any]'  #43 (line in Coconut source)
_floor = _math.floor  # type: _coconut.typing.Callable[..., T.Any]  #44 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #44 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #44 (line in Coconut source)
__annotations__["_floor"] = '_coconut.typing.Callable[..., T.Any]'  #44 (line in Coconut source)




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool  #54 (line in Coconut source)

not_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[bool], bool]  #56 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #56 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #56 (line in Coconut source)
__annotations__["not_"] = '_coconut.typing.Callable[[bool], bool]'  #56 (line in Coconut source)
not_ = (_coconut.operator.not_)  #57 (line in Coconut source)

otherwise = True  # type: bool  #59 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #59 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #59 (line in Coconut source)
__annotations__["otherwise"] = 'bool'  #59 (line in Coconut source)

#### Maybe:
class Maybe():  #62 (line in Coconut source)
    @staticmethod  #63 (line in Coconut source)
    @_coconut_tco  #64 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'Maybe':  #64 (line in Coconut source)
        return _coconut_tail_call(Just, x)  #64 (line in Coconut source)


    @staticmethod  #66 (line in Coconut source)
    def __fail__(msg: 'str') -> 'Maybe':  #67 (line in Coconut source)
        return (nothing)  #67 (line in Coconut source)


    @staticmethod  #69 (line in Coconut source)
    def __mempty__() -> 'Maybe':  #70 (line in Coconut source)
        return (nothing)  #70 (line in Coconut source)


_coconut_call_set_names(Maybe)  #72 (line in Coconut source)
class Nothing(_coconut.collections.namedtuple("Nothing", ()), Maybe):  #72 (line in Coconut source)
    """
    -- Nothing is the data type; use nothing for the canonical instance
    """  #75 (line in Coconut source)

    __slots__ = ()  #77 (line in Coconut source)
    _coconut_is_data = True  #77 (line in Coconut source)
    __match_args__ = ()  #77 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #77 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #77 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #77 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #77 (line in Coconut source)
    def __eq__(self, other):  #77 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #77 (line in Coconut source)
    def __hash__(self):  #77 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #77 (line in Coconut source)
_coconut_call_set_names(Nothing)  #77 (line in Coconut source)
nothing = Nothing()  # type: Maybe  #77 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #77 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #77 (line in Coconut source)
__annotations__["nothing"] = 'Maybe'  #77 (line in Coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #79 (line in Coconut source)
    __slots__ = ()  #79 (line in Coconut source)
    _coconut_is_data = True  #79 (line in Coconut source)
    __match_args__ = ('x',)  #79 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #79 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #79 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #79 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #79 (line in Coconut source)
    def __eq__(self, other):  #79 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #79 (line in Coconut source)
    def __hash__(self):  #79 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #79 (line in Coconut source)


_coconut_call_set_names(Just)  #81 (line in Coconut source)
derivingOrd(Nothing, Just)  #81 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #83 (line in Coconut source)
    @_coconut_tco  #83 (line in Coconut source)
    @_coconut_mark_as_match  #83 (line in Coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #83 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #83 (line in Coconut source)
else:  #83 (line in Coconut source)
    @_coconut_tco  #83 (line in Coconut source)
    @_coconut_mark_as_match  #83 (line in Coconut source)
    def maybe(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #83 (line in Coconut source)

        _coconut_match_check_0 = False  #83 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #83 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #83 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #83 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #83 (line in Coconut source)
        if not _coconut_match_check_0:  #83 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #83 (line in Coconut source)
            _coconut_match_set_name_default = _coconut_sentinel  #83 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #83 (line in Coconut source)
                _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #83 (line in Coconut source)
                _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)  # type: ignore  #83 (line in Coconut source)
                _coconut_match_set_name_default = _coconut_match_temp_0  #83 (line in Coconut source)
                if not _coconut_match_kwargs:  #83 (line in Coconut source)
                    _coconut_match_check_0 = True  #83 (line in Coconut source)
            if _coconut_match_check_0:  #83 (line in Coconut source)
                _coconut_match_check_0 = False  #83 (line in Coconut source)
                if not _coconut_match_check_0:  #83 (line in Coconut source)
                    if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #83 (line in Coconut source)
                        _coconut_match_temp_2 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(0, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(0, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 0  # type: ignore  #83 (line in Coconut source)
                        if _coconut_match_temp_2:  #83 (line in Coconut source)
                            _coconut_match_check_0 = True  #83 (line in Coconut source)

                if not _coconut_match_check_0:  #83 (line in Coconut source)
                    if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #83 (line in Coconut source)
                        _coconut_match_check_0 = True  #83 (line in Coconut source)
                    if _coconut_match_check_0:  #83 (line in Coconut source)
                        _coconut_match_check_0 = False  #83 (line in Coconut source)
                        if not _coconut_match_check_0:  #83 (line in Coconut source)
                            if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #83 (line in Coconut source)
                                _coconut_match_check_0 = True  #83 (line in Coconut source)

                        if not _coconut_match_check_0:  #83 (line in Coconut source)
                            if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #83 (line in Coconut source)
                                _coconut_match_temp_3 = _coconut.getattr(Nothing, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #83 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_3, _coconut.tuple):  #83 (line in Coconut source)
                                    raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #83 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_3) < 0:  #83 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_3),))  #83 (line in Coconut source)
                                _coconut_match_check_0 = True  #83 (line in Coconut source)




            if _coconut_match_check_0:  #83 (line in Coconut source)
                if _coconut_match_set_name_default is not _coconut_sentinel:  #83 (line in Coconut source)
                    default = _coconut_match_set_name_default  #83 (line in Coconut source)

            if _coconut_match_check_0:  #83 (line in Coconut source)

                    return (default)  #86 (line in Coconut source)

        if not _coconut_match_check_0:  #87 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #87 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #87 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #87 (line in Coconut source)
                _coconut_match_temp_4 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #87 (line in Coconut source)
                _coconut_match_temp_5 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)  # type: ignore  #87 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_4  #87 (line in Coconut source)
                if not _coconut_match_kwargs:  #87 (line in Coconut source)
                    _coconut_match_check_0 = True  #87 (line in Coconut source)
            if _coconut_match_check_0:  #87 (line in Coconut source)
                _coconut_match_check_0 = False  #87 (line in Coconut source)
                if not _coconut_match_check_0:  #87 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                    if (_coconut_match_temp_5) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #87 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_match_args[2][0]  #87 (line in Coconut source)
                        _coconut_match_temp_6 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #87 (line in Coconut source)
                        if _coconut_match_temp_6:  #87 (line in Coconut source)
                            _coconut_match_check_0 = True  #87 (line in Coconut source)
                    if _coconut_match_check_0:  #87 (line in Coconut source)
                        if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                            x = _coconut_match_set_name_x  #87 (line in Coconut source)

                if not _coconut_match_check_0:  #87 (line in Coconut source)
                    if (not _coconut_match_temp_5) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #87 (line in Coconut source)
                        _coconut_match_check_0 = True  #87 (line in Coconut source)
                    if _coconut_match_check_0:  #87 (line in Coconut source)
                        _coconut_match_check_0 = False  #87 (line in Coconut source)
                        if not _coconut_match_check_0:  #87 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                            if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_args[2]  #87 (line in Coconut source)
                                _coconut_match_check_0 = True  #87 (line in Coconut source)
                            if _coconut_match_check_0:  #87 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #87 (line in Coconut source)

                        if not _coconut_match_check_0:  #87 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                            if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                                _coconut_match_temp_7 = _coconut.getattr(Just, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #87 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_7, _coconut.tuple):  #87 (line in Coconut source)
                                    raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #87 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_7) < 1:  #87 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_7),))  #87 (line in Coconut source)
                                _coconut_match_temp_8 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_7[0], _coconut_sentinel)  #87 (line in Coconut source)
                                if _coconut_match_temp_8 is not _coconut_sentinel:  #87 (line in Coconut source)
                                    _coconut_match_set_name_x = _coconut_match_temp_8  #87 (line in Coconut source)
                                    _coconut_match_check_0 = True  #87 (line in Coconut source)
                            if _coconut_match_check_0:  #87 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #87 (line in Coconut source)




            if _coconut_match_check_0:  #87 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #87 (line in Coconut source)
                    func = _coconut_match_set_name_func  #87 (line in Coconut source)

            if _coconut_match_check_0:  #87 (line in Coconut source)

                    return _coconut_tail_call(_coconut_call_or_coefficient, func, x)  #87 (line in Coconut source)

#### Either:

        if not _coconut_match_check_0:  #90 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def maybe:', _coconut_match_args)  #90 (line in Coconut source)


class Either():  #90 (line in Coconut source)
    @staticmethod  #91 (line in Coconut source)
    @_coconut_tco  #92 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #92 (line in Coconut source)
        return _coconut_tail_call(Right, x)  #92 (line in Coconut source)


    @staticmethod  #94 (line in Coconut source)
    @_coconut_tco  #95 (line in Coconut source)
    def __fail__(msg: 'str') -> 'Either':  #95 (line in Coconut source)
        return _coconut_tail_call(Left, msg)  #95 (line in Coconut source)


_coconut_call_set_names(Either)  #97 (line in Coconut source)
class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #97 (line in Coconut source)
    __slots__ = ()  #97 (line in Coconut source)
    _coconut_is_data = True  #97 (line in Coconut source)
    __match_args__ = ('x',)  #97 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #97 (line in Coconut source)
    def __eq__(self, other):  #97 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #97 (line in Coconut source)
    def __hash__(self):  #97 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #97 (line in Coconut source)
    @staticmethod  #98 (line in Coconut source)
    def __bool__() -> 'bool':  #99 (line in Coconut source)
        return (False)  #99 (line in Coconut source)


    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #101 (line in Coconut source)
        return (self)  #101 (line in Coconut source)


_coconut_call_set_names(Left)  #103 (line in Coconut source)
class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #103 (line in Coconut source)
    __slots__ = ()  #103 (line in Coconut source)
    _coconut_is_data = True  #103 (line in Coconut source)
    __match_args__ = ('x',)  #103 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #103 (line in Coconut source)
    def __eq__(self, other):  #103 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #103 (line in Coconut source)
    def __hash__(self):  #103 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #103 (line in Coconut source)


_coconut_call_set_names(Right)  #105 (line in Coconut source)
derivingOrd(Left, Right)  #105 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #107 (line in Coconut source)
    @_coconut_tco  #107 (line in Coconut source)
    @_coconut_mark_as_match  #107 (line in Coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #107 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #107 (line in Coconut source)
else:  #107 (line in Coconut source)
    @_coconut_tco  #107 (line in Coconut source)
    @_coconut_mark_as_match  #107 (line in Coconut source)
    def either(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #107 (line in Coconut source)

        _coconut_match_check_1 = False  #107 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #107 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #107 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #107 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #107 (line in Coconut source)
        if not _coconut_match_check_1:  #107 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #107 (line in Coconut source)
            _coconut_match_set_name_left_func = _coconut_sentinel  #107 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #107 (line in Coconut source)
                _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #107 (line in Coconut source)
                _coconut_match_temp_10 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)  # type: ignore  #107 (line in Coconut source)
                _coconut_match_set_name_left_func = _coconut_match_temp_9  #107 (line in Coconut source)
                if not _coconut_match_kwargs:  #107 (line in Coconut source)
                    _coconut_match_check_1 = True  #107 (line in Coconut source)
            if _coconut_match_check_1:  #107 (line in Coconut source)
                _coconut_match_check_1 = False  #107 (line in Coconut source)
                if not _coconut_match_check_1:  #107 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_sentinel  #107 (line in Coconut source)
                    if (_coconut_match_temp_10) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #107 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_match_args[2][0]  #107 (line in Coconut source)
                        _coconut_match_temp_11 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #107 (line in Coconut source)
                        if _coconut_match_temp_11:  #107 (line in Coconut source)
                            _coconut_match_check_1 = True  #107 (line in Coconut source)
                    if _coconut_match_check_1:  #107 (line in Coconut source)
                        if _coconut_match_set_name_x is not _coconut_sentinel:  #107 (line in Coconut source)
                            x = _coconut_match_set_name_x  #107 (line in Coconut source)

                if not _coconut_match_check_1:  #107 (line in Coconut source)
                    if (not _coconut_match_temp_10) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #107 (line in Coconut source)
                        _coconut_match_check_1 = True  #107 (line in Coconut source)
                    if _coconut_match_check_1:  #107 (line in Coconut source)
                        _coconut_match_check_1 = False  #107 (line in Coconut source)
                        if not _coconut_match_check_1:  #107 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #107 (line in Coconut source)
                            if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #107 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_args[2]  #107 (line in Coconut source)
                                _coconut_match_check_1 = True  #107 (line in Coconut source)
                            if _coconut_match_check_1:  #107 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #107 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #107 (line in Coconut source)

                        if not _coconut_match_check_1:  #107 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #107 (line in Coconut source)
                            if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #107 (line in Coconut source)
                                _coconut_match_temp_12 = _coconut.getattr(Left, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #107 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_12, _coconut.tuple):  #107 (line in Coconut source)
                                    raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #107 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_12) < 1:  #107 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_12),))  #107 (line in Coconut source)
                                _coconut_match_temp_13 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_12[0], _coconut_sentinel)  #107 (line in Coconut source)
                                if _coconut_match_temp_13 is not _coconut_sentinel:  #107 (line in Coconut source)
                                    _coconut_match_set_name_x = _coconut_match_temp_13  #107 (line in Coconut source)
                                    _coconut_match_check_1 = True  #107 (line in Coconut source)
                            if _coconut_match_check_1:  #107 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #107 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #107 (line in Coconut source)




            if _coconut_match_check_1:  #107 (line in Coconut source)
                if _coconut_match_set_name_left_func is not _coconut_sentinel:  #107 (line in Coconut source)
                    left_func = _coconut_match_set_name_left_func  #107 (line in Coconut source)

            if _coconut_match_check_1:  #107 (line in Coconut source)

                    return _coconut_tail_call(_coconut_call_or_coefficient, left_func, x)  #110 (line in Coconut source)

        if not _coconut_match_check_1:  #111 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #111 (line in Coconut source)
            _coconut_match_set_name_right_func = _coconut_sentinel  #111 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #111 (line in Coconut source)
                _coconut_match_temp_14 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #111 (line in Coconut source)
                _coconut_match_temp_15 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)  # type: ignore  #111 (line in Coconut source)
                _coconut_match_set_name_right_func = _coconut_match_temp_14  #111 (line in Coconut source)
                if not _coconut_match_kwargs:  #111 (line in Coconut source)
                    _coconut_match_check_1 = True  #111 (line in Coconut source)
            if _coconut_match_check_1:  #111 (line in Coconut source)
                _coconut_match_check_1 = False  #111 (line in Coconut source)
                if not _coconut_match_check_1:  #111 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                    if (_coconut_match_temp_15) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #111 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_match_args[2][0]  #111 (line in Coconut source)
                        _coconut_match_temp_16 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #111 (line in Coconut source)
                        if _coconut_match_temp_16:  #111 (line in Coconut source)
                            _coconut_match_check_1 = True  #111 (line in Coconut source)
                    if _coconut_match_check_1:  #111 (line in Coconut source)
                        if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                            x = _coconut_match_set_name_x  #111 (line in Coconut source)

                if not _coconut_match_check_1:  #111 (line in Coconut source)
                    if (not _coconut_match_temp_15) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #111 (line in Coconut source)
                        _coconut_match_check_1 = True  #111 (line in Coconut source)
                    if _coconut_match_check_1:  #111 (line in Coconut source)
                        _coconut_match_check_1 = False  #111 (line in Coconut source)
                        if not _coconut_match_check_1:  #111 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                            if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #111 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_args[2]  #111 (line in Coconut source)
                                _coconut_match_check_1 = True  #111 (line in Coconut source)
                            if _coconut_match_check_1:  #111 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #111 (line in Coconut source)

                        if not _coconut_match_check_1:  #111 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                            if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #111 (line in Coconut source)
                                _coconut_match_temp_17 = _coconut.getattr(Right, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #111 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_17, _coconut.tuple):  #111 (line in Coconut source)
                                    raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #111 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_17) < 1:  #111 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_17),))  #111 (line in Coconut source)
                                _coconut_match_temp_18 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_17[0], _coconut_sentinel)  #111 (line in Coconut source)
                                if _coconut_match_temp_18 is not _coconut_sentinel:  #111 (line in Coconut source)
                                    _coconut_match_set_name_x = _coconut_match_temp_18  #111 (line in Coconut source)
                                    _coconut_match_check_1 = True  #111 (line in Coconut source)
                            if _coconut_match_check_1:  #111 (line in Coconut source)
                                if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                                    x = _coconut_match_set_name_x  #111 (line in Coconut source)




            if _coconut_match_check_1:  #111 (line in Coconut source)
                if _coconut_match_set_name_right_func is not _coconut_sentinel:  #111 (line in Coconut source)
                    right_func = _coconut_match_set_name_right_func  #111 (line in Coconut source)

            if _coconut_match_check_1:  #111 (line in Coconut source)

                    return _coconut_tail_call(_coconut_call_or_coefficient, right_func, x)  #111 (line in Coconut source)

#### Ordering:

        if not _coconut_match_check_1:  #114 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def either:', _coconut_match_args)  #114 (line in Coconut source)


class Ordering():  #114 (line in Coconut source)
    @staticmethod  #115 (line in Coconut source)
    def __mempty__() -> 'Ordering':  #116 (line in Coconut source)
        return (eq)  #116 (line in Coconut source)


_coconut_call_set_names(Ordering)  #118 (line in Coconut source)
class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #118 (line in Coconut source)
    __slots__ = ()  #118 (line in Coconut source)
    _coconut_is_data = True  #118 (line in Coconut source)
    __match_args__ = ()  #118 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #118 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #118 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #118 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #118 (line in Coconut source)
    def __eq__(self, other):  #118 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #118 (line in Coconut source)
    def __hash__(self):  #118 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #118 (line in Coconut source)
    @staticmethod  #119 (line in Coconut source)
    def __bool__() -> 'bool':  #120 (line in Coconut source)
        return (True)  #120 (line in Coconut source)


_coconut_call_set_names(LT)  #122 (line in Coconut source)
class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #122 (line in Coconut source)
    __slots__ = ()  #122 (line in Coconut source)
    _coconut_is_data = True  #122 (line in Coconut source)
    __match_args__ = ()  #122 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #122 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #122 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #122 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #122 (line in Coconut source)
    def __eq__(self, other):  #122 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #122 (line in Coconut source)
    def __hash__(self):  #122 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #122 (line in Coconut source)


_coconut_call_set_names(EQ)  #124 (line in Coconut source)
class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #124 (line in Coconut source)
    __slots__ = ()  #124 (line in Coconut source)
    _coconut_is_data = True  #124 (line in Coconut source)
    __match_args__ = ()  #124 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #124 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #124 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #124 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #124 (line in Coconut source)
    def __eq__(self, other):  #124 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #124 (line in Coconut source)
    def __hash__(self):  #124 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #124 (line in Coconut source)
    @staticmethod  #125 (line in Coconut source)
    def __bool__() -> 'bool':  #126 (line in Coconut source)
        return (True)  #126 (line in Coconut source)


_coconut_call_set_names(GT)  #128 (line in Coconut source)
derivingOrd(LT, EQ, GT)  #128 (line in Coconut source)
derivingBoundedEnum(LT, EQ, GT)  #129 (line in Coconut source)

lt = LT()  # type: Ordering  #131 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #131 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #131 (line in Coconut source)
__annotations__["lt"] = 'Ordering'  #131 (line in Coconut source)
eq = EQ()  # type: Ordering  #132 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #132 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #132 (line in Coconut source)
__annotations__["eq"] = 'Ordering'  #132 (line in Coconut source)
gt = GT()  # type: Ordering  #133 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #133 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #133 (line in Coconut source)
__annotations__["gt"] = 'Ordering'  #133 (line in Coconut source)

#### Char:
Char = T.NewType("Char", str)  #136 (line in Coconut source)

#### String:
String = str  #139 (line in Coconut source)


### Tuples:
fst = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Ta]  #143 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #143 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #143 (line in Coconut source)
__annotations__["fst"] = '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Ta]'  #143 (line in Coconut source)
fst = _coconut.operator.itemgetter((0))  #144 (line in Coconut source)

snd = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tb]  #146 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #146 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #146 (line in Coconut source)
__annotations__["snd"] = '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tb]'  #146 (line in Coconut source)
snd = _coconut.operator.itemgetter((1))  #147 (line in Coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #149 (line in Coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #152 (line in Coconut source)
    return (lambda *args: func(args))  # type: ignore  #153 (line in Coconut source)


def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tc]':  #155 (line in Coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #158 (line in Coconut source)
    return (lambda args: func(*args))  #159 (line in Coconut source)



## Basic type classes:

#### Eq:

Eq = object  #166 (line in Coconut source)

#### Ord:
Ord = Eq  #169 (line in Coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #170 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #172 (line in Coconut source)
    @_coconut_mark_as_match  #172 (line in Coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #172 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #172 (line in Coconut source)
else:  #172 (line in Coconut source)
    @_coconut_mark_as_match  #172 (line in Coconut source)
    def compare(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #172 (line in Coconut source)

        _coconut_match_check_2 = False  #172 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #172 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #172 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #172 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #172 (line in Coconut source)
        if not _coconut_match_check_2:  #172 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #172 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #172 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #172 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #172 (line in Coconut source)
                _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #172 (line in Coconut source)
                _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #172 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_19  #172 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_20  #172 (line in Coconut source)
                if not _coconut_match_kwargs:  #172 (line in Coconut source)
                    _coconut_match_check_2 = True  #172 (line in Coconut source)
            if _coconut_match_check_2:  #172 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #172 (line in Coconut source)
                    x = _coconut_match_set_name_x  #172 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #172 (line in Coconut source)
                    y = _coconut_match_set_name_y  #172 (line in Coconut source)
            if _coconut_match_check_2 and not (x == y):  #172 (line in Coconut source)
                _coconut_match_check_2 = False  #172 (line in Coconut source)

            if _coconut_match_check_2:  #172 (line in Coconut source)

                    return (eq)  #174 (line in Coconut source)

        if not _coconut_match_check_2:  #175 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #175 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #175 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #175 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #175 (line in Coconut source)
                _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #175 (line in Coconut source)
                _coconut_match_temp_22 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #175 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_21  #175 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_22  #175 (line in Coconut source)
                if not _coconut_match_kwargs:  #175 (line in Coconut source)
                    _coconut_match_check_2 = True  #175 (line in Coconut source)
            if _coconut_match_check_2:  #175 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #175 (line in Coconut source)
                    x = _coconut_match_set_name_x  #175 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #175 (line in Coconut source)
                    y = _coconut_match_set_name_y  #175 (line in Coconut source)
            if _coconut_match_check_2 and not (x < y):  #175 (line in Coconut source)
                _coconut_match_check_2 = False  #175 (line in Coconut source)

            if _coconut_match_check_2:  #175 (line in Coconut source)

                    return (lt)  #175 (line in Coconut source)

        if not _coconut_match_check_2:  #176 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #176 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #176 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #176 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #176 (line in Coconut source)
                _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #176 (line in Coconut source)
                _coconut_match_temp_24 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #176 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_23  #176 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_24  #176 (line in Coconut source)
                if not _coconut_match_kwargs:  #176 (line in Coconut source)
                    _coconut_match_check_2 = True  #176 (line in Coconut source)
            if _coconut_match_check_2:  #176 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #176 (line in Coconut source)
                    x = _coconut_match_set_name_x  #176 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #176 (line in Coconut source)
                    y = _coconut_match_set_name_y  #176 (line in Coconut source)
            if _coconut_match_check_2 and not (x > y):  #176 (line in Coconut source)
                _coconut_match_check_2 = False  #176 (line in Coconut source)

            if _coconut_match_check_2:  #176 (line in Coconut source)

                    return (gt)  #176 (line in Coconut source)

# type: ignore
        if not _coconut_match_check_2:  # type: ignore  #178 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def compare:', _coconut_match_args)  # type: ignore  #178 (line in Coconut source)
# type: ignore
# type: ignore
max = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  # type: ignore  #178 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #178 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #178 (line in Coconut source)
__annotations__["max"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  # type: ignore  #178 (line in Coconut source)
max = _max  #179 (line in Coconut source)

min = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  # type: ignore  #181 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #181 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #181 (line in Coconut source)
__annotations__["min"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  # type: ignore  #181 (line in Coconut source)
min = _min  #182 (line in Coconut source)

#### Enum:
Enum = Ord  #185 (line in Coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #186 (line in Coconut source)

succ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #188 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #188 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #188 (line in Coconut source)
__annotations__["succ"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #188 (line in Coconut source)
succ = (_coconut_partial(_coconut.operator.add, 1))  #189 (line in Coconut source)

pred = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #191 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #191 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #191 (line in Coconut source)
__annotations__["pred"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #191 (line in Coconut source)
pred = (_coconut_complex_partial(_coconut_minus, {1: 1}, 2, ()))  #192 (line in Coconut source)

toEnum = NotImplemented  #194 (line in Coconut source)

fromEnum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Enum], int]  #196 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #196 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #196 (line in Coconut source)
__annotations__["fromEnum"] = '_coconut.typing.Callable[[Enum], int]'  #196 (line in Coconut source)
fromEnum = _int  #197 (line in Coconut source)

@_coconut_tco  #199 (line in Coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #199 (line in Coconut source)
    return _coconut_tail_call(iterate, succ, first)  #200 (line in Coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #202 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #203 (line in Coconut source)
    return (iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first) if step >= 0 else ())  # type: ignore  #204 (line in Coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #206 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #207 (line in Coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #208 (line in Coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #210 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #211 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #212 (line in Coconut source)
    steps = dist / step if step != 0 else 0  #213 (line in Coconut source)
    if steps < 0:  #214 (line in Coconut source)
        return (())  #215 (line in Coconut source)
    counter = iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first)  #216 (line in Coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #217 (line in Coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #221 (line in Coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #222 (line in Coconut source)

@_coconut_tco  #224 (line in Coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #224 (line in Coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #228 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #230 (line in Coconut source)
        return (False)  # type: ignore  #231 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #234 (line in Coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #235 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #238 (line in Coconut source)


@_coconut_tco  #240 (line in Coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #240 (line in Coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #244 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #246 (line in Coconut source)
        return (True)  # type: ignore  #247 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #250 (line in Coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #251 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #254 (line in Coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #263 (line in Coconut source)

#### Integer:
Integer = int  #266 (line in Coconut source)

#### Float:
Float = float  #269 (line in Coconut source)

#### Double:
Double = float  #272 (line in Coconut source)

#### Rational:
Rational = _fractions.Fraction  #275 (line in Coconut source)

@_coconut_tco  #277 (line in Coconut source)
def over(x, y):  #277 (line in Coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #282 (line in Coconut source)
    return _coconut_tail_call(_coconut_call_or_coefficient, Rational, x, y)  #283 (line in Coconut source)

_coconut_op_U25_U25 = over  #284 (line in Coconut source)

#### Word:
Word = Int  #287 (line in Coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #293 (line in Coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #294 (line in Coconut source)

negate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #296 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #296 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #296 (line in Coconut source)
__annotations__["negate"] = '_coconut.typing.Callable[[TNum], TNum]'  #296 (line in Coconut source)
negate = (_coconut_minus)  #297 (line in Coconut source)

abs = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #299 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #299 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #299 (line in Coconut source)
__annotations__["abs"] = '_coconut.typing.Callable[[TNum], TNum]'  #299 (line in Coconut source)
abs = _abs  #300 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #302 (line in Coconut source)
    @_coconut_mark_as_match  #302 (line in Coconut source)
    def signum(x: 'Num') -> 'int':  #302 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #302 (line in Coconut source)
else:  #302 (line in Coconut source)
    @_coconut_mark_as_match  #302 (line in Coconut source)
    def signum(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #302 (line in Coconut source)

        _coconut_match_check_3 = False  #302 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #302 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #302 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #302 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #302 (line in Coconut source)
        if not _coconut_match_check_3:  #302 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #302 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 1:  #302 (line in Coconut source)
                if _coconut_match_args[0] == 0:  #302 (line in Coconut source)
                    if not _coconut_match_kwargs:  #302 (line in Coconut source)
                        _coconut_match_check_3 = True  #302 (line in Coconut source)

            if _coconut_match_check_3:  #302 (line in Coconut source)

                    return (0)  #304 (line in Coconut source)

        if not _coconut_match_check_3:  #305 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #305 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #305 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #305 (line in Coconut source)
                _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #305 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_25  #305 (line in Coconut source)
                if not _coconut_match_kwargs:  #305 (line in Coconut source)
                    _coconut_match_check_3 = True  #305 (line in Coconut source)
            if _coconut_match_check_3:  #305 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #305 (line in Coconut source)
                    x = _coconut_match_set_name_x  #305 (line in Coconut source)
            if _coconut_match_check_3 and not (x > 0):  #305 (line in Coconut source)
                _coconut_match_check_3 = False  #305 (line in Coconut source)

            if _coconut_match_check_3:  #305 (line in Coconut source)

                    return (1)  #305 (line in Coconut source)

        if not _coconut_match_check_3:  #306 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #306 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #306 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #306 (line in Coconut source)
                _coconut_match_temp_26 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #306 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_26  #306 (line in Coconut source)
                if not _coconut_match_kwargs:  #306 (line in Coconut source)
                    _coconut_match_check_3 = True  #306 (line in Coconut source)
            if _coconut_match_check_3:  #306 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #306 (line in Coconut source)
                    x = _coconut_match_set_name_x  #306 (line in Coconut source)
            if _coconut_match_check_3 and not (x < 0):  #306 (line in Coconut source)
                _coconut_match_check_3 = False  #306 (line in Coconut source)

            if _coconut_match_check_3:  #306 (line in Coconut source)

                    return (-1)  #306 (line in Coconut source)


        if not _coconut_match_check_3:  #308 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def signum:', _coconut_match_args)  #308 (line in Coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #308 (line in Coconut source)
    return (x)  #308 (line in Coconut source)

#### Real:

Real = Num  #311 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #313 (line in Coconut source)
    @_coconut_tco  #313 (line in Coconut source)
    @_coconut_mark_as_match  #313 (line in Coconut source)
    def toRational(real: 'Real') -> 'Rational':  #313 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #313 (line in Coconut source)
else:  #313 (line in Coconut source)
    @_coconut_tco  #313 (line in Coconut source)
    @_coconut_mark_as_match  #313 (line in Coconut source)
    def toRational(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #313 (line in Coconut source)

        _coconut_match_check_4 = False  #313 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #313 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #313 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #313 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #313 (line in Coconut source)
        if not _coconut_match_check_4:  #313 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #313 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_sentinel  #313 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #313 (line in Coconut source)
                _coconut_match_temp_27 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #313 (line in Coconut source)
                if (isinstance)(_coconut_match_temp_27, float):  #313 (line in Coconut source)
                    _coconut_match_set_name_real = _coconut_match_temp_27  #313 (line in Coconut source)
                    if not _coconut_match_kwargs:  #313 (line in Coconut source)
                        _coconut_match_check_4 = True  #313 (line in Coconut source)
            if _coconut_match_check_4:  #313 (line in Coconut source)
                if _coconut_match_set_name_real is not _coconut_sentinel:  #313 (line in Coconut source)
                    real = _coconut_match_set_name_real  #313 (line in Coconut source)

            if _coconut_match_check_4:  #313 (line in Coconut source)

                    return _coconut_tail_call(Rational.from_float, real)  #316 (line in Coconut source)

        if not _coconut_match_check_4:  #317 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #317 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_sentinel  #317 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #317 (line in Coconut source)
                _coconut_match_temp_28 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #317 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_28  #317 (line in Coconut source)
                if not _coconut_match_kwargs:  #317 (line in Coconut source)
                    _coconut_match_check_4 = True  #317 (line in Coconut source)
            if _coconut_match_check_4:  #317 (line in Coconut source)
                if _coconut_match_set_name_real is not _coconut_sentinel:  #317 (line in Coconut source)
                    real = _coconut_match_set_name_real  #317 (line in Coconut source)

            if _coconut_match_check_4:  #317 (line in Coconut source)

                    return _coconut_tail_call(Rational, real)  #318 (line in Coconut source)

#### Integral:

        if not _coconut_match_check_4:  #321 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def toRational:', _coconut_match_args)  #321 (line in Coconut source)


Integral = int  #321 (line in Coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #323 (line in Coconut source)
    divxy = x // y  #324 (line in Coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #325 (line in Coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #327 (line in Coconut source)
    modxy = x % y  #328 (line in Coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #329 (line in Coconut source)


div = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #331 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #331 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #331 (line in Coconut source)
__annotations__["div"] = '_coconut.typing.Callable[[int, int], int]'  #331 (line in Coconut source)
div = (_coconut.operator.floordiv)  #332 (line in Coconut source)

mod = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #334 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #334 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #334 (line in Coconut source)
__annotations__["mod"] = '_coconut.typing.Callable[[int, int], int]'  #334 (line in Coconut source)
mod = (_coconut.operator.mod)  #335 (line in Coconut source)

def quotRem(x: 'int', y: 'int') -> '(_coconut.typing.Tuple[int, int])':  #337 (line in Coconut source)
    divxy, modxy = divmod(x, y)  #338 (line in Coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #339 (line in Coconut source)
    return (divxy + adj, modxy - y * adj)  #340 (line in Coconut source)


divMod = divmod  #342 (line in Coconut source)

toInteger = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Integer]  #344 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #344 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #344 (line in Coconut source)
__annotations__["toInteger"] = '_coconut.typing.Callable[[Integral], Integer]'  #344 (line in Coconut source)
toInteger = _int  #345 (line in Coconut source)

#### Fractional:
Fractional = Rational  #348 (line in Coconut source)

recip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Fractional], Fractional]  #350 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #350 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #350 (line in Coconut source)
__annotations__["recip"] = '_coconut.typing.Callable[[Fractional], Fractional]'  #350 (line in Coconut source)
recip = (_coconut_partial(_coconut.operator.truediv, 1))  #351 (line in Coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #353 (line in Coconut source)
    return (x)  #353 (line in Coconut source)

#### Floating:

Floating = float  #356 (line in Coconut source)

from math import pi  # NOQA  #358 (line in Coconut source)
from math import exp  # NOQA  #358 (line in Coconut source)
from math import log  # NOQA  #358 (line in Coconut source)
from math import sqrt  # NOQA  #358 (line in Coconut source)
from math import sin  # NOQA  #358 (line in Coconut source)
from math import cos  # NOQA  #358 (line in Coconut source)
from math import tan  # NOQA  #358 (line in Coconut source)
from math import asin  # NOQA  #358 (line in Coconut source)
from math import acos  # NOQA  #358 (line in Coconut source)
from math import atan  # NOQA  #358 (line in Coconut source)
from math import sinh  # NOQA  #358 (line in Coconut source)
from math import cosh  # NOQA  #358 (line in Coconut source)
from math import tanh  # NOQA  #358 (line in Coconut source)
from math import asinh  # NOQA  #358 (line in Coconut source)
from math import acosh  # NOQA  #358 (line in Coconut source)
from math import atanh  # NOQA  #358 (line in Coconut source)

@_coconut_tco  #377 (line in Coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #377 (line in Coconut source)
    return _coconut_tail_call(log, x, base)  #378 (line in Coconut source)

#### RealFrac:

RealFrac = Rational  #381 (line in Coconut source)

def properFraction(x: 'RealFrac') -> '(_coconut.typing.Tuple[int, RealFrac])':  #383 (line in Coconut source)
    floor_x = floor(x)  #384 (line in Coconut source)
    return (floor_x, x - floor_x)  #385 (line in Coconut source)


truncate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #387 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #387 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #387 (line in Coconut source)
__annotations__["truncate"] = '_coconut.typing.Callable[[RealFrac], int]'  #387 (line in Coconut source)
truncate = _int  #388 (line in Coconut source)

round = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #390 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #390 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #390 (line in Coconut source)
__annotations__["round"] = '_coconut.typing.Callable[[RealFrac], int]'  #390 (line in Coconut source)
round = _round  #391 (line in Coconut source)

ceiling = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #393 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #393 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #393 (line in Coconut source)
__annotations__["ceiling"] = '_coconut.typing.Callable[[RealFrac], int]'  #393 (line in Coconut source)
ceiling = _ceil  #394 (line in Coconut source)

floor = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #396 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #396 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #396 (line in Coconut source)
__annotations__["floor"] = '_coconut.typing.Callable[[RealFrac], int]'  #396 (line in Coconut source)
floor = _floor  #397 (line in Coconut source)

#### RealFloat:
RealFloat = float  #400 (line in Coconut source)

def floatRadix(x: 'float') -> 'int':  #402 (line in Coconut source)
    return (2)  #402 (line in Coconut source)


def floatDigits(x: 'float') -> 'int':  #404 (line in Coconut source)
    return (53)  #404 (line in Coconut source)


def floatRange(x: 'float') -> '(_coconut.typing.Tuple[int, int])':  #406 (line in Coconut source)
    return ((-1021, 1024))  #406 (line in Coconut source)


decodeFloat = NotImplemented  #408 (line in Coconut source)

encodeFloat = NotImplemented  #410 (line in Coconut source)

exponent = NotImplemented  #412 (line in Coconut source)

significand = NotImplemented  #414 (line in Coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #416 (line in Coconut source)
    return (x * 2**power)  #417 (line in Coconut source)

# NOQA
from math import isnan as isNaN  # NOQA  #419 (line in Coconut source)
from math import isinf as isInfinite  # NOQA  #419 (line in Coconut source)
from math import atan2  # NOQA  #419 (line in Coconut source)

isDenormalized = NotImplemented  #425 (line in Coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #427 (line in Coconut source)
    return (x == 0 and str(x).startswith("-"))  #428 (line in Coconut source)


def isIEEE(x: 'float') -> 'bool':  #430 (line in Coconut source)
    return (True)  #430 (line in Coconut source)


### Numeric functions:

def subtract(x, y):  #434 (line in Coconut source)
    return (y - x)  #435 (line in Coconut source)


def even(x: 'int') -> 'bool':  #437 (line in Coconut source)
    return (x % 2 == 0)  #438 (line in Coconut source)


def odd(x: 'int') -> 'bool':  #440 (line in Coconut source)
    return (x % 2 == 1)  #441 (line in Coconut source)


gcd = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #443 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #443 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #443 (line in Coconut source)
__annotations__["gcd"] = '_coconut.typing.Callable[[int, int], int]'  #443 (line in Coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #444 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #446 (line in Coconut source)
    @_coconut_mark_as_match  #446 (line in Coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #446 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #446 (line in Coconut source)
else:  #446 (line in Coconut source)
    @_coconut_mark_as_match  #446 (line in Coconut source)
    def lcm(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #446 (line in Coconut source)

        _coconut_match_check_5 = False  #446 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #446 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #446 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #446 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #446 (line in Coconut source)
        if not _coconut_match_check_5:  #446 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #446 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #446 (line in Coconut source)
                if _coconut_match_args[1] == 0:  #446 (line in Coconut source)
                    if not _coconut_match_kwargs:  #446 (line in Coconut source)
                        _coconut_match_check_5 = True  #446 (line in Coconut source)

            if _coconut_match_check_5:  #446 (line in Coconut source)

                    return (0)  #448 (line in Coconut source)

        if not _coconut_match_check_5:  #449 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #449 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #449 (line in Coconut source)
                if _coconut_match_args[0] == 0:  #449 (line in Coconut source)
                    if not _coconut_match_kwargs:  #449 (line in Coconut source)
                        _coconut_match_check_5 = True  #449 (line in Coconut source)

            if _coconut_match_check_5:  #449 (line in Coconut source)

                    return (0)  #449 (line in Coconut source)

        if not _coconut_match_check_5:  #450 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #450 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #450 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #450 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #450 (line in Coconut source)
                _coconut_match_temp_29 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #450 (line in Coconut source)
                _coconut_match_temp_30 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #450 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_29  #450 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_30  #450 (line in Coconut source)
                if not _coconut_match_kwargs:  #450 (line in Coconut source)
                    _coconut_match_check_5 = True  #450 (line in Coconut source)
            if _coconut_match_check_5:  #450 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #450 (line in Coconut source)
                    x = _coconut_match_set_name_x  #450 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #450 (line in Coconut source)
                    y = _coconut_match_set_name_y  #450 (line in Coconut source)

            if _coconut_match_check_5:  #450 (line in Coconut source)

                    return (abs(y) * (abs(x) // gcd(x, y)))  #451 (line in Coconut source)


        if not _coconut_match_check_5:  #453 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def lcm:', _coconut_match_args)  #453 (line in Coconut source)


fromIntegral = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Num]  #453 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #453 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #453 (line in Coconut source)
__annotations__["fromIntegral"] = '_coconut.typing.Callable[[Integral], Num]'  #453 (line in Coconut source)
fromIntegral = fromInteger  #454 (line in Coconut source)

realToFrac = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Real], Fractional]  #456 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #456 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #456 (line in Coconut source)
__annotations__["realToFrac"] = '_coconut.typing.Callable[[Real], Fractional]'  #456 (line in Coconut source)
realToFrac = toRational  #457 (line in Coconut source)



## Monoids:
Monoid = T.Iterable  #462 (line in Coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #463 (line in Coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #465 (line in Coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #468 (line in Coconut source)
    __slots__ = ()  #469 (line in Coconut source)
    _coconut_is_data = True  #469 (line in Coconut source)
    __match_args__ = ()  #469 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #469 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #469 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #469 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #469 (line in Coconut source)
    def __eq__(self, other):  #469 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #469 (line in Coconut source)
    def __hash__(self):  #469 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #469 (line in Coconut source)
    @staticmethod  #469 (line in Coconut source)
    @_coconut_tco  #470 (line in Coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #470 (line in Coconut source)
        if (hasattr)(M, "__mempty__"):  #471 (line in Coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #472 (line in Coconut source)
        return _coconut_tail_call(makedata, type(M))  #473 (line in Coconut source)


_coconut_call_set_names(Mempty)  #475 (line in Coconut source)
mempty = Mempty()  # type: T.Any  #475 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #475 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #475 (line in Coconut source)
__annotations__["mempty"] = 'T.Any'  #475 (line in Coconut source)

@_coconut_tco  #477 (line in Coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #477 (line in Coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #482 (line in Coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #484 (line in Coconut source)
    y = (asTypeOf)(y, x)  #485 (line in Coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #488 (line in Coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #489 (line in Coconut source)

# Default implementation
    if not x:  #492 (line in Coconut source)
        return (y)  #493 (line in Coconut source)
    if not y:  #494 (line in Coconut source)
        return (x)  #495 (line in Coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #496 (line in Coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #497 (line in Coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #498 (line in Coconut source)


@_coconut_tco  #500 (line in Coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #500 (line in Coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #501 (line in Coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #508 (line in Coconut source)

@_coconut_tco  # type: ignore  #510 (line in Coconut source)
def fmap(f: '_coconut.typing.Callable[[Ta], Tb]', xs: 'Functor[Ta]') -> 'Functor[Tb]':  # type: ignore  #510 (line in Coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #513 (line in Coconut source)
    try:  #514 (line in Coconut source)
# Default implementation
        return (_fmap(f, xs))  #516 (line in Coconut source)

    except TypeError:  #518 (line in Coconut source)
# Function instance
        if callable(xs):  #520 (line in Coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #521 (line in Coconut source)

        raise  #523 (line in Coconut source)


@_coconut_tco  #525 (line in Coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #525 (line in Coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #529 (line in Coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #530 (line in Coconut source)

_coconut_op_U3c_U24 = fmapConst  #531 (line in Coconut source)

#### Applicative:
Applicative = Functor  #534 (line in Coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #535 (line in Coconut source)

if TYPE_CHECKING:  #537 (line in Coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #538 (line in Coconut source)
        ...  #539 (line in Coconut source)

else:  #540 (line in Coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #541 (line in Coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #545 (line in Coconut source)

        __slots__ = ()  #547 (line in Coconut source)
        _coconut_is_data = True  #547 (line in Coconut source)
        __match_args__ = ('val',)  #547 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #547 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #547 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #547 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #547 (line in Coconut source)
        def __eq__(self, other):  #547 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #547 (line in Coconut source)
        def __hash__(self):  #547 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #547 (line in Coconut source)
        def __join__(self) -> 'T.Any':  #547 (line in Coconut source)
            return (self.val)  #547 (line in Coconut source)


        def __call__(self, arg: 'T.Any') -> 'T.Any':  #549 (line in Coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #550 (line in Coconut source)
            return (self.val)  #551 (line in Coconut source)


        @_coconut_tco  #553 (line in Coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #553 (line in Coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #555 (line in Coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #556 (line in Coconut source)

            try:  #558 (line in Coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #560 (line in Coconut source)

            except TypeError:  #562 (line in Coconut source)
# Check for functions
                if callable(M):  #564 (line in Coconut source)
                    return _coconut_tail_call(const, self.val)  #565 (line in Coconut source)

# Fallback
                raise  #568 (line in Coconut source)


    _coconut_call_set_names(pure)  #570 (line in Coconut source)
@_coconut_tco  #570 (line in Coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #570 (line in Coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #577 (line in Coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #579 (line in Coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #580 (line in Coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #583 (line in Coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #584 (line in Coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  #587 (line in Coconut source)

_coconut_op_U3c_U2a_U3e = ap  #588 (line in Coconut source)

@_coconut_tco  #590 (line in Coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #590 (line in Coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #594 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #595 (line in Coconut source)

_coconut_op_U2a_U3e = seqAr  #596 (line in Coconut source)

@_coconut_tco  #598 (line in Coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #598 (line in Coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #602 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #603 (line in Coconut source)

_coconut_op_U3c_U2a = seqAl  #604 (line in Coconut source)

def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #606 (line in Coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #610 (line in Coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut_partial(_coconut_partial, func), f1), f2))  # type: ignore  #611 (line in Coconut source)

#### Monad:

Monad = Applicative  #614 (line in Coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #615 (line in Coconut source)

@_coconut_tco  #617 (line in Coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #617 (line in Coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #622 (line in Coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #623 (line in Coconut source)

_coconut_op_U3e_U3e_U3e_U3d = bind  #624 (line in Coconut source)

@_coconut_tco  #626 (line in Coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #626 (line in Coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #630 (line in Coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #631 (line in Coconut source)

_coconut_op_U3e_U3e_U3e = seqM  #632 (line in Coconut source)

return_ = pure  #634 (line in Coconut source)

if TYPE_CHECKING:  #636 (line in Coconut source)
    def fail(msg: 'str') -> 'T.Any':  #637 (line in Coconut source)
        ...  #638 (line in Coconut source)

else:  #639 (line in Coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #640 (line in Coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #643 (line in Coconut source)

        __slots__ = ()  #645 (line in Coconut source)
        _coconut_is_data = True  #645 (line in Coconut source)
        __match_args__ = ('msg',)  #645 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #645 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #645 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #645 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #645 (line in Coconut source)
        def __eq__(self, other):  #645 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #645 (line in Coconut source)
        def __hash__(self):  #645 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #645 (line in Coconut source)
        @staticmethod  #645 (line in Coconut source)
        def __bool__() -> 'bool':  #646 (line in Coconut source)
            return (False)  #646 (line in Coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #648 (line in Coconut source)
            return (self)  #648 (line in Coconut source)


        @_coconut_tco  #650 (line in Coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #650 (line in Coconut source)
            if (hasattr)(M, "__fail__"):  #651 (line in Coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #652 (line in Coconut source)
            return _coconut_tail_call(makedata, type(M))  #653 (line in Coconut source)

# sequence_ and mapM_ defined in Foldable


    _coconut_call_set_names(fail)  #657 (line in Coconut source)
@_coconut_tco  #657 (line in Coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #657 (line in Coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #661 (line in Coconut source)
    return _coconut_tail_call((bind), m, func)  #662 (line in Coconut source)

_coconut_op_U3d_U3c_U3c_U3c = bindFrom  #663 (line in Coconut source)

@_coconut_tco  #665 (line in Coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #665 (line in Coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #672 (line in Coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #674 (line in Coconut source)
    _coconut_match_check_6 = False  #674 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #674 (line in Coconut source)
        _coconut_match_check_6 = True  #674 (line in Coconut source)
    if _coconut_match_check_6:  #674 (line in Coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #675 (line in Coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #678 (line in Coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #681 (line in Coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #682 (line in Coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  #685 (line in Coconut source)
    _coconut_case_match_check_0 = False  #685 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #685 (line in Coconut source)
        _coconut_case_match_check_0 = True  #685 (line in Coconut source)
    if _coconut_case_match_check_0:  #685 (line in Coconut source)
        if not ms:  #689 (line in Coconut source)
            return (ms)  # type: ignore  #690 (line in Coconut source)
        vals = []  # type: ignore  #691 (line in Coconut source)
        fallback = ms  #692 (line in Coconut source)
        for m in (ms):  #693 (line in Coconut source)
            if m:  #694 (line in Coconut source)
                vals.extend(m)  # type: ignore  #695 (line in Coconut source)
            else:  #696 (line in Coconut source)
                fallback = m  # type: ignore  #697 (line in Coconut source)
        if not vals:  #698 (line in Coconut source)
            return (fallback)  # type: ignore  #699 (line in Coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  # type: ignore  #700 (line in Coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #703 (line in Coconut source)
        _coconut_case_match_check_0 = True  #703 (line in Coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #703 (line in Coconut source)
            _coconut_case_match_check_0 = False  #703 (line in Coconut source)
        if _coconut_case_match_check_0:  #703 (line in Coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #704 (line in Coconut source)

    if not _coconut_case_match_check_0:  #706 (line in Coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #707 (line in Coconut source)


if _coconut.typing.TYPE_CHECKING:  #709 (line in Coconut source)
    @_coconut_tco  #709 (line in Coconut source)
    @_coconut_mark_as_match  #709 (line in Coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]',) -> 'TMonad':  #709 (line in Coconut source)
        """
    The call
        do([m1, m2, ...], func)
    is equivalent to the sequence of binds
        m1 `bind` x1 ->
            m2 `bind` x2 ->
                ...
                    func(x1, x2, ...)
    which is meant to mimic the do notation
        x1 <- m1
        x2 <- m2
        ...
        func(x1, x2, ...)
    or do can also be used as a decorator such that
        @do$([m1, m2, ...])
        def func(x1, x2, ...) =
            ...
    also does the same thing.
    """  #728 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #729 (line in Coconut source)
else:  #729 (line in Coconut source)
    @_coconut_tco  #729 (line in Coconut source)
    @_coconut_mark_as_match  #729 (line in Coconut source)
    def do(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #729 (line in Coconut source)
        """
    The call
        do([m1, m2, ...], func)
    is equivalent to the sequence of binds
        m1 `bind` x1 ->
            m2 `bind` x2 ->
                ...
                    func(x1, x2, ...)
    which is meant to mimic the do notation
        x1 <- m1
        x2 <- m2
        ...
        func(x1, x2, ...)
    or do can also be used as a decorator such that
        @do$([m1, m2, ...])
        def func(x1, x2, ...) =
            ...
    also does the same thing.
    """  #728 (line in Coconut source)

        _coconut_match_check_7 = False  #729 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #729 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #729 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #729 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #729 (line in Coconut source)
        if not _coconut_match_check_7:  #729 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #729 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #729 (line in Coconut source)
            if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #729 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #729 (line in Coconut source)
                    _coconut_match_temp_31 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #729 (line in Coconut source)
                    _coconut_match_set_name_func = _coconut_match_temp_31  #729 (line in Coconut source)
                    if not _coconut_match_kwargs:  #729 (line in Coconut source)
                        _coconut_match_check_7 = True  #729 (line in Coconut source)
            if _coconut_match_check_7:  #729 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #729 (line in Coconut source)
                    func = _coconut_match_set_name_func  #729 (line in Coconut source)

            if _coconut_match_check_7:  #729 (line in Coconut source)

                    return _coconut_tail_call(func)  #733 (line in Coconut source)

        if not _coconut_match_check_7:  #734 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #734 (line in Coconut source)
            _coconut_match_set_name_m = _coconut_sentinel  #734 (line in Coconut source)
            _coconut_match_set_name_ms = _coconut_sentinel  #734 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #734 (line in Coconut source)
            if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #734 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #734 (line in Coconut source)
                    _coconut_match_set_name_m = _coconut_match_args[0][0]  #734 (line in Coconut source)
                    _coconut_match_temp_33 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #734 (line in Coconut source)
                    _coconut_match_temp_32 = _coconut.list(_coconut_match_args[0][1:])  #734 (line in Coconut source)
                    _coconut_match_set_name_func = _coconut_match_temp_33  #734 (line in Coconut source)
                    _coconut_match_set_name_ms = _coconut_match_temp_32  #734 (line in Coconut source)
                    if not _coconut_match_kwargs:  #734 (line in Coconut source)
                        _coconut_match_check_7 = True  #734 (line in Coconut source)
            if _coconut_match_check_7:  #734 (line in Coconut source)
                if _coconut_match_set_name_m is not _coconut_sentinel:  #734 (line in Coconut source)
                    m = _coconut_match_set_name_m  #734 (line in Coconut source)
                if _coconut_match_set_name_ms is not _coconut_sentinel:  #734 (line in Coconut source)
                    ms = _coconut_match_set_name_ms  #734 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #734 (line in Coconut source)
                    func = _coconut_match_set_name_func  #734 (line in Coconut source)

            if _coconut_match_check_7:  #734 (line in Coconut source)

                    return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut_partial(func, x)))  #735 (line in Coconut source)



## Folds and traversals:

#### Foldable:

        if not _coconut_match_check_7:  #742 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def do:', _coconut_match_args)  #742 (line in Coconut source)


Foldable = T.Sequence  #742 (line in Coconut source)

@_coconut_tco  #744 (line in Coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #744 (line in Coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #745 (line in Coconut source)


mapM_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]  #747 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #747 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #747 (line in Coconut source)
__annotations__["mapM_"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #747 (line in Coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #748 (line in Coconut source)

@_coconut_tco  #750 (line in Coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #750 (line in Coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #751 (line in Coconut source)


@_coconut_tco  #753 (line in Coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #753 (line in Coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #754 (line in Coconut source)


@_coconut_tco  #756 (line in Coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #756 (line in Coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #757 (line in Coconut source)


foldl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]  #759 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #759 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #759 (line in Coconut source)
__annotations__["foldl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #759 (line in Coconut source)
foldl1 = reduce  #760 (line in Coconut source)

@_coconut_tco  #762 (line in Coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #762 (line in Coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #763 (line in Coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #765 (line in Coconut source)
    return (len(xs) == 0)  #766 (line in Coconut source)


length = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable], int]  #768 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #768 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #768 (line in Coconut source)
__annotations__["length"] = '_coconut.typing.Callable[[Foldable], int]'  #768 (line in Coconut source)
length = len  #769 (line in Coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #771 (line in Coconut source)
    return (e in xs)  #772 (line in Coconut source)


maximum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #774 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #774 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #774 (line in Coconut source)
__annotations__["maximum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #774 (line in Coconut source)
maximum = _max  #775 (line in Coconut source)

minimum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #777 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #777 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #777 (line in Coconut source)
__annotations__["minimum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #777 (line in Coconut source)
minimum = _min  #778 (line in Coconut source)

sum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #780 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #780 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #780 (line in Coconut source)
__annotations__["sum"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #780 (line in Coconut source)
sum = _sum  #781 (line in Coconut source)

product = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #783 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #783 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #783 (line in Coconut source)
__annotations__["product"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #783 (line in Coconut source)
product = _coconut_partial(reduce, _coconut.operator.mul)  #784 (line in Coconut source)

#### Traversable:
Traversable = T.Iterable  #787 (line in Coconut source)

@_coconut_tco  #789 (line in Coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #789 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #790 (line in Coconut source)


@_coconut_tco  #792 (line in Coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #792 (line in Coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #793 (line in Coconut source)


traverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]  #795 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #795 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #795 (line in Coconut source)
__annotations__["traverse"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #795 (line in Coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  # type: ignore  #796 (line in Coconut source)

sequence = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]  #798 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #798 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #798 (line in Coconut source)
__annotations__["sequence"] = '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #798 (line in Coconut source)
sequence = sequenceA  #799 (line in Coconut source)

mapM = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]  #801 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #801 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #801 (line in Coconut source)
__annotations__["mapM"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #801 (line in Coconut source)
mapM = traverse  #802 (line in Coconut source)



## Miscellaneous functions:
id = ident  # type: _coconut.typing.Callable[[Ta], Ta]  #807 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #807 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #807 (line in Coconut source)
__annotations__["id"] = '_coconut.typing.Callable[[Ta], Ta]'  #807 (line in Coconut source)

@_coconut_tco  #809 (line in Coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #809 (line in Coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #813 (line in Coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #814 (line in Coconut source)


if _coconut.typing.TYPE_CHECKING:  #816 (line in Coconut source)
    @_coconut.typing.overload  #816 (line in Coconut source)
    @_coconut_tco  #816 (line in Coconut source)
    @_coconut_mark_as_match  #816 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta',) -> 'Tb':  #816 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #823 (line in Coconut source)
    @_coconut.typing.overload  #823 (line in Coconut source)
    @_coconut_tco  #823 (line in Coconut source)
    @_coconut_mark_as_match  #823 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta',) -> '_coconut.typing.Callable[[Tb], Tc]':  #823 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #823 (line in Coconut source)
    @_coconut.typing.overload  #823 (line in Coconut source)
    @_coconut_tco  #823 (line in Coconut source)
    @_coconut_mark_as_match  #823 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta',) -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #823 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #823 (line in Coconut source)
    @_coconut.typing.overload  #823 (line in Coconut source)
    @_coconut_tco  #823 (line in Coconut source)
    @_coconut_mark_as_match  #823 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta',) -> 'T.Any':  #823 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #823 (line in Coconut source)
    @_coconut_tco  #823 (line in Coconut source)
    @_coconut_mark_as_match  #823 (line in Coconut source)
    def apply(*_coconut_args, **_coconut_kwargs):  #823 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #823 (line in Coconut source)
else:  #823 (line in Coconut source)
    @_coconut_tco  #823 (line in Coconut source)
    @_coconut_mark_as_match  #823 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #823 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #822 (line in Coconut source)

        _coconut_match_check_8 = False  #823 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #823 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #823 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #823 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #823 (line in Coconut source)
        if not _coconut_match_check_8:  #823 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #823 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #823 (line in Coconut source)
            _coconut_match_set_name_arg = _coconut_sentinel  #823 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "func" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "arg" in _coconut_match_kwargs)) == 1):  #823 (line in Coconut source)
                _coconut_match_temp_34 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("func")  #823 (line in Coconut source)
                _coconut_match_temp_35 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("arg")  #823 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_34  #823 (line in Coconut source)
                _coconut_match_set_name_arg = _coconut_match_temp_35  #823 (line in Coconut source)
                if not _coconut_match_kwargs:  #823 (line in Coconut source)
                    _coconut_match_check_8 = True  #823 (line in Coconut source)
            if _coconut_match_check_8:  #823 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #823 (line in Coconut source)
                    func = _coconut_match_set_name_func  #823 (line in Coconut source)
                if _coconut_match_set_name_arg is not _coconut_sentinel:  #823 (line in Coconut source)
                    arg = _coconut_match_set_name_arg  #823 (line in Coconut source)

            if _coconut_match_check_8:  #823 (line in Coconut source)

                    return _coconut_tail_call((of), func, arg)  #840 (line in Coconut source)

        if not _coconut_match_check_8:  #841 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def apply:', _coconut_match_args)  #841 (line in Coconut source)


_coconut_op_U24_U24 = apply  #841 (line in Coconut source)

@_coconut_tco  #843 (line in Coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #843 (line in Coconut source)
    while True:  #844 (line in Coconut source)
        if cond(x):  #844 (line in Coconut source)
            return (x)  #845 (line in Coconut source)
        try:  # tail recursive  #846 (line in Coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_57  # type: ignore  # tail recursive  #846 (line in Coconut source)
        except _coconut.NameError:  # tail recursive  #846 (line in Coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #846 (line in Coconut source)
        if _coconut_tre_check_0:  # tail recursive  #846 (line in Coconut source)
            (cond, func, x,) = (cond, func, func(x),)  # tail recursive  #846 (line in Coconut source)
            continue  # tail recursive  #846 (line in Coconut source)
        else:  # tail recursive  #846 (line in Coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #847 (line in Coconut source)
        return None  #848 (line in Coconut source)

_coconut_recursive_func_57 = until  #848 (line in Coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #848 (line in Coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #852 (line in Coconut source)
    if TYPE_CHECKING:  #853 (line in Coconut source)
        return (x)  #853 (line in Coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #855 (line in Coconut source)
        for i in ((takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count())):  #856 (line in Coconut source)
            if (isinstance)(x, pure):  #857 (line in Coconut source)
                x = x.pure_as(y)  #858 (line in Coconut source)
            elif (isinstance)(x, fail):  #859 (line in Coconut source)
                x = x.fail_as(y)  #860 (line in Coconut source)
            elif (isinstance)(x, Mempty):  #861 (line in Coconut source)
                x = x.mempty_as(y)  #862 (line in Coconut source)
            else:  #863 (line in Coconut source)
                break  #864 (line in Coconut source)
    return (x)  #865 (line in Coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #867 (line in Coconut source)

def error(msg: 'str') -> 'None':  #869 (line in Coconut source)
    raise Exception(msg)  #870 (line in Coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #872 (line in Coconut source)
    raise Exception(msg) from None  #873 (line in Coconut source)


undefined = None  # type: T.Any  #875 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #875 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #875 (line in Coconut source)
__annotations__["undefined"] = 'T.Any'  #875 (line in Coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #877 (line in Coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #880 (line in Coconut source)
    return (y)  #881 (line in Coconut source)


@_coconut_tco  #883 (line in Coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #883 (line in Coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #888 (line in Coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #889 (line in Coconut source)




# List operations:

@_coconut_tco  #895 (line in Coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #895 (line in Coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #899 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #900 (line in Coconut source)

# type: ignore
map = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]  # type: ignore  #902 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #902 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #902 (line in Coconut source)
__annotations__["map"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #902 (line in Coconut source)
map = _map  # type: ignore  #903 (line in Coconut source)

@_coconut_tco  #905 (line in Coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #905 (line in Coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #909 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #910 (line in Coconut source)

_coconut_op_U2b_U2b = chain  #911 (line in Coconut source)

filter = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  # type: ignore  #913 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #913 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #913 (line in Coconut source)
__annotations__["filter"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #913 (line in Coconut source)
filter = _filter  # type: ignore  #914 (line in Coconut source)

head = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #916 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #916 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #916 (line in Coconut source)
__annotations__["head"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #916 (line in Coconut source)
head = _coconut_partial(_coconut_iter_getitem, index=(0))  #917 (line in Coconut source)

last = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #919 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #919 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #919 (line in Coconut source)
__annotations__["last"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #919 (line in Coconut source)
last = _coconut_partial(_coconut_iter_getitem, index=(-1))  #920 (line in Coconut source)

tail = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #922 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #922 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #922 (line in Coconut source)
__annotations__["tail"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #922 (line in Coconut source)
tail = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #923 (line in Coconut source)

init = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #925 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #925 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #925 (line in Coconut source)
__annotations__["init"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #925 (line in Coconut source)
init = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #926 (line in Coconut source)

@_coconut_tco  #928 (line in Coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #928 (line in Coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #932 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #933 (line in Coconut source)

_coconut_op_U21_U21 = at  #934 (line in Coconut source)

reverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]  #936 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #936 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #936 (line in Coconut source)
__annotations__["reverse"] = '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #936 (line in Coconut source)
reverse = _reversed  #937 (line in Coconut source)



## Special folds:
and_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #942 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #942 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #942 (line in Coconut source)
__annotations__["and_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #942 (line in Coconut source)
and_ = _all  #943 (line in Coconut source)

or_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #945 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #945 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #945 (line in Coconut source)
__annotations__["or_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #945 (line in Coconut source)
or_ = _any  #946 (line in Coconut source)

any = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #948 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #948 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #948 (line in Coconut source)
__annotations__["any"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #948 (line in Coconut source)
any = _coconut_forward_compose(map, or_)  #949 (line in Coconut source)

all = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #951 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #951 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #951 (line in Coconut source)
__annotations__["all"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #951 (line in Coconut source)
all = _coconut_forward_compose(map, and_)  #952 (line in Coconut source)

@_coconut_tco  #954 (line in Coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #954 (line in Coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #955 (line in Coconut source)


concatMap = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]  #957 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #957 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #957 (line in Coconut source)
__annotations__["concatMap"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #957 (line in Coconut source)
concatMap = _coconut_forward_compose(map, concat)  #958 (line in Coconut source)



## Building lists:

### Scans:
@_coconut_tco  #965 (line in Coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #965 (line in Coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #966 (line in Coconut source)


scanl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #968 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #968 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #968 (line in Coconut source)
__annotations__["scanl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #968 (line in Coconut source)
scanl1 = scan  #969 (line in Coconut source)

@_coconut_tco  #971 (line in Coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #971 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #972 (line in Coconut source)


@_coconut_tco  #974 (line in Coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #974 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #975 (line in Coconut source)

### Infinite lists:

@recursive_generator  #978 (line in Coconut source)
@_coconut_tco  #979 (line in Coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #979 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #980 (line in Coconut source)


@recursive_generator  #982 (line in Coconut source)
@_coconut_tco  #983 (line in Coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #983 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #984 (line in Coconut source)


@_coconut_tco  #986 (line in Coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #986 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #987 (line in Coconut source)


if TYPE_CHECKING:  #989 (line in Coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  # type: ignore  #990 (line in Coconut source)
        ...  #991 (line in Coconut source)

else:  #992 (line in Coconut source)
    @recursive_generator  #993 (line in Coconut source)
    @_coconut_tco  #994 (line in Coconut source)
    @_coconut_mark_as_match  #994 (line in Coconut source)
    def cycle(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #994 (line in Coconut source)
        _coconut_match_check_9 = False  #994 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #994 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #994 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #994 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #994 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #994 (line in Coconut source)
            _coconut_match_temp_36 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #994 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_36  #994 (line in Coconut source)
            if not _coconut_match_kwargs:  #994 (line in Coconut source)
                _coconut_match_check_9 = True  #994 (line in Coconut source)
        if _coconut_match_check_9:  #994 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #994 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #994 (line in Coconut source)
        if _coconut_match_check_9 and not (len(xs) > 0):  #994 (line in Coconut source)
            _coconut_match_check_9 = False  #994 (line in Coconut source)
        if not _coconut_match_check_9:  #994 (line in Coconut source)
            raise _coconut_FunctionMatchError('def \\cycle(xs if len(xs) > 0) =', _coconut_match_args)  #994 (line in Coconut source)

        return _coconut_tail_call(_cycle, xs)  #995 (line in Coconut source)



## Sublists:

@_coconut_tco  #1000 (line in Coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1000 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #1001 (line in Coconut source)


@_coconut_tco  #1003 (line in Coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1003 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #1004 (line in Coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]])':  #1006 (line in Coconut source)
    reit = reiterable(xs)  #1007 (line in Coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #1008 (line in Coconut source)


takeWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1010 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1010 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1010 (line in Coconut source)
__annotations__["takeWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1010 (line in Coconut source)
takeWhile = takewhile  #1011 (line in Coconut source)

dropWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1013 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1013 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1013 (line in Coconut source)
__annotations__["dropWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1013 (line in Coconut source)
dropWhile = dropwhile  #1014 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #1016 (line in Coconut source)
    @_coconut_mark_as_match  #1016 (line in Coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]])':  #1016 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #1016 (line in Coconut source)
else:  #1016 (line in Coconut source)
    @_coconut_mark_as_match  #1016 (line in Coconut source)
    def span(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1016 (line in Coconut source)

        _coconut_match_check_10 = False  #1016 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1016 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1016 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1016 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #1016 (line in Coconut source)
        if not _coconut_match_check_10:  #1016 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1016 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #1016 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1016 (line in Coconut source)
                    if not _coconut_match_kwargs:  #1016 (line in Coconut source)
                        _coconut_match_check_10 = True  #1016 (line in Coconut source)

            if _coconut_match_check_10:  #1016 (line in Coconut source)

                    return (([], []))  #1019 (line in Coconut source)

        if not _coconut_match_check_10:  #1020 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1020 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_sentinel  #1020 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #1020 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_sentinel  #1020 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1020 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1020 (line in Coconut source)
                    _coconut_match_temp_37 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1020 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[1][0]  #1020 (line in Coconut source)
                    _coconut_match_set_name_cond = _coconut_match_temp_37  #1020 (line in Coconut source)
                    _coconut_match_temp_38 = _coconut.list(_coconut_match_args[1][1:])  #1020 (line in Coconut source)
                    _coconut_match_set_name_xs = _coconut_match_temp_38  #1020 (line in Coconut source)
                    if not _coconut_match_kwargs:  #1020 (line in Coconut source)
                        _coconut_match_check_10 = True  #1020 (line in Coconut source)
            if _coconut_match_check_10:  #1020 (line in Coconut source)
                if _coconut_match_set_name_cond is not _coconut_sentinel:  #1020 (line in Coconut source)
                    cond = _coconut_match_set_name_cond  #1020 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #1020 (line in Coconut source)
                    x = _coconut_match_set_name_x  #1020 (line in Coconut source)
                if _coconut_match_set_name_xs is not _coconut_sentinel:  #1020 (line in Coconut source)
                    xs = _coconut_match_set_name_xs  #1020 (line in Coconut source)
            if _coconut_match_check_10 and not (cond(x)):  #1020 (line in Coconut source)
                _coconut_match_check_10 = False  #1020 (line in Coconut source)

            if _coconut_match_check_10:  #1020 (line in Coconut source)

                    ys, zs = span(cond, xs)  #1021 (line in Coconut source)
                    return (([x,] + ys, zs))  #1022 (line in Coconut source)

        if not _coconut_match_check_10:  #1023 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1023 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_sentinel  #1023 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_sentinel  #1023 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1023 (line in Coconut source)
                _coconut_match_temp_39 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1023 (line in Coconut source)
                _coconut_match_temp_40 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1023 (line in Coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_39  #1023 (line in Coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_40  #1023 (line in Coconut source)
                if not _coconut_match_kwargs:  #1023 (line in Coconut source)
                    _coconut_match_check_10 = True  #1023 (line in Coconut source)
            if _coconut_match_check_10:  #1023 (line in Coconut source)
                if _coconut_match_set_name_cond is not _coconut_sentinel:  #1023 (line in Coconut source)
                    cond = _coconut_match_set_name_cond  #1023 (line in Coconut source)
                if _coconut_match_set_name_xs is not _coconut_sentinel:  #1023 (line in Coconut source)
                    xs = _coconut_match_set_name_xs  #1023 (line in Coconut source)

            if _coconut_match_check_10:  #1023 (line in Coconut source)

                    return (([], xs))  #1024 (line in Coconut source)


        if not _coconut_match_check_10:  #1026 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def span:', _coconut_match_args)  #1026 (line in Coconut source)


@_coconut_tco  #1026 (line in Coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #1026 (line in Coconut source)
    """
    break_ = break
    """  #1029 (line in Coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1030 (line in Coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #1035 (line in Coconut source)
    return (e not in xs)  #1036 (line in Coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> 'Maybe':  #1038 (line in Coconut source)
    try:  #1039 (line in Coconut source)
        return (((Just)((_coconut_iter_getitem(((dropwhile)(lambda pair: pair[0] != key, assocs)), (0)))[1])))  #1040 (line in Coconut source)
    except IndexError:  #1047 (line in Coconut source)
        return (nothing)  #1048 (line in Coconut source)



## Zipping and unzipping lists:
# type: ignore
zip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]  # type: ignore  #1053 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #1053 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #1053 (line in Coconut source)
__annotations__["zip"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]'  # type: ignore  #1053 (line in Coconut source)
zip = _zip  # type: ignore  #1054 (line in Coconut source)

zip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]  #1056 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1056 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1056 (line in Coconut source)
__annotations__["zip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]'  #1056 (line in Coconut source)
zip3 = _zip  #1057 (line in Coconut source)

@_coconut_tco  #1059 (line in Coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #1059 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2)  #1060 (line in Coconut source)


@_coconut_tco  #1062 (line in Coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1062 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2, xs3)  #1063 (line in Coconut source)


@_coconut_tco  #1065 (line in Coconut source)
def unzip(xs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]])':  #1065 (line in Coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1066 (line in Coconut source)


unzip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]  #1068 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1068 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1068 (line in Coconut source)
__annotations__["unzip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]'  #1068 (line in Coconut source)
unzip3 = unzip  # type: ignore  #1069 (line in Coconut source)



## Functions on strings:
lines = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1074 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1074 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1074 (line in Coconut source)
__annotations__["lines"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1074 (line in Coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1075 (line in Coconut source)

words = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1077 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1077 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1077 (line in Coconut source)
__annotations__["words"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1077 (line in Coconut source)
words = _coconut.operator.methodcaller("split")  #1078 (line in Coconut source)

@_coconut_tco  #1080 (line in Coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1080 (line in Coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1081 (line in Coconut source)


unwords = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]  #1083 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1083 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1083 (line in Coconut source)
__annotations__["unwords"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1083 (line in Coconut source)
unwords = " ".join  #1084 (line in Coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1092 (line in Coconut source)

Show = T.Any  #1094 (line in Coconut source)

showsPrec = NotImplemented  #1096 (line in Coconut source)

show = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Ta], str]  #1098 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1098 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1098 (line in Coconut source)
__annotations__["show"] = '_coconut.typing.Callable[[Ta], str]'  #1098 (line in Coconut source)
show = repr  #1099 (line in Coconut source)

def shows(x: 'Show') -> 'ShowS':  #1101 (line in Coconut source)
    return (lambda s: repr(x) + s)  #1102 (line in Coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1104 (line in Coconut source)
    return (lambda s: repr(list(xs)) + s)  #1105 (line in Coconut source)


def showString(x: 'str') -> 'ShowS':  #1107 (line in Coconut source)
    return (lambda s: x + s)  #1108 (line in Coconut source)


showChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], ShowS]  #1110 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1110 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1110 (line in Coconut source)
__annotations__["showChar"] = '_coconut.typing.Callable[[Char], ShowS]'  #1110 (line in Coconut source)
showChar = showString  #1111 (line in Coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1113 (line in Coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1114 (line in Coconut source)



## Converting from String:

ReadS = NotImplemented  #1122 (line in Coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1124 (line in Coconut source)

readsPrec = NotImplemented  #1135 (line in Coconut source)

readList = NotImplemented  #1137 (line in Coconut source)

reads = NotImplemented  #1139 (line in Coconut source)

readParen = NotImplemented  #1141 (line in Coconut source)

@_coconut_tco  #1143 (line in Coconut source)
def read(s: 'str') -> 'Read':  #1143 (line in Coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1144 (line in Coconut source)


lex = NotImplemented  #1146 (line in Coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1154 (line in Coconut source)
    __slots__ = ()  #1154 (line in Coconut source)
    _coconut_is_data = True  #1154 (line in Coconut source)
    __match_args__ = ('io_func',)  #1154 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1154 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1154 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1154 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #1154 (line in Coconut source)
    def __eq__(self, other):  #1154 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1154 (line in Coconut source)
    def __hash__(self):  #1154 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #1154 (line in Coconut source)
    @staticmethod  #1155 (line in Coconut source)
    @_coconut_tco  #1156 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1156 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1157 (line in Coconut source)


    @staticmethod  #1159 (line in Coconut source)
    @_coconut_tco  #1160 (line in Coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1160 (line in Coconut source)
        def _coconut_lambda_0():  #1161 (line in Coconut source)
            raise IOError(msg)  #1161 (line in Coconut source)

        return _coconut_tail_call(IO, _coconut_lambda_0)  #1161 (line in Coconut source)


    @_coconut_tco  #1163 (line in Coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1163 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1164 (line in Coconut source)


    @_coconut_tco  #1166 (line in Coconut source)
    def __join__(self) -> 'IO':  #1166 (line in Coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1167 (line in Coconut source)


    @staticmethod  #1169 (line in Coconut source)
    @_coconut_tco  #1170 (line in Coconut source)
    def __mempty__() -> 'IO':  #1170 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1171 (line in Coconut source)


    @_coconut_tco  #1173 (line in Coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1173 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1174 (line in Coconut source)


_coconut_call_set_names(IO)  #1176 (line in Coconut source)
_nullIO = IO(lambda: None)  # type: IO  #1176 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1176 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1176 (line in Coconut source)
__annotations__["_nullIO"] = 'IO'  #1176 (line in Coconut source)

@_coconut_tco  #1178 (line in Coconut source)
def asIO(io: 'IO') -> 'IO':  #1178 (line in Coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1183 (line in Coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1184 (line in Coconut source)


@_coconut_tco  #1186 (line in Coconut source)
def unIO(io: 'IO') -> 'T.Any':  #1186 (line in Coconut source)
    """
    The unIO function is an impure function which performs the
    I/O contained in the given IO object and returns the result.
    In particular, the recommendation is to write
        @unIO
        @do$([io1, io2, ...])
        def main(r1, r2, ...) =
            ...
    which is equivalent to the Haskell code
        main = do
            r1 <- io1
            r2 <- io2
            ...
    """  #1200 (line in Coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1201 (line in Coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1209 (line in Coconut source)
def putStr(s: 'str') -> 'IO':  #1209 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s, end=""))  #1210 (line in Coconut source)


putChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], IO]  #1212 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1212 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1212 (line in Coconut source)
__annotations__["putChar"] = '_coconut.typing.Callable[[Char], IO]'  #1212 (line in Coconut source)
putChar = putStr  #1213 (line in Coconut source)

@_coconut_tco  #1215 (line in Coconut source)
def putStrLn(s: 'str') -> 'IO':  #1215 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s))  #1216 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1218 (line in Coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1218 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, show(x)))  #1219 (line in Coconut source)


### Input functions:

getChar = IO(_coconut_partial(sys.stdin.read, 1))  # type: IO  #1223 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1223 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1223 (line in Coconut source)
__annotations__["getChar"] = 'IO'  #1223 (line in Coconut source)

getLine = IO(input)  # type: IO  #1225 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1225 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1225 (line in Coconut source)
__annotations__["getLine"] = 'IO'  #1225 (line in Coconut source)

getContents = IO(sys.stdin.read)  # type: IO  #1227 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1227 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1227 (line in Coconut source)
__annotations__["getContents"] = 'IO'  #1227 (line in Coconut source)

@_coconut_tco  #1229 (line in Coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1229 (line in Coconut source)
    def do_interact():  #1230 (line in Coconut source)
        while True:  #1231 (line in Coconut source)
            (_print)((func)(input()))  #1232 (line in Coconut source)

    return _coconut_tail_call(IO, do_interact)  #1233 (line in Coconut source)


### Files:

FilePath = str  #1237 (line in Coconut source)

@_coconut_tco  #1239 (line in Coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1239 (line in Coconut source)
    def do_readFile() -> 'str':  #1240 (line in Coconut source)
        with open(fpath, "r+") as f:  #1241 (line in Coconut source)
            return (f.read())  #1242 (line in Coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1243 (line in Coconut source)


@_coconut_tco  #1245 (line in Coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1245 (line in Coconut source)
    def do_writeFile() -> 'None':  #1246 (line in Coconut source)
        with open(fpath, "w+") as f:  #1247 (line in Coconut source)
            f.write(text)  #1248 (line in Coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1249 (line in Coconut source)


@_coconut_tco  #1251 (line in Coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1251 (line in Coconut source)
    def do_appendFile() -> 'None':  #1252 (line in Coconut source)
        with open(fpath, "a+") as f:  #1253 (line in Coconut source)
            f.write(text)  #1254 (line in Coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1255 (line in Coconut source)


@_coconut_tco  #1257 (line in Coconut source)
def readIO(s: 'str') -> 'IO':  #1257 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(read, s))  #1258 (line in Coconut source)


@_coconut_tco  #1260 (line in Coconut source)
def readLn() -> 'IO':  #1260 (line in Coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1261 (line in Coconut source)



## Exception handling:

@_coconut_tco  #1266 (line in Coconut source)
def ioError(err: 'IOError') -> 'IO':  #1266 (line in Coconut source)
    def _coconut_lambda_1():  #1267 (line in Coconut source)
        raise err  #1267 (line in Coconut source)

    return _coconut_tail_call(IO, _coconut_lambda_1)  #1267 (line in Coconut source)


@_coconut_tco  #1269 (line in Coconut source)
def userError(msg: 'str') -> 'IOError':  #1269 (line in Coconut source)
    return _coconut_tail_call(IOError, msg)  #1270 (line in Coconut source)
