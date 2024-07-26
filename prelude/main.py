#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe8b393ab

# Compiled with Coconut version 3.1.1-post_dev3

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.1-post_dev3', '35', True)
_coconut_cached__coconut__ = _coconut_sys.modules.get('__coconut__')
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules['_coconut_cached__coconut__'] = _coconut_cached__coconut__
        del _coconut_sys.modules['__coconut__']
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == '__coconut__':  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == '__coconut__':  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
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

class Eq(T.Protocol):  #166 (line in Coconut source)
    def __eq__(self, other: 'object') -> 'bool':  #167 (line in Coconut source)
        return (bot)  #167 (line in Coconut source)

#### Ord:

_coconut_call_set_names(Eq)  #170 (line in Coconut source)
class Ord(Eq, T.Protocol, T.Generic[Tcontra]):  #170 (line in Coconut source)
    def __lt__(self: 'Tcontra', other: 'Tcontra') -> 'bool':  #171 (line in Coconut source)
        return (bot)  #171 (line in Coconut source)

    def __gt__(self: 'Tcontra', other: 'Tcontra') -> 'bool':  #172 (line in Coconut source)
        return (bot)  #172 (line in Coconut source)

    def __le__(self: 'Tcontra', other: 'Tcontra') -> 'bool':  #173 (line in Coconut source)
        return (bot)  #173 (line in Coconut source)

    def __ge__(self: 'Tcontra', other: 'Tcontra') -> 'bool':  #174 (line in Coconut source)
        return (bot)  #174 (line in Coconut source)



_coconut_call_set_names(Ord)  #177 (line in Coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #177 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #179 (line in Coconut source)
    @_coconut_mark_as_match  #179 (line in Coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #179 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #179 (line in Coconut source)
else:  #179 (line in Coconut source)
    @_coconut_mark_as_match  #179 (line in Coconut source)
    def compare(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #179 (line in Coconut source)

        _coconut_match_check_2 = False  #179 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #179 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #179 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #179 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #179 (line in Coconut source)
        if not _coconut_match_check_2:  #179 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #179 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #179 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #179 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #179 (line in Coconut source)
                _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #179 (line in Coconut source)
                _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #179 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_19  #179 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_20  #179 (line in Coconut source)
                if not _coconut_match_kwargs:  #179 (line in Coconut source)
                    _coconut_match_check_2 = True  #179 (line in Coconut source)
            if _coconut_match_check_2:  #179 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #179 (line in Coconut source)
                    x = _coconut_match_set_name_x  #179 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #179 (line in Coconut source)
                    y = _coconut_match_set_name_y  #179 (line in Coconut source)
            if _coconut_match_check_2 and not (x == y):  #179 (line in Coconut source)
                _coconut_match_check_2 = False  #179 (line in Coconut source)

            if _coconut_match_check_2:  #179 (line in Coconut source)

                    return (eq)  #181 (line in Coconut source)

        if not _coconut_match_check_2:  #182 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #182 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #182 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #182 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #182 (line in Coconut source)
                _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #182 (line in Coconut source)
                _coconut_match_temp_22 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #182 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_21  #182 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_22  #182 (line in Coconut source)
                if not _coconut_match_kwargs:  #182 (line in Coconut source)
                    _coconut_match_check_2 = True  #182 (line in Coconut source)
            if _coconut_match_check_2:  #182 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #182 (line in Coconut source)
                    x = _coconut_match_set_name_x  #182 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #182 (line in Coconut source)
                    y = _coconut_match_set_name_y  #182 (line in Coconut source)
            if _coconut_match_check_2 and not (x < y):  #182 (line in Coconut source)
                _coconut_match_check_2 = False  #182 (line in Coconut source)

            if _coconut_match_check_2:  #182 (line in Coconut source)

                    return (lt)  #182 (line in Coconut source)

        if not _coconut_match_check_2:  #183 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #183 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #183 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #183 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #183 (line in Coconut source)
                _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #183 (line in Coconut source)
                _coconut_match_temp_24 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #183 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_23  #183 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_24  #183 (line in Coconut source)
                if not _coconut_match_kwargs:  #183 (line in Coconut source)
                    _coconut_match_check_2 = True  #183 (line in Coconut source)
            if _coconut_match_check_2:  #183 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #183 (line in Coconut source)
                    x = _coconut_match_set_name_x  #183 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #183 (line in Coconut source)
                    y = _coconut_match_set_name_y  #183 (line in Coconut source)
            if _coconut_match_check_2 and not (x > y):  #183 (line in Coconut source)
                _coconut_match_check_2 = False  #183 (line in Coconut source)

            if _coconut_match_check_2:  #183 (line in Coconut source)

                    return (gt)  #183 (line in Coconut source)

# type: ignore
        if not _coconut_match_check_2:  # type: ignore  #185 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def compare:', _coconut_match_args)  # type: ignore  #185 (line in Coconut source)
# type: ignore
# type: ignore
max = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  # type: ignore  #185 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #185 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #185 (line in Coconut source)
__annotations__["max"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  # type: ignore  #185 (line in Coconut source)
max = _max  #186 (line in Coconut source)

min = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  # type: ignore  #188 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #188 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #188 (line in Coconut source)
__annotations__["min"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  # type: ignore  #188 (line in Coconut source)
min = _min  #189 (line in Coconut source)

#### Enum:
if _coconut.typing.TYPE_CHECKING:  #192 (line in Coconut source)
    class _coconut_protocol_intersection_0(Ord, (_coconut_SupportsAdd), (_coconut_SupportsMinus), _coconut.typing.Protocol): pass  #192 (line in Coconut source)
Enum = '_coconut_protocol_intersection_0'  # type: _coconut.typing.TypeAlias  #192 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #192 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #192 (line in Coconut source)
__annotations__["Enum"] = '_coconut.typing.TypeAlias'  #192 (line in Coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #193 (line in Coconut source)

succ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #195 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #195 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #195 (line in Coconut source)
__annotations__["succ"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #195 (line in Coconut source)
succ = (_coconut_partial(_coconut.operator.add, 1))  #196 (line in Coconut source)

pred = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #198 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #198 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #198 (line in Coconut source)
__annotations__["pred"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #198 (line in Coconut source)
pred = (_coconut_complex_partial(_coconut_minus, {1: 1}, 2, ()))  #199 (line in Coconut source)

toEnum = NotImplemented  #201 (line in Coconut source)

fromEnum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Enum], int]  #203 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #203 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #203 (line in Coconut source)
__annotations__["fromEnum"] = '_coconut.typing.Callable[[Enum], int]'  #203 (line in Coconut source)
fromEnum = _int  #204 (line in Coconut source)

@_coconut_tco  #206 (line in Coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #206 (line in Coconut source)
    return _coconut_tail_call(iterate, succ, first)  #207 (line in Coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #209 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #210 (line in Coconut source)
    return (iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first) if step >= 0 else ())  # type: ignore  #211 (line in Coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #213 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #214 (line in Coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #215 (line in Coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #217 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #218 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #219 (line in Coconut source)
    steps = dist / step if step != 0 else 0  #220 (line in Coconut source)
    if steps < 0:  #221 (line in Coconut source)
        return (())  #222 (line in Coconut source)
    counter = iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first)  #223 (line in Coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #224 (line in Coconut source)


#### Bounded:

class _HasBounds(T.Protocol):  #228 (line in Coconut source)
    def __maxBound__(self) -> 'T.Any':  #229 (line in Coconut source)
        return (bot)  #229 (line in Coconut source)

    def __minBound__(self) -> 'T.Any':  #230 (line in Coconut source)
        return (bot)  #230 (line in Coconut source)


_coconut_call_set_names(_HasBounds)  #232 (line in Coconut source)
Bounded = '_coconut.typing.Union[bool, _HasBounds, T.Iterable[Bounded]]'  # type: _coconut.typing.TypeAlias  #232 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #232 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #232 (line in Coconut source)
__annotations__["Bounded"] = '_coconut.typing.TypeAlias'  #232 (line in Coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #233 (line in Coconut source)

@_coconut_tco  #235 (line in Coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #235 (line in Coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #239 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #241 (line in Coconut source)
        return (False)  # type: ignore  #242 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #245 (line in Coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #246 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #249 (line in Coconut source)


@_coconut_tco  #251 (line in Coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #251 (line in Coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #255 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #257 (line in Coconut source)
        return (True)  # type: ignore  #258 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #261 (line in Coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #262 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #265 (line in Coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #274 (line in Coconut source)

#### Integer:
Integer = int  #277 (line in Coconut source)

#### Float:
Float = float  #280 (line in Coconut source)

#### Double:
Double = float  #283 (line in Coconut source)

#### Rational:
Rational = _fractions.Fraction  #286 (line in Coconut source)

@_coconut_tco  #288 (line in Coconut source)
def over(x, y):  #288 (line in Coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #293 (line in Coconut source)
    return _coconut_tail_call(_coconut_call_or_coefficient, Rational, x, y)  #294 (line in Coconut source)

_coconut_op_U25_U25 = over  #295 (line in Coconut source)

#### Word:
Word = Int  #298 (line in Coconut source)


### Numeric type classes:

#### Num:
Num = '_coconut.typing.Union[int, float, Rational]'  # type: _coconut.typing.TypeAlias  #304 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #304 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #304 (line in Coconut source)
__annotations__["Num"] = '_coconut.typing.TypeAlias'  #304 (line in Coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #305 (line in Coconut source)

negate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #307 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #307 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #307 (line in Coconut source)
__annotations__["negate"] = '_coconut.typing.Callable[[TNum], TNum]'  #307 (line in Coconut source)
negate = (_coconut_minus)  #308 (line in Coconut source)

abs = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #310 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #310 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #310 (line in Coconut source)
__annotations__["abs"] = '_coconut.typing.Callable[[TNum], TNum]'  #310 (line in Coconut source)
abs = _abs  #311 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #313 (line in Coconut source)
    @_coconut_mark_as_match  #313 (line in Coconut source)
    def signum(x: 'Num') -> 'int':  #313 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #313 (line in Coconut source)
else:  #313 (line in Coconut source)
    @_coconut_mark_as_match  #313 (line in Coconut source)
    def signum(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #313 (line in Coconut source)

        _coconut_match_check_3 = False  #313 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #313 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #313 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #313 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #313 (line in Coconut source)
        if not _coconut_match_check_3:  #313 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #313 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 1:  #313 (line in Coconut source)
                if _coconut_match_args[0] == 0:  #313 (line in Coconut source)
                    if not _coconut_match_kwargs:  #313 (line in Coconut source)
                        _coconut_match_check_3 = True  #313 (line in Coconut source)

            if _coconut_match_check_3:  #313 (line in Coconut source)

                    return (0)  #315 (line in Coconut source)

        if not _coconut_match_check_3:  #316 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #316 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #316 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #316 (line in Coconut source)
                _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #316 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_25  #316 (line in Coconut source)
                if not _coconut_match_kwargs:  #316 (line in Coconut source)
                    _coconut_match_check_3 = True  #316 (line in Coconut source)
            if _coconut_match_check_3:  #316 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #316 (line in Coconut source)
                    x = _coconut_match_set_name_x  #316 (line in Coconut source)
            if _coconut_match_check_3 and not (x > 0):  #316 (line in Coconut source)
                _coconut_match_check_3 = False  #316 (line in Coconut source)

            if _coconut_match_check_3:  #316 (line in Coconut source)

                    return (1)  #316 (line in Coconut source)

        if not _coconut_match_check_3:  #317 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #317 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #317 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #317 (line in Coconut source)
                _coconut_match_temp_26 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #317 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_26  #317 (line in Coconut source)
                if not _coconut_match_kwargs:  #317 (line in Coconut source)
                    _coconut_match_check_3 = True  #317 (line in Coconut source)
            if _coconut_match_check_3:  #317 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #317 (line in Coconut source)
                    x = _coconut_match_set_name_x  #317 (line in Coconut source)
            if _coconut_match_check_3 and not (x < 0):  #317 (line in Coconut source)
                _coconut_match_check_3 = False  #317 (line in Coconut source)

            if _coconut_match_check_3:  #317 (line in Coconut source)

                    return (-1)  #317 (line in Coconut source)


        if not _coconut_match_check_3:  #319 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def signum:', _coconut_match_args)  #319 (line in Coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #319 (line in Coconut source)
    return (x)  #319 (line in Coconut source)

#### Real:

Real = Num  #322 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #324 (line in Coconut source)
    @_coconut_tco  #324 (line in Coconut source)
    @_coconut_mark_as_match  #324 (line in Coconut source)
    def toRational(real: 'Real') -> 'Rational':  #324 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #324 (line in Coconut source)
else:  #324 (line in Coconut source)
    @_coconut_tco  #324 (line in Coconut source)
    @_coconut_mark_as_match  #324 (line in Coconut source)
    def toRational(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #324 (line in Coconut source)

        _coconut_match_check_4 = False  #324 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #324 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #324 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #324 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #324 (line in Coconut source)
        if not _coconut_match_check_4:  #324 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #324 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_sentinel  #324 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #324 (line in Coconut source)
                _coconut_match_temp_27 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #324 (line in Coconut source)
                if (isinstance)(_coconut_match_temp_27, float):  #324 (line in Coconut source)
                    _coconut_match_set_name_real = _coconut_match_temp_27  #324 (line in Coconut source)
                    if not _coconut_match_kwargs:  #324 (line in Coconut source)
                        _coconut_match_check_4 = True  #324 (line in Coconut source)
            if _coconut_match_check_4:  #324 (line in Coconut source)
                if _coconut_match_set_name_real is not _coconut_sentinel:  #324 (line in Coconut source)
                    real = _coconut_match_set_name_real  #324 (line in Coconut source)

            if _coconut_match_check_4:  #324 (line in Coconut source)

                    return _coconut_tail_call(Rational.from_float, real)  #327 (line in Coconut source)

        if not _coconut_match_check_4:  #328 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #328 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_sentinel  #328 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #328 (line in Coconut source)
                _coconut_match_temp_28 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #328 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_28  #328 (line in Coconut source)
                if not _coconut_match_kwargs:  #328 (line in Coconut source)
                    _coconut_match_check_4 = True  #328 (line in Coconut source)
            if _coconut_match_check_4:  #328 (line in Coconut source)
                if _coconut_match_set_name_real is not _coconut_sentinel:  #328 (line in Coconut source)
                    real = _coconut_match_set_name_real  #328 (line in Coconut source)

            if _coconut_match_check_4:  #328 (line in Coconut source)

                    return _coconut_tail_call(Rational, real)  #329 (line in Coconut source)

#### Integral:

        if not _coconut_match_check_4:  #332 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def toRational:', _coconut_match_args)  #332 (line in Coconut source)


Integral = int  #332 (line in Coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #334 (line in Coconut source)
    divxy = x // y  #335 (line in Coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #336 (line in Coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #338 (line in Coconut source)
    modxy = x % y  #339 (line in Coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #340 (line in Coconut source)


div = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #342 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #342 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #342 (line in Coconut source)
__annotations__["div"] = '_coconut.typing.Callable[[int, int], int]'  #342 (line in Coconut source)
div = (_coconut.operator.floordiv)  #343 (line in Coconut source)

mod = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #345 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #345 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #345 (line in Coconut source)
__annotations__["mod"] = '_coconut.typing.Callable[[int, int], int]'  #345 (line in Coconut source)
mod = (_coconut.operator.mod)  #346 (line in Coconut source)

def quotRem(x: 'int', y: 'int') -> '(_coconut.typing.Tuple[int, int])':  #348 (line in Coconut source)
    divxy, modxy = divmod(x, y)  #349 (line in Coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #350 (line in Coconut source)
    return (divxy + adj, modxy - y * adj)  #351 (line in Coconut source)


divMod = divmod  #353 (line in Coconut source)

toInteger = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Integer]  #355 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #355 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #355 (line in Coconut source)
__annotations__["toInteger"] = '_coconut.typing.Callable[[Integral], Integer]'  #355 (line in Coconut source)
toInteger = _int  #356 (line in Coconut source)

#### Fractional:
Fractional = Rational  #359 (line in Coconut source)

recip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Fractional], Fractional]  #361 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #361 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #361 (line in Coconut source)
__annotations__["recip"] = '_coconut.typing.Callable[[Fractional], Fractional]'  #361 (line in Coconut source)
recip = (_coconut_partial(_coconut.operator.truediv, 1))  #362 (line in Coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #364 (line in Coconut source)
    return (x)  #364 (line in Coconut source)

#### Floating:

Floating = float  #367 (line in Coconut source)

from math import pi  # NOQA  #369 (line in Coconut source)
from math import exp  # NOQA  #369 (line in Coconut source)
from math import log  # NOQA  #369 (line in Coconut source)
from math import sqrt  # NOQA  #369 (line in Coconut source)
from math import sin  # NOQA  #369 (line in Coconut source)
from math import cos  # NOQA  #369 (line in Coconut source)
from math import tan  # NOQA  #369 (line in Coconut source)
from math import asin  # NOQA  #369 (line in Coconut source)
from math import acos  # NOQA  #369 (line in Coconut source)
from math import atan  # NOQA  #369 (line in Coconut source)
from math import sinh  # NOQA  #369 (line in Coconut source)
from math import cosh  # NOQA  #369 (line in Coconut source)
from math import tanh  # NOQA  #369 (line in Coconut source)
from math import asinh  # NOQA  #369 (line in Coconut source)
from math import acosh  # NOQA  #369 (line in Coconut source)
from math import atanh  # NOQA  #369 (line in Coconut source)

@_coconut_tco  #388 (line in Coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #388 (line in Coconut source)
    return _coconut_tail_call(log, x, base)  #389 (line in Coconut source)

#### RealFrac:

RealFrac = Rational  #392 (line in Coconut source)

def properFraction(x: 'RealFrac') -> '(_coconut.typing.Tuple[int, RealFrac])':  #394 (line in Coconut source)
    floor_x = floor(x)  #395 (line in Coconut source)
    return (floor_x, x - floor_x)  #396 (line in Coconut source)


truncate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #398 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #398 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #398 (line in Coconut source)
__annotations__["truncate"] = '_coconut.typing.Callable[[RealFrac], int]'  #398 (line in Coconut source)
truncate = _int  #399 (line in Coconut source)

round = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #401 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #401 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #401 (line in Coconut source)
__annotations__["round"] = '_coconut.typing.Callable[[RealFrac], int]'  #401 (line in Coconut source)
round = _round  #402 (line in Coconut source)

ceiling = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #404 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #404 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #404 (line in Coconut source)
__annotations__["ceiling"] = '_coconut.typing.Callable[[RealFrac], int]'  #404 (line in Coconut source)
ceiling = _ceil  #405 (line in Coconut source)

floor = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #407 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #407 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #407 (line in Coconut source)
__annotations__["floor"] = '_coconut.typing.Callable[[RealFrac], int]'  #407 (line in Coconut source)
floor = _floor  #408 (line in Coconut source)

#### RealFloat:
RealFloat = float  #411 (line in Coconut source)

def floatRadix(x: 'float') -> 'int':  #413 (line in Coconut source)
    return (2)  #413 (line in Coconut source)


def floatDigits(x: 'float') -> 'int':  #415 (line in Coconut source)
    return (53)  #415 (line in Coconut source)


def floatRange(x: 'float') -> '(_coconut.typing.Tuple[int, int])':  #417 (line in Coconut source)
    return ((-1021, 1024))  #417 (line in Coconut source)


decodeFloat = NotImplemented  #419 (line in Coconut source)

encodeFloat = NotImplemented  #421 (line in Coconut source)

exponent = NotImplemented  #423 (line in Coconut source)

significand = NotImplemented  #425 (line in Coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #427 (line in Coconut source)
    return (x * 2**power)  #428 (line in Coconut source)

# NOQA
from math import isnan as isNaN  # NOQA  #430 (line in Coconut source)
from math import isinf as isInfinite  # NOQA  #430 (line in Coconut source)
from math import atan2  # NOQA  #430 (line in Coconut source)

isDenormalized = NotImplemented  #436 (line in Coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #438 (line in Coconut source)
    return (x == 0 and str(x).startswith("-"))  #439 (line in Coconut source)


def isIEEE(x: 'float') -> 'bool':  #441 (line in Coconut source)
    return (True)  #441 (line in Coconut source)


### Numeric functions:

def subtract(x, y):  #445 (line in Coconut source)
    return (y - x)  #446 (line in Coconut source)


def even(x: 'int') -> 'bool':  #448 (line in Coconut source)
    return (x % 2 == 0)  #449 (line in Coconut source)


def odd(x: 'int') -> 'bool':  #451 (line in Coconut source)
    return (x % 2 == 1)  #452 (line in Coconut source)


gcd = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #454 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #454 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #454 (line in Coconut source)
__annotations__["gcd"] = '_coconut.typing.Callable[[int, int], int]'  #454 (line in Coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #455 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #457 (line in Coconut source)
    @_coconut_mark_as_match  #457 (line in Coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #457 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #457 (line in Coconut source)
else:  #457 (line in Coconut source)
    @_coconut_mark_as_match  #457 (line in Coconut source)
    def lcm(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #457 (line in Coconut source)

        _coconut_match_check_5 = False  #457 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #457 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #457 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #457 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #457 (line in Coconut source)
        if not _coconut_match_check_5:  #457 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #457 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #457 (line in Coconut source)
                if _coconut_match_args[1] == 0:  #457 (line in Coconut source)
                    if not _coconut_match_kwargs:  #457 (line in Coconut source)
                        _coconut_match_check_5 = True  #457 (line in Coconut source)

            if _coconut_match_check_5:  #457 (line in Coconut source)

                    return (0)  #459 (line in Coconut source)

        if not _coconut_match_check_5:  #460 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #460 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #460 (line in Coconut source)
                if _coconut_match_args[0] == 0:  #460 (line in Coconut source)
                    if not _coconut_match_kwargs:  #460 (line in Coconut source)
                        _coconut_match_check_5 = True  #460 (line in Coconut source)

            if _coconut_match_check_5:  #460 (line in Coconut source)

                    return (0)  #460 (line in Coconut source)

        if not _coconut_match_check_5:  #461 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #461 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #461 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_sentinel  #461 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #461 (line in Coconut source)
                _coconut_match_temp_29 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #461 (line in Coconut source)
                _coconut_match_temp_30 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #461 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_29  #461 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_30  #461 (line in Coconut source)
                if not _coconut_match_kwargs:  #461 (line in Coconut source)
                    _coconut_match_check_5 = True  #461 (line in Coconut source)
            if _coconut_match_check_5:  #461 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #461 (line in Coconut source)
                    x = _coconut_match_set_name_x  #461 (line in Coconut source)
                if _coconut_match_set_name_y is not _coconut_sentinel:  #461 (line in Coconut source)
                    y = _coconut_match_set_name_y  #461 (line in Coconut source)

            if _coconut_match_check_5:  #461 (line in Coconut source)

                    return (abs(y) * (abs(x) // gcd(x, y)))  #462 (line in Coconut source)


        if not _coconut_match_check_5:  #464 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def lcm:', _coconut_match_args)  #464 (line in Coconut source)


fromIntegral = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Num]  #464 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #464 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #464 (line in Coconut source)
__annotations__["fromIntegral"] = '_coconut.typing.Callable[[Integral], Num]'  #464 (line in Coconut source)
fromIntegral = fromInteger  #465 (line in Coconut source)

realToFrac = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Real], Fractional]  #467 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #467 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #467 (line in Coconut source)
__annotations__["realToFrac"] = '_coconut.typing.Callable[[Real], Fractional]'  #467 (line in Coconut source)
realToFrac = toRational  #468 (line in Coconut source)



## Monoids:
Monoid = T.Iterable  #473 (line in Coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #474 (line in Coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #476 (line in Coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #479 (line in Coconut source)
    __slots__ = ()  #480 (line in Coconut source)
    _coconut_is_data = True  #480 (line in Coconut source)
    __match_args__ = ()  #480 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #480 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #480 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #480 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #480 (line in Coconut source)
    def __eq__(self, other):  #480 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #480 (line in Coconut source)
    def __hash__(self):  #480 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #480 (line in Coconut source)
    @staticmethod  #480 (line in Coconut source)
    @_coconut_tco  #481 (line in Coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #481 (line in Coconut source)
        if (hasattr)(M, "__mempty__"):  #482 (line in Coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #483 (line in Coconut source)
        return _coconut_tail_call(makedata, type(M))  #484 (line in Coconut source)


_coconut_call_set_names(Mempty)  #486 (line in Coconut source)
mempty = Mempty()  # type: T.Any  #486 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #486 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #486 (line in Coconut source)
__annotations__["mempty"] = 'T.Any'  #486 (line in Coconut source)

@_coconut_tco  #488 (line in Coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #488 (line in Coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #493 (line in Coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #495 (line in Coconut source)
    y = (asTypeOf)(y, x)  #496 (line in Coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #499 (line in Coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #500 (line in Coconut source)

# Default implementation
    if not x:  #503 (line in Coconut source)
        return (y)  #504 (line in Coconut source)
    if not y:  #505 (line in Coconut source)
        return (x)  #506 (line in Coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #507 (line in Coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #508 (line in Coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #509 (line in Coconut source)


@_coconut_tco  #511 (line in Coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #511 (line in Coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #512 (line in Coconut source)



## Monads and functors:

#### Functor:

class _HasFMap(T.Protocol, T.Generic[Tco]):  #519 (line in Coconut source)
    _coconut_typevar_B_0 = _coconut.typing.TypeVar("_coconut_typevar_B_0")  #520 (line in Coconut source)

    def __fmap__(self: 'Functor[Tco]', func: '_coconut.typing.Callable[[Tco], _coconut_typevar_B_0]') -> 'Functor[_coconut_typevar_B_0]':  #520 (line in Coconut source)
        return (bot)  #520 (line in Coconut source)


_coconut_call_set_names(_HasFMap)  #522 (line in Coconut source)
_coconut_typevar_A_0 = _coconut.typing.TypeVar("_coconut_typevar_A_0")  #522 (line in Coconut source)
Functor = '_coconut.typing.Union[Applicative[_coconut_typevar_A_0], _HasFMap[_coconut_typevar_A_0]]'  # type: _coconut.typing.TypeAlias  #522 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #522 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #522 (line in Coconut source)
__annotations__["Functor"] = '_coconut.typing.TypeAlias'  #522 (line in Coconut source)
TFunctor = T.TypeVar("TFunctor", bound=Functor)  #523 (line in Coconut source)

@_coconut_tco  # type: ignore  #525 (line in Coconut source)
def fmap(f: '_coconut.typing.Callable[[Ta], Tb]', xs: 'Functor[Ta]') -> 'Functor[Tb]':  # type: ignore  #525 (line in Coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #528 (line in Coconut source)
    try:  #529 (line in Coconut source)
# Default implementation
        return (_fmap(f, xs))  #531 (line in Coconut source)

    except TypeError:  #533 (line in Coconut source)
# Function instance
        if callable(xs):  #535 (line in Coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #536 (line in Coconut source)

        raise  #538 (line in Coconut source)


@_coconut_tco  #540 (line in Coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #540 (line in Coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #544 (line in Coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #545 (line in Coconut source)

_coconut_op_U3c_U24 = fmapConst  #546 (line in Coconut source)

#### Applicative:
class _DefinesApp(T.Protocol, T.Generic[Tco]):  #549 (line in Coconut source)
    _coconut_typevar_B_1 = _coconut.typing.TypeVar("_coconut_typevar_B_1")  #550 (line in Coconut source)

    def __fmap__(self: 'Functor[Tco]', func: '_coconut.typing.Callable[[Tco], _coconut_typevar_B_1]') -> 'Functor[_coconut_typevar_B_1]':  #550 (line in Coconut source)
        return (bot)  #550 (line in Coconut source)

    def __pure__(self: 'Functor[Tco]') -> 'Tco':  #551 (line in Coconut source)
        return (bot)  #551 (line in Coconut source)


_coconut_call_set_names(_DefinesApp)  #553 (line in Coconut source)
_coconut_typevar_A_1 = _coconut.typing.TypeVar("_coconut_typevar_A_1")  #553 (line in Coconut source)
Applicative = '_coconut.typing.Union[Monad[_coconut_typevar_A_1], T.Iterable[_coconut_typevar_A_1], _DefinesApp[_coconut_typevar_A_1]]'  # type: _coconut.typing.TypeAlias  #553 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #553 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #553 (line in Coconut source)
__annotations__["Applicative"] = '_coconut.typing.TypeAlias'  #553 (line in Coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #554 (line in Coconut source)

if TYPE_CHECKING:  #556 (line in Coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #557 (line in Coconut source)
        ...  #558 (line in Coconut source)

else:  #559 (line in Coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #560 (line in Coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #564 (line in Coconut source)

        __slots__ = ()  #566 (line in Coconut source)
        _coconut_is_data = True  #566 (line in Coconut source)
        __match_args__ = ('val',)  #566 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #566 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #566 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #566 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #566 (line in Coconut source)
        def __eq__(self, other):  #566 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #566 (line in Coconut source)
        def __hash__(self):  #566 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #566 (line in Coconut source)
        def __join__(self) -> 'T.Any':  #566 (line in Coconut source)
            return (self.val)  #566 (line in Coconut source)


        def __call__(self, arg: 'T.Any') -> 'T.Any':  #568 (line in Coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #569 (line in Coconut source)
            return (self.val)  #570 (line in Coconut source)


        @_coconut_tco  #572 (line in Coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #572 (line in Coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #574 (line in Coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #575 (line in Coconut source)

            try:  #577 (line in Coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #579 (line in Coconut source)

            except TypeError:  #581 (line in Coconut source)
# Check for functions
                if callable(M):  #583 (line in Coconut source)
                    return _coconut_tail_call(const, self.val)  # type: ignore  #584 (line in Coconut source)

# Fallback
                raise  #587 (line in Coconut source)


    _coconut_call_set_names(pure)  #589 (line in Coconut source)
@_coconut_tco  #589 (line in Coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #589 (line in Coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #596 (line in Coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #598 (line in Coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #599 (line in Coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #602 (line in Coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #603 (line in Coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  # type: ignore  #606 (line in Coconut source)

_coconut_op_U3c_U2a_U3e = ap  #607 (line in Coconut source)

@_coconut_tco  #609 (line in Coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #609 (line in Coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #613 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #614 (line in Coconut source)

_coconut_op_U2a_U3e = seqAr  #615 (line in Coconut source)

@_coconut_tco  #617 (line in Coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #617 (line in Coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #621 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #622 (line in Coconut source)

_coconut_op_U3c_U2a = seqAl  #623 (line in Coconut source)

def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #625 (line in Coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #629 (line in Coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut_partial(_coconut_partial, func), f1), f2))  # type: ignore  #630 (line in Coconut source)

#### Monad:

class _DefinesMonad(T.Protocol, T.Generic[Tco]):  #633 (line in Coconut source)
    _coconut_typevar_B_2 = _coconut.typing.TypeVar("_coconut_typevar_B_2")  #634 (line in Coconut source)

    def __fmap__(self: 'Functor[Tco]', func: '_coconut.typing.Callable[[Tco], _coconut_typevar_B_2]') -> 'Functor[_coconut_typevar_B_2]':  #634 (line in Coconut source)
        return (bot)  #634 (line in Coconut source)

    def __pure__(self: 'Functor[Tco]') -> 'Tco':  #635 (line in Coconut source)
        return (bot)  #635 (line in Coconut source)

    def __join__(self: 'Functor') -> 'Functor[Tco]':  #636 (line in Coconut source)
        return (bot)  #636 (line in Coconut source)


_coconut_call_set_names(_DefinesMonad)  #638 (line in Coconut source)
class _DefaultMonad(T.Protocol, T.Generic[Tco]):  #638 (line in Coconut source)
    def __iter__(self) -> 'T.Iterator[Tco]':  #639 (line in Coconut source)
        return (bot)  #639 (line in Coconut source)

    def __bool__(self) -> 'bool':  #640 (line in Coconut source)
        return (bot)  #640 (line in Coconut source)


_coconut_call_set_names(_DefaultMonad)  #642 (line in Coconut source)
_coconut_typevar_A_2 = _coconut.typing.TypeVar("_coconut_typevar_A_2")  #642 (line in Coconut source)
Monad = '_coconut.typing.Union[_DefaultMonad[_coconut_typevar_A_2], (_coconut.typing.Callable[..., _coconut_typevar_A_2]), _DefinesMonad[_coconut_typevar_A_2]]'  # type: _coconut.typing.TypeAlias  #642 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #642 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #642 (line in Coconut source)
__annotations__["Monad"] = '_coconut.typing.TypeAlias'  #642 (line in Coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #643 (line in Coconut source)

@_coconut_tco  #645 (line in Coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #645 (line in Coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #650 (line in Coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #651 (line in Coconut source)

_coconut_op_U3e_U3e_U3e_U3d = bind  #652 (line in Coconut source)

@_coconut_tco  #654 (line in Coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #654 (line in Coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #658 (line in Coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #659 (line in Coconut source)

_coconut_op_U3e_U3e_U3e = seqM  #660 (line in Coconut source)

return_ = pure  #662 (line in Coconut source)

if TYPE_CHECKING:  #664 (line in Coconut source)
    def fail(msg: 'str') -> 'T.Any':  #665 (line in Coconut source)
        ...  #666 (line in Coconut source)

else:  #667 (line in Coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #668 (line in Coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #671 (line in Coconut source)

        __slots__ = ()  #673 (line in Coconut source)
        _coconut_is_data = True  #673 (line in Coconut source)
        __match_args__ = ('msg',)  #673 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #673 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #673 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #673 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #673 (line in Coconut source)
        def __eq__(self, other):  #673 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #673 (line in Coconut source)
        def __hash__(self):  #673 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #673 (line in Coconut source)
        @staticmethod  #673 (line in Coconut source)
        def __bool__() -> 'bool':  #674 (line in Coconut source)
            return (False)  #674 (line in Coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #676 (line in Coconut source)
            return (self)  #676 (line in Coconut source)


        @_coconut_tco  #678 (line in Coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #678 (line in Coconut source)
            if (hasattr)(M, "__fail__"):  #679 (line in Coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #680 (line in Coconut source)
            return _coconut_tail_call(makedata, type(M))  #681 (line in Coconut source)

# sequence_ and mapM_ defined in Foldable


    _coconut_call_set_names(fail)  #685 (line in Coconut source)
@_coconut_tco  #685 (line in Coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #685 (line in Coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #689 (line in Coconut source)
    return _coconut_tail_call((bind), m, func)  #690 (line in Coconut source)

_coconut_op_U3d_U3c_U3c_U3c = bindFrom  #691 (line in Coconut source)

@_coconut_tco  #693 (line in Coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #693 (line in Coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #700 (line in Coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #702 (line in Coconut source)
    _coconut_match_check_6 = False  #702 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #702 (line in Coconut source)
        _coconut_match_check_6 = True  #702 (line in Coconut source)
    if _coconut_match_check_6:  #702 (line in Coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  # type: ignore  #703 (line in Coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #706 (line in Coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #709 (line in Coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #710 (line in Coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  # type: ignore  #713 (line in Coconut source)
    _coconut_case_match_check_0 = False  # type: ignore  #713 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  # type: ignore  #713 (line in Coconut source)
        _coconut_case_match_check_0 = True  # type: ignore  #713 (line in Coconut source)
    if _coconut_case_match_check_0:  # type: ignore  #713 (line in Coconut source)
        if not ms:  #717 (line in Coconut source)
            return (ms)  # type: ignore  #718 (line in Coconut source)
        vals = []  # type: ignore  #719 (line in Coconut source)
        fallback = ms  #720 (line in Coconut source)
        for m in (ms):  # type: ignore  #721 (line in Coconut source)
            if m:  #722 (line in Coconut source)
                vals.extend(m)  # type: ignore  #723 (line in Coconut source)
            else:  #724 (line in Coconut source)
                fallback = m  # type: ignore  #725 (line in Coconut source)
        if not vals:  #726 (line in Coconut source)
            return (fallback)  # type: ignore  #727 (line in Coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  # type: ignore  #728 (line in Coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #731 (line in Coconut source)
        _coconut_case_match_check_0 = True  #731 (line in Coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #731 (line in Coconut source)
            _coconut_case_match_check_0 = False  #731 (line in Coconut source)
        if _coconut_case_match_check_0:  #731 (line in Coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #732 (line in Coconut source)

    if not _coconut_case_match_check_0:  #734 (line in Coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #735 (line in Coconut source)


if _coconut.typing.TYPE_CHECKING:  #737 (line in Coconut source)
    @_coconut_tco  #737 (line in Coconut source)
    @_coconut_mark_as_match  #737 (line in Coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]',) -> 'TMonad':  #737 (line in Coconut source)
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
    """  #756 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #757 (line in Coconut source)
else:  #757 (line in Coconut source)
    @_coconut_tco  #757 (line in Coconut source)
    @_coconut_mark_as_match  #757 (line in Coconut source)
    def do(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #757 (line in Coconut source)
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
    """  #756 (line in Coconut source)

        _coconut_match_check_7 = False  #757 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #757 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #757 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #757 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #757 (line in Coconut source)
        if not _coconut_match_check_7:  #757 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #757 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #757 (line in Coconut source)
            if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #757 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #757 (line in Coconut source)
                    _coconut_match_temp_31 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #757 (line in Coconut source)
                    _coconut_match_set_name_func = _coconut_match_temp_31  #757 (line in Coconut source)
                    if not _coconut_match_kwargs:  #757 (line in Coconut source)
                        _coconut_match_check_7 = True  #757 (line in Coconut source)
            if _coconut_match_check_7:  #757 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #757 (line in Coconut source)
                    func = _coconut_match_set_name_func  #757 (line in Coconut source)

            if _coconut_match_check_7:  #757 (line in Coconut source)

                    return _coconut_tail_call(func)  #761 (line in Coconut source)

        if not _coconut_match_check_7:  #762 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #762 (line in Coconut source)
            _coconut_match_set_name_m = _coconut_sentinel  #762 (line in Coconut source)
            _coconut_match_set_name_ms = _coconut_sentinel  #762 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #762 (line in Coconut source)
            if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #762 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #762 (line in Coconut source)
                    _coconut_match_set_name_m = _coconut_match_args[0][0]  #762 (line in Coconut source)
                    _coconut_match_temp_33 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #762 (line in Coconut source)
                    _coconut_match_temp_32 = _coconut.list(_coconut_match_args[0][1:])  #762 (line in Coconut source)
                    _coconut_match_set_name_func = _coconut_match_temp_33  #762 (line in Coconut source)
                    _coconut_match_set_name_ms = _coconut_match_temp_32  #762 (line in Coconut source)
                    if not _coconut_match_kwargs:  #762 (line in Coconut source)
                        _coconut_match_check_7 = True  #762 (line in Coconut source)
            if _coconut_match_check_7:  #762 (line in Coconut source)
                if _coconut_match_set_name_m is not _coconut_sentinel:  #762 (line in Coconut source)
                    m = _coconut_match_set_name_m  #762 (line in Coconut source)
                if _coconut_match_set_name_ms is not _coconut_sentinel:  #762 (line in Coconut source)
                    ms = _coconut_match_set_name_ms  #762 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #762 (line in Coconut source)
                    func = _coconut_match_set_name_func  #762 (line in Coconut source)

            if _coconut_match_check_7:  #762 (line in Coconut source)

                    return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut_partial(func, x)))  #763 (line in Coconut source)



## Folds and traversals:

#### Foldable:

        if not _coconut_match_check_7:  #770 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def do:', _coconut_match_args)  #770 (line in Coconut source)


Foldable = T.Sequence  #770 (line in Coconut source)

@_coconut_tco  #772 (line in Coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #772 (line in Coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #773 (line in Coconut source)


mapM_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]  #775 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #775 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #775 (line in Coconut source)
__annotations__["mapM_"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #775 (line in Coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #776 (line in Coconut source)

@_coconut_tco  #778 (line in Coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #778 (line in Coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #779 (line in Coconut source)


@_coconut_tco  #781 (line in Coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #781 (line in Coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #782 (line in Coconut source)


@_coconut_tco  #784 (line in Coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #784 (line in Coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #785 (line in Coconut source)


foldl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]  #787 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #787 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #787 (line in Coconut source)
__annotations__["foldl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #787 (line in Coconut source)
foldl1 = reduce  #788 (line in Coconut source)

@_coconut_tco  #790 (line in Coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #790 (line in Coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #791 (line in Coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #793 (line in Coconut source)
    return (len(xs) == 0)  #794 (line in Coconut source)


length = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable], int]  #796 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #796 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #796 (line in Coconut source)
__annotations__["length"] = '_coconut.typing.Callable[[Foldable], int]'  #796 (line in Coconut source)
length = len  #797 (line in Coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #799 (line in Coconut source)
    return (e in xs)  #800 (line in Coconut source)


maximum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #802 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #802 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #802 (line in Coconut source)
__annotations__["maximum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #802 (line in Coconut source)
maximum = _max  #803 (line in Coconut source)

minimum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #805 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #805 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #805 (line in Coconut source)
__annotations__["minimum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #805 (line in Coconut source)
minimum = _min  #806 (line in Coconut source)

sum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #808 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #808 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #808 (line in Coconut source)
__annotations__["sum"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #808 (line in Coconut source)
sum = _sum  #809 (line in Coconut source)

product = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #811 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #811 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #811 (line in Coconut source)
__annotations__["product"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #811 (line in Coconut source)
product = _coconut_partial(reduce, _coconut.operator.mul)  #812 (line in Coconut source)

#### Traversable:
Traversable = T.Iterable  #815 (line in Coconut source)

@_coconut_tco  #817 (line in Coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #817 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #818 (line in Coconut source)


@_coconut_tco  #820 (line in Coconut source)
def sequence(fs: 'Traversable[Monad[Ta]]') -> 'Monad[Traversable[Ta]]':  #820 (line in Coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #821 (line in Coconut source)


sequenceA = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Traversable[Applicative[Ta]]], Applicative[Traversable[Ta]]]  #823 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #823 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #823 (line in Coconut source)
__annotations__["sequenceA"] = '_coconut.typing.Callable[[Traversable[Applicative[Ta]]], Applicative[Traversable[Ta]]]'  #823 (line in Coconut source)
sequenceA = sequence  # type: ignore  #824 (line in Coconut source)

mapM = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]  #826 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #826 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #826 (line in Coconut source)
__annotations__["mapM"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #826 (line in Coconut source)
mapM = _coconut_forward_compose(fmap, sequence)  # type: ignore  #827 (line in Coconut source)

traverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]  #829 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #829 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #829 (line in Coconut source)
__annotations__["traverse"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #829 (line in Coconut source)
traverse = mapM  # type: ignore  #830 (line in Coconut source)



## Miscellaneous functions:
id = ident  # type: _coconut.typing.Callable[[Ta], Ta]  #835 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #835 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #835 (line in Coconut source)
__annotations__["id"] = '_coconut.typing.Callable[[Ta], Ta]'  #835 (line in Coconut source)

@_coconut_tco  #837 (line in Coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #837 (line in Coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #841 (line in Coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #842 (line in Coconut source)


if _coconut.typing.TYPE_CHECKING:  #844 (line in Coconut source)
    @_coconut.typing.overload  #844 (line in Coconut source)
    @_coconut_tco  #844 (line in Coconut source)
    @_coconut_mark_as_match  #844 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta',) -> 'Tb':  #844 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #851 (line in Coconut source)
    @_coconut.typing.overload  #851 (line in Coconut source)
    @_coconut_tco  #851 (line in Coconut source)
    @_coconut_mark_as_match  #851 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta',) -> '_coconut.typing.Callable[[Tb], Tc]':  #851 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #851 (line in Coconut source)
    @_coconut.typing.overload  #851 (line in Coconut source)
    @_coconut_tco  #851 (line in Coconut source)
    @_coconut_mark_as_match  #851 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta',) -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #851 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #851 (line in Coconut source)
    @_coconut.typing.overload  #851 (line in Coconut source)
    @_coconut_tco  #851 (line in Coconut source)
    @_coconut_mark_as_match  #851 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta',) -> 'T.Any':  #851 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #851 (line in Coconut source)
    @_coconut_tco  #851 (line in Coconut source)
    @_coconut_mark_as_match  #851 (line in Coconut source)
    def apply(*_coconut_args, **_coconut_kwargs):  #851 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #851 (line in Coconut source)
else:  #851 (line in Coconut source)
    @_coconut_tco  #851 (line in Coconut source)
    @_coconut_mark_as_match  #851 (line in Coconut source)
    def apply(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #851 (line in Coconut source)
        """
    apply :: (a -> b) -> a -> b
    apply = ($)
    -- apply will automatically curry functions as in Haskell function
    --  application (see also `of` for the more general version)
    """  #850 (line in Coconut source)

        _coconut_match_check_8 = False  #851 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #851 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #851 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #851 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #851 (line in Coconut source)
        if not _coconut_match_check_8:  #851 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #851 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #851 (line in Coconut source)
            _coconut_match_set_name_arg = _coconut_sentinel  #851 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "func" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "arg" in _coconut_match_kwargs)) == 1):  #851 (line in Coconut source)
                _coconut_match_temp_34 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("func")  #851 (line in Coconut source)
                _coconut_match_temp_35 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("arg")  #851 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_34  #851 (line in Coconut source)
                _coconut_match_set_name_arg = _coconut_match_temp_35  #851 (line in Coconut source)
                if not _coconut_match_kwargs:  #851 (line in Coconut source)
                    _coconut_match_check_8 = True  #851 (line in Coconut source)
            if _coconut_match_check_8:  #851 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #851 (line in Coconut source)
                    func = _coconut_match_set_name_func  #851 (line in Coconut source)
                if _coconut_match_set_name_arg is not _coconut_sentinel:  #851 (line in Coconut source)
                    arg = _coconut_match_set_name_arg  #851 (line in Coconut source)

            if _coconut_match_check_8:  #851 (line in Coconut source)

                    return _coconut_tail_call((of), func, arg)  #868 (line in Coconut source)

        if not _coconut_match_check_8:  #869 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def apply:', _coconut_match_args)  #869 (line in Coconut source)


_coconut_op_U24_U24 = apply  #869 (line in Coconut source)

@_coconut_tco  #871 (line in Coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #871 (line in Coconut source)
    while True:  #872 (line in Coconut source)
        if cond(x):  #872 (line in Coconut source)
            return (x)  #873 (line in Coconut source)
        try:  # tail recursive  #874 (line in Coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_57  # type: ignore  # tail recursive  #874 (line in Coconut source)
        except _coconut.NameError:  # tail recursive  #874 (line in Coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #874 (line in Coconut source)
        if _coconut_tre_check_0:  # tail recursive  #874 (line in Coconut source)
            (cond, func, x,) = (cond, func, func(x),)  # tail recursive  #874 (line in Coconut source)
            continue  # tail recursive  #874 (line in Coconut source)
        else:  # tail recursive  #874 (line in Coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #875 (line in Coconut source)
        return None  #876 (line in Coconut source)

_coconut_recursive_func_57 = until  #876 (line in Coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #876 (line in Coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #880 (line in Coconut source)
    if TYPE_CHECKING:  #881 (line in Coconut source)
        return (x)  #881 (line in Coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #883 (line in Coconut source)
        for i in ((takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count())):  #884 (line in Coconut source)
            if (isinstance)(x, pure):  #885 (line in Coconut source)
                x = x.pure_as(y)  #886 (line in Coconut source)
            elif (isinstance)(x, fail):  #887 (line in Coconut source)
                x = x.fail_as(y)  #888 (line in Coconut source)
            elif (isinstance)(x, Mempty):  #889 (line in Coconut source)
                x = x.mempty_as(y)  #890 (line in Coconut source)
            else:  #891 (line in Coconut source)
                break  #892 (line in Coconut source)
    return (x)  #893 (line in Coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #895 (line in Coconut source)

def error(msg: 'str') -> 'None':  #897 (line in Coconut source)
    raise Exception(msg)  #898 (line in Coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #900 (line in Coconut source)
    raise Exception(msg) from None  #901 (line in Coconut source)


undefined = None  # type: T.Any  #903 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #903 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #903 (line in Coconut source)
__annotations__["undefined"] = 'T.Any'  #903 (line in Coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #905 (line in Coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #908 (line in Coconut source)
    return (y)  #909 (line in Coconut source)


@_coconut_tco  #911 (line in Coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #911 (line in Coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #916 (line in Coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #917 (line in Coconut source)




# List operations:

@_coconut_tco  #923 (line in Coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #923 (line in Coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #927 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #928 (line in Coconut source)

# type: ignore
map = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]  # type: ignore  #930 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #930 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #930 (line in Coconut source)
__annotations__["map"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #930 (line in Coconut source)
map = _map  # type: ignore  #931 (line in Coconut source)

@_coconut_tco  #933 (line in Coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #933 (line in Coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #937 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #938 (line in Coconut source)

_coconut_op_U2b_U2b = chain  #939 (line in Coconut source)

filter = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  # type: ignore  #941 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #941 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #941 (line in Coconut source)
__annotations__["filter"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #941 (line in Coconut source)
filter = _filter  # type: ignore  #942 (line in Coconut source)

head = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #944 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #944 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #944 (line in Coconut source)
__annotations__["head"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #944 (line in Coconut source)
head = _coconut_partial(_coconut_iter_getitem, index=(0))  #945 (line in Coconut source)

last = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #947 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #947 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #947 (line in Coconut source)
__annotations__["last"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #947 (line in Coconut source)
last = _coconut_partial(_coconut_iter_getitem, index=(-1))  #948 (line in Coconut source)

tail = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #950 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #950 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #950 (line in Coconut source)
__annotations__["tail"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #950 (line in Coconut source)
tail = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #951 (line in Coconut source)

init = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #953 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #953 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #953 (line in Coconut source)
__annotations__["init"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #953 (line in Coconut source)
init = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #954 (line in Coconut source)

@_coconut_tco  #956 (line in Coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #956 (line in Coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #960 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #961 (line in Coconut source)

_coconut_op_U21_U21 = at  #962 (line in Coconut source)

reverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]  #964 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #964 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #964 (line in Coconut source)
__annotations__["reverse"] = '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #964 (line in Coconut source)
reverse = _reversed  #965 (line in Coconut source)



## Special folds:
and_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #970 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #970 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #970 (line in Coconut source)
__annotations__["and_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #970 (line in Coconut source)
and_ = _all  #971 (line in Coconut source)

or_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #973 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #973 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #973 (line in Coconut source)
__annotations__["or_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #973 (line in Coconut source)
or_ = _any  #974 (line in Coconut source)

any = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #976 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #976 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #976 (line in Coconut source)
__annotations__["any"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #976 (line in Coconut source)
any = _coconut_forward_compose(map, or_)  #977 (line in Coconut source)

all = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #979 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #979 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #979 (line in Coconut source)
__annotations__["all"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #979 (line in Coconut source)
all = _coconut_forward_compose(map, and_)  #980 (line in Coconut source)

@_coconut_tco  #982 (line in Coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #982 (line in Coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #983 (line in Coconut source)


concatMap = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]  #985 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #985 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #985 (line in Coconut source)
__annotations__["concatMap"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #985 (line in Coconut source)
concatMap = _coconut_forward_compose(map, concat)  #986 (line in Coconut source)



## Building lists:

### Scans:
@_coconut_tco  #993 (line in Coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #993 (line in Coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #994 (line in Coconut source)


scanl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #996 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #996 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #996 (line in Coconut source)
__annotations__["scanl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #996 (line in Coconut source)
scanl1 = scan  #997 (line in Coconut source)

@_coconut_tco  #999 (line in Coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #999 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #1000 (line in Coconut source)


@_coconut_tco  #1002 (line in Coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1002 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #1003 (line in Coconut source)

### Infinite lists:

@recursive_generator  #1006 (line in Coconut source)
@_coconut_tco  #1007 (line in Coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #1007 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #1008 (line in Coconut source)


@recursive_generator  #1010 (line in Coconut source)
@_coconut_tco  #1011 (line in Coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #1011 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #1012 (line in Coconut source)


@_coconut_tco  #1014 (line in Coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #1014 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #1015 (line in Coconut source)


if TYPE_CHECKING:  #1017 (line in Coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  # type: ignore  #1018 (line in Coconut source)
        ...  #1019 (line in Coconut source)

else:  #1020 (line in Coconut source)
    @recursive_generator  #1021 (line in Coconut source)
    @_coconut_tco  #1022 (line in Coconut source)
    @_coconut_mark_as_match  #1022 (line in Coconut source)
    def cycle(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1022 (line in Coconut source)
        _coconut_match_check_9 = False  #1022 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1022 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1022 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1022 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1022 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #1022 (line in Coconut source)
            _coconut_match_temp_36 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #1022 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_36  #1022 (line in Coconut source)
            if not _coconut_match_kwargs:  #1022 (line in Coconut source)
                _coconut_match_check_9 = True  #1022 (line in Coconut source)
        if _coconut_match_check_9:  #1022 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1022 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1022 (line in Coconut source)
        if _coconut_match_check_9 and not (len(xs) > 0):  #1022 (line in Coconut source)
            _coconut_match_check_9 = False  #1022 (line in Coconut source)
        if not _coconut_match_check_9:  #1022 (line in Coconut source)
            raise _coconut_FunctionMatchError('def \\cycle(xs if len(xs) > 0) =', _coconut_match_args)  #1022 (line in Coconut source)

        return _coconut_tail_call(_cycle, xs)  #1023 (line in Coconut source)



## Sublists:

@_coconut_tco  #1028 (line in Coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1028 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #1029 (line in Coconut source)


@_coconut_tco  #1031 (line in Coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1031 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #1032 (line in Coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]])':  #1034 (line in Coconut source)
    reit = reiterable(xs)  #1035 (line in Coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #1036 (line in Coconut source)


takeWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1038 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1038 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1038 (line in Coconut source)
__annotations__["takeWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1038 (line in Coconut source)
takeWhile = takewhile  #1039 (line in Coconut source)

dropWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1041 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1041 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1041 (line in Coconut source)
__annotations__["dropWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1041 (line in Coconut source)
dropWhile = dropwhile  #1042 (line in Coconut source)

if _coconut.typing.TYPE_CHECKING:  #1044 (line in Coconut source)
    @_coconut_mark_as_match  #1044 (line in Coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]])':  #1044 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #1044 (line in Coconut source)
else:  #1044 (line in Coconut source)
    @_coconut_mark_as_match  #1044 (line in Coconut source)
    def span(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1044 (line in Coconut source)

        _coconut_match_check_10 = False  #1044 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1044 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1044 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1044 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #1044 (line in Coconut source)
        if not _coconut_match_check_10:  #1044 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1044 (line in Coconut source)
            if _coconut.len(_coconut_match_args) == 2:  #1044 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1044 (line in Coconut source)
                    if not _coconut_match_kwargs:  #1044 (line in Coconut source)
                        _coconut_match_check_10 = True  #1044 (line in Coconut source)

            if _coconut_match_check_10:  #1044 (line in Coconut source)

                    return (([], []))  #1047 (line in Coconut source)

        if not _coconut_match_check_10:  #1048 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1048 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_sentinel  #1048 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_sentinel  #1048 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_sentinel  #1048 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1048 (line in Coconut source)
                if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1048 (line in Coconut source)
                    _coconut_match_temp_37 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1048 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[1][0]  #1048 (line in Coconut source)
                    _coconut_match_set_name_cond = _coconut_match_temp_37  #1048 (line in Coconut source)
                    _coconut_match_temp_38 = _coconut.list(_coconut_match_args[1][1:])  #1048 (line in Coconut source)
                    _coconut_match_set_name_xs = _coconut_match_temp_38  #1048 (line in Coconut source)
                    if not _coconut_match_kwargs:  #1048 (line in Coconut source)
                        _coconut_match_check_10 = True  #1048 (line in Coconut source)
            if _coconut_match_check_10:  #1048 (line in Coconut source)
                if _coconut_match_set_name_cond is not _coconut_sentinel:  #1048 (line in Coconut source)
                    cond = _coconut_match_set_name_cond  #1048 (line in Coconut source)
                if _coconut_match_set_name_x is not _coconut_sentinel:  #1048 (line in Coconut source)
                    x = _coconut_match_set_name_x  #1048 (line in Coconut source)
                if _coconut_match_set_name_xs is not _coconut_sentinel:  #1048 (line in Coconut source)
                    xs = _coconut_match_set_name_xs  #1048 (line in Coconut source)
            if _coconut_match_check_10 and not (cond(x)):  #1048 (line in Coconut source)
                _coconut_match_check_10 = False  #1048 (line in Coconut source)

            if _coconut_match_check_10:  #1048 (line in Coconut source)

                    ys, zs = span(cond, xs)  #1049 (line in Coconut source)
                    return (([x,] + ys, zs))  #1050 (line in Coconut source)

        if not _coconut_match_check_10:  #1051 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #1051 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_sentinel  #1051 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_sentinel  #1051 (line in Coconut source)
            if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1051 (line in Coconut source)
                _coconut_match_temp_39 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1051 (line in Coconut source)
                _coconut_match_temp_40 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1051 (line in Coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_39  #1051 (line in Coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_40  #1051 (line in Coconut source)
                if not _coconut_match_kwargs:  #1051 (line in Coconut source)
                    _coconut_match_check_10 = True  #1051 (line in Coconut source)
            if _coconut_match_check_10:  #1051 (line in Coconut source)
                if _coconut_match_set_name_cond is not _coconut_sentinel:  #1051 (line in Coconut source)
                    cond = _coconut_match_set_name_cond  #1051 (line in Coconut source)
                if _coconut_match_set_name_xs is not _coconut_sentinel:  #1051 (line in Coconut source)
                    xs = _coconut_match_set_name_xs  #1051 (line in Coconut source)

            if _coconut_match_check_10:  #1051 (line in Coconut source)

                    return (([], xs))  #1052 (line in Coconut source)


        if not _coconut_match_check_10:  #1054 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def span:', _coconut_match_args)  #1054 (line in Coconut source)


@_coconut_tco  #1054 (line in Coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #1054 (line in Coconut source)
    """
    break_ = break
    """  #1057 (line in Coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1058 (line in Coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #1063 (line in Coconut source)
    return (e not in xs)  #1064 (line in Coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> 'Maybe':  #1066 (line in Coconut source)
    try:  #1067 (line in Coconut source)
        return (((Just)((_coconut_iter_getitem(((dropwhile)(lambda pair: pair[0] != key, assocs)), (0)))[1])))  #1068 (line in Coconut source)
    except IndexError:  #1075 (line in Coconut source)
        return (nothing)  #1076 (line in Coconut source)



## Zipping and unzipping lists:
# type: ignore
zip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]  # type: ignore  #1081 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #1081 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #1081 (line in Coconut source)
__annotations__["zip"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]'  # type: ignore  #1081 (line in Coconut source)
zip = _zip  # type: ignore  #1082 (line in Coconut source)

zip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]  #1084 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1084 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1084 (line in Coconut source)
__annotations__["zip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]'  #1084 (line in Coconut source)
zip3 = _zip  #1085 (line in Coconut source)

@_coconut_tco  #1087 (line in Coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #1087 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2)  #1088 (line in Coconut source)


@_coconut_tco  #1090 (line in Coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1090 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2, xs3)  #1091 (line in Coconut source)


@_coconut_tco  #1093 (line in Coconut source)
def unzip(xs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]])':  #1093 (line in Coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1094 (line in Coconut source)


unzip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]  #1096 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1096 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1096 (line in Coconut source)
__annotations__["unzip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]'  #1096 (line in Coconut source)
unzip3 = unzip  # type: ignore  #1097 (line in Coconut source)



## Functions on strings:
lines = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1102 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1102 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1102 (line in Coconut source)
__annotations__["lines"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1102 (line in Coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1103 (line in Coconut source)

words = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1105 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1105 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1105 (line in Coconut source)
__annotations__["words"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1105 (line in Coconut source)
words = _coconut.operator.methodcaller("split")  #1106 (line in Coconut source)

@_coconut_tco  #1108 (line in Coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1108 (line in Coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1109 (line in Coconut source)


unwords = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]  #1111 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1111 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1111 (line in Coconut source)
__annotations__["unwords"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1111 (line in Coconut source)
unwords = " ".join  #1112 (line in Coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1120 (line in Coconut source)

Show = T.Any  #1122 (line in Coconut source)

showsPrec = NotImplemented  #1124 (line in Coconut source)

show = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Ta], str]  #1126 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1126 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1126 (line in Coconut source)
__annotations__["show"] = '_coconut.typing.Callable[[Ta], str]'  #1126 (line in Coconut source)
show = repr  #1127 (line in Coconut source)

def shows(x: 'Show') -> 'ShowS':  #1129 (line in Coconut source)
    return (lambda s: repr(x) + s)  #1130 (line in Coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1132 (line in Coconut source)
    return (lambda s: repr(list(xs)) + s)  #1133 (line in Coconut source)


def showString(x: 'str') -> 'ShowS':  #1135 (line in Coconut source)
    return (lambda s: x + s)  #1136 (line in Coconut source)


showChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], ShowS]  #1138 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1138 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1138 (line in Coconut source)
__annotations__["showChar"] = '_coconut.typing.Callable[[Char], ShowS]'  #1138 (line in Coconut source)
showChar = showString  #1139 (line in Coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1141 (line in Coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1142 (line in Coconut source)



## Converting from String:

ReadS = NotImplemented  #1150 (line in Coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1152 (line in Coconut source)

readsPrec = NotImplemented  #1163 (line in Coconut source)

readList = NotImplemented  #1165 (line in Coconut source)

reads = NotImplemented  #1167 (line in Coconut source)

readParen = NotImplemented  #1169 (line in Coconut source)

@_coconut_tco  #1171 (line in Coconut source)
def read(s: 'str') -> 'Read':  #1171 (line in Coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1172 (line in Coconut source)


lex = NotImplemented  #1174 (line in Coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1182 (line in Coconut source)
    __slots__ = ()  #1182 (line in Coconut source)
    _coconut_is_data = True  #1182 (line in Coconut source)
    __match_args__ = ('io_func',)  #1182 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1182 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1182 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1182 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #1182 (line in Coconut source)
    def __eq__(self, other):  #1182 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1182 (line in Coconut source)
    def __hash__(self):  #1182 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ _coconut.hash(self.__class__)  #1182 (line in Coconut source)
    @staticmethod  #1183 (line in Coconut source)
    @_coconut_tco  #1184 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1184 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1185 (line in Coconut source)


    @staticmethod  #1187 (line in Coconut source)
    @_coconut_tco  #1188 (line in Coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1188 (line in Coconut source)
        def _coconut_lambda_0():  #1189 (line in Coconut source)
            raise IOError(msg)  #1189 (line in Coconut source)

        return _coconut_tail_call(IO, _coconut_lambda_0)  #1189 (line in Coconut source)


    @_coconut_tco  #1191 (line in Coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1191 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1192 (line in Coconut source)


    @_coconut_tco  #1194 (line in Coconut source)
    def __join__(self) -> 'IO':  #1194 (line in Coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1195 (line in Coconut source)


    @staticmethod  #1197 (line in Coconut source)
    @_coconut_tco  #1198 (line in Coconut source)
    def __mempty__() -> 'IO':  #1198 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1199 (line in Coconut source)


    @_coconut_tco  #1201 (line in Coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1201 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1202 (line in Coconut source)


_coconut_call_set_names(IO)  #1204 (line in Coconut source)
_nullIO = IO(lambda: None)  # type: IO  #1204 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1204 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1204 (line in Coconut source)
__annotations__["_nullIO"] = 'IO'  #1204 (line in Coconut source)

@_coconut_tco  #1206 (line in Coconut source)
def asIO(io: 'IO') -> 'IO':  #1206 (line in Coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1211 (line in Coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1212 (line in Coconut source)


@_coconut_tco  #1214 (line in Coconut source)
def unIO(io: 'IO') -> 'T.Any':  #1214 (line in Coconut source)
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
    """  #1228 (line in Coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1229 (line in Coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1237 (line in Coconut source)
def putStr(s: 'str') -> 'IO':  #1237 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s, end=""))  #1238 (line in Coconut source)


putChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], IO]  #1240 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1240 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1240 (line in Coconut source)
__annotations__["putChar"] = '_coconut.typing.Callable[[Char], IO]'  #1240 (line in Coconut source)
putChar = putStr  #1241 (line in Coconut source)

@_coconut_tco  #1243 (line in Coconut source)
def putStrLn(s: 'str') -> 'IO':  #1243 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s))  #1244 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1246 (line in Coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1246 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, show(x)))  #1247 (line in Coconut source)


### Input functions:

getChar = IO(_coconut_partial(sys.stdin.read, 1))  # type: IO  #1251 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1251 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1251 (line in Coconut source)
__annotations__["getChar"] = 'IO'  #1251 (line in Coconut source)

getLine = IO(input)  # type: IO  #1253 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1253 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1253 (line in Coconut source)
__annotations__["getLine"] = 'IO'  #1253 (line in Coconut source)

getContents = IO(sys.stdin.read)  # type: IO  #1255 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1255 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1255 (line in Coconut source)
__annotations__["getContents"] = 'IO'  #1255 (line in Coconut source)

@_coconut_tco  #1257 (line in Coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1257 (line in Coconut source)
    def do_interact():  #1258 (line in Coconut source)
        while True:  #1259 (line in Coconut source)
            (_print)((func)(input()))  #1260 (line in Coconut source)

    return _coconut_tail_call(IO, do_interact)  #1261 (line in Coconut source)


### Files:

FilePath = str  #1265 (line in Coconut source)

@_coconut_tco  #1267 (line in Coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1267 (line in Coconut source)
    def do_readFile() -> 'str':  #1268 (line in Coconut source)
        with open(fpath, "r+") as f:  #1269 (line in Coconut source)
            return (f.read())  #1270 (line in Coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1271 (line in Coconut source)


@_coconut_tco  #1273 (line in Coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1273 (line in Coconut source)
    def do_writeFile() -> 'None':  #1274 (line in Coconut source)
        with open(fpath, "w+") as f:  #1275 (line in Coconut source)
            f.write(text)  #1276 (line in Coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1277 (line in Coconut source)


@_coconut_tco  #1279 (line in Coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1279 (line in Coconut source)
    def do_appendFile() -> 'None':  #1280 (line in Coconut source)
        with open(fpath, "a+") as f:  #1281 (line in Coconut source)
            f.write(text)  #1282 (line in Coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1283 (line in Coconut source)


@_coconut_tco  #1285 (line in Coconut source)
def readIO(s: 'str') -> 'IO':  #1285 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(read, s))  #1286 (line in Coconut source)


@_coconut_tco  #1288 (line in Coconut source)
def readLn() -> 'IO':  #1288 (line in Coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1289 (line in Coconut source)



## Exception handling:

@_coconut_tco  #1294 (line in Coconut source)
def ioError(err: 'IOError') -> 'IO':  #1294 (line in Coconut source)
    def _coconut_lambda_1():  #1295 (line in Coconut source)
        raise err  #1295 (line in Coconut source)

    return _coconut_tail_call(IO, _coconut_lambda_1)  #1295 (line in Coconut source)


@_coconut_tco  #1297 (line in Coconut source)
def userError(msg: 'str') -> 'IOError':  #1297 (line in Coconut source)
    return _coconut_tail_call(IOError, msg)  #1298 (line in Coconut source)
