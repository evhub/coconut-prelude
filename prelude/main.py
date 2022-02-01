#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x5c775d13

# Compiled with Coconut version 2.0.0-a_dev38 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == "__coconut__":
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == "__coconut__":
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Helpers:

#### Imports:
sys = _coconut_sys  #4 (line num in coconut source)
import fractions as _fractions  #5 (line num in coconut source)
import math as _math  #6 (line num in coconut source)
import ast as _ast  #7 (line num in coconut source)
from math import gcd as _gcd  #8 (line num in coconut source)

from prelude.util import *  # type: ignore  #10 (line num in coconut source)

#### Untyped built-ins:
_max: '_coconut.typing.Callable[..., T.Any]' = max  #13 (line num in coconut source)
_min: '_coconut.typing.Callable[..., T.Any]' = min  #14 (line num in coconut source)
_zip: '_coconut.typing.Callable[..., T.Any]' = zip  #15 (line num in coconut source)
_abs: '_coconut.typing.Callable[..., T.Any]' = abs  #16 (line num in coconut source)
_round: '_coconut.typing.Callable[..., T.Any]' = round  #17 (line num in coconut source)
_fmap: '_coconut.typing.Callable[..., T.Any]' = fmap  #18 (line num in coconut source)
_reduce: '_coconut.typing.Callable[..., T.Any]' = reduce  #19 (line num in coconut source)
_all: '_coconut.typing.Callable[..., T.Any]' = all  #20 (line num in coconut source)
_any: '_coconut.typing.Callable[..., T.Any]' = any  #21 (line num in coconut source)
_map: '_coconut.typing.Callable[..., T.Any]' = map  #22 (line num in coconut source)
_filter: '_coconut.typing.Callable[..., T.Any]' = filter  #23 (line num in coconut source)
_int: '_coconut.typing.Callable[..., T.Any]' = int  #24 (line num in coconut source)
_sum: '_coconut.typing.Callable[..., T.Any]' = sum  #25 (line num in coconut source)
_reversed: '_coconut.typing.Callable[..., T.Any]' = reversed  #26 (line num in coconut source)
_print: '_coconut.typing.Callable[..., T.Any]' = print  #27 (line num in coconut source)
_ceil: '_coconut.typing.Callable[..., T.Any]' = _math.ceil  #28 (line num in coconut source)
_floor: '_coconut.typing.Callable[..., T.Any]' = _math.floor  #29 (line num in coconut source)




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool  #39 (line num in coconut source)

not_: '_coconut.typing.Callable[[bool], bool]'  #41 (line num in coconut source)
not_ = (_coconut.operator.not_)  #42 (line num in coconut source)

otherwise: 'bool' = True  #44 (line num in coconut source)

#### Maybe:
class Maybe:  #47 (line num in coconut source)
    @staticmethod  #48 (line num in coconut source)
    @_coconut_tco  #49 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'Maybe':  #49 (line num in coconut source)
        return _coconut_tail_call(Just, x)  #49 (line num in coconut source)


    @staticmethod  #51 (line num in coconut source)
    def __fail__(msg: 'str') -> 'Maybe':  #52 (line num in coconut source)
        return (nothing)  #52 (line num in coconut source)


    @staticmethod  #54 (line num in coconut source)
    def __mempty__() -> 'Maybe':  #55 (line num in coconut source)
        return (nothing)  #55 (line num in coconut source)


class Nothing(_coconut.collections.namedtuple("Nothing", ()), Maybe):  #57 (line num in coconut source)
    """-- Nothing is the data type; use nothing for the canonical instance"""  #58 (line num in coconut source)

    _coconut_is_data = True  #60 (line num in coconut source)
    __slots__ = ()  #60 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #60 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #60 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #60 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #60 (line num in coconut source)
    def __eq__(self, other):  #60 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #60 (line num in coconut source)
    def __hash__(self):  #60 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #60 (line num in coconut source)
    __match_args__ = ()  #60 (line num in coconut source)
nothing: 'Maybe' = Nothing()  #60 (line num in coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #62 (line num in coconut source)
    _coconut_is_data = True  #62 (line num in coconut source)
    __slots__ = ()  #62 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #62 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #62 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #62 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #62 (line num in coconut source)
    def __eq__(self, other):  #62 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #62 (line num in coconut source)
    def __hash__(self):  #62 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #62 (line num in coconut source)
    __match_args__ = ('x',)  #62 (line num in coconut source)

derivingOrd(Nothing, Just)  #64 (line num in coconut source)

if TYPE_CHECKING:  #66 (line num in coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #67 (line num in coconut source)
        ...  #68 (line num in coconut source)

else:  #69 (line num in coconut source)
    @_coconut_mark_as_match  #70 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #70 (line num in coconut source)
        _coconut_match_check_0 = False  #70 (line num in coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #70 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #70 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #70 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #70 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)   # type: ignore  #70 (line num in coconut source)
            _coconut_match_set_name_default = _coconut_match_temp_0  #70 (line num in coconut source)
            if not _coconut_match_kwargs:  #70 (line num in coconut source)
                _coconut_match_check_0 = True  #70 (line num in coconut source)
        if _coconut_match_check_0:  #70 (line num in coconut source)
            _coconut_match_check_0 = False  #70 (line num in coconut source)
            if not _coconut_match_check_0:  #70 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)) and (_coconut.len(_coconut_match_args[2]) == 0):  #70 (line num in coconut source)
                    _coconut_match_check_0 = True  #70 (line num in coconut source)

            if not _coconut_match_check_0:  #70 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #70 (line num in coconut source)
                    _coconut_match_check_0 = True  #70 (line num in coconut source)
                if _coconut_match_check_0:  #70 (line num in coconut source)
                    _coconut_match_check_0 = False  #70 (line num in coconut source)
                    if not _coconut_match_check_0:  #70 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #70 (line num in coconut source)
                            _coconut_match_check_0 = True  #70 (line num in coconut source)

                    if not _coconut_match_check_0:  #70 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #70 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Nothing, '__match_args__', ())  #70 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #70 (line num in coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #70 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 0:  #70 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #70 (line num in coconut source)
                            _coconut_match_check_0 = True  #70 (line num in coconut source)




        if _coconut_match_check_0:  #70 (line num in coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #70 (line num in coconut source)
                default = _coconut_match_set_name_default  #70 (line num in coconut source)
        if not _coconut_match_check_0:  #70 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #70 (line num in coconut source)

        return (default)  #70 (line num in coconut source)

    @_coconut_addpattern(maybe)  #71 (line num in coconut source)
    @_coconut_tco  #71 (line num in coconut source)
    @_coconut_mark_as_match  #71 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #71 (line num in coconut source)
        _coconut_match_check_1 = False  #71 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #71 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #71 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #71 (line num in coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #71 (line num in coconut source)
            _coconut_match_temp_4 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)   # type: ignore  #71 (line num in coconut source)
            _coconut_match_set_name_func = _coconut_match_temp_3  #71 (line num in coconut source)
            if not _coconut_match_kwargs:  #71 (line num in coconut source)
                _coconut_match_check_1 = True  #71 (line num in coconut source)
        if _coconut_match_check_1:  #71 (line num in coconut source)
            _coconut_match_check_1 = False  #71 (line num in coconut source)
            if not _coconut_match_check_1:  #71 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #71 (line num in coconut source)
                if (_coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) == 1):  #71 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #71 (line num in coconut source)
                    _coconut_match_check_1 = True  #71 (line num in coconut source)
                if _coconut_match_check_1:  #71 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #71 (line num in coconut source)
                        x = _coconut_match_set_name_x  #71 (line num in coconut source)

            if not _coconut_match_check_1:  #71 (line num in coconut source)
                if (not _coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #71 (line num in coconut source)
                    _coconut_match_check_1 = True  #71 (line num in coconut source)
                if _coconut_match_check_1:  #71 (line num in coconut source)
                    _coconut_match_check_1 = False  #71 (line num in coconut source)
                    if not _coconut_match_check_1:  #71 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #71 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #71 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #71 (line num in coconut source)
                            _coconut_match_check_1 = True  #71 (line num in coconut source)
                        if _coconut_match_check_1:  #71 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #71 (line num in coconut source)
                                x = _coconut_match_set_name_x  #71 (line num in coconut source)

                    if not _coconut_match_check_1:  #71 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #71 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #71 (line num in coconut source)
                            _coconut_match_temp_5 = _coconut.getattr(Just, '__match_args__', ())  #71 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_5, _coconut.tuple):  #71 (line num in coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #71 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_5) < 1:  #71 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_5),))  #71 (line num in coconut source)
                            _coconut_match_temp_6 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_5[0], _coconut_sentinel)  #71 (line num in coconut source)
                            if _coconut_match_temp_6 is not _coconut_sentinel:  #71 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_6  #71 (line num in coconut source)
                                _coconut_match_check_1 = True  #71 (line num in coconut source)
                        if _coconut_match_check_1:  #71 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #71 (line num in coconut source)
                                x = _coconut_match_set_name_x  #71 (line num in coconut source)




        if _coconut_match_check_1:  #71 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #71 (line num in coconut source)
                func = _coconut_match_set_name_func  #71 (line num in coconut source)
        if not _coconut_match_check_1:  #71 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #71 (line num in coconut source)

        return _coconut_tail_call(func, x)  #71 (line num in coconut source)

#### Either:

class Either:  #74 (line num in coconut source)
    @staticmethod  #75 (line num in coconut source)
    @_coconut_tco  #76 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #76 (line num in coconut source)
        return _coconut_tail_call(Right, x)  #76 (line num in coconut source)


    @staticmethod  #78 (line num in coconut source)
    @_coconut_tco  #79 (line num in coconut source)
    def __fail__(msg: 'str') -> 'Either':  #79 (line num in coconut source)
        return _coconut_tail_call(Left, msg)  #79 (line num in coconut source)


class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #81 (line num in coconut source)
    _coconut_is_data = True  #81 (line num in coconut source)
    __slots__ = ()  #81 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #81 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #81 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #81 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #81 (line num in coconut source)
    def __eq__(self, other):  #81 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #81 (line num in coconut source)
    def __hash__(self):  #81 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #81 (line num in coconut source)
    __match_args__ = ('x',)  #81 (line num in coconut source)
    @staticmethod  #82 (line num in coconut source)
    def __bool__() -> 'bool':  #83 (line num in coconut source)
        return (False)  #83 (line num in coconut source)


    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #85 (line num in coconut source)
        return (self)  #85 (line num in coconut source)


class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #87 (line num in coconut source)
    _coconut_is_data = True  #87 (line num in coconut source)
    __slots__ = ()  #87 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #87 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #87 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #87 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #87 (line num in coconut source)
    def __eq__(self, other):  #87 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #87 (line num in coconut source)
    def __hash__(self):  #87 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #87 (line num in coconut source)
    __match_args__ = ('x',)  #87 (line num in coconut source)

derivingOrd(Left, Right)  #89 (line num in coconut source)

if TYPE_CHECKING:  #91 (line num in coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #92 (line num in coconut source)
        ...  #93 (line num in coconut source)

else:  #94 (line num in coconut source)
    @_coconut_tco  #95 (line num in coconut source)
    @_coconut_mark_as_match  #95 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #95 (line num in coconut source)
        _coconut_match_check_2 = False  #95 (line num in coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #95 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #95 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #95 (line num in coconut source)
            _coconut_match_temp_7 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #95 (line num in coconut source)
            _coconut_match_temp_8 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)   # type: ignore  #95 (line num in coconut source)
            _coconut_match_set_name_left_func = _coconut_match_temp_7  #95 (line num in coconut source)
            if not _coconut_match_kwargs:  #95 (line num in coconut source)
                _coconut_match_check_2 = True  #95 (line num in coconut source)
        if _coconut_match_check_2:  #95 (line num in coconut source)
            _coconut_match_check_2 = False  #95 (line num in coconut source)
            if not _coconut_match_check_2:  #95 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #95 (line num in coconut source)
                if (_coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) == 1):  #95 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #95 (line num in coconut source)
                    _coconut_match_check_2 = True  #95 (line num in coconut source)
                if _coconut_match_check_2:  #95 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #95 (line num in coconut source)
                        x = _coconut_match_set_name_x  #95 (line num in coconut source)

            if not _coconut_match_check_2:  #95 (line num in coconut source)
                if (not _coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #95 (line num in coconut source)
                    _coconut_match_check_2 = True  #95 (line num in coconut source)
                if _coconut_match_check_2:  #95 (line num in coconut source)
                    _coconut_match_check_2 = False  #95 (line num in coconut source)
                    if not _coconut_match_check_2:  #95 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #95 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #95 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #95 (line num in coconut source)
                            _coconut_match_check_2 = True  #95 (line num in coconut source)
                        if _coconut_match_check_2:  #95 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #95 (line num in coconut source)
                                x = _coconut_match_set_name_x  #95 (line num in coconut source)

                    if not _coconut_match_check_2:  #95 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #95 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #95 (line num in coconut source)
                            _coconut_match_temp_9 = _coconut.getattr(Left, '__match_args__', ())  #95 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_9, _coconut.tuple):  #95 (line num in coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #95 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_9) < 1:  #95 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_9),))  #95 (line num in coconut source)
                            _coconut_match_temp_10 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_9[0], _coconut_sentinel)  #95 (line num in coconut source)
                            if _coconut_match_temp_10 is not _coconut_sentinel:  #95 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_10  #95 (line num in coconut source)
                                _coconut_match_check_2 = True  #95 (line num in coconut source)
                        if _coconut_match_check_2:  #95 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #95 (line num in coconut source)
                                x = _coconut_match_set_name_x  #95 (line num in coconut source)




        if _coconut_match_check_2:  #95 (line num in coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #95 (line num in coconut source)
                left_func = _coconut_match_set_name_left_func  #95 (line num in coconut source)
        if not _coconut_match_check_2:  #95 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #95 (line num in coconut source)

        return _coconut_tail_call(left_func, x)  #95 (line num in coconut source)

    @_coconut_addpattern(either)  #96 (line num in coconut source)
    @_coconut_tco  #96 (line num in coconut source)
    @_coconut_mark_as_match  #96 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #96 (line num in coconut source)
        _coconut_match_check_3 = False  #96 (line num in coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #96 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #96 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #96 (line num in coconut source)
            _coconut_match_temp_11 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #96 (line num in coconut source)
            _coconut_match_temp_12 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)   # type: ignore  #96 (line num in coconut source)
            _coconut_match_set_name_right_func = _coconut_match_temp_11  #96 (line num in coconut source)
            if not _coconut_match_kwargs:  #96 (line num in coconut source)
                _coconut_match_check_3 = True  #96 (line num in coconut source)
        if _coconut_match_check_3:  #96 (line num in coconut source)
            _coconut_match_check_3 = False  #96 (line num in coconut source)
            if not _coconut_match_check_3:  #96 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #96 (line num in coconut source)
                if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) == 1):  #96 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #96 (line num in coconut source)
                    _coconut_match_check_3 = True  #96 (line num in coconut source)
                if _coconut_match_check_3:  #96 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #96 (line num in coconut source)
                        x = _coconut_match_set_name_x  #96 (line num in coconut source)

            if not _coconut_match_check_3:  #96 (line num in coconut source)
                if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #96 (line num in coconut source)
                    _coconut_match_check_3 = True  #96 (line num in coconut source)
                if _coconut_match_check_3:  #96 (line num in coconut source)
                    _coconut_match_check_3 = False  #96 (line num in coconut source)
                    if not _coconut_match_check_3:  #96 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #96 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #96 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #96 (line num in coconut source)
                            _coconut_match_check_3 = True  #96 (line num in coconut source)
                        if _coconut_match_check_3:  #96 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #96 (line num in coconut source)
                                x = _coconut_match_set_name_x  #96 (line num in coconut source)

                    if not _coconut_match_check_3:  #96 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #96 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #96 (line num in coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(Right, '__match_args__', ())  #96 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #96 (line num in coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #96 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #96 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #96 (line num in coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_13[0], _coconut_sentinel)  #96 (line num in coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #96 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_14  #96 (line num in coconut source)
                                _coconut_match_check_3 = True  #96 (line num in coconut source)
                        if _coconut_match_check_3:  #96 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #96 (line num in coconut source)
                                x = _coconut_match_set_name_x  #96 (line num in coconut source)




        if _coconut_match_check_3:  #96 (line num in coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #96 (line num in coconut source)
                right_func = _coconut_match_set_name_right_func  #96 (line num in coconut source)
        if not _coconut_match_check_3:  #96 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #96 (line num in coconut source)

        return _coconut_tail_call(right_func, x)  #96 (line num in coconut source)

#### Ordering:

class Ordering:  #99 (line num in coconut source)
    @staticmethod  #100 (line num in coconut source)
    def __mempty__() -> 'Ordering':  #101 (line num in coconut source)
        return (eq)  #101 (line num in coconut source)


class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #103 (line num in coconut source)
    _coconut_is_data = True  #103 (line num in coconut source)
    __slots__ = ()  #103 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #103 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #103 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #103 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #103 (line num in coconut source)
    def __eq__(self, other):  #103 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #103 (line num in coconut source)
    def __hash__(self):  #103 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #103 (line num in coconut source)
    __match_args__ = ()  #103 (line num in coconut source)
    @staticmethod  #104 (line num in coconut source)
    def __bool__() -> 'bool':  #105 (line num in coconut source)
        return (True)  #105 (line num in coconut source)


class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #107 (line num in coconut source)
    _coconut_is_data = True  #107 (line num in coconut source)
    __slots__ = ()  #107 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #107 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #107 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #107 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #107 (line num in coconut source)
    def __eq__(self, other):  #107 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #107 (line num in coconut source)
    def __hash__(self):  #107 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #107 (line num in coconut source)
    __match_args__ = ()  #107 (line num in coconut source)

class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #109 (line num in coconut source)
    _coconut_is_data = True  #109 (line num in coconut source)
    __slots__ = ()  #109 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #109 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #109 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #109 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #109 (line num in coconut source)
    def __eq__(self, other):  #109 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #109 (line num in coconut source)
    def __hash__(self):  #109 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #109 (line num in coconut source)
    __match_args__ = ()  #109 (line num in coconut source)
    @staticmethod  #110 (line num in coconut source)
    def __bool__() -> 'bool':  #111 (line num in coconut source)
        return (True)  #111 (line num in coconut source)


derivingOrd(LT, EQ, GT)  #113 (line num in coconut source)
derivingBoundedEnum(LT, EQ, GT)  #114 (line num in coconut source)

lt: 'Ordering' = LT()  #116 (line num in coconut source)
eq: 'Ordering' = EQ()  #117 (line num in coconut source)
gt: 'Ordering' = GT()  #118 (line num in coconut source)

#### Char:
Char = T.NewType("Char", str)  #121 (line num in coconut source)

#### String:
String = str  #124 (line num in coconut source)


### Tuples:
fst: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]'  #128 (line num in coconut source)
fst = _coconut.operator.itemgetter((0))  #129 (line num in coconut source)

snd: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]'  #131 (line num in coconut source)
snd = _coconut.operator.itemgetter((1))  #132 (line num in coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #134 (line num in coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #137 (line num in coconut source)
    return (lambda *args: func(args))  # type: ignore  #138 (line num in coconut source)


def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]':  #140 (line num in coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #143 (line num in coconut source)
    return (lambda args: func(*args))  #144 (line num in coconut source)



## Basic type classes:

#### Eq:

Eq = object  #151 (line num in coconut source)

#### Ord:
Ord = Eq  #154 (line num in coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #155 (line num in coconut source)

if TYPE_CHECKING:  #157 (line num in coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #158 (line num in coconut source)
        ...  #159 (line num in coconut source)

else:  #160 (line num in coconut source)
    @_coconut_mark_as_match  #161 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #161 (line num in coconut source)
        _coconut_match_check_4 = False  #161 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #161 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #161 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #161 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #161 (line num in coconut source)
            _coconut_match_temp_15 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #161 (line num in coconut source)
            _coconut_match_temp_16 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #161 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_15  #161 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_16  #161 (line num in coconut source)
            if not _coconut_match_kwargs:  #161 (line num in coconut source)
                _coconut_match_check_4 = True  #161 (line num in coconut source)
        if _coconut_match_check_4:  #161 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #161 (line num in coconut source)
                x = _coconut_match_set_name_x  #161 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #161 (line num in coconut source)
                y = _coconut_match_set_name_y  #161 (line num in coconut source)
        if _coconut_match_check_4 and not (x == y):  #161 (line num in coconut source)
            _coconut_match_check_4 = False  #161 (line num in coconut source)
        if not _coconut_match_check_4:  #161 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #161 (line num in coconut source)

        return (eq)  #161 (line num in coconut source)

    @_coconut_addpattern(compare)  #162 (line num in coconut source)
    @_coconut_mark_as_match  #162 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #162 (line num in coconut source)
        _coconut_match_check_5 = False  #162 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #162 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #162 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #162 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #162 (line num in coconut source)
            _coconut_match_temp_17 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #162 (line num in coconut source)
            _coconut_match_temp_18 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #162 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_17  #162 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_18  #162 (line num in coconut source)
            if not _coconut_match_kwargs:  #162 (line num in coconut source)
                _coconut_match_check_5 = True  #162 (line num in coconut source)
        if _coconut_match_check_5:  #162 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #162 (line num in coconut source)
                x = _coconut_match_set_name_x  #162 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #162 (line num in coconut source)
                y = _coconut_match_set_name_y  #162 (line num in coconut source)
        if _coconut_match_check_5 and not (x < y):  #162 (line num in coconut source)
            _coconut_match_check_5 = False  #162 (line num in coconut source)
        if not _coconut_match_check_5:  #162 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #162 (line num in coconut source)

        return (lt)  #162 (line num in coconut source)

    @_coconut_addpattern(compare)  #163 (line num in coconut source)
    @_coconut_mark_as_match  #163 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #163 (line num in coconut source)
        _coconut_match_check_6 = False  #163 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #163 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #163 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #163 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #163 (line num in coconut source)
            _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #163 (line num in coconut source)
            _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #163 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_19  #163 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_20  #163 (line num in coconut source)
            if not _coconut_match_kwargs:  #163 (line num in coconut source)
                _coconut_match_check_6 = True  #163 (line num in coconut source)
        if _coconut_match_check_6:  #163 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #163 (line num in coconut source)
                x = _coconut_match_set_name_x  #163 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #163 (line num in coconut source)
                y = _coconut_match_set_name_y  #163 (line num in coconut source)
        if _coconut_match_check_6 and not (x > y):  #163 (line num in coconut source)
            _coconut_match_check_6 = False  #163 (line num in coconut source)
        if not _coconut_match_check_6:  #163 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #163 (line num in coconut source)

        return (gt)  #163 (line num in coconut source)


max: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #165 (line num in coconut source)
max = _max  #166 (line num in coconut source)

min: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #168 (line num in coconut source)
min = _min  #169 (line num in coconut source)

#### Enum:
Enum = Ord  #172 (line num in coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #173 (line num in coconut source)

succ: '_coconut.typing.Callable[[TEnum], TEnum]'  #175 (line num in coconut source)
succ = _coconut.functools.partial((_coconut.operator.add), 1)  #176 (line num in coconut source)

pred: '_coconut.typing.Callable[[TEnum], TEnum]'  #178 (line num in coconut source)
pred = _coconut_partial((_coconut_minus), {1: 1}, 2)  #179 (line num in coconut source)

toEnum = NotImplemented  #181 (line num in coconut source)

fromEnum: '_coconut.typing.Callable[[Enum], int]'  #183 (line num in coconut source)
fromEnum = _int  #184 (line num in coconut source)

@_coconut_tco  #186 (line num in coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #186 (line num in coconut source)
    return _coconut_tail_call(iterate, succ, first)  #187 (line num in coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #189 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #190 (line num in coconut source)
    return (iterate(_coconut.functools.partial((_coconut.operator.add), step), first) if step >= 0 else ())  # type: ignore  #191 (line num in coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #193 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #194 (line num in coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #195 (line num in coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #197 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #198 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #199 (line num in coconut source)
    steps = dist / step if step != 0 else 0  #200 (line num in coconut source)
    if steps < 0:  #201 (line num in coconut source)
        return (())  #202 (line num in coconut source)
    counter = iterate(_coconut.functools.partial((_coconut.operator.add), step), first)  #203 (line num in coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #204 (line num in coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #208 (line num in coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #209 (line num in coconut source)

@_coconut_tco  #211 (line num in coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #211 (line num in coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #215 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #217 (line num in coconut source)
        return (False)  # type: ignore  #218 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #221 (line num in coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #222 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(_fmap, minBound, b)  #225 (line num in coconut source)


@_coconut_tco  #227 (line num in coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #227 (line num in coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #231 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #233 (line num in coconut source)
        return (True)  # type: ignore  #234 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #237 (line num in coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #238 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(_fmap, maxBound, b)  #241 (line num in coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #250 (line num in coconut source)

#### Integer:
Integer = int  #253 (line num in coconut source)

#### Float:
Float = float  #256 (line num in coconut source)

#### Double:
Double = float  #259 (line num in coconut source)

#### Rational:
Rational = _fractions.Fraction  #262 (line num in coconut source)

@_coconut_tco  #264 (line num in coconut source)
def over(x, y):  #264 (line num in coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #269 (line num in coconut source)
    return _coconut_tail_call(Rational, x, y)  #270 (line num in coconut source)

#### Word:

Word = Int  #273 (line num in coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #279 (line num in coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #280 (line num in coconut source)

negate: '_coconut.typing.Callable[[TNum], TNum]'  #282 (line num in coconut source)
negate = (_coconut_minus)  #283 (line num in coconut source)

abs: '_coconut.typing.Callable[[TNum], TNum]'  #285 (line num in coconut source)
abs = _abs  #286 (line num in coconut source)

if TYPE_CHECKING:  #288 (line num in coconut source)
    def signum(x: 'Num') -> 'int':  #289 (line num in coconut source)
        ...  #290 (line num in coconut source)

else:  #291 (line num in coconut source)
    @_coconut_mark_as_match  #292 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #292 (line num in coconut source)
        _coconut_match_check_7 = False  #292 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #292 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #292 (line num in coconut source)
            if _coconut_match_args[0] == 0:  #292 (line num in coconut source)
                if not _coconut_match_kwargs:  #292 (line num in coconut source)
                    _coconut_match_check_7 = True  #292 (line num in coconut source)
        if not _coconut_match_check_7:  #292 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #292 (line num in coconut source)

        return (0)  #292 (line num in coconut source)

    @_coconut_addpattern(signum)  #293 (line num in coconut source)
    @_coconut_mark_as_match  #293 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #293 (line num in coconut source)
        _coconut_match_check_8 = False  #293 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #293 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #293 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #293 (line num in coconut source)
            _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #293 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_21  #293 (line num in coconut source)
            if not _coconut_match_kwargs:  #293 (line num in coconut source)
                _coconut_match_check_8 = True  #293 (line num in coconut source)
        if _coconut_match_check_8:  #293 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #293 (line num in coconut source)
                x = _coconut_match_set_name_x  #293 (line num in coconut source)
        if _coconut_match_check_8 and not (x > 0):  #293 (line num in coconut source)
            _coconut_match_check_8 = False  #293 (line num in coconut source)
        if not _coconut_match_check_8:  #293 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #293 (line num in coconut source)

        return (1)  #293 (line num in coconut source)

    @_coconut_addpattern(signum)  #294 (line num in coconut source)
    @_coconut_mark_as_match  #294 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #294 (line num in coconut source)
        _coconut_match_check_9 = False  #294 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #294 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #294 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #294 (line num in coconut source)
            _coconut_match_temp_22 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #294 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_22  #294 (line num in coconut source)
            if not _coconut_match_kwargs:  #294 (line num in coconut source)
                _coconut_match_check_9 = True  #294 (line num in coconut source)
        if _coconut_match_check_9:  #294 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #294 (line num in coconut source)
                x = _coconut_match_set_name_x  #294 (line num in coconut source)
        if _coconut_match_check_9 and not (x < 0):  #294 (line num in coconut source)
            _coconut_match_check_9 = False  #294 (line num in coconut source)
        if not _coconut_match_check_9:  #294 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #294 (line num in coconut source)

        return (-1)  #294 (line num in coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #296 (line num in coconut source)
    return (x)  #296 (line num in coconut source)

#### Real:

Real = Num  #299 (line num in coconut source)

if TYPE_CHECKING:  #301 (line num in coconut source)
    def toRational(real: 'Real') -> 'Rational':  #302 (line num in coconut source)
        ...  #303 (line num in coconut source)

else:  #304 (line num in coconut source)
    @_coconut_tco  #305 (line num in coconut source)
    @_coconut_mark_as_match  #305 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #305 (line num in coconut source)
        _coconut_match_check_10 = False  #305 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #305 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #305 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #305 (line num in coconut source)
            _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #305 (line num in coconut source)
            if (isinstance)(_coconut_match_temp_23, float):  #305 (line num in coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_23  #305 (line num in coconut source)
                if not _coconut_match_kwargs:  #305 (line num in coconut source)
                    _coconut_match_check_10 = True  #305 (line num in coconut source)
        if _coconut_match_check_10:  #305 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #305 (line num in coconut source)
                real = _coconut_match_set_name_real  #305 (line num in coconut source)
        if not _coconut_match_check_10:  #305 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #305 (line num in coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #306 (line num in coconut source)

    @_coconut_addpattern(toRational)  #307 (line num in coconut source)
    @_coconut_tco  #307 (line num in coconut source)
    @_coconut_mark_as_match  #307 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #307 (line num in coconut source)
        _coconut_match_check_11 = False  #307 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #307 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #307 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #307 (line num in coconut source)
            _coconut_match_temp_24 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #307 (line num in coconut source)
            _coconut_match_set_name_real = _coconut_match_temp_24  #307 (line num in coconut source)
            if not _coconut_match_kwargs:  #307 (line num in coconut source)
                _coconut_match_check_11 = True  #307 (line num in coconut source)
        if _coconut_match_check_11:  #307 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #307 (line num in coconut source)
                real = _coconut_match_set_name_real  #307 (line num in coconut source)
        if not _coconut_match_check_11:  #307 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #307 (line num in coconut source)

        return _coconut_tail_call(Rational, real)  #308 (line num in coconut source)

#### Integral:

Integral = int  #311 (line num in coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #313 (line num in coconut source)
    divxy = x // y  #314 (line num in coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #315 (line num in coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #317 (line num in coconut source)
    modxy = x % y  #318 (line num in coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #319 (line num in coconut source)


div: '_coconut.typing.Callable[[int, int], int]'  #321 (line num in coconut source)
div = (_coconut.operator.floordiv)  #322 (line num in coconut source)

mod: '_coconut.typing.Callable[[int, int], int]'  #324 (line num in coconut source)
mod = (_coconut.operator.mod)  #325 (line num in coconut source)

def quotRem(x: 'int', y: 'int') -> 'T.Tuple[int, int]':  #327 (line num in coconut source)
    divxy, modxy = divmod(x, y)  #328 (line num in coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #329 (line num in coconut source)
    return (divxy + adj, modxy - y * adj)  #330 (line num in coconut source)


divMod = divmod  #332 (line num in coconut source)

toInteger: '_coconut.typing.Callable[[Integral], Integer]'  #334 (line num in coconut source)
toInteger = _int  #335 (line num in coconut source)

#### Fractional:
Fractional = Rational  #338 (line num in coconut source)

recip: '_coconut.typing.Callable[[Fractional], Fractional]'  #340 (line num in coconut source)
recip = _coconut.functools.partial((_coconut.operator.truediv), 1)  #341 (line num in coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #343 (line num in coconut source)
    return (x)  #343 (line num in coconut source)

#### Floating:

Floating = float  #346 (line num in coconut source)

from math import pi  #348 (line num in coconut source)
from math import exp  #348 (line num in coconut source)
from math import log  #348 (line num in coconut source)
from math import sqrt  #348 (line num in coconut source)
from math import sin  #348 (line num in coconut source)
from math import cos  #348 (line num in coconut source)
from math import tan  #348 (line num in coconut source)
from math import asin  #348 (line num in coconut source)
from math import acos  #348 (line num in coconut source)
from math import atan  #348 (line num in coconut source)
from math import sinh  #348 (line num in coconut source)
from math import cosh  #348 (line num in coconut source)
from math import tanh  #348 (line num in coconut source)
from math import asinh  #348 (line num in coconut source)
from math import acosh  #348 (line num in coconut source)
from math import atanh  #348 (line num in coconut source)

@_coconut_tco  #367 (line num in coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #367 (line num in coconut source)
    return _coconut_tail_call(log, x, base)  #368 (line num in coconut source)

#### RealFrac:

RealFrac = Rational  #371 (line num in coconut source)

def properFraction(x: 'RealFrac') -> 'T.Tuple[int, RealFrac]':  #373 (line num in coconut source)
    floor_x = floor(x)  #374 (line num in coconut source)
    return (floor_x, x - floor_x)  #375 (line num in coconut source)


truncate: '_coconut.typing.Callable[[RealFrac], int]'  #377 (line num in coconut source)
truncate = _int  #378 (line num in coconut source)

round: '_coconut.typing.Callable[[RealFrac], int]'  #380 (line num in coconut source)
round = _round  #381 (line num in coconut source)

ceiling: '_coconut.typing.Callable[[RealFrac], int]'  #383 (line num in coconut source)
ceiling = _ceil  #384 (line num in coconut source)

floor: '_coconut.typing.Callable[[RealFrac], int]'  #386 (line num in coconut source)
floor = _floor  #387 (line num in coconut source)

#### RealFloat:
RealFloat = float  #390 (line num in coconut source)

def floatRadix(x: 'float') -> 'int':  #392 (line num in coconut source)
    return (2)  #392 (line num in coconut source)


def floatDigits(x: 'float') -> 'int':  #394 (line num in coconut source)
    return (53)  #394 (line num in coconut source)


def floatRange(x: 'float') -> 'T.Tuple[int, int]':  #396 (line num in coconut source)
    return ((-1021, 1024))  #396 (line num in coconut source)


decodeFloat = NotImplemented  #398 (line num in coconut source)

encodeFloat = NotImplemented  #400 (line num in coconut source)

exponent = NotImplemented  #402 (line num in coconut source)

significand = NotImplemented  #404 (line num in coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #406 (line num in coconut source)
    return (x * 2**power)  #407 (line num in coconut source)


from math import isnan as isNaN  #409 (line num in coconut source)
from math import isinf as isInfinite  #409 (line num in coconut source)
from math import atan2  #409 (line num in coconut source)

isDenormalized = NotImplemented  #415 (line num in coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #417 (line num in coconut source)
    return (x == 0 and str(x).startswith("-"))  #418 (line num in coconut source)


def isIEEE(x: 'float') -> 'bool':  #420 (line num in coconut source)
    return (True)  #420 (line num in coconut source)


### Numeric functions:

def subtract(x, y):  #424 (line num in coconut source)
    return (y - x)  #425 (line num in coconut source)


def even(x: 'int') -> 'bool':  #427 (line num in coconut source)
    return (x % 2 == 0)  #428 (line num in coconut source)


def odd(x: 'int') -> 'bool':  #430 (line num in coconut source)
    return (x % 2 == 1)  #431 (line num in coconut source)


gcd: '_coconut.typing.Callable[[int, int], int]'  #433 (line num in coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #434 (line num in coconut source)

if TYPE_CHECKING:  #436 (line num in coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #437 (line num in coconut source)
        ...  #438 (line num in coconut source)

else:  #439 (line num in coconut source)
    @_coconut_mark_as_match  #440 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #440 (line num in coconut source)
        _coconut_match_check_12 = False  #440 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #440 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #440 (line num in coconut source)
            if _coconut_match_args[1] == 0:  #440 (line num in coconut source)
                if not _coconut_match_kwargs:  #440 (line num in coconut source)
                    _coconut_match_check_12 = True  #440 (line num in coconut source)
        if not _coconut_match_check_12:  #440 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #440 (line num in coconut source)

        return (0)  #440 (line num in coconut source)

    @_coconut_addpattern(lcm)  #441 (line num in coconut source)
    @_coconut_mark_as_match  #441 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #441 (line num in coconut source)
        _coconut_match_check_13 = False  #441 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #441 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #441 (line num in coconut source)
            if _coconut_match_args[0] == 0:  #441 (line num in coconut source)
                if not _coconut_match_kwargs:  #441 (line num in coconut source)
                    _coconut_match_check_13 = True  #441 (line num in coconut source)
        if not _coconut_match_check_13:  #441 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #441 (line num in coconut source)

        return (0)  #441 (line num in coconut source)

    @_coconut_addpattern(lcm)  #442 (line num in coconut source)
    @_coconut_mark_as_match  #442 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #442 (line num in coconut source)
        _coconut_match_check_14 = False  #442 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #442 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #442 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #442 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #442 (line num in coconut source)
            _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #442 (line num in coconut source)
            _coconut_match_temp_26 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #442 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_25  #442 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_26  #442 (line num in coconut source)
            if not _coconut_match_kwargs:  #442 (line num in coconut source)
                _coconut_match_check_14 = True  #442 (line num in coconut source)
        if _coconut_match_check_14:  #442 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #442 (line num in coconut source)
                x = _coconut_match_set_name_x  #442 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #442 (line num in coconut source)
                y = _coconut_match_set_name_y  #442 (line num in coconut source)
        if not _coconut_match_check_14:  #442 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #442 (line num in coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #443 (line num in coconut source)


fromIntegral: '_coconut.typing.Callable[[Integral], Num]'  #445 (line num in coconut source)
fromIntegral = fromInteger  #446 (line num in coconut source)

realToFrac: '_coconut.typing.Callable[[Real], Fractional]'  #448 (line num in coconut source)
realToFrac = toRational  #449 (line num in coconut source)



## Monoids:
Monoid = T.Iterable  #454 (line num in coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #455 (line num in coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #457 (line num in coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #460 (line num in coconut source)
    _coconut_is_data = True  #461 (line num in coconut source)
    __slots__ = ()  #461 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #461 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #461 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #461 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #461 (line num in coconut source)
    def __eq__(self, other):  #461 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #461 (line num in coconut source)
    def __hash__(self):  #461 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #461 (line num in coconut source)
    __match_args__ = ()  #461 (line num in coconut source)
    @staticmethod  #461 (line num in coconut source)
    @_coconut_tco  #462 (line num in coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #462 (line num in coconut source)
        if (hasattr)(M, "__mempty__"):  #463 (line num in coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #464 (line num in coconut source)
        return _coconut_tail_call(makedata, type(M))  #465 (line num in coconut source)


mempty: 'T.Any' = Mempty()  #467 (line num in coconut source)

@_coconut_tco  #469 (line num in coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #469 (line num in coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #474 (line num in coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #476 (line num in coconut source)
    y = (asTypeOf)(y, x)  #477 (line num in coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #480 (line num in coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #481 (line num in coconut source)

# Default implementation
    if not x:  #484 (line num in coconut source)
        return (y)  #485 (line num in coconut source)
    if not y:  #486 (line num in coconut source)
        return (x)  #487 (line num in coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #488 (line num in coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #489 (line num in coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #490 (line num in coconut source)


@_coconut_tco  #492 (line num in coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #492 (line num in coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #493 (line num in coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #500 (line num in coconut source)

fmap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], Functor[Ta]], Functor[Tb]]'  # type: ignore  #502 (line num in coconut source)
fmap = _fmap  #503 (line num in coconut source)

@_coconut_tco  #505 (line num in coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #505 (line num in coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #509 (line num in coconut source)
    return _coconut_tail_call(_fmap, lambda _: x, xs)  #510 (line num in coconut source)

#### Applicative:

Applicative = Functor  #513 (line num in coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #514 (line num in coconut source)

if TYPE_CHECKING:  #516 (line num in coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #517 (line num in coconut source)
        ...  #518 (line num in coconut source)

else:  #519 (line num in coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #520 (line num in coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #524 (line num in coconut source)
        _coconut_is_data = True  #525 (line num in coconut source)
        __slots__ = ()  #525 (line num in coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #525 (line num in coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #525 (line num in coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #525 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #525 (line num in coconut source)
        def __eq__(self, other):  #525 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #525 (line num in coconut source)
        def __hash__(self):  #525 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #525 (line num in coconut source)
        __match_args__ = ('val',)  #525 (line num in coconut source)
        def __join__(self) -> 'T.Any':  #525 (line num in coconut source)
            return (self.val)  #525 (line num in coconut source)


        @_coconut_tco  #527 (line num in coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #527 (line num in coconut source)
            if (hasattr)(M, "__pure__"):  #528 (line num in coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #529 (line num in coconut source)
            return _coconut_tail_call(makedata, type(M), self.val)  #530 (line num in coconut source)


@_coconut_tco  #532 (line num in coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #532 (line num in coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #539 (line num in coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #541 (line num in coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #542 (line num in coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #545 (line num in coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #546 (line num in coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: _fmap(f, xs))  #549 (line num in coconut source)


@_coconut_tco  #551 (line num in coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #551 (line num in coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #555 (line num in coconut source)
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #556 (line num in coconut source)


@_coconut_tco  #558 (line num in coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #558 (line num in coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #562 (line num in coconut source)
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #563 (line num in coconut source)


def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #565 (line num in coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #569 (line num in coconut source)
    return (lambda f1, f2: (ap)(_fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2))  #570 (line num in coconut source)

#### Monad:

Monad = Applicative  #573 (line num in coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #574 (line num in coconut source)

@_coconut_tco  #576 (line num in coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #576 (line num in coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #581 (line num in coconut source)
    return _coconut_tail_call(join, _fmap(func, m))  # type: ignore  #582 (line num in coconut source)


@_coconut_tco  #584 (line num in coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #584 (line num in coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #588 (line num in coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #589 (line num in coconut source)


return_ = pure  #591 (line num in coconut source)

if TYPE_CHECKING:  #593 (line num in coconut source)
    def fail(msg: 'str') -> 'T.Any':  #594 (line num in coconut source)
        ...  #595 (line num in coconut source)

else:  #596 (line num in coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #597 (line num in coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #600 (line num in coconut source)
        _coconut_is_data = True  #601 (line num in coconut source)
        __slots__ = ()  #601 (line num in coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #601 (line num in coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #601 (line num in coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #601 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #601 (line num in coconut source)
        def __eq__(self, other):  #601 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #601 (line num in coconut source)
        def __hash__(self):  #601 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #601 (line num in coconut source)
        __match_args__ = ('msg',)  #601 (line num in coconut source)
        @staticmethod  #601 (line num in coconut source)
        def __bool__() -> 'bool':  #602 (line num in coconut source)
            return (False)  #602 (line num in coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #604 (line num in coconut source)
            return (self)  #604 (line num in coconut source)


        @_coconut_tco  #606 (line num in coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #606 (line num in coconut source)
            if (hasattr)(M, "__fail__"):  #607 (line num in coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #608 (line num in coconut source)
            return _coconut_tail_call(makedata, type(M))  #609 (line num in coconut source)

# sequence_ and mapM_ defined in Foldable


@_coconut_tco  #613 (line num in coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #613 (line num in coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #617 (line num in coconut source)
    return _coconut_tail_call((bind), m, func)  #618 (line num in coconut source)


@_coconut_tco  #620 (line num in coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #620 (line num in coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation identifies non-failures using __bool__
    """  #627 (line num in coconut source)
# Resolve ms being pure or fail
    ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #629 (line num in coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #632 (line num in coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #635 (line num in coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #636 (line num in coconut source)

# Default implementation
    if not ms:  #639 (line num in coconut source)
        return (ms)  # type: ignore  #640 (line num in coconut source)
    vals = []  # type: ignore  #641 (line num in coconut source)
    fallback = ms  #642 (line num in coconut source)
    for m in ms:  #643 (line num in coconut source)
        if m:  #644 (line num in coconut source)
            vals.extend(m)  # type: ignore  #645 (line num in coconut source)
        else:  #646 (line num in coconut source)
            fallback = m  # type: ignore  #647 (line num in coconut source)
    if not vals:  #648 (line num in coconut source)
        return (fallback)  # type: ignore  #649 (line num in coconut source)
    return _coconut_tail_call(makedata, type(ms), *vals)  #650 (line num in coconut source)


if TYPE_CHECKING:  #652 (line num in coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]') -> 'TMonad':  #653 (line num in coconut source)
        ...  #654 (line num in coconut source)

else:  #655 (line num in coconut source)
    @_coconut_tco  #656 (line num in coconut source)
    @_coconut_mark_as_match  #656 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #656 (line num in coconut source)
        _coconut_match_check_15 = False  #656 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #656 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #656 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #656 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #656 (line num in coconut source)
                _coconut_match_temp_27 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #656 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_27  #656 (line num in coconut source)
                if not _coconut_match_kwargs:  #656 (line num in coconut source)
                    _coconut_match_check_15 = True  #656 (line num in coconut source)
        if _coconut_match_check_15:  #656 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #656 (line num in coconut source)
                func = _coconut_match_set_name_func  #656 (line num in coconut source)
        if not _coconut_match_check_15:  #656 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #656 (line num in coconut source)

        return _coconut_tail_call(func)  #656 (line num in coconut source)

    @_coconut_addpattern(do)  #657 (line num in coconut source)
    @_coconut_tco  #657 (line num in coconut source)
    @_coconut_mark_as_match  #657 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #657 (line num in coconut source)
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
        """  #676 (line num in coconut source)
        _coconut_match_check_16 = False  #677 (line num in coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #677 (line num in coconut source)
        _coconut_match_set_name_ms = _coconut_sentinel  #677 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #677 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #677 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #677 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #677 (line num in coconut source)
                _coconut_match_set_name_m = _coconut_match_args[0][0]  #677 (line num in coconut source)
                _coconut_match_temp_29 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #677 (line num in coconut source)
                _coconut_match_temp_28 = _coconut.list(_coconut_match_args[0][1:])  #677 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_29  #677 (line num in coconut source)
                _coconut_match_set_name_ms = _coconut_match_temp_28  #677 (line num in coconut source)
                if not _coconut_match_kwargs:  #677 (line num in coconut source)
                    _coconut_match_check_16 = True  #677 (line num in coconut source)
        if _coconut_match_check_16:  #677 (line num in coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #677 (line num in coconut source)
                m = _coconut_match_set_name_m  #677 (line num in coconut source)
            if _coconut_match_set_name_ms is not _coconut_sentinel:  #677 (line num in coconut source)
                ms = _coconut_match_set_name_ms  #677 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #677 (line num in coconut source)
                func = _coconut_match_set_name_func  #677 (line num in coconut source)
        if not _coconut_match_check_16:  #677 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #677 (line num in coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))  #677 (line num in coconut source)



## Folds and traversals:

#### Foldable:

Foldable = T.Sequence  #684 (line num in coconut source)

@_coconut_tco  #686 (line num in coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #686 (line num in coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #687 (line num in coconut source)


mapM_: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #689 (line num in coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #690 (line num in coconut source)

@_coconut_tco  #692 (line num in coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #692 (line num in coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #693 (line num in coconut source)


@_coconut_tco  #695 (line num in coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #695 (line num in coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #696 (line num in coconut source)


@_coconut_tco  #698 (line num in coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #698 (line num in coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #699 (line num in coconut source)


foldl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #701 (line num in coconut source)
foldl1 = reduce  #702 (line num in coconut source)

@_coconut_tco  #704 (line num in coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #704 (line num in coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #705 (line num in coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #707 (line num in coconut source)
    return (len(xs) == 0)  #708 (line num in coconut source)


length: '_coconut.typing.Callable[[Foldable], int]'  #710 (line num in coconut source)
length = len  #711 (line num in coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #713 (line num in coconut source)
    return (e in xs)  #714 (line num in coconut source)


maximum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #716 (line num in coconut source)
maximum = _max  #717 (line num in coconut source)

minimum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #719 (line num in coconut source)
minimum = _min  #720 (line num in coconut source)

sum: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #722 (line num in coconut source)
sum = _sum  #723 (line num in coconut source)

product: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #725 (line num in coconut source)
product = _coconut.functools.partial(reduce, _coconut.operator.mul)  #726 (line num in coconut source)

#### Traversable:
Traversable = T.Iterable  #729 (line num in coconut source)

@_coconut_tco  #731 (line num in coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #731 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #732 (line num in coconut source)


@_coconut_tco  #734 (line num in coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #734 (line num in coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #735 (line num in coconut source)


traverse: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #737 (line num in coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  #738 (line num in coconut source)

sequence: '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #740 (line num in coconut source)
sequence = sequenceA  #741 (line num in coconut source)

mapM: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #743 (line num in coconut source)
mapM = traverse  #744 (line num in coconut source)



## Miscellaneous functions:
def id(x: 'Ta') -> 'Ta':  #749 (line num in coconut source)
    return (x)  #749 (line num in coconut source)


@_coconut_tco  #751 (line num in coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #751 (line num in coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #755 (line num in coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #756 (line num in coconut source)


if TYPE_CHECKING:  #758 (line num in coconut source)
    @T.overload  #759 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #760 (line num in coconut source)
        ...  #761 (line num in coconut source)

    @T.overload  #762 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #763 (line num in coconut source)
        ...  #764 (line num in coconut source)

    @T.overload  #765 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #766 (line num in coconut source)
        ...  #767 (line num in coconut source)

    @T.overload  #768 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta') -> 'T.Any':  #769 (line num in coconut source)
        ...  #770 (line num in coconut source)

    def apply(func, arg):  #771 (line num in coconut source)
        ...  #772 (line num in coconut source)

else:  #773 (line num in coconut source)
    @_coconut_tco  #774 (line num in coconut source)
    def apply(func, arg):  #774 (line num in coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #780 (line num in coconut source)
        return _coconut_tail_call((of), func, arg)  #781 (line num in coconut source)


@_coconut_tco  #783 (line num in coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #783 (line num in coconut source)
    while True:  #784 (line num in coconut source)
        if cond(x):  #784 (line num in coconut source)
            return (x)  #785 (line num in coconut source)
        try:  # tail recursive  #786 (line num in coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_70  # tail recursive  #786 (line num in coconut source)
        except _coconut.NameError:  # tail recursive  #786 (line num in coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #786 (line num in coconut source)
        if _coconut_tre_check_0:  # tail recursive  #786 (line num in coconut source)
            cond, func, x = cond, func, func(x)  # tail recursive  #786 (line num in coconut source)
            continue  # tail recursive  #786 (line num in coconut source)
        else:  # tail recursive  #786 (line num in coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  # tail recursive  #786 (line num in coconut source)
# tail recursive

        return None  #788 (line num in coconut source)
_coconut_recursive_func_70 = until  #788 (line num in coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #788 (line num in coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #792 (line num in coconut source)
    if TYPE_CHECKING:  #793 (line num in coconut source)
        return (x)  #793 (line num in coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #795 (line num in coconut source)
        for i in (takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count()):  #796 (line num in coconut source)
            if (isinstance)(x, pure):  #797 (line num in coconut source)
                x = x.pure_as(y)  #798 (line num in coconut source)
            elif (isinstance)(x, fail):  #799 (line num in coconut source)
                x = x.fail_as(y)  #800 (line num in coconut source)
            elif (isinstance)(x, Mempty):  #801 (line num in coconut source)
                x = x.mempty_as(y)  #802 (line num in coconut source)
            else:  #803 (line num in coconut source)
                break  #804 (line num in coconut source)
    return (x)  #805 (line num in coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #807 (line num in coconut source)

def error(msg: 'str') -> 'None':  #809 (line num in coconut source)
    raise Exception(msg)  #810 (line num in coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #812 (line num in coconut source)
    raise Exception(msg) from None  #813 (line num in coconut source)


undefined: 'T.Any' = None  #815 (line num in coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #817 (line num in coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #820 (line num in coconut source)
    return (y)  #821 (line num in coconut source)


@_coconut_tco  #823 (line num in coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #823 (line num in coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #828 (line num in coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #829 (line num in coconut source)




# List operations:

@_coconut_tco  #835 (line num in coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #835 (line num in coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #839 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #840 (line num in coconut source)

# type: ignore
map: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #842 (line num in coconut source)
map = _map  # type: ignore  #843 (line num in coconut source)

@_coconut_tco  #845 (line num in coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #845 (line num in coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #849 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #850 (line num in coconut source)

# type: ignore
filter: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #852 (line num in coconut source)
filter = _filter  # type: ignore  #853 (line num in coconut source)

head: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #855 (line num in coconut source)
head = _coconut.functools.partial(_coconut_iter_getitem, index=(0))  #856 (line num in coconut source)

last: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #858 (line num in coconut source)
last = _coconut.functools.partial(_coconut_iter_getitem, index=(-1))  #859 (line num in coconut source)

tail: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #861 (line num in coconut source)
tail = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #862 (line num in coconut source)

init: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #864 (line num in coconut source)
init = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #865 (line num in coconut source)

@_coconut_tco  #867 (line num in coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #867 (line num in coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #871 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #872 (line num in coconut source)


reverse: '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #874 (line num in coconut source)
reverse = _reversed  #875 (line num in coconut source)



## Special folds:
and_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #880 (line num in coconut source)
and_ = _all  #881 (line num in coconut source)

or_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #883 (line num in coconut source)
or_ = _any  #884 (line num in coconut source)

any: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #886 (line num in coconut source)
any = _coconut_forward_compose(map, or_)  #887 (line num in coconut source)

all: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #889 (line num in coconut source)
all = _coconut_forward_compose(map, and_)  #890 (line num in coconut source)

@_coconut_tco  #892 (line num in coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #892 (line num in coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #893 (line num in coconut source)


concatMap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #895 (line num in coconut source)
concatMap = _coconut_forward_compose(map, concat)  #896 (line num in coconut source)



## Building lists:

### Scans:
@_coconut_tco  #903 (line num in coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #903 (line num in coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #904 (line num in coconut source)


scanl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #906 (line num in coconut source)
scanl1 = scan  #907 (line num in coconut source)

@_coconut_tco  #909 (line num in coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #909 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #910 (line num in coconut source)


@_coconut_tco  #912 (line num in coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #912 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #913 (line num in coconut source)

### Infinite lists:

@recursive_iterator  #916 (line num in coconut source)
@_coconut_tco  #917 (line num in coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #917 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #918 (line num in coconut source)


@recursive_iterator  #920 (line num in coconut source)
@_coconut_tco  #921 (line num in coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #921 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #922 (line num in coconut source)


@_coconut_tco  #924 (line num in coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #924 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #925 (line num in coconut source)


if TYPE_CHECKING:  #927 (line num in coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #928 (line num in coconut source)
        ...  #929 (line num in coconut source)

else:  #930 (line num in coconut source)
    @recursive_iterator  #931 (line num in coconut source)
    @_coconut_tco  #932 (line num in coconut source)
    @_coconut_mark_as_match  #932 (line num in coconut source)
    def cycle(*_coconut_match_args, **_coconut_match_kwargs):  #932 (line num in coconut source)
        _coconut_match_check_17 = False  #932 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #932 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #932 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #932 (line num in coconut source)
            _coconut_match_temp_30 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #932 (line num in coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_30  #932 (line num in coconut source)
            if not _coconut_match_kwargs:  #932 (line num in coconut source)
                _coconut_match_check_17 = True  #932 (line num in coconut source)
        if _coconut_match_check_17:  #932 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #932 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #932 (line num in coconut source)
        if _coconut_match_check_17 and not (len(xs) > 0):  #932 (line num in coconut source)
            _coconut_match_check_17 = False  #932 (line num in coconut source)
        if not _coconut_match_check_17:  #932 (line num in coconut source)
            raise _coconut_FunctionMatchError('def cycle(xs if len(xs) > 0) =', _coconut_match_args)  #932 (line num in coconut source)

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))  #933 (line num in coconut source)



## Sublists:

@_coconut_tco  #938 (line num in coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #938 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #939 (line num in coconut source)


@_coconut_tco  #941 (line num in coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #941 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #942 (line num in coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> 'T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]':  #944 (line num in coconut source)
    reit = reiterable(xs)  #945 (line num in coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #946 (line num in coconut source)


takeWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #948 (line num in coconut source)
takeWhile = takewhile  #949 (line num in coconut source)

dropWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #951 (line num in coconut source)
dropWhile = dropwhile  #952 (line num in coconut source)

if TYPE_CHECKING:  #954 (line num in coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]':  #955 (line num in coconut source)
        ...  #956 (line num in coconut source)

else:  #957 (line num in coconut source)
    @_coconut_mark_as_match  #958 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #958 (line num in coconut source)
        _coconut_match_check_18 = False  #958 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #958 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #958 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #958 (line num in coconut source)
                if not _coconut_match_kwargs:  #958 (line num in coconut source)
                    _coconut_match_check_18 = True  #958 (line num in coconut source)
        if not _coconut_match_check_18:  #958 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #958 (line num in coconut source)

        return (([], []))  #958 (line num in coconut source)

    @_coconut_addpattern(span)  #959 (line num in coconut source)
    @_coconut_mark_as_match  #959 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #959 (line num in coconut source)
        _coconut_match_check_19 = False  #959 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #959 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #959 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #959 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #959 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #959 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #959 (line num in coconut source)
                _coconut_match_temp_31 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #959 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_args[1][0]  #959 (line num in coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_31  #959 (line num in coconut source)
                _coconut_match_temp_32 = _coconut.list(_coconut_match_args[1][1:])  #959 (line num in coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_32  #959 (line num in coconut source)
                if not _coconut_match_kwargs:  #959 (line num in coconut source)
                    _coconut_match_check_19 = True  #959 (line num in coconut source)
        if _coconut_match_check_19:  #959 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #959 (line num in coconut source)
                cond = _coconut_match_set_name_cond  #959 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #959 (line num in coconut source)
                x = _coconut_match_set_name_x  #959 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #959 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #959 (line num in coconut source)
        if _coconut_match_check_19 and not (cond(x)):  #959 (line num in coconut source)
            _coconut_match_check_19 = False  #959 (line num in coconut source)
        if not _coconut_match_check_19:  #959 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #959 (line num in coconut source)

        ys, zs = span(cond, xs)  #960 (line num in coconut source)
        return (([x,] + ys, zs))  #961 (line num in coconut source)

    @_coconut_addpattern(span)  #962 (line num in coconut source)
    @_coconut_mark_as_match  #962 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #962 (line num in coconut source)
        _coconut_match_check_20 = False  #962 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #962 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #962 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #962 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #962 (line num in coconut source)
            _coconut_match_temp_33 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #962 (line num in coconut source)
            _coconut_match_temp_34 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #962 (line num in coconut source)
            _coconut_match_set_name_cond = _coconut_match_temp_33  #962 (line num in coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_34  #962 (line num in coconut source)
            if not _coconut_match_kwargs:  #962 (line num in coconut source)
                _coconut_match_check_20 = True  #962 (line num in coconut source)
        if _coconut_match_check_20:  #962 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #962 (line num in coconut source)
                cond = _coconut_match_set_name_cond  #962 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #962 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #962 (line num in coconut source)
        if not _coconut_match_check_20:  #962 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #962 (line num in coconut source)

        return (([], xs))  #963 (line num in coconut source)


@_coconut_tco  #965 (line num in coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #965 (line num in coconut source)
    """
    break_ = break
    """  #968 (line num in coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #969 (line num in coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #974 (line num in coconut source)
    return (e not in xs)  #975 (line num in coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'Maybe':  #977 (line num in coconut source)
    try:  #978 (line num in coconut source)
        return (((Just)((_coconut_iter_getitem((dropwhile)(lambda pair: pair[0] != key, assocs), (0)))[1])))  #979 (line num in coconut source)
    except StopIteration:  #986 (line num in coconut source)
        return (nothing)  #987 (line num in coconut source)



## Zipping and unzipping lists:
# type: ignore
zip: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]'  # type: ignore  #992 (line num in coconut source)
zip = _zip  # type: ignore  #993 (line num in coconut source)

zip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]'  #995 (line num in coconut source)
zip3 = _zip  #996 (line num in coconut source)

@_coconut_tco  #998 (line num in coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #998 (line num in coconut source)
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))  #999 (line num in coconut source)


@_coconut_tco  #1001 (line num in coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1001 (line num in coconut source)
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))  #1002 (line num in coconut source)


@_coconut_tco  #1004 (line num in coconut source)
def unzip(xs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]':  #1004 (line num in coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1005 (line num in coconut source)


unzip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]'  #1007 (line num in coconut source)
unzip3 = unzip  # type: ignore  #1008 (line num in coconut source)



## Functions on strings:
lines: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1013 (line num in coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1014 (line num in coconut source)

words: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1016 (line num in coconut source)
words = _coconut.operator.methodcaller("split")  #1017 (line num in coconut source)

@_coconut_tco  #1019 (line num in coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1019 (line num in coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1020 (line num in coconut source)


unwords: '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1022 (line num in coconut source)
unwords = " ".join  #1023 (line num in coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1031 (line num in coconut source)

Show = T.Any  #1033 (line num in coconut source)

showsPrec = NotImplemented  #1035 (line num in coconut source)

show: '_coconut.typing.Callable[[Ta], str]'  #1037 (line num in coconut source)
show = repr  #1038 (line num in coconut source)

def shows(x: 'Show') -> 'ShowS':  #1040 (line num in coconut source)
    return (lambda s: repr(x) + s)  #1041 (line num in coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1043 (line num in coconut source)
    return (lambda s: repr(list(xs)) + s)  #1044 (line num in coconut source)


def showString(x: 'str') -> 'ShowS':  #1046 (line num in coconut source)
    return (lambda s: x + s)  #1047 (line num in coconut source)


showChar: '_coconut.typing.Callable[[Char], ShowS]'  #1049 (line num in coconut source)
showChar = showString  #1050 (line num in coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1052 (line num in coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1053 (line num in coconut source)



## Converting from String:

ReadS = NotImplemented  #1061 (line num in coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1063 (line num in coconut source)

readsPrec = NotImplemented  #1074 (line num in coconut source)

readList = NotImplemented  #1076 (line num in coconut source)

reads = NotImplemented  #1078 (line num in coconut source)

readParen = NotImplemented  #1080 (line num in coconut source)

@_coconut_tco  #1082 (line num in coconut source)
def read(s: 'str') -> 'Read':  #1082 (line num in coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1083 (line num in coconut source)


lex = NotImplemented  #1085 (line num in coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1093 (line num in coconut source)
    _coconut_is_data = True  #1093 (line num in coconut source)
    __slots__ = ()  #1093 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1093 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1093 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1093 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #1093 (line num in coconut source)
    def __eq__(self, other):  #1093 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1093 (line num in coconut source)
    def __hash__(self):  #1093 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1093 (line num in coconut source)
    __match_args__ = ('io_func',)  #1093 (line num in coconut source)
    @staticmethod  #1094 (line num in coconut source)
    @_coconut_tco  #1095 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1095 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1096 (line num in coconut source)


    @staticmethod  #1098 (line num in coconut source)
    @_coconut_tco  #1099 (line num in coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1099 (line num in coconut source)
        def _coconut_lambda_0():  #1100 (line num in coconut source)
            raise IOError(msg)  #1100 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_lambda_0)  #1100 (line num in coconut source)


    @_coconut_tco  #1102 (line num in coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1102 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1103 (line num in coconut source)


    @_coconut_tco  #1105 (line num in coconut source)
    def __join__(self) -> 'IO':  #1105 (line num in coconut source)
        return _coconut_tail_call(_fmap, unIO, self)  #1106 (line num in coconut source)


    @staticmethod  #1108 (line num in coconut source)
    @_coconut_tco  #1109 (line num in coconut source)
    def __mempty__() -> 'IO':  #1109 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1110 (line num in coconut source)


    @_coconut_tco  #1112 (line num in coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1112 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1113 (line num in coconut source)


_nullIO: 'IO' = IO(lambda: None)  #1115 (line num in coconut source)

@_coconut_tco  #1117 (line num in coconut source)
def asIO(io: 'IO') -> 'IO':  #1117 (line num in coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1122 (line num in coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1123 (line num in coconut source)


@_coconut_tco  #1125 (line num in coconut source)
def unIO(io: 'IO') -> 'Ta':  #1125 (line num in coconut source)
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
    """  #1139 (line num in coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1140 (line num in coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1148 (line num in coconut source)
def putStr(s: 'str') -> 'IO':  #1148 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))  #1149 (line num in coconut source)


putChar: '_coconut.typing.Callable[[Char], IO]'  #1151 (line num in coconut source)
putChar = putStr  #1152 (line num in coconut source)

@_coconut_tco  #1154 (line num in coconut source)
def putStrLn(s: 'str') -> 'IO':  #1154 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))  #1155 (line num in coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1157 (line num in coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1157 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))  #1158 (line num in coconut source)


### Input functions:

getChar: 'IO' = IO(_coconut.functools.partial(sys.stdin.read, 1))  #1162 (line num in coconut source)

getLine: 'IO' = IO(input)  #1164 (line num in coconut source)

getContents: 'IO' = IO(sys.stdin.read)  #1166 (line num in coconut source)

@_coconut_tco  #1168 (line num in coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1168 (line num in coconut source)
    def do_interact():  #1169 (line num in coconut source)
        while True:  #1170 (line num in coconut source)
            (_print)((func)(input()))  #1171 (line num in coconut source)

    return _coconut_tail_call(IO, do_interact)  #1172 (line num in coconut source)


### Files:

FilePath = str  #1176 (line num in coconut source)

@_coconut_tco  #1178 (line num in coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1178 (line num in coconut source)
    def do_readFile() -> 'str':  #1179 (line num in coconut source)
        with open(fpath, "r+") as f:  #1180 (line num in coconut source)
            return (f.read())  #1181 (line num in coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1182 (line num in coconut source)


@_coconut_tco  #1184 (line num in coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1184 (line num in coconut source)
    def do_writeFile() -> 'None':  #1185 (line num in coconut source)
        with open(fpath, "w+") as f:  #1186 (line num in coconut source)
            f.write(text)  #1187 (line num in coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1188 (line num in coconut source)


@_coconut_tco  #1190 (line num in coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1190 (line num in coconut source)
    def do_appendFile() -> 'None':  #1191 (line num in coconut source)
        with open(fpath, "a+") as f:  #1192 (line num in coconut source)
            f.write(text)  #1193 (line num in coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1194 (line num in coconut source)


@_coconut_tco  #1196 (line num in coconut source)
def readIO(s: 'str') -> 'IO':  #1196 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))  #1197 (line num in coconut source)


@_coconut_tco  #1199 (line num in coconut source)
def readLn() -> 'IO':  #1199 (line num in coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1200 (line num in coconut source)



## Exception handling:

@_coconut_tco  #1205 (line num in coconut source)
def ioError(err: 'IOError') -> 'IO':  #1205 (line num in coconut source)
    def _coconut_lambda_1():  #1206 (line num in coconut source)
        raise err  #1206 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut_lambda_1)  #1206 (line num in coconut source)


@_coconut_tco  #1208 (line num in coconut source)
def userError(msg: 'str') -> 'IOError':  #1208 (line num in coconut source)
    return _coconut_tail_call(IOError, msg)  #1209 (line num in coconut source)
