#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6dd9eb8d

# Compiled with Coconut version 3.0.3-post_dev33

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.0.3-post_dev33', '35', True)
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter
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
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #77 (line in Coconut source)
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
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #79 (line in Coconut source)


_coconut_call_set_names(Just)  #81 (line in Coconut source)
derivingOrd(Nothing, Just)  #81 (line in Coconut source)

if TYPE_CHECKING:  #83 (line in Coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #84 (line in Coconut source)
        ...  #85 (line in Coconut source)

else:  #86 (line in Coconut source)
    @_coconut_mark_as_match  #87 (line in Coconut source)
    def maybe(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #87 (line in Coconut source)
        _coconut_match_check_0 = False  #87 (line in Coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #87 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #87 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #87 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #87 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #87 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #87 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)  # type: ignore  #87 (line in Coconut source)
            _coconut_match_set_name_default = _coconut_match_temp_0  #87 (line in Coconut source)
            if not _coconut_match_kwargs:  #87 (line in Coconut source)
                _coconut_match_check_0 = True  #87 (line in Coconut source)
        if _coconut_match_check_0:  #87 (line in Coconut source)
            _coconut_match_check_0 = False  #87 (line in Coconut source)
            if not _coconut_match_check_0:  #87 (line in Coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #87 (line in Coconut source)
                    _coconut_match_temp_2 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(0, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(0, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 0  # type: ignore  #87 (line in Coconut source)
                    if _coconut_match_temp_2:  #87 (line in Coconut source)
                        _coconut_match_check_0 = True  #87 (line in Coconut source)

            if not _coconut_match_check_0:  #87 (line in Coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #87 (line in Coconut source)
                    _coconut_match_check_0 = True  #87 (line in Coconut source)
                if _coconut_match_check_0:  #87 (line in Coconut source)
                    _coconut_match_check_0 = False  #87 (line in Coconut source)
                    if not _coconut_match_check_0:  #87 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                            _coconut_match_check_0 = True  #87 (line in Coconut source)

                    if not _coconut_match_check_0:  #87 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(Nothing, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #87 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_3, _coconut.tuple):  #87 (line in Coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #87 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_3) < 0:  #87 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_3),))  #87 (line in Coconut source)
                            _coconut_match_check_0 = True  #87 (line in Coconut source)




        if _coconut_match_check_0:  #87 (line in Coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #87 (line in Coconut source)
                default = _coconut_match_set_name_default  #87 (line in Coconut source)
        if not _coconut_match_check_0:  #87 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #87 (line in Coconut source)

        return (default)  #87 (line in Coconut source)

    try:  #88 (line in Coconut source)
        _coconut_addpattern_0 = _coconut_addpattern(maybe)  # type: ignore  #88 (line in Coconut source)
    except _coconut.NameError:  #88 (line in Coconut source)
        _coconut_addpattern_0 = lambda f: f  #88 (line in Coconut source)
    @_coconut_addpattern_0  #88 (line in Coconut source)
    @_coconut_tco  #88 (line in Coconut source)
    @_coconut_mark_as_match  #88 (line in Coconut source)
    def maybe(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #88 (line in Coconut source)
        _coconut_match_check_1 = False  #88 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #88 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #88 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #88 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #88 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #88 (line in Coconut source)
            _coconut_match_temp_4 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #88 (line in Coconut source)
            _coconut_match_temp_5 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)  # type: ignore  #88 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_match_temp_4  #88 (line in Coconut source)
            if not _coconut_match_kwargs:  #88 (line in Coconut source)
                _coconut_match_check_1 = True  #88 (line in Coconut source)
        if _coconut_match_check_1:  #88 (line in Coconut source)
            _coconut_match_check_1 = False  #88 (line in Coconut source)
            if not _coconut_match_check_1:  #88 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #88 (line in Coconut source)
                if (_coconut_match_temp_5) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #88 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #88 (line in Coconut source)
                    _coconut_match_temp_6 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #88 (line in Coconut source)
                    if _coconut_match_temp_6:  #88 (line in Coconut source)
                        _coconut_match_check_1 = True  #88 (line in Coconut source)
                if _coconut_match_check_1:  #88 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #88 (line in Coconut source)
                        x = _coconut_match_set_name_x  #88 (line in Coconut source)

            if not _coconut_match_check_1:  #88 (line in Coconut source)
                if (not _coconut_match_temp_5) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #88 (line in Coconut source)
                    _coconut_match_check_1 = True  #88 (line in Coconut source)
                if _coconut_match_check_1:  #88 (line in Coconut source)
                    _coconut_match_check_1 = False  #88 (line in Coconut source)
                    if not _coconut_match_check_1:  #88 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #88 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #88 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #88 (line in Coconut source)
                            _coconut_match_check_1 = True  #88 (line in Coconut source)
                        if _coconut_match_check_1:  #88 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #88 (line in Coconut source)
                                x = _coconut_match_set_name_x  #88 (line in Coconut source)

                    if not _coconut_match_check_1:  #88 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #88 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #88 (line in Coconut source)
                            _coconut_match_temp_7 = _coconut.getattr(Just, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #88 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_7, _coconut.tuple):  #88 (line in Coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #88 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_7) < 1:  #88 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_7),))  #88 (line in Coconut source)
                            _coconut_match_temp_8 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_7[0], _coconut_sentinel)  #88 (line in Coconut source)
                            if _coconut_match_temp_8 is not _coconut_sentinel:  #88 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_8  #88 (line in Coconut source)
                                _coconut_match_check_1 = True  #88 (line in Coconut source)
                        if _coconut_match_check_1:  #88 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #88 (line in Coconut source)
                                x = _coconut_match_set_name_x  #88 (line in Coconut source)




        if _coconut_match_check_1:  #88 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #88 (line in Coconut source)
                func = _coconut_match_set_name_func  #88 (line in Coconut source)
        if not _coconut_match_check_1:  #88 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #88 (line in Coconut source)

        return _coconut_tail_call(_coconut_call_or_coefficient, func, x)  #88 (line in Coconut source)

#### Either:

class Either():  #91 (line in Coconut source)
    @staticmethod  #92 (line in Coconut source)
    @_coconut_tco  #93 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #93 (line in Coconut source)
        return _coconut_tail_call(Right, x)  #93 (line in Coconut source)


    @staticmethod  #95 (line in Coconut source)
    @_coconut_tco  #96 (line in Coconut source)
    def __fail__(msg: 'str') -> 'Either':  #96 (line in Coconut source)
        return _coconut_tail_call(Left, msg)  #96 (line in Coconut source)


_coconut_call_set_names(Either)  #98 (line in Coconut source)
class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #98 (line in Coconut source)
    __slots__ = ()  #98 (line in Coconut source)
    _coconut_is_data = True  #98 (line in Coconut source)
    __match_args__ = ('x',)  #98 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #98 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #98 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #98 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #98 (line in Coconut source)
    def __eq__(self, other):  #98 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #98 (line in Coconut source)
    def __hash__(self):  #98 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #98 (line in Coconut source)
    @staticmethod  #99 (line in Coconut source)
    def __bool__() -> 'bool':  #100 (line in Coconut source)
        return (False)  #100 (line in Coconut source)


    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #102 (line in Coconut source)
        return (self)  #102 (line in Coconut source)


_coconut_call_set_names(Left)  #104 (line in Coconut source)
class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #104 (line in Coconut source)
    __slots__ = ()  #104 (line in Coconut source)
    _coconut_is_data = True  #104 (line in Coconut source)
    __match_args__ = ('x',)  #104 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #104 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #104 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #104 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #104 (line in Coconut source)
    def __eq__(self, other):  #104 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #104 (line in Coconut source)
    def __hash__(self):  #104 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #104 (line in Coconut source)


_coconut_call_set_names(Right)  #106 (line in Coconut source)
derivingOrd(Left, Right)  #106 (line in Coconut source)

if TYPE_CHECKING:  #108 (line in Coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #109 (line in Coconut source)
        ...  #110 (line in Coconut source)

else:  #111 (line in Coconut source)
    @_coconut_tco  #112 (line in Coconut source)
    @_coconut_mark_as_match  #112 (line in Coconut source)
    def either(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #112 (line in Coconut source)
        _coconut_match_check_2 = False  #112 (line in Coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #112 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #112 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #112 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #112 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #112 (line in Coconut source)
            _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #112 (line in Coconut source)
            _coconut_match_temp_10 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)  # type: ignore  #112 (line in Coconut source)
            _coconut_match_set_name_left_func = _coconut_match_temp_9  #112 (line in Coconut source)
            if not _coconut_match_kwargs:  #112 (line in Coconut source)
                _coconut_match_check_2 = True  #112 (line in Coconut source)
        if _coconut_match_check_2:  #112 (line in Coconut source)
            _coconut_match_check_2 = False  #112 (line in Coconut source)
            if not _coconut_match_check_2:  #112 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                if (_coconut_match_temp_10) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #112 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #112 (line in Coconut source)
                    _coconut_match_temp_11 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #112 (line in Coconut source)
                    if _coconut_match_temp_11:  #112 (line in Coconut source)
                        _coconut_match_check_2 = True  #112 (line in Coconut source)
                if _coconut_match_check_2:  #112 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                        x = _coconut_match_set_name_x  #112 (line in Coconut source)

            if not _coconut_match_check_2:  #112 (line in Coconut source)
                if (not _coconut_match_temp_10) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #112 (line in Coconut source)
                    _coconut_match_check_2 = True  #112 (line in Coconut source)
                if _coconut_match_check_2:  #112 (line in Coconut source)
                    _coconut_match_check_2 = False  #112 (line in Coconut source)
                    if not _coconut_match_check_2:  #112 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #112 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #112 (line in Coconut source)
                            _coconut_match_check_2 = True  #112 (line in Coconut source)
                        if _coconut_match_check_2:  #112 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                                x = _coconut_match_set_name_x  #112 (line in Coconut source)

                    if not _coconut_match_check_2:  #112 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #112 (line in Coconut source)
                            _coconut_match_temp_12 = _coconut.getattr(Left, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #112 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_12, _coconut.tuple):  #112 (line in Coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #112 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_12) < 1:  #112 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_12),))  #112 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_12[0], _coconut_sentinel)  #112 (line in Coconut source)
                            if _coconut_match_temp_13 is not _coconut_sentinel:  #112 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_13  #112 (line in Coconut source)
                                _coconut_match_check_2 = True  #112 (line in Coconut source)
                        if _coconut_match_check_2:  #112 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                                x = _coconut_match_set_name_x  #112 (line in Coconut source)




        if _coconut_match_check_2:  #112 (line in Coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #112 (line in Coconut source)
                left_func = _coconut_match_set_name_left_func  #112 (line in Coconut source)
        if not _coconut_match_check_2:  #112 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #112 (line in Coconut source)

        return _coconut_tail_call(_coconut_call_or_coefficient, left_func, x)  #112 (line in Coconut source)

    try:  #113 (line in Coconut source)
        _coconut_addpattern_1 = _coconut_addpattern(either)  # type: ignore  #113 (line in Coconut source)
    except _coconut.NameError:  #113 (line in Coconut source)
        _coconut_addpattern_1 = lambda f: f  #113 (line in Coconut source)
    @_coconut_addpattern_1  #113 (line in Coconut source)
    @_coconut_tco  #113 (line in Coconut source)
    @_coconut_mark_as_match  #113 (line in Coconut source)
    def either(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #113 (line in Coconut source)
        _coconut_match_check_3 = False  #113 (line in Coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #113 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #113 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #113 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #113 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #113 (line in Coconut source)
            _coconut_match_temp_14 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #113 (line in Coconut source)
            _coconut_match_temp_15 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)  # type: ignore  #113 (line in Coconut source)
            _coconut_match_set_name_right_func = _coconut_match_temp_14  #113 (line in Coconut source)
            if not _coconut_match_kwargs:  #113 (line in Coconut source)
                _coconut_match_check_3 = True  #113 (line in Coconut source)
        if _coconut_match_check_3:  #113 (line in Coconut source)
            _coconut_match_check_3 = False  #113 (line in Coconut source)
            if not _coconut_match_check_3:  #113 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #113 (line in Coconut source)
                if (_coconut_match_temp_15) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) >= 1):  #113 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #113 (line in Coconut source)
                    _coconut_match_temp_16 = _coconut.len(_coconut_match_args[2]) <= _coconut.max(1, _coconut.len(_coconut_match_args[2].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {}) and _coconut_match_args[2][i] == _coconut.getattr(_coconut_match_args[2], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[2].__match_args__))) if _coconut.hasattr(_coconut_match_args[2], "__match_args__") else _coconut.len(_coconut_match_args[2]) == 1  # type: ignore  #113 (line in Coconut source)
                    if _coconut_match_temp_16:  #113 (line in Coconut source)
                        _coconut_match_check_3 = True  #113 (line in Coconut source)
                if _coconut_match_check_3:  #113 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #113 (line in Coconut source)
                        x = _coconut_match_set_name_x  #113 (line in Coconut source)

            if not _coconut_match_check_3:  #113 (line in Coconut source)
                if (not _coconut_match_temp_15) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #113 (line in Coconut source)
                    _coconut_match_check_3 = True  #113 (line in Coconut source)
                if _coconut_match_check_3:  #113 (line in Coconut source)
                    _coconut_match_check_3 = False  #113 (line in Coconut source)
                    if not _coconut_match_check_3:  #113 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #113 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #113 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #113 (line in Coconut source)
                            _coconut_match_check_3 = True  #113 (line in Coconut source)
                        if _coconut_match_check_3:  #113 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #113 (line in Coconut source)
                                x = _coconut_match_set_name_x  #113 (line in Coconut source)

                    if not _coconut_match_check_3:  #113 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #113 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #113 (line in Coconut source)
                            _coconut_match_temp_17 = _coconut.getattr(Right, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #113 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_17, _coconut.tuple):  #113 (line in Coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #113 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_17) < 1:  #113 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_17),))  #113 (line in Coconut source)
                            _coconut_match_temp_18 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_17[0], _coconut_sentinel)  #113 (line in Coconut source)
                            if _coconut_match_temp_18 is not _coconut_sentinel:  #113 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_18  #113 (line in Coconut source)
                                _coconut_match_check_3 = True  #113 (line in Coconut source)
                        if _coconut_match_check_3:  #113 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #113 (line in Coconut source)
                                x = _coconut_match_set_name_x  #113 (line in Coconut source)




        if _coconut_match_check_3:  #113 (line in Coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #113 (line in Coconut source)
                right_func = _coconut_match_set_name_right_func  #113 (line in Coconut source)
        if not _coconut_match_check_3:  #113 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #113 (line in Coconut source)

        return _coconut_tail_call(_coconut_call_or_coefficient, right_func, x)  #113 (line in Coconut source)

#### Ordering:

class Ordering():  #116 (line in Coconut source)
    @staticmethod  #117 (line in Coconut source)
    def __mempty__() -> 'Ordering':  #118 (line in Coconut source)
        return (eq)  #118 (line in Coconut source)


_coconut_call_set_names(Ordering)  #120 (line in Coconut source)
class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #120 (line in Coconut source)
    __slots__ = ()  #120 (line in Coconut source)
    _coconut_is_data = True  #120 (line in Coconut source)
    __match_args__ = ()  #120 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #120 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #120 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #120 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #120 (line in Coconut source)
    def __eq__(self, other):  #120 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #120 (line in Coconut source)
    def __hash__(self):  #120 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #120 (line in Coconut source)
    @staticmethod  #121 (line in Coconut source)
    def __bool__() -> 'bool':  #122 (line in Coconut source)
        return (True)  #122 (line in Coconut source)


_coconut_call_set_names(LT)  #124 (line in Coconut source)
class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #124 (line in Coconut source)
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
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #124 (line in Coconut source)


_coconut_call_set_names(EQ)  #126 (line in Coconut source)
class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #126 (line in Coconut source)
    __slots__ = ()  #126 (line in Coconut source)
    _coconut_is_data = True  #126 (line in Coconut source)
    __match_args__ = ()  #126 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #126 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #126 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #126 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #126 (line in Coconut source)
    def __eq__(self, other):  #126 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #126 (line in Coconut source)
    def __hash__(self):  #126 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #126 (line in Coconut source)
    @staticmethod  #127 (line in Coconut source)
    def __bool__() -> 'bool':  #128 (line in Coconut source)
        return (True)  #128 (line in Coconut source)


_coconut_call_set_names(GT)  #130 (line in Coconut source)
derivingOrd(LT, EQ, GT)  #130 (line in Coconut source)
derivingBoundedEnum(LT, EQ, GT)  #131 (line in Coconut source)

lt = LT()  # type: Ordering  #133 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #133 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #133 (line in Coconut source)
__annotations__["lt"] = 'Ordering'  #133 (line in Coconut source)
eq = EQ()  # type: Ordering  #134 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #134 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #134 (line in Coconut source)
__annotations__["eq"] = 'Ordering'  #134 (line in Coconut source)
gt = GT()  # type: Ordering  #135 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #135 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #135 (line in Coconut source)
__annotations__["gt"] = 'Ordering'  #135 (line in Coconut source)

#### Char:
Char = T.NewType("Char", str)  #138 (line in Coconut source)

#### String:
String = str  #141 (line in Coconut source)


### Tuples:
fst = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Ta]  #145 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #145 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #145 (line in Coconut source)
__annotations__["fst"] = '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Ta]'  #145 (line in Coconut source)
fst = _coconut.operator.itemgetter((0))  #146 (line in Coconut source)

snd = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tb]  #148 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #148 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #148 (line in Coconut source)
__annotations__["snd"] = '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tb]'  #148 (line in Coconut source)
snd = _coconut.operator.itemgetter((1))  #149 (line in Coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #151 (line in Coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #154 (line in Coconut source)
    return (lambda *args: func(args))  # type: ignore  #155 (line in Coconut source)


def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[(_coconut.typing.Tuple[Ta, Tb])], Tc]':  #157 (line in Coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #160 (line in Coconut source)
    return (lambda args: func(*args))  #161 (line in Coconut source)



## Basic type classes:

#### Eq:

Eq = object  #168 (line in Coconut source)

#### Ord:
Ord = Eq  #171 (line in Coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #172 (line in Coconut source)

if TYPE_CHECKING:  #174 (line in Coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #175 (line in Coconut source)
        ...  #176 (line in Coconut source)

else:  #177 (line in Coconut source)
    @_coconut_mark_as_match  #178 (line in Coconut source)
    def compare(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #178 (line in Coconut source)
        _coconut_match_check_4 = False  #178 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #178 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #178 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #178 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #178 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #178 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #178 (line in Coconut source)
            _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #178 (line in Coconut source)
            _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #178 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_19  #178 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_20  #178 (line in Coconut source)
            if not _coconut_match_kwargs:  #178 (line in Coconut source)
                _coconut_match_check_4 = True  #178 (line in Coconut source)
        if _coconut_match_check_4:  #178 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #178 (line in Coconut source)
                x = _coconut_match_set_name_x  #178 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #178 (line in Coconut source)
                y = _coconut_match_set_name_y  #178 (line in Coconut source)
        if _coconut_match_check_4 and not (x == y):  #178 (line in Coconut source)
            _coconut_match_check_4 = False  #178 (line in Coconut source)
        if not _coconut_match_check_4:  #178 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #178 (line in Coconut source)

        return (eq)  #178 (line in Coconut source)

    try:  #179 (line in Coconut source)
        _coconut_addpattern_2 = _coconut_addpattern(compare)  # type: ignore  #179 (line in Coconut source)
    except _coconut.NameError:  #179 (line in Coconut source)
        _coconut_addpattern_2 = lambda f: f  #179 (line in Coconut source)
    @_coconut_addpattern_2  #179 (line in Coconut source)
    @_coconut_mark_as_match  #179 (line in Coconut source)
    def compare(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #179 (line in Coconut source)
        _coconut_match_check_5 = False  #179 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #179 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #179 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #179 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #179 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #179 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #179 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #179 (line in Coconut source)
            _coconut_match_temp_22 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #179 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_21  #179 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_22  #179 (line in Coconut source)
            if not _coconut_match_kwargs:  #179 (line in Coconut source)
                _coconut_match_check_5 = True  #179 (line in Coconut source)
        if _coconut_match_check_5:  #179 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #179 (line in Coconut source)
                x = _coconut_match_set_name_x  #179 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #179 (line in Coconut source)
                y = _coconut_match_set_name_y  #179 (line in Coconut source)
        if _coconut_match_check_5 and not (x < y):  #179 (line in Coconut source)
            _coconut_match_check_5 = False  #179 (line in Coconut source)
        if not _coconut_match_check_5:  #179 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #179 (line in Coconut source)

        return (lt)  #179 (line in Coconut source)

    try:  #180 (line in Coconut source)
        _coconut_addpattern_3 = _coconut_addpattern(compare)  # type: ignore  #180 (line in Coconut source)
    except _coconut.NameError:  #180 (line in Coconut source)
        _coconut_addpattern_3 = lambda f: f  #180 (line in Coconut source)
    @_coconut_addpattern_3  #180 (line in Coconut source)
    @_coconut_mark_as_match  #180 (line in Coconut source)
    def compare(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #180 (line in Coconut source)
        _coconut_match_check_6 = False  #180 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #180 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #180 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #180 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #180 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #180 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #180 (line in Coconut source)
            _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #180 (line in Coconut source)
            _coconut_match_temp_24 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #180 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_23  #180 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_24  #180 (line in Coconut source)
            if not _coconut_match_kwargs:  #180 (line in Coconut source)
                _coconut_match_check_6 = True  #180 (line in Coconut source)
        if _coconut_match_check_6:  #180 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #180 (line in Coconut source)
                x = _coconut_match_set_name_x  #180 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #180 (line in Coconut source)
                y = _coconut_match_set_name_y  #180 (line in Coconut source)
        if _coconut_match_check_6 and not (x > y):  #180 (line in Coconut source)
            _coconut_match_check_6 = False  #180 (line in Coconut source)
        if not _coconut_match_check_6:  #180 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #180 (line in Coconut source)

        return (gt)  #180 (line in Coconut source)


max = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  #182 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #182 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #182 (line in Coconut source)
__annotations__["max"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #182 (line in Coconut source)
max = _max  #183 (line in Coconut source)

min = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  #185 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #185 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #185 (line in Coconut source)
__annotations__["min"] = '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #185 (line in Coconut source)
min = _min  #186 (line in Coconut source)

#### Enum:
Enum = Ord  #189 (line in Coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #190 (line in Coconut source)

succ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #192 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #192 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #192 (line in Coconut source)
__annotations__["succ"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #192 (line in Coconut source)
succ = (_coconut_partial(_coconut.operator.add, 1))  #193 (line in Coconut source)

pred = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TEnum], TEnum]  #195 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #195 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #195 (line in Coconut source)
__annotations__["pred"] = '_coconut.typing.Callable[[TEnum], TEnum]'  #195 (line in Coconut source)
pred = (_coconut_complex_partial(_coconut_minus, {1: 1}, 2, ()))  #196 (line in Coconut source)

toEnum = NotImplemented  #198 (line in Coconut source)

fromEnum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Enum], int]  #200 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #200 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #200 (line in Coconut source)
__annotations__["fromEnum"] = '_coconut.typing.Callable[[Enum], int]'  #200 (line in Coconut source)
fromEnum = _int  #201 (line in Coconut source)

@_coconut_tco  #203 (line in Coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #203 (line in Coconut source)
    return _coconut_tail_call(iterate, succ, first)  #204 (line in Coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #206 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #207 (line in Coconut source)
    return (iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first) if step >= 0 else ())  # type: ignore  #208 (line in Coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #210 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #211 (line in Coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #212 (line in Coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #214 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #215 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #216 (line in Coconut source)
    steps = dist / step if step != 0 else 0  #217 (line in Coconut source)
    if steps < 0:  #218 (line in Coconut source)
        return (())  #219 (line in Coconut source)
    counter = iterate((_coconut_complex_partial(_coconut.operator.add, {1: step}, 2, ())), first)  #220 (line in Coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #221 (line in Coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #225 (line in Coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #226 (line in Coconut source)

@_coconut_tco  #228 (line in Coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #228 (line in Coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #232 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #234 (line in Coconut source)
        return (False)  # type: ignore  #235 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #238 (line in Coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #239 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #242 (line in Coconut source)


@_coconut_tco  #244 (line in Coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #244 (line in Coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #248 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #250 (line in Coconut source)
        return (True)  # type: ignore  #251 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #254 (line in Coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #255 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #258 (line in Coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #267 (line in Coconut source)

#### Integer:
Integer = int  #270 (line in Coconut source)

#### Float:
Float = float  #273 (line in Coconut source)

#### Double:
Double = float  #276 (line in Coconut source)

#### Rational:
Rational = _fractions.Fraction  #279 (line in Coconut source)

@_coconut_tco  #281 (line in Coconut source)
def over(x, y):  #281 (line in Coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #286 (line in Coconut source)
    return _coconut_tail_call(_coconut_call_or_coefficient, Rational, x, y)  #287 (line in Coconut source)

_coconut_op_U25_U25 = over  #288 (line in Coconut source)

#### Word:
Word = Int  #291 (line in Coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #297 (line in Coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #298 (line in Coconut source)

negate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #300 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #300 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #300 (line in Coconut source)
__annotations__["negate"] = '_coconut.typing.Callable[[TNum], TNum]'  #300 (line in Coconut source)
negate = (_coconut_minus)  #301 (line in Coconut source)

abs = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[TNum], TNum]  #303 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #303 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #303 (line in Coconut source)
__annotations__["abs"] = '_coconut.typing.Callable[[TNum], TNum]'  #303 (line in Coconut source)
abs = _abs  #304 (line in Coconut source)

if TYPE_CHECKING:  #306 (line in Coconut source)
    def signum(x: 'Num') -> 'int':  #307 (line in Coconut source)
        ...  #308 (line in Coconut source)

else:  #309 (line in Coconut source)
    @_coconut_mark_as_match  #310 (line in Coconut source)
    def signum(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #310 (line in Coconut source)
        _coconut_match_check_7 = False  #310 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #310 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #310 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #310 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #310 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #310 (line in Coconut source)
                if not _coconut_match_kwargs:  #310 (line in Coconut source)
                    _coconut_match_check_7 = True  #310 (line in Coconut source)
        if not _coconut_match_check_7:  #310 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #310 (line in Coconut source)

        return (0)  #310 (line in Coconut source)

    try:  #311 (line in Coconut source)
        _coconut_addpattern_4 = _coconut_addpattern(signum)  # type: ignore  #311 (line in Coconut source)
    except _coconut.NameError:  #311 (line in Coconut source)
        _coconut_addpattern_4 = lambda f: f  #311 (line in Coconut source)
    @_coconut_addpattern_4  #311 (line in Coconut source)
    @_coconut_mark_as_match  #311 (line in Coconut source)
    def signum(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #311 (line in Coconut source)
        _coconut_match_check_8 = False  #311 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #311 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #311 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #311 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #311 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #311 (line in Coconut source)
            _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #311 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_25  #311 (line in Coconut source)
            if not _coconut_match_kwargs:  #311 (line in Coconut source)
                _coconut_match_check_8 = True  #311 (line in Coconut source)
        if _coconut_match_check_8:  #311 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #311 (line in Coconut source)
                x = _coconut_match_set_name_x  #311 (line in Coconut source)
        if _coconut_match_check_8 and not (x > 0):  #311 (line in Coconut source)
            _coconut_match_check_8 = False  #311 (line in Coconut source)
        if not _coconut_match_check_8:  #311 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #311 (line in Coconut source)

        return (1)  #311 (line in Coconut source)

    try:  #312 (line in Coconut source)
        _coconut_addpattern_5 = _coconut_addpattern(signum)  # type: ignore  #312 (line in Coconut source)
    except _coconut.NameError:  #312 (line in Coconut source)
        _coconut_addpattern_5 = lambda f: f  #312 (line in Coconut source)
    @_coconut_addpattern_5  #312 (line in Coconut source)
    @_coconut_mark_as_match  #312 (line in Coconut source)
    def signum(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #312 (line in Coconut source)
        _coconut_match_check_9 = False  #312 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #312 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #312 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #312 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #312 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #312 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #312 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_26  #312 (line in Coconut source)
            if not _coconut_match_kwargs:  #312 (line in Coconut source)
                _coconut_match_check_9 = True  #312 (line in Coconut source)
        if _coconut_match_check_9:  #312 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #312 (line in Coconut source)
                x = _coconut_match_set_name_x  #312 (line in Coconut source)
        if _coconut_match_check_9 and not (x < 0):  #312 (line in Coconut source)
            _coconut_match_check_9 = False  #312 (line in Coconut source)
        if not _coconut_match_check_9:  #312 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #312 (line in Coconut source)

        return (-1)  #312 (line in Coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #314 (line in Coconut source)
    return (x)  #314 (line in Coconut source)

#### Real:

Real = Num  #317 (line in Coconut source)

if TYPE_CHECKING:  #319 (line in Coconut source)
    def toRational(real: 'Real') -> 'Rational':  #320 (line in Coconut source)
        ...  #321 (line in Coconut source)

else:  #322 (line in Coconut source)
    @_coconut_tco  #323 (line in Coconut source)
    @_coconut_mark_as_match  #323 (line in Coconut source)
    def toRational(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #323 (line in Coconut source)
        _coconut_match_check_10 = False  #323 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #323 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #323 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #323 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #323 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #323 (line in Coconut source)
            _coconut_match_temp_27 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #323 (line in Coconut source)
            if (isinstance)(_coconut_match_temp_27, float):  #323 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_27  #323 (line in Coconut source)
                if not _coconut_match_kwargs:  #323 (line in Coconut source)
                    _coconut_match_check_10 = True  #323 (line in Coconut source)
        if _coconut_match_check_10:  #323 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #323 (line in Coconut source)
                real = _coconut_match_set_name_real  #323 (line in Coconut source)
        if not _coconut_match_check_10:  #323 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #323 (line in Coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #324 (line in Coconut source)

    try:  #325 (line in Coconut source)
        _coconut_addpattern_6 = _coconut_addpattern(toRational)  # type: ignore  #325 (line in Coconut source)
    except _coconut.NameError:  #325 (line in Coconut source)
        _coconut_addpattern_6 = lambda f: f  #325 (line in Coconut source)
    @_coconut_addpattern_6  #325 (line in Coconut source)
    @_coconut_tco  #325 (line in Coconut source)
    @_coconut_mark_as_match  #325 (line in Coconut source)
    def toRational(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #325 (line in Coconut source)
        _coconut_match_check_11 = False  #325 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #325 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #325 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #325 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #325 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #325 (line in Coconut source)
            _coconut_match_temp_28 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #325 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_match_temp_28  #325 (line in Coconut source)
            if not _coconut_match_kwargs:  #325 (line in Coconut source)
                _coconut_match_check_11 = True  #325 (line in Coconut source)
        if _coconut_match_check_11:  #325 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #325 (line in Coconut source)
                real = _coconut_match_set_name_real  #325 (line in Coconut source)
        if not _coconut_match_check_11:  #325 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #325 (line in Coconut source)

        return _coconut_tail_call(Rational, real)  #326 (line in Coconut source)

#### Integral:

Integral = int  #329 (line in Coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #331 (line in Coconut source)
    divxy = x // y  #332 (line in Coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #333 (line in Coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #335 (line in Coconut source)
    modxy = x % y  #336 (line in Coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #337 (line in Coconut source)


div = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #339 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #339 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #339 (line in Coconut source)
__annotations__["div"] = '_coconut.typing.Callable[[int, int], int]'  #339 (line in Coconut source)
div = (_coconut.operator.floordiv)  #340 (line in Coconut source)

mod = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #342 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #342 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #342 (line in Coconut source)
__annotations__["mod"] = '_coconut.typing.Callable[[int, int], int]'  #342 (line in Coconut source)
mod = (_coconut.operator.mod)  #343 (line in Coconut source)

def quotRem(x: 'int', y: 'int') -> '(_coconut.typing.Tuple[int, int])':  #345 (line in Coconut source)
    divxy, modxy = divmod(x, y)  #346 (line in Coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #347 (line in Coconut source)
    return (divxy + adj, modxy - y * adj)  #348 (line in Coconut source)


divMod = divmod  #350 (line in Coconut source)

toInteger = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Integer]  #352 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #352 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #352 (line in Coconut source)
__annotations__["toInteger"] = '_coconut.typing.Callable[[Integral], Integer]'  #352 (line in Coconut source)
toInteger = _int  #353 (line in Coconut source)

#### Fractional:
Fractional = Rational  #356 (line in Coconut source)

recip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Fractional], Fractional]  #358 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #358 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #358 (line in Coconut source)
__annotations__["recip"] = '_coconut.typing.Callable[[Fractional], Fractional]'  #358 (line in Coconut source)
recip = (_coconut_partial(_coconut.operator.truediv, 1))  #359 (line in Coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #361 (line in Coconut source)
    return (x)  #361 (line in Coconut source)

#### Floating:

Floating = float  #364 (line in Coconut source)

from math import pi  # NOQA  #366 (line in Coconut source)
from math import exp  # NOQA  #366 (line in Coconut source)
from math import log  # NOQA  #366 (line in Coconut source)
from math import sqrt  # NOQA  #366 (line in Coconut source)
from math import sin  # NOQA  #366 (line in Coconut source)
from math import cos  # NOQA  #366 (line in Coconut source)
from math import tan  # NOQA  #366 (line in Coconut source)
from math import asin  # NOQA  #366 (line in Coconut source)
from math import acos  # NOQA  #366 (line in Coconut source)
from math import atan  # NOQA  #366 (line in Coconut source)
from math import sinh  # NOQA  #366 (line in Coconut source)
from math import cosh  # NOQA  #366 (line in Coconut source)
from math import tanh  # NOQA  #366 (line in Coconut source)
from math import asinh  # NOQA  #366 (line in Coconut source)
from math import acosh  # NOQA  #366 (line in Coconut source)
from math import atanh  # NOQA  #366 (line in Coconut source)

@_coconut_tco  #385 (line in Coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #385 (line in Coconut source)
    return _coconut_tail_call(log, x, base)  #386 (line in Coconut source)

#### RealFrac:

RealFrac = Rational  #389 (line in Coconut source)

def properFraction(x: 'RealFrac') -> '(_coconut.typing.Tuple[int, RealFrac])':  #391 (line in Coconut source)
    floor_x = floor(x)  #392 (line in Coconut source)
    return (floor_x, x - floor_x)  #393 (line in Coconut source)


truncate = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #395 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #395 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #395 (line in Coconut source)
__annotations__["truncate"] = '_coconut.typing.Callable[[RealFrac], int]'  #395 (line in Coconut source)
truncate = _int  #396 (line in Coconut source)

round = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #398 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #398 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #398 (line in Coconut source)
__annotations__["round"] = '_coconut.typing.Callable[[RealFrac], int]'  #398 (line in Coconut source)
round = _round  #399 (line in Coconut source)

ceiling = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #401 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #401 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #401 (line in Coconut source)
__annotations__["ceiling"] = '_coconut.typing.Callable[[RealFrac], int]'  #401 (line in Coconut source)
ceiling = _ceil  #402 (line in Coconut source)

floor = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[RealFrac], int]  #404 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #404 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #404 (line in Coconut source)
__annotations__["floor"] = '_coconut.typing.Callable[[RealFrac], int]'  #404 (line in Coconut source)
floor = _floor  #405 (line in Coconut source)

#### RealFloat:
RealFloat = float  #408 (line in Coconut source)

def floatRadix(x: 'float') -> 'int':  #410 (line in Coconut source)
    return (2)  #410 (line in Coconut source)


def floatDigits(x: 'float') -> 'int':  #412 (line in Coconut source)
    return (53)  #412 (line in Coconut source)


def floatRange(x: 'float') -> '(_coconut.typing.Tuple[int, int])':  #414 (line in Coconut source)
    return ((-1021, 1024))  #414 (line in Coconut source)


decodeFloat = NotImplemented  #416 (line in Coconut source)

encodeFloat = NotImplemented  #418 (line in Coconut source)

exponent = NotImplemented  #420 (line in Coconut source)

significand = NotImplemented  #422 (line in Coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #424 (line in Coconut source)
    return (x * 2**power)  #425 (line in Coconut source)

# NOQA
from math import isnan as isNaN  # NOQA  #427 (line in Coconut source)
from math import isinf as isInfinite  # NOQA  #427 (line in Coconut source)
from math import atan2  # NOQA  #427 (line in Coconut source)

isDenormalized = NotImplemented  #433 (line in Coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #435 (line in Coconut source)
    return (x == 0 and str(x).startswith("-"))  #436 (line in Coconut source)


def isIEEE(x: 'float') -> 'bool':  #438 (line in Coconut source)
    return (True)  #438 (line in Coconut source)


### Numeric functions:

def subtract(x, y):  #442 (line in Coconut source)
    return (y - x)  #443 (line in Coconut source)


def even(x: 'int') -> 'bool':  #445 (line in Coconut source)
    return (x % 2 == 0)  #446 (line in Coconut source)


def odd(x: 'int') -> 'bool':  #448 (line in Coconut source)
    return (x % 2 == 1)  #449 (line in Coconut source)


gcd = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[int, int], int]  #451 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #451 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #451 (line in Coconut source)
__annotations__["gcd"] = '_coconut.typing.Callable[[int, int], int]'  #451 (line in Coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #452 (line in Coconut source)

if TYPE_CHECKING:  #454 (line in Coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #455 (line in Coconut source)
        ...  #456 (line in Coconut source)

else:  #457 (line in Coconut source)
    @_coconut_mark_as_match  #458 (line in Coconut source)
    def lcm(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #458 (line in Coconut source)
        _coconut_match_check_12 = False  #458 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #458 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #458 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #458 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #458 (line in Coconut source)
            if _coconut_match_args[1] == 0:  #458 (line in Coconut source)
                if not _coconut_match_kwargs:  #458 (line in Coconut source)
                    _coconut_match_check_12 = True  #458 (line in Coconut source)
        if not _coconut_match_check_12:  #458 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #458 (line in Coconut source)

        return (0)  #458 (line in Coconut source)

    try:  #459 (line in Coconut source)
        _coconut_addpattern_7 = _coconut_addpattern(lcm)  # type: ignore  #459 (line in Coconut source)
    except _coconut.NameError:  #459 (line in Coconut source)
        _coconut_addpattern_7 = lambda f: f  #459 (line in Coconut source)
    @_coconut_addpattern_7  #459 (line in Coconut source)
    @_coconut_mark_as_match  #459 (line in Coconut source)
    def lcm(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #459 (line in Coconut source)
        _coconut_match_check_13 = False  #459 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #459 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #459 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #459 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #459 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #459 (line in Coconut source)
                if not _coconut_match_kwargs:  #459 (line in Coconut source)
                    _coconut_match_check_13 = True  #459 (line in Coconut source)
        if not _coconut_match_check_13:  #459 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #459 (line in Coconut source)

        return (0)  #459 (line in Coconut source)

    try:  #460 (line in Coconut source)
        _coconut_addpattern_8 = _coconut_addpattern(lcm)  # type: ignore  #460 (line in Coconut source)
    except _coconut.NameError:  #460 (line in Coconut source)
        _coconut_addpattern_8 = lambda f: f  #460 (line in Coconut source)
    @_coconut_addpattern_8  #460 (line in Coconut source)
    @_coconut_mark_as_match  #460 (line in Coconut source)
    def lcm(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #460 (line in Coconut source)
        _coconut_match_check_14 = False  #460 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #460 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #460 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #460 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #460 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #460 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #460 (line in Coconut source)
            _coconut_match_temp_29 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #460 (line in Coconut source)
            _coconut_match_temp_30 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #460 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_29  #460 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_30  #460 (line in Coconut source)
            if not _coconut_match_kwargs:  #460 (line in Coconut source)
                _coconut_match_check_14 = True  #460 (line in Coconut source)
        if _coconut_match_check_14:  #460 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #460 (line in Coconut source)
                x = _coconut_match_set_name_x  #460 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #460 (line in Coconut source)
                y = _coconut_match_set_name_y  #460 (line in Coconut source)
        if not _coconut_match_check_14:  #460 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #460 (line in Coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #461 (line in Coconut source)


fromIntegral = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Integral], Num]  #463 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #463 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #463 (line in Coconut source)
__annotations__["fromIntegral"] = '_coconut.typing.Callable[[Integral], Num]'  #463 (line in Coconut source)
fromIntegral = fromInteger  #464 (line in Coconut source)

realToFrac = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Real], Fractional]  #466 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #466 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #466 (line in Coconut source)
__annotations__["realToFrac"] = '_coconut.typing.Callable[[Real], Fractional]'  #466 (line in Coconut source)
realToFrac = toRational  #467 (line in Coconut source)



## Monoids:
Monoid = T.Iterable  #472 (line in Coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #473 (line in Coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #475 (line in Coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #478 (line in Coconut source)
    __slots__ = ()  #479 (line in Coconut source)
    _coconut_is_data = True  #479 (line in Coconut source)
    __match_args__ = ()  #479 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #479 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #479 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #479 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #479 (line in Coconut source)
    def __eq__(self, other):  #479 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #479 (line in Coconut source)
    def __hash__(self):  #479 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #479 (line in Coconut source)
    @staticmethod  #479 (line in Coconut source)
    @_coconut_tco  #480 (line in Coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #480 (line in Coconut source)
        if (hasattr)(M, "__mempty__"):  #481 (line in Coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #482 (line in Coconut source)
        return _coconut_tail_call(makedata, type(M))  #483 (line in Coconut source)


_coconut_call_set_names(Mempty)  #485 (line in Coconut source)
mempty = Mempty()  # type: T.Any  #485 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #485 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #485 (line in Coconut source)
__annotations__["mempty"] = 'T.Any'  #485 (line in Coconut source)

@_coconut_tco  #487 (line in Coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #487 (line in Coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #492 (line in Coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #494 (line in Coconut source)
    y = (asTypeOf)(y, x)  #495 (line in Coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #498 (line in Coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #499 (line in Coconut source)

# Default implementation
    if not x:  #502 (line in Coconut source)
        return (y)  #503 (line in Coconut source)
    if not y:  #504 (line in Coconut source)
        return (x)  #505 (line in Coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #506 (line in Coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #507 (line in Coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #508 (line in Coconut source)


@_coconut_tco  #510 (line in Coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #510 (line in Coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #511 (line in Coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #518 (line in Coconut source)

@_coconut_tco  # type: ignore  #520 (line in Coconut source)
def fmap(f: '_coconut.typing.Callable[[Ta], Tb]', xs: 'Functor[Ta]') -> 'Functor[Tb]':  # type: ignore  #520 (line in Coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #523 (line in Coconut source)
    try:  #524 (line in Coconut source)
# Default implementation
        return (_fmap(f, xs))  #526 (line in Coconut source)

    except TypeError:  #528 (line in Coconut source)
# Function instance
        if callable(xs):  #530 (line in Coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #531 (line in Coconut source)

        raise  #533 (line in Coconut source)


@_coconut_tco  #535 (line in Coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #535 (line in Coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #539 (line in Coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #540 (line in Coconut source)

_coconut_op_U3c_U24 = fmapConst  #541 (line in Coconut source)

#### Applicative:
Applicative = Functor  #544 (line in Coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #545 (line in Coconut source)

if TYPE_CHECKING:  #547 (line in Coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #548 (line in Coconut source)
        ...  #549 (line in Coconut source)

else:  #550 (line in Coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #551 (line in Coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #555 (line in Coconut source)

        __slots__ = ()  #557 (line in Coconut source)
        _coconut_is_data = True  #557 (line in Coconut source)
        __match_args__ = ('val',)  #557 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #557 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #557 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #557 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #557 (line in Coconut source)
        def __eq__(self, other):  #557 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #557 (line in Coconut source)
        def __hash__(self):  #557 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #557 (line in Coconut source)
        def __join__(self) -> 'T.Any':  #557 (line in Coconut source)
            return (self.val)  #557 (line in Coconut source)


        def __call__(self, arg: 'T.Any') -> 'T.Any':  #559 (line in Coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #560 (line in Coconut source)
            return (self.val)  #561 (line in Coconut source)


        @_coconut_tco  #563 (line in Coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #563 (line in Coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #565 (line in Coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #566 (line in Coconut source)

            try:  #568 (line in Coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #570 (line in Coconut source)

            except TypeError:  #572 (line in Coconut source)
# Check for functions
                if callable(M):  #574 (line in Coconut source)
                    return _coconut_tail_call(const, self.val)  #575 (line in Coconut source)

# Fallback
                raise  #578 (line in Coconut source)


    _coconut_call_set_names(pure)  #580 (line in Coconut source)
@_coconut_tco  #580 (line in Coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #580 (line in Coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #587 (line in Coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #589 (line in Coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #590 (line in Coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #593 (line in Coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #594 (line in Coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  #597 (line in Coconut source)

_coconut_op_U3c_U2a_U3e = ap  #598 (line in Coconut source)

@_coconut_tco  #600 (line in Coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #600 (line in Coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #604 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #605 (line in Coconut source)

_coconut_op_U2a_U3e = seqAr  #606 (line in Coconut source)

@_coconut_tco  #608 (line in Coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #608 (line in Coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #612 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #613 (line in Coconut source)

_coconut_op_U3c_U2a = seqAl  #614 (line in Coconut source)

def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #616 (line in Coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #620 (line in Coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut_partial(_coconut_partial, func), f1), f2))  # type: ignore  #621 (line in Coconut source)

#### Monad:

Monad = Applicative  #624 (line in Coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #625 (line in Coconut source)

@_coconut_tco  #627 (line in Coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #627 (line in Coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #632 (line in Coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #633 (line in Coconut source)

_coconut_op_U3e_U3e_U3e_U3d = bind  #634 (line in Coconut source)

@_coconut_tco  #636 (line in Coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #636 (line in Coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #640 (line in Coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #641 (line in Coconut source)

_coconut_op_U3e_U3e_U3e = seqM  #642 (line in Coconut source)

return_ = pure  #644 (line in Coconut source)

if TYPE_CHECKING:  #646 (line in Coconut source)
    def fail(msg: 'str') -> 'T.Any':  #647 (line in Coconut source)
        ...  #648 (line in Coconut source)

else:  #649 (line in Coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #650 (line in Coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #653 (line in Coconut source)

        __slots__ = ()  #655 (line in Coconut source)
        _coconut_is_data = True  #655 (line in Coconut source)
        __match_args__ = ('msg',)  #655 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #655 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #655 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #655 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #655 (line in Coconut source)
        def __eq__(self, other):  #655 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #655 (line in Coconut source)
        def __hash__(self):  #655 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #655 (line in Coconut source)
        @staticmethod  #655 (line in Coconut source)
        def __bool__() -> 'bool':  #656 (line in Coconut source)
            return (False)  #656 (line in Coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #658 (line in Coconut source)
            return (self)  #658 (line in Coconut source)


        @_coconut_tco  #660 (line in Coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #660 (line in Coconut source)
            if (hasattr)(M, "__fail__"):  #661 (line in Coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #662 (line in Coconut source)
            return _coconut_tail_call(makedata, type(M))  #663 (line in Coconut source)

# sequence_ and mapM_ defined in Foldable


    _coconut_call_set_names(fail)  #667 (line in Coconut source)
@_coconut_tco  #667 (line in Coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #667 (line in Coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #671 (line in Coconut source)
    return _coconut_tail_call((bind), m, func)  #672 (line in Coconut source)

_coconut_op_U3d_U3c_U3c_U3c = bindFrom  #673 (line in Coconut source)

@_coconut_tco  #675 (line in Coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #675 (line in Coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #682 (line in Coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #684 (line in Coconut source)
    _coconut_match_check_15 = False  #684 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #684 (line in Coconut source)
        _coconut_match_check_15 = True  #684 (line in Coconut source)
    if _coconut_match_check_15:  #684 (line in Coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #685 (line in Coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #688 (line in Coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #691 (line in Coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #692 (line in Coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  #695 (line in Coconut source)
    _coconut_case_match_check_0 = False  #695 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #695 (line in Coconut source)
        _coconut_case_match_check_0 = True  #695 (line in Coconut source)
    if _coconut_case_match_check_0:  #695 (line in Coconut source)
        if not ms:  #699 (line in Coconut source)
            return (ms)  # type: ignore  #700 (line in Coconut source)
        vals = []  # type: ignore  #701 (line in Coconut source)
        fallback = ms  #702 (line in Coconut source)
        for m in (ms):  #703 (line in Coconut source)
            if m:  #704 (line in Coconut source)
                vals.extend(m)  # type: ignore  #705 (line in Coconut source)
            else:  #706 (line in Coconut source)
                fallback = m  # type: ignore  #707 (line in Coconut source)
        if not vals:  #708 (line in Coconut source)
            return (fallback)  # type: ignore  #709 (line in Coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  # type: ignore  #710 (line in Coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #713 (line in Coconut source)
        _coconut_case_match_check_0 = True  #713 (line in Coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #713 (line in Coconut source)
            _coconut_case_match_check_0 = False  #713 (line in Coconut source)
        if _coconut_case_match_check_0:  #713 (line in Coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #714 (line in Coconut source)

    if not _coconut_case_match_check_0:  #716 (line in Coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #717 (line in Coconut source)


if TYPE_CHECKING:  #719 (line in Coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]') -> 'TMonad':  #720 (line in Coconut source)
        ...  #721 (line in Coconut source)

else:  #722 (line in Coconut source)
    @_coconut_tco  #723 (line in Coconut source)
    @_coconut_mark_as_match  #723 (line in Coconut source)
    def do(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #723 (line in Coconut source)
        _coconut_match_check_16 = False  #723 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #723 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #723 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #723 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #723 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #723 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #723 (line in Coconut source)
                _coconut_match_temp_31 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #723 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_31  #723 (line in Coconut source)
                if not _coconut_match_kwargs:  #723 (line in Coconut source)
                    _coconut_match_check_16 = True  #723 (line in Coconut source)
        if _coconut_match_check_16:  #723 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #723 (line in Coconut source)
                func = _coconut_match_set_name_func  #723 (line in Coconut source)
        if not _coconut_match_check_16:  #723 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #723 (line in Coconut source)

        return _coconut_tail_call(func)  #723 (line in Coconut source)

    try:  #724 (line in Coconut source)
        _coconut_addpattern_9 = _coconut_addpattern(do)  # type: ignore  #724 (line in Coconut source)
    except _coconut.NameError:  #724 (line in Coconut source)
        _coconut_addpattern_9 = lambda f: f  #724 (line in Coconut source)
    @_coconut_addpattern_9  #724 (line in Coconut source)
    @_coconut_tco  #724 (line in Coconut source)
    @_coconut_mark_as_match  #724 (line in Coconut source)
    def do(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #724 (line in Coconut source)
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
        """  #743 (line in Coconut source)
        _coconut_match_check_17 = False  #744 (line in Coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #744 (line in Coconut source)
        _coconut_match_set_name_ms = _coconut_sentinel  #744 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #744 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #744 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #744 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #744 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #744 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #744 (line in Coconut source)
                _coconut_match_set_name_m = _coconut_match_args[0][0]  #744 (line in Coconut source)
                _coconut_match_temp_33 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #744 (line in Coconut source)
                _coconut_match_temp_32 = _coconut.list(_coconut_match_args[0][1:])  #744 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_33  #744 (line in Coconut source)
                _coconut_match_set_name_ms = _coconut_match_temp_32  #744 (line in Coconut source)
                if not _coconut_match_kwargs:  #744 (line in Coconut source)
                    _coconut_match_check_17 = True  #744 (line in Coconut source)
        if _coconut_match_check_17:  #744 (line in Coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #744 (line in Coconut source)
                m = _coconut_match_set_name_m  #744 (line in Coconut source)
            if _coconut_match_set_name_ms is not _coconut_sentinel:  #744 (line in Coconut source)
                ms = _coconut_match_set_name_ms  #744 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #744 (line in Coconut source)
                func = _coconut_match_set_name_func  #744 (line in Coconut source)
        if not _coconut_match_check_17:  #744 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #744 (line in Coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut_partial(func, x)))  #744 (line in Coconut source)



## Folds and traversals:

#### Foldable:

Foldable = T.Sequence  #751 (line in Coconut source)

@_coconut_tco  #753 (line in Coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #753 (line in Coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #754 (line in Coconut source)


mapM_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]  #756 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #756 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #756 (line in Coconut source)
__annotations__["mapM_"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #756 (line in Coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #757 (line in Coconut source)

@_coconut_tco  #759 (line in Coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #759 (line in Coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #760 (line in Coconut source)


@_coconut_tco  #762 (line in Coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #762 (line in Coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #763 (line in Coconut source)


@_coconut_tco  #765 (line in Coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #765 (line in Coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #766 (line in Coconut source)


foldl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]  #768 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #768 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #768 (line in Coconut source)
__annotations__["foldl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #768 (line in Coconut source)
foldl1 = reduce  #769 (line in Coconut source)

@_coconut_tco  #771 (line in Coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #771 (line in Coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #772 (line in Coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #774 (line in Coconut source)
    return (len(xs) == 0)  #775 (line in Coconut source)


length = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable], int]  #777 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #777 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #777 (line in Coconut source)
__annotations__["length"] = '_coconut.typing.Callable[[Foldable], int]'  #777 (line in Coconut source)
length = len  #778 (line in Coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #780 (line in Coconut source)
    return (e in xs)  #781 (line in Coconut source)


maximum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #783 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #783 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #783 (line in Coconut source)
__annotations__["maximum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #783 (line in Coconut source)
maximum = _max  #784 (line in Coconut source)

minimum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #786 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #786 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #786 (line in Coconut source)
__annotations__["minimum"] = '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #786 (line in Coconut source)
minimum = _min  #787 (line in Coconut source)

sum = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #789 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #789 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #789 (line in Coconut source)
__annotations__["sum"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #789 (line in Coconut source)
sum = _sum  #790 (line in Coconut source)

product = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #792 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #792 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #792 (line in Coconut source)
__annotations__["product"] = '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #792 (line in Coconut source)
product = _coconut_partial(reduce, _coconut.operator.mul)  #793 (line in Coconut source)

#### Traversable:
Traversable = T.Iterable  #796 (line in Coconut source)

@_coconut_tco  #798 (line in Coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #798 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #799 (line in Coconut source)


@_coconut_tco  #801 (line in Coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #801 (line in Coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #802 (line in Coconut source)


traverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]  #804 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #804 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #804 (line in Coconut source)
__annotations__["traverse"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #804 (line in Coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  # type: ignore  #805 (line in Coconut source)

sequence = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]  #807 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #807 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #807 (line in Coconut source)
__annotations__["sequence"] = '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #807 (line in Coconut source)
sequence = sequenceA  #808 (line in Coconut source)

mapM = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]  #810 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #810 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #810 (line in Coconut source)
__annotations__["mapM"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #810 (line in Coconut source)
mapM = traverse  #811 (line in Coconut source)



## Miscellaneous functions:
id = ident  # type: _coconut.typing.Callable[[Ta], Ta]  #816 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #816 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #816 (line in Coconut source)
__annotations__["id"] = '_coconut.typing.Callable[[Ta], Ta]'  #816 (line in Coconut source)

@_coconut_tco  #818 (line in Coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #818 (line in Coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #822 (line in Coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #823 (line in Coconut source)


if TYPE_CHECKING:  #825 (line in Coconut source)
    @T.overload  #826 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #827 (line in Coconut source)
        ...  #828 (line in Coconut source)

    @T.overload  #829 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #830 (line in Coconut source)
        ...  #831 (line in Coconut source)

    @T.overload  #832 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #833 (line in Coconut source)
        ...  #834 (line in Coconut source)

    @T.overload  #835 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta') -> 'T.Any':  #836 (line in Coconut source)
        ...  #837 (line in Coconut source)

    def apply(func, arg):  #838 (line in Coconut source)
        ...  #839 (line in Coconut source)

else:  #840 (line in Coconut source)
    @_coconut_tco  #841 (line in Coconut source)
    def apply(func, arg):  #841 (line in Coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #847 (line in Coconut source)
        return _coconut_tail_call((of), func, arg)  #848 (line in Coconut source)

_coconut_op_U24_U24 = apply  #849 (line in Coconut source)

@_coconut_tco  #851 (line in Coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #851 (line in Coconut source)
    while True:  #852 (line in Coconut source)
        if cond(x):  #852 (line in Coconut source)
            return (x)  #853 (line in Coconut source)
        try:  # tail recursive  #854 (line in Coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_65  # type: ignore  # tail recursive  #854 (line in Coconut source)
        except _coconut.NameError:  # tail recursive  #854 (line in Coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #854 (line in Coconut source)
        if _coconut_tre_check_0:  # tail recursive  #854 (line in Coconut source)
            (cond, func, x,) = (cond, func, func(x),)  # tail recursive  #854 (line in Coconut source)
            continue  # tail recursive  #854 (line in Coconut source)
        else:  # tail recursive  #854 (line in Coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #855 (line in Coconut source)
        return None  #856 (line in Coconut source)

_coconut_recursive_func_65 = until  #856 (line in Coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #856 (line in Coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #860 (line in Coconut source)
    if TYPE_CHECKING:  #861 (line in Coconut source)
        return (x)  #861 (line in Coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #863 (line in Coconut source)
        for i in ((takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count())):  #864 (line in Coconut source)
            if (isinstance)(x, pure):  #865 (line in Coconut source)
                x = x.pure_as(y)  #866 (line in Coconut source)
            elif (isinstance)(x, fail):  #867 (line in Coconut source)
                x = x.fail_as(y)  #868 (line in Coconut source)
            elif (isinstance)(x, Mempty):  #869 (line in Coconut source)
                x = x.mempty_as(y)  #870 (line in Coconut source)
            else:  #871 (line in Coconut source)
                break  #872 (line in Coconut source)
    return (x)  #873 (line in Coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #875 (line in Coconut source)

def error(msg: 'str') -> 'None':  #877 (line in Coconut source)
    raise Exception(msg)  #878 (line in Coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #880 (line in Coconut source)
    raise Exception(msg) from None  #881 (line in Coconut source)


undefined = None  # type: T.Any  #883 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #883 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #883 (line in Coconut source)
__annotations__["undefined"] = 'T.Any'  #883 (line in Coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #885 (line in Coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #888 (line in Coconut source)
    return (y)  #889 (line in Coconut source)


@_coconut_tco  #891 (line in Coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #891 (line in Coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #896 (line in Coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #897 (line in Coconut source)




# List operations:

@_coconut_tco  #903 (line in Coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #903 (line in Coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #907 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #908 (line in Coconut source)

# type: ignore
map = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]  # type: ignore  #910 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #910 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #910 (line in Coconut source)
__annotations__["map"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #910 (line in Coconut source)
map = _map  # type: ignore  #911 (line in Coconut source)

@_coconut_tco  #913 (line in Coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #913 (line in Coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #917 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #918 (line in Coconut source)

_coconut_op_U2b_U2b = chain  #919 (line in Coconut source)

filter = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  # type: ignore  #921 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #921 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #921 (line in Coconut source)
__annotations__["filter"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #921 (line in Coconut source)
filter = _filter  # type: ignore  #922 (line in Coconut source)

head = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #924 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #924 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #924 (line in Coconut source)
__annotations__["head"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #924 (line in Coconut source)
head = _coconut_partial(_coconut_iter_getitem, index=(0))  #925 (line in Coconut source)

last = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #927 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #927 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #927 (line in Coconut source)
__annotations__["last"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #927 (line in Coconut source)
last = _coconut_partial(_coconut_iter_getitem, index=(-1))  #928 (line in Coconut source)

tail = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #930 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #930 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #930 (line in Coconut source)
__annotations__["tail"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #930 (line in Coconut source)
tail = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #931 (line in Coconut source)

init = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #933 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #933 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #933 (line in Coconut source)
__annotations__["init"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #933 (line in Coconut source)
init = _coconut_partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #934 (line in Coconut source)

@_coconut_tco  #936 (line in Coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #936 (line in Coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #940 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #941 (line in Coconut source)

_coconut_op_U21_U21 = at  #942 (line in Coconut source)

reverse = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]  #944 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #944 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #944 (line in Coconut source)
__annotations__["reverse"] = '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #944 (line in Coconut source)
reverse = _reversed  #945 (line in Coconut source)



## Special folds:
and_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #950 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #950 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #950 (line in Coconut source)
__annotations__["and_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #950 (line in Coconut source)
and_ = _all  #951 (line in Coconut source)

or_ = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Foldable[bool]], bool]  #953 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #953 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #953 (line in Coconut source)
__annotations__["or_"] = '_coconut.typing.Callable[[Foldable[bool]], bool]'  #953 (line in Coconut source)
or_ = _any  #954 (line in Coconut source)

any = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #956 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #956 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #956 (line in Coconut source)
__annotations__["any"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #956 (line in Coconut source)
any = _coconut_forward_compose(map, or_)  #957 (line in Coconut source)

all = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #959 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #959 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #959 (line in Coconut source)
__annotations__["all"] = '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #959 (line in Coconut source)
all = _coconut_forward_compose(map, and_)  #960 (line in Coconut source)

@_coconut_tco  #962 (line in Coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #962 (line in Coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #963 (line in Coconut source)


concatMap = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]  #965 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #965 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #965 (line in Coconut source)
__annotations__["concatMap"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #965 (line in Coconut source)
concatMap = _coconut_forward_compose(map, concat)  #966 (line in Coconut source)



## Building lists:

### Scans:
@_coconut_tco  #973 (line in Coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #973 (line in Coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #974 (line in Coconut source)


scanl1 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #976 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #976 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #976 (line in Coconut source)
__annotations__["scanl1"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #976 (line in Coconut source)
scanl1 = scan  #977 (line in Coconut source)

@_coconut_tco  #979 (line in Coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #979 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #980 (line in Coconut source)


@_coconut_tco  #982 (line in Coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #982 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #983 (line in Coconut source)

### Infinite lists:

@recursive_generator  #986 (line in Coconut source)
@_coconut_tco  #987 (line in Coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #987 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #988 (line in Coconut source)


@recursive_generator  #990 (line in Coconut source)
@_coconut_tco  #991 (line in Coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #991 (line in Coconut source)
    return _coconut_tail_call(_coconut_flatten, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #992 (line in Coconut source)


@_coconut_tco  #994 (line in Coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #994 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #995 (line in Coconut source)


if TYPE_CHECKING:  #997 (line in Coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  # type: ignore  #998 (line in Coconut source)
        ...  #999 (line in Coconut source)

else:  #1000 (line in Coconut source)
    @recursive_generator  #1001 (line in Coconut source)
    @_coconut_tco  #1002 (line in Coconut source)
    @_coconut_mark_as_match  #1002 (line in Coconut source)
    def cycle(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1002 (line in Coconut source)
        _coconut_match_check_18 = False  #1002 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1002 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1002 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1002 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1002 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #1002 (line in Coconut source)
            _coconut_match_temp_34 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #1002 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_34  #1002 (line in Coconut source)
            if not _coconut_match_kwargs:  #1002 (line in Coconut source)
                _coconut_match_check_18 = True  #1002 (line in Coconut source)
        if _coconut_match_check_18:  #1002 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1002 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1002 (line in Coconut source)
        if _coconut_match_check_18 and not (len(xs) > 0):  #1002 (line in Coconut source)
            _coconut_match_check_18 = False  #1002 (line in Coconut source)
        if not _coconut_match_check_18:  #1002 (line in Coconut source)
            raise _coconut_FunctionMatchError('def \\cycle(xs if len(xs) > 0) =', _coconut_match_args)  #1002 (line in Coconut source)

        return _coconut_tail_call(_cycle, xs)  #1003 (line in Coconut source)



## Sublists:

@_coconut_tco  #1008 (line in Coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1008 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #1009 (line in Coconut source)


@_coconut_tco  #1011 (line in Coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #1011 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #1012 (line in Coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]])':  #1014 (line in Coconut source)
    reit = reiterable(xs)  #1015 (line in Coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #1016 (line in Coconut source)


takeWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1018 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1018 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1018 (line in Coconut source)
__annotations__["takeWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1018 (line in Coconut source)
takeWhile = takewhile  #1019 (line in Coconut source)

dropWhile = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1021 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1021 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1021 (line in Coconut source)
__annotations__["dropWhile"] = '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #1021 (line in Coconut source)
dropWhile = dropwhile  #1022 (line in Coconut source)

if TYPE_CHECKING:  #1024 (line in Coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]])':  #1025 (line in Coconut source)
        ...  #1026 (line in Coconut source)

else:  #1027 (line in Coconut source)
    @_coconut_mark_as_match  #1028 (line in Coconut source)
    def span(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1028 (line in Coconut source)
        _coconut_match_check_19 = False  #1028 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1028 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1028 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1028 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #1028 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1028 (line in Coconut source)
                if not _coconut_match_kwargs:  #1028 (line in Coconut source)
                    _coconut_match_check_19 = True  #1028 (line in Coconut source)
        if not _coconut_match_check_19:  #1028 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #1028 (line in Coconut source)

        return (([], []))  #1028 (line in Coconut source)

    try:  #1029 (line in Coconut source)
        _coconut_addpattern_10 = _coconut_addpattern(span)  # type: ignore  #1029 (line in Coconut source)
    except _coconut.NameError:  #1029 (line in Coconut source)
        _coconut_addpattern_10 = lambda f: f  #1029 (line in Coconut source)
    @_coconut_addpattern_10  #1029 (line in Coconut source)
    @_coconut_mark_as_match  #1029 (line in Coconut source)
    def span(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1029 (line in Coconut source)
        _coconut_match_check_20 = False  #1029 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1029 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #1029 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1029 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1029 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1029 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1029 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1029 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1029 (line in Coconut source)
                _coconut_match_temp_35 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1029 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_args[1][0]  #1029 (line in Coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_35  #1029 (line in Coconut source)
                _coconut_match_temp_36 = _coconut.list(_coconut_match_args[1][1:])  #1029 (line in Coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_36  #1029 (line in Coconut source)
                if not _coconut_match_kwargs:  #1029 (line in Coconut source)
                    _coconut_match_check_20 = True  #1029 (line in Coconut source)
        if _coconut_match_check_20:  #1029 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1029 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1029 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #1029 (line in Coconut source)
                x = _coconut_match_set_name_x  #1029 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1029 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1029 (line in Coconut source)
        if _coconut_match_check_20 and not (cond(x)):  #1029 (line in Coconut source)
            _coconut_match_check_20 = False  #1029 (line in Coconut source)
        if not _coconut_match_check_20:  #1029 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #1029 (line in Coconut source)

        ys, zs = span(cond, xs)  #1030 (line in Coconut source)
        return (([x,] + ys, zs))  #1031 (line in Coconut source)

    try:  #1032 (line in Coconut source)
        _coconut_addpattern_11 = _coconut_addpattern(span)  # type: ignore  #1032 (line in Coconut source)
    except _coconut.NameError:  #1032 (line in Coconut source)
        _coconut_addpattern_11 = lambda f: f  #1032 (line in Coconut source)
    @_coconut_addpattern_11  #1032 (line in Coconut source)
    @_coconut_mark_as_match  #1032 (line in Coconut source)
    def span(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #1032 (line in Coconut source)
        _coconut_match_check_21 = False  #1032 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1032 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1032 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1032 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #1032 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #1032 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1032 (line in Coconut source)
            _coconut_match_temp_37 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1032 (line in Coconut source)
            _coconut_match_temp_38 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1032 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_match_temp_37  #1032 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_38  #1032 (line in Coconut source)
            if not _coconut_match_kwargs:  #1032 (line in Coconut source)
                _coconut_match_check_21 = True  #1032 (line in Coconut source)
        if _coconut_match_check_21:  #1032 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1032 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1032 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1032 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1032 (line in Coconut source)
        if not _coconut_match_check_21:  #1032 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #1032 (line in Coconut source)

        return (([], xs))  #1033 (line in Coconut source)


@_coconut_tco  #1035 (line in Coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #1035 (line in Coconut source)
    """
    break_ = break
    """  #1038 (line in Coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1039 (line in Coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #1044 (line in Coconut source)
    return (e not in xs)  #1045 (line in Coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> 'Maybe':  #1047 (line in Coconut source)
    try:  #1048 (line in Coconut source)
        return (((Just)((_coconut_iter_getitem(((dropwhile)(lambda pair: pair[0] != key, assocs)), (0)))[1])))  #1049 (line in Coconut source)
    except IndexError:  #1056 (line in Coconut source)
        return (nothing)  #1057 (line in Coconut source)



## Zipping and unzipping lists:
# type: ignore
zip = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]  # type: ignore  #1062 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  # type: ignore  #1062 (line in Coconut source)
    __annotations__ = {}  # type: ignore  # type: ignore  #1062 (line in Coconut source)
__annotations__["zip"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]]'  # type: ignore  #1062 (line in Coconut source)
zip = _zip  # type: ignore  #1063 (line in Coconut source)

zip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]  #1065 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1065 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1065 (line in Coconut source)
__annotations__["zip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]]'  #1065 (line in Coconut source)
zip3 = _zip  #1066 (line in Coconut source)

@_coconut_tco  #1068 (line in Coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #1068 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2)  #1069 (line in Coconut source)


@_coconut_tco  #1071 (line in Coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1071 (line in Coconut source)
    return _coconut_tail_call(_map, func, xs1, xs2, xs3)  #1072 (line in Coconut source)


@_coconut_tco  #1074 (line in Coconut source)
def unzip(xs: '_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb])]') -> '(_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]])':  #1074 (line in Coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1075 (line in Coconut source)


unzip3 = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]  #1077 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1077 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1077 (line in Coconut source)
__annotations__["unzip3"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[(_coconut.typing.Tuple[Ta, Tb, Tc])]], (_coconut.typing.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]])]'  #1077 (line in Coconut source)
unzip3 = unzip  # type: ignore  #1078 (line in Coconut source)



## Functions on strings:
lines = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1083 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1083 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1083 (line in Coconut source)
__annotations__["lines"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1083 (line in Coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1084 (line in Coconut source)

words = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1086 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1086 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1086 (line in Coconut source)
__annotations__["words"] = '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1086 (line in Coconut source)
words = _coconut.operator.methodcaller("split")  #1087 (line in Coconut source)

@_coconut_tco  #1089 (line in Coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1089 (line in Coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1090 (line in Coconut source)


unwords = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]  #1092 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1092 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1092 (line in Coconut source)
__annotations__["unwords"] = '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1092 (line in Coconut source)
unwords = " ".join  #1093 (line in Coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1101 (line in Coconut source)

Show = T.Any  #1103 (line in Coconut source)

showsPrec = NotImplemented  #1105 (line in Coconut source)

show = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Ta], str]  #1107 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1107 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1107 (line in Coconut source)
__annotations__["show"] = '_coconut.typing.Callable[[Ta], str]'  #1107 (line in Coconut source)
show = repr  #1108 (line in Coconut source)

def shows(x: 'Show') -> 'ShowS':  #1110 (line in Coconut source)
    return (lambda s: repr(x) + s)  #1111 (line in Coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1113 (line in Coconut source)
    return (lambda s: repr(list(xs)) + s)  #1114 (line in Coconut source)


def showString(x: 'str') -> 'ShowS':  #1116 (line in Coconut source)
    return (lambda s: x + s)  #1117 (line in Coconut source)


showChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], ShowS]  #1119 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1119 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1119 (line in Coconut source)
__annotations__["showChar"] = '_coconut.typing.Callable[[Char], ShowS]'  #1119 (line in Coconut source)
showChar = showString  #1120 (line in Coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1122 (line in Coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1123 (line in Coconut source)



## Converting from String:

ReadS = NotImplemented  #1131 (line in Coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1133 (line in Coconut source)

readsPrec = NotImplemented  #1144 (line in Coconut source)

readList = NotImplemented  #1146 (line in Coconut source)

reads = NotImplemented  #1148 (line in Coconut source)

readParen = NotImplemented  #1150 (line in Coconut source)

@_coconut_tco  #1152 (line in Coconut source)
def read(s: 'str') -> 'Read':  #1152 (line in Coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1153 (line in Coconut source)


lex = NotImplemented  #1155 (line in Coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1163 (line in Coconut source)
    __slots__ = ()  #1163 (line in Coconut source)
    _coconut_is_data = True  #1163 (line in Coconut source)
    __match_args__ = ('io_func',)  #1163 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1163 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1163 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1163 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #1163 (line in Coconut source)
    def __eq__(self, other):  #1163 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1163 (line in Coconut source)
    def __hash__(self):  #1163 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1163 (line in Coconut source)
    @staticmethod  #1164 (line in Coconut source)
    @_coconut_tco  #1165 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1165 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1166 (line in Coconut source)


    @staticmethod  #1168 (line in Coconut source)
    @_coconut_tco  #1169 (line in Coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1169 (line in Coconut source)
        def _coconut_lambda_0():  #1170 (line in Coconut source)
            raise IOError(msg)  #1170 (line in Coconut source)

        return _coconut_tail_call(IO, _coconut_lambda_0)  #1170 (line in Coconut source)


    @_coconut_tco  #1172 (line in Coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1172 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1173 (line in Coconut source)


    @_coconut_tco  #1175 (line in Coconut source)
    def __join__(self) -> 'IO':  #1175 (line in Coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1176 (line in Coconut source)


    @staticmethod  #1178 (line in Coconut source)
    @_coconut_tco  #1179 (line in Coconut source)
    def __mempty__() -> 'IO':  #1179 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1180 (line in Coconut source)


    @_coconut_tco  #1182 (line in Coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1182 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1183 (line in Coconut source)


_coconut_call_set_names(IO)  #1185 (line in Coconut source)
_nullIO = IO(lambda: None)  # type: IO  #1185 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1185 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1185 (line in Coconut source)
__annotations__["_nullIO"] = 'IO'  #1185 (line in Coconut source)

@_coconut_tco  #1187 (line in Coconut source)
def asIO(io: 'IO') -> 'IO':  #1187 (line in Coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1192 (line in Coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1193 (line in Coconut source)


@_coconut_tco  #1195 (line in Coconut source)
def unIO(io: 'IO') -> 'T.Any':  #1195 (line in Coconut source)
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
    """  #1209 (line in Coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1210 (line in Coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1218 (line in Coconut source)
def putStr(s: 'str') -> 'IO':  #1218 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s, end=""))  #1219 (line in Coconut source)


putChar = _coconut.typing.cast(_coconut.typing.Any, ...)  # type: _coconut.typing.Callable[[Char], IO]  #1221 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1221 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1221 (line in Coconut source)
__annotations__["putChar"] = '_coconut.typing.Callable[[Char], IO]'  #1221 (line in Coconut source)
putChar = putStr  #1222 (line in Coconut source)

@_coconut_tco  #1224 (line in Coconut source)
def putStrLn(s: 'str') -> 'IO':  #1224 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, s))  #1225 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1227 (line in Coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1227 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(_print, show(x)))  #1228 (line in Coconut source)


### Input functions:

getChar = IO(_coconut_partial(sys.stdin.read, 1))  # type: IO  #1232 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1232 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1232 (line in Coconut source)
__annotations__["getChar"] = 'IO'  #1232 (line in Coconut source)

getLine = IO(input)  # type: IO  #1234 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1234 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1234 (line in Coconut source)
__annotations__["getLine"] = 'IO'  #1234 (line in Coconut source)

getContents = IO(sys.stdin.read)  # type: IO  #1236 (line in Coconut source)
if "__annotations__" not in _coconut.locals():  #1236 (line in Coconut source)
    __annotations__ = {}  # type: ignore  #1236 (line in Coconut source)
__annotations__["getContents"] = 'IO'  #1236 (line in Coconut source)

@_coconut_tco  #1238 (line in Coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1238 (line in Coconut source)
    def do_interact():  #1239 (line in Coconut source)
        while True:  #1240 (line in Coconut source)
            (_print)((func)(input()))  #1241 (line in Coconut source)

    return _coconut_tail_call(IO, do_interact)  #1242 (line in Coconut source)


### Files:

FilePath = str  #1246 (line in Coconut source)

@_coconut_tco  #1248 (line in Coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1248 (line in Coconut source)
    def do_readFile() -> 'str':  #1249 (line in Coconut source)
        with open(fpath, "r+") as f:  #1250 (line in Coconut source)
            return (f.read())  #1251 (line in Coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1252 (line in Coconut source)


@_coconut_tco  #1254 (line in Coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1254 (line in Coconut source)
    def do_writeFile() -> 'None':  #1255 (line in Coconut source)
        with open(fpath, "w+") as f:  #1256 (line in Coconut source)
            f.write(text)  #1257 (line in Coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1258 (line in Coconut source)


@_coconut_tco  #1260 (line in Coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1260 (line in Coconut source)
    def do_appendFile() -> 'None':  #1261 (line in Coconut source)
        with open(fpath, "a+") as f:  #1262 (line in Coconut source)
            f.write(text)  #1263 (line in Coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1264 (line in Coconut source)


@_coconut_tco  #1266 (line in Coconut source)
def readIO(s: 'str') -> 'IO':  #1266 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_partial(read, s))  #1267 (line in Coconut source)


@_coconut_tco  #1269 (line in Coconut source)
def readLn() -> 'IO':  #1269 (line in Coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1270 (line in Coconut source)



## Exception handling:

@_coconut_tco  #1275 (line in Coconut source)
def ioError(err: 'IOError') -> 'IO':  #1275 (line in Coconut source)
    def _coconut_lambda_1():  #1276 (line in Coconut source)
        raise err  #1276 (line in Coconut source)

    return _coconut_tail_call(IO, _coconut_lambda_1)  #1276 (line in Coconut source)


@_coconut_tco  #1278 (line in Coconut source)
def userError(msg: 'str') -> 'IOError':  #1278 (line in Coconut source)
    return _coconut_tail_call(IOError, msg)  #1279 (line in Coconut source)
