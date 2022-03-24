#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x41ba6780

# Compiled with Coconut version 2.0.0-a_dev48 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
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
    """
    -- Nothing is the data type; use nothing for the canonical instance
    """  #60 (line num in coconut source)

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
    __match_args__ = ()  #62 (line num in coconut source)
nothing: 'Maybe' = Nothing()  #62 (line num in coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #64 (line num in coconut source)
    _coconut_is_data = True  #64 (line num in coconut source)
    __slots__ = ()  #64 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #64 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #64 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #64 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #64 (line num in coconut source)
    def __eq__(self, other):  #64 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #64 (line num in coconut source)
    def __hash__(self):  #64 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #64 (line num in coconut source)
    __match_args__ = ('x',)  #64 (line num in coconut source)

derivingOrd(Nothing, Just)  #66 (line num in coconut source)

if TYPE_CHECKING:  #68 (line num in coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #69 (line num in coconut source)
        ...  #70 (line num in coconut source)

else:  #71 (line num in coconut source)
    @_coconut_mark_as_match  #72 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #72 (line num in coconut source)
        _coconut_match_check_0 = False  #72 (line num in coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #72 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #72 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #72 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #72 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)  # type: ignore  #72 (line num in coconut source)
            _coconut_match_set_name_default = _coconut_match_temp_0  #72 (line num in coconut source)
            if not _coconut_match_kwargs:  #72 (line num in coconut source)
                _coconut_match_check_0 = True  #72 (line num in coconut source)
        if _coconut_match_check_0:  #72 (line num in coconut source)
            _coconut_match_check_0 = False  #72 (line num in coconut source)
            if not _coconut_match_check_0:  #72 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)) and (_coconut.len(_coconut_match_args[2]) == 0):  #72 (line num in coconut source)
                    _coconut_match_check_0 = True  #72 (line num in coconut source)

            if not _coconut_match_check_0:  #72 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #72 (line num in coconut source)
                    _coconut_match_check_0 = True  #72 (line num in coconut source)
                if _coconut_match_check_0:  #72 (line num in coconut source)
                    _coconut_match_check_0 = False  #72 (line num in coconut source)
                    if not _coconut_match_check_0:  #72 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #72 (line num in coconut source)
                            _coconut_match_check_0 = True  #72 (line num in coconut source)

                    if not _coconut_match_check_0:  #72 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #72 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Nothing, '__match_args__', ())  #72 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #72 (line num in coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #72 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 0:  #72 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #72 (line num in coconut source)
                            _coconut_match_check_0 = True  #72 (line num in coconut source)




        if _coconut_match_check_0:  #72 (line num in coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #72 (line num in coconut source)
                default = _coconut_match_set_name_default  #72 (line num in coconut source)
        if not _coconut_match_check_0:  #72 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #72 (line num in coconut source)

        return (default)  #72 (line num in coconut source)

    @_coconut_addpattern(maybe)  #73 (line num in coconut source)
    @_coconut_tco  #73 (line num in coconut source)
    @_coconut_mark_as_match  #73 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #73 (line num in coconut source)
        _coconut_match_check_1 = False  #73 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #73 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #73 (line num in coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #73 (line num in coconut source)
            _coconut_match_temp_4 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)  # type: ignore  #73 (line num in coconut source)
            _coconut_match_set_name_func = _coconut_match_temp_3  #73 (line num in coconut source)
            if not _coconut_match_kwargs:  #73 (line num in coconut source)
                _coconut_match_check_1 = True  #73 (line num in coconut source)
        if _coconut_match_check_1:  #73 (line num in coconut source)
            _coconut_match_check_1 = False  #73 (line num in coconut source)
            if not _coconut_match_check_1:  #73 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #73 (line num in coconut source)
                if (_coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) == 1):  #73 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #73 (line num in coconut source)
                    _coconut_match_check_1 = True  #73 (line num in coconut source)
                if _coconut_match_check_1:  #73 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line num in coconut source)
                        x = _coconut_match_set_name_x  #73 (line num in coconut source)

            if not _coconut_match_check_1:  #73 (line num in coconut source)
                if (not _coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #73 (line num in coconut source)
                    _coconut_match_check_1 = True  #73 (line num in coconut source)
                if _coconut_match_check_1:  #73 (line num in coconut source)
                    _coconut_match_check_1 = False  #73 (line num in coconut source)
                    if not _coconut_match_check_1:  #73 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #73 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #73 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #73 (line num in coconut source)
                            _coconut_match_check_1 = True  #73 (line num in coconut source)
                        if _coconut_match_check_1:  #73 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line num in coconut source)
                                x = _coconut_match_set_name_x  #73 (line num in coconut source)

                    if not _coconut_match_check_1:  #73 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #73 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #73 (line num in coconut source)
                            _coconut_match_temp_5 = _coconut.getattr(Just, '__match_args__', ())  #73 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_5, _coconut.tuple):  #73 (line num in coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #73 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_5) < 1:  #73 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_5),))  #73 (line num in coconut source)
                            _coconut_match_temp_6 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_5[0], _coconut_sentinel)  #73 (line num in coconut source)
                            if _coconut_match_temp_6 is not _coconut_sentinel:  #73 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_6  #73 (line num in coconut source)
                                _coconut_match_check_1 = True  #73 (line num in coconut source)
                        if _coconut_match_check_1:  #73 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line num in coconut source)
                                x = _coconut_match_set_name_x  #73 (line num in coconut source)




        if _coconut_match_check_1:  #73 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #73 (line num in coconut source)
                func = _coconut_match_set_name_func  #73 (line num in coconut source)
        if not _coconut_match_check_1:  #73 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #73 (line num in coconut source)

        return _coconut_tail_call(func, x)  #73 (line num in coconut source)

#### Either:

class Either:  #76 (line num in coconut source)
    @staticmethod  #77 (line num in coconut source)
    @_coconut_tco  #78 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #78 (line num in coconut source)
        return _coconut_tail_call(Right, x)  #78 (line num in coconut source)


    @staticmethod  #80 (line num in coconut source)
    @_coconut_tco  #81 (line num in coconut source)
    def __fail__(msg: 'str') -> 'Either':  #81 (line num in coconut source)
        return _coconut_tail_call(Left, msg)  #81 (line num in coconut source)


class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #83 (line num in coconut source)
    _coconut_is_data = True  #83 (line num in coconut source)
    __slots__ = ()  #83 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #83 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #83 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #83 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #83 (line num in coconut source)
    def __eq__(self, other):  #83 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #83 (line num in coconut source)
    def __hash__(self):  #83 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #83 (line num in coconut source)
    __match_args__ = ('x',)  #83 (line num in coconut source)
    @staticmethod  #84 (line num in coconut source)
    def __bool__() -> 'bool':  #85 (line num in coconut source)
        return (False)  #85 (line num in coconut source)


    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #87 (line num in coconut source)
        return (self)  #87 (line num in coconut source)


class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #89 (line num in coconut source)
    _coconut_is_data = True  #89 (line num in coconut source)
    __slots__ = ()  #89 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #89 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #89 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #89 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #89 (line num in coconut source)
    def __eq__(self, other):  #89 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #89 (line num in coconut source)
    def __hash__(self):  #89 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #89 (line num in coconut source)
    __match_args__ = ('x',)  #89 (line num in coconut source)

derivingOrd(Left, Right)  #91 (line num in coconut source)

if TYPE_CHECKING:  #93 (line num in coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #94 (line num in coconut source)
        ...  #95 (line num in coconut source)

else:  #96 (line num in coconut source)
    @_coconut_tco  #97 (line num in coconut source)
    @_coconut_mark_as_match  #97 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #97 (line num in coconut source)
        _coconut_match_check_2 = False  #97 (line num in coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #97 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #97 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #97 (line num in coconut source)
            _coconut_match_temp_7 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #97 (line num in coconut source)
            _coconut_match_temp_8 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)  # type: ignore  #97 (line num in coconut source)
            _coconut_match_set_name_left_func = _coconut_match_temp_7  #97 (line num in coconut source)
            if not _coconut_match_kwargs:  #97 (line num in coconut source)
                _coconut_match_check_2 = True  #97 (line num in coconut source)
        if _coconut_match_check_2:  #97 (line num in coconut source)
            _coconut_match_check_2 = False  #97 (line num in coconut source)
            if not _coconut_match_check_2:  #97 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #97 (line num in coconut source)
                if (_coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) == 1):  #97 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #97 (line num in coconut source)
                    _coconut_match_check_2 = True  #97 (line num in coconut source)
                if _coconut_match_check_2:  #97 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line num in coconut source)
                        x = _coconut_match_set_name_x  #97 (line num in coconut source)

            if not _coconut_match_check_2:  #97 (line num in coconut source)
                if (not _coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #97 (line num in coconut source)
                    _coconut_match_check_2 = True  #97 (line num in coconut source)
                if _coconut_match_check_2:  #97 (line num in coconut source)
                    _coconut_match_check_2 = False  #97 (line num in coconut source)
                    if not _coconut_match_check_2:  #97 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #97 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #97 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #97 (line num in coconut source)
                            _coconut_match_check_2 = True  #97 (line num in coconut source)
                        if _coconut_match_check_2:  #97 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line num in coconut source)
                                x = _coconut_match_set_name_x  #97 (line num in coconut source)

                    if not _coconut_match_check_2:  #97 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #97 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #97 (line num in coconut source)
                            _coconut_match_temp_9 = _coconut.getattr(Left, '__match_args__', ())  #97 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_9, _coconut.tuple):  #97 (line num in coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #97 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_9) < 1:  #97 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_9),))  #97 (line num in coconut source)
                            _coconut_match_temp_10 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_9[0], _coconut_sentinel)  #97 (line num in coconut source)
                            if _coconut_match_temp_10 is not _coconut_sentinel:  #97 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_10  #97 (line num in coconut source)
                                _coconut_match_check_2 = True  #97 (line num in coconut source)
                        if _coconut_match_check_2:  #97 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line num in coconut source)
                                x = _coconut_match_set_name_x  #97 (line num in coconut source)




        if _coconut_match_check_2:  #97 (line num in coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #97 (line num in coconut source)
                left_func = _coconut_match_set_name_left_func  #97 (line num in coconut source)
        if not _coconut_match_check_2:  #97 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #97 (line num in coconut source)

        return _coconut_tail_call(left_func, x)  #97 (line num in coconut source)

    @_coconut_addpattern(either)  #98 (line num in coconut source)
    @_coconut_tco  #98 (line num in coconut source)
    @_coconut_mark_as_match  #98 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #98 (line num in coconut source)
        _coconut_match_check_3 = False  #98 (line num in coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #98 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #98 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #98 (line num in coconut source)
            _coconut_match_temp_11 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #98 (line num in coconut source)
            _coconut_match_temp_12 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)  # type: ignore  #98 (line num in coconut source)
            _coconut_match_set_name_right_func = _coconut_match_temp_11  #98 (line num in coconut source)
            if not _coconut_match_kwargs:  #98 (line num in coconut source)
                _coconut_match_check_3 = True  #98 (line num in coconut source)
        if _coconut_match_check_3:  #98 (line num in coconut source)
            _coconut_match_check_3 = False  #98 (line num in coconut source)
            if not _coconut_match_check_3:  #98 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #98 (line num in coconut source)
                if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) == 1):  #98 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #98 (line num in coconut source)
                    _coconut_match_check_3 = True  #98 (line num in coconut source)
                if _coconut_match_check_3:  #98 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line num in coconut source)
                        x = _coconut_match_set_name_x  #98 (line num in coconut source)

            if not _coconut_match_check_3:  #98 (line num in coconut source)
                if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #98 (line num in coconut source)
                    _coconut_match_check_3 = True  #98 (line num in coconut source)
                if _coconut_match_check_3:  #98 (line num in coconut source)
                    _coconut_match_check_3 = False  #98 (line num in coconut source)
                    if not _coconut_match_check_3:  #98 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #98 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #98 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #98 (line num in coconut source)
                            _coconut_match_check_3 = True  #98 (line num in coconut source)
                        if _coconut_match_check_3:  #98 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line num in coconut source)
                                x = _coconut_match_set_name_x  #98 (line num in coconut source)

                    if not _coconut_match_check_3:  #98 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #98 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #98 (line num in coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(Right, '__match_args__', ())  #98 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #98 (line num in coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #98 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #98 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #98 (line num in coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_13[0], _coconut_sentinel)  #98 (line num in coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #98 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_14  #98 (line num in coconut source)
                                _coconut_match_check_3 = True  #98 (line num in coconut source)
                        if _coconut_match_check_3:  #98 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line num in coconut source)
                                x = _coconut_match_set_name_x  #98 (line num in coconut source)




        if _coconut_match_check_3:  #98 (line num in coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #98 (line num in coconut source)
                right_func = _coconut_match_set_name_right_func  #98 (line num in coconut source)
        if not _coconut_match_check_3:  #98 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #98 (line num in coconut source)

        return _coconut_tail_call(right_func, x)  #98 (line num in coconut source)

#### Ordering:

class Ordering:  #101 (line num in coconut source)
    @staticmethod  #102 (line num in coconut source)
    def __mempty__() -> 'Ordering':  #103 (line num in coconut source)
        return (eq)  #103 (line num in coconut source)


class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #105 (line num in coconut source)
    _coconut_is_data = True  #105 (line num in coconut source)
    __slots__ = ()  #105 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #105 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #105 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #105 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #105 (line num in coconut source)
    def __eq__(self, other):  #105 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #105 (line num in coconut source)
    def __hash__(self):  #105 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #105 (line num in coconut source)
    __match_args__ = ()  #105 (line num in coconut source)
    @staticmethod  #106 (line num in coconut source)
    def __bool__() -> 'bool':  #107 (line num in coconut source)
        return (True)  #107 (line num in coconut source)


class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #109 (line num in coconut source)
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

class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #111 (line num in coconut source)
    _coconut_is_data = True  #111 (line num in coconut source)
    __slots__ = ()  #111 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #111 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #111 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #111 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #111 (line num in coconut source)
    def __eq__(self, other):  #111 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #111 (line num in coconut source)
    def __hash__(self):  #111 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #111 (line num in coconut source)
    __match_args__ = ()  #111 (line num in coconut source)
    @staticmethod  #112 (line num in coconut source)
    def __bool__() -> 'bool':  #113 (line num in coconut source)
        return (True)  #113 (line num in coconut source)


derivingOrd(LT, EQ, GT)  #115 (line num in coconut source)
derivingBoundedEnum(LT, EQ, GT)  #116 (line num in coconut source)

lt: 'Ordering' = LT()  #118 (line num in coconut source)
eq: 'Ordering' = EQ()  #119 (line num in coconut source)
gt: 'Ordering' = GT()  #120 (line num in coconut source)

#### Char:
Char = T.NewType("Char", str)  #123 (line num in coconut source)

#### String:
String = str  #126 (line num in coconut source)


### Tuples:
fst: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]'  #130 (line num in coconut source)
fst = _coconut.operator.itemgetter((0))  #131 (line num in coconut source)

snd: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]'  #133 (line num in coconut source)
snd = _coconut.operator.itemgetter((1))  #134 (line num in coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #136 (line num in coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #139 (line num in coconut source)
    return (lambda *args: func(args))  # type: ignore  #140 (line num in coconut source)


def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]':  #142 (line num in coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #145 (line num in coconut source)
    return (lambda args: func(*args))  #146 (line num in coconut source)



## Basic type classes:

#### Eq:

Eq = object  #153 (line num in coconut source)

#### Ord:
Ord = Eq  #156 (line num in coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #157 (line num in coconut source)

if TYPE_CHECKING:  #159 (line num in coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #160 (line num in coconut source)
        ...  #161 (line num in coconut source)

else:  #162 (line num in coconut source)
    @_coconut_mark_as_match  #163 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #163 (line num in coconut source)
        _coconut_match_check_4 = False  #163 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #163 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #163 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #163 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #163 (line num in coconut source)
            _coconut_match_temp_15 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #163 (line num in coconut source)
            _coconut_match_temp_16 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #163 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_15  #163 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_16  #163 (line num in coconut source)
            if not _coconut_match_kwargs:  #163 (line num in coconut source)
                _coconut_match_check_4 = True  #163 (line num in coconut source)
        if _coconut_match_check_4:  #163 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #163 (line num in coconut source)
                x = _coconut_match_set_name_x  #163 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #163 (line num in coconut source)
                y = _coconut_match_set_name_y  #163 (line num in coconut source)
        if _coconut_match_check_4 and not (x == y):  #163 (line num in coconut source)
            _coconut_match_check_4 = False  #163 (line num in coconut source)
        if not _coconut_match_check_4:  #163 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #163 (line num in coconut source)

        return (eq)  #163 (line num in coconut source)

    @_coconut_addpattern(compare)  #164 (line num in coconut source)
    @_coconut_mark_as_match  #164 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #164 (line num in coconut source)
        _coconut_match_check_5 = False  #164 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #164 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #164 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #164 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #164 (line num in coconut source)
            _coconut_match_temp_17 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #164 (line num in coconut source)
            _coconut_match_temp_18 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #164 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_17  #164 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_18  #164 (line num in coconut source)
            if not _coconut_match_kwargs:  #164 (line num in coconut source)
                _coconut_match_check_5 = True  #164 (line num in coconut source)
        if _coconut_match_check_5:  #164 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #164 (line num in coconut source)
                x = _coconut_match_set_name_x  #164 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #164 (line num in coconut source)
                y = _coconut_match_set_name_y  #164 (line num in coconut source)
        if _coconut_match_check_5 and not (x < y):  #164 (line num in coconut source)
            _coconut_match_check_5 = False  #164 (line num in coconut source)
        if not _coconut_match_check_5:  #164 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #164 (line num in coconut source)

        return (lt)  #164 (line num in coconut source)

    @_coconut_addpattern(compare)  #165 (line num in coconut source)
    @_coconut_mark_as_match  #165 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #165 (line num in coconut source)
        _coconut_match_check_6 = False  #165 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #165 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #165 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #165 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #165 (line num in coconut source)
            _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #165 (line num in coconut source)
            _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #165 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_19  #165 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_20  #165 (line num in coconut source)
            if not _coconut_match_kwargs:  #165 (line num in coconut source)
                _coconut_match_check_6 = True  #165 (line num in coconut source)
        if _coconut_match_check_6:  #165 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #165 (line num in coconut source)
                x = _coconut_match_set_name_x  #165 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #165 (line num in coconut source)
                y = _coconut_match_set_name_y  #165 (line num in coconut source)
        if _coconut_match_check_6 and not (x > y):  #165 (line num in coconut source)
            _coconut_match_check_6 = False  #165 (line num in coconut source)
        if not _coconut_match_check_6:  #165 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #165 (line num in coconut source)

        return (gt)  #165 (line num in coconut source)


max: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #167 (line num in coconut source)
max = _max  #168 (line num in coconut source)

min: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #170 (line num in coconut source)
min = _min  #171 (line num in coconut source)

#### Enum:
Enum = Ord  #174 (line num in coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #175 (line num in coconut source)

succ: '_coconut.typing.Callable[[TEnum], TEnum]'  #177 (line num in coconut source)
succ = _coconut.functools.partial((_coconut.operator.add), 1)  #178 (line num in coconut source)

pred: '_coconut.typing.Callable[[TEnum], TEnum]'  #180 (line num in coconut source)
pred = _coconut_partial((_coconut_minus), {1: 1}, 2)  #181 (line num in coconut source)

toEnum = NotImplemented  #183 (line num in coconut source)

fromEnum: '_coconut.typing.Callable[[Enum], int]'  #185 (line num in coconut source)
fromEnum = _int  #186 (line num in coconut source)

@_coconut_tco  #188 (line num in coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #188 (line num in coconut source)
    return _coconut_tail_call(iterate, succ, first)  #189 (line num in coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #191 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #192 (line num in coconut source)
    return (iterate(_coconut.functools.partial((_coconut.operator.add), step), first) if step >= 0 else ())  # type: ignore  #193 (line num in coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #195 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #196 (line num in coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #197 (line num in coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #199 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #200 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #201 (line num in coconut source)
    steps = dist / step if step != 0 else 0  #202 (line num in coconut source)
    if steps < 0:  #203 (line num in coconut source)
        return (())  #204 (line num in coconut source)
    counter = iterate(_coconut.functools.partial((_coconut.operator.add), step), first)  #205 (line num in coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #206 (line num in coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #210 (line num in coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #211 (line num in coconut source)

@_coconut_tco  #213 (line num in coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #213 (line num in coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #217 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #219 (line num in coconut source)
        return (False)  # type: ignore  #220 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #223 (line num in coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #224 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #227 (line num in coconut source)


@_coconut_tco  #229 (line num in coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #229 (line num in coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #233 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #235 (line num in coconut source)
        return (True)  # type: ignore  #236 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #239 (line num in coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #240 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #243 (line num in coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #252 (line num in coconut source)

#### Integer:
Integer = int  #255 (line num in coconut source)

#### Float:
Float = float  #258 (line num in coconut source)

#### Double:
Double = float  #261 (line num in coconut source)

#### Rational:
Rational = _fractions.Fraction  #264 (line num in coconut source)

@_coconut_tco  #266 (line num in coconut source)
def over(x, y):  #266 (line num in coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #271 (line num in coconut source)
    return _coconut_tail_call(Rational, x, y)  #272 (line num in coconut source)

#### Word:

Word = Int  #275 (line num in coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #281 (line num in coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #282 (line num in coconut source)

negate: '_coconut.typing.Callable[[TNum], TNum]'  #284 (line num in coconut source)
negate = (_coconut_minus)  #285 (line num in coconut source)

abs: '_coconut.typing.Callable[[TNum], TNum]'  #287 (line num in coconut source)
abs = _abs  #288 (line num in coconut source)

if TYPE_CHECKING:  #290 (line num in coconut source)
    def signum(x: 'Num') -> 'int':  #291 (line num in coconut source)
        ...  #292 (line num in coconut source)

else:  #293 (line num in coconut source)
    @_coconut_mark_as_match  #294 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #294 (line num in coconut source)
        _coconut_match_check_7 = False  #294 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #294 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #294 (line num in coconut source)
            if _coconut_match_args[0] == 0:  #294 (line num in coconut source)
                if not _coconut_match_kwargs:  #294 (line num in coconut source)
                    _coconut_match_check_7 = True  #294 (line num in coconut source)
        if not _coconut_match_check_7:  #294 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #294 (line num in coconut source)

        return (0)  #294 (line num in coconut source)

    @_coconut_addpattern(signum)  #295 (line num in coconut source)
    @_coconut_mark_as_match  #295 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #295 (line num in coconut source)
        _coconut_match_check_8 = False  #295 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #295 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #295 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #295 (line num in coconut source)
            _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #295 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_21  #295 (line num in coconut source)
            if not _coconut_match_kwargs:  #295 (line num in coconut source)
                _coconut_match_check_8 = True  #295 (line num in coconut source)
        if _coconut_match_check_8:  #295 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #295 (line num in coconut source)
                x = _coconut_match_set_name_x  #295 (line num in coconut source)
        if _coconut_match_check_8 and not (x > 0):  #295 (line num in coconut source)
            _coconut_match_check_8 = False  #295 (line num in coconut source)
        if not _coconut_match_check_8:  #295 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #295 (line num in coconut source)

        return (1)  #295 (line num in coconut source)

    @_coconut_addpattern(signum)  #296 (line num in coconut source)
    @_coconut_mark_as_match  #296 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #296 (line num in coconut source)
        _coconut_match_check_9 = False  #296 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #296 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #296 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #296 (line num in coconut source)
            _coconut_match_temp_22 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #296 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_22  #296 (line num in coconut source)
            if not _coconut_match_kwargs:  #296 (line num in coconut source)
                _coconut_match_check_9 = True  #296 (line num in coconut source)
        if _coconut_match_check_9:  #296 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #296 (line num in coconut source)
                x = _coconut_match_set_name_x  #296 (line num in coconut source)
        if _coconut_match_check_9 and not (x < 0):  #296 (line num in coconut source)
            _coconut_match_check_9 = False  #296 (line num in coconut source)
        if not _coconut_match_check_9:  #296 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #296 (line num in coconut source)

        return (-1)  #296 (line num in coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #298 (line num in coconut source)
    return (x)  #298 (line num in coconut source)

#### Real:

Real = Num  #301 (line num in coconut source)

if TYPE_CHECKING:  #303 (line num in coconut source)
    def toRational(real: 'Real') -> 'Rational':  #304 (line num in coconut source)
        ...  #305 (line num in coconut source)

else:  #306 (line num in coconut source)
    @_coconut_tco  #307 (line num in coconut source)
    @_coconut_mark_as_match  #307 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #307 (line num in coconut source)
        _coconut_match_check_10 = False  #307 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #307 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #307 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #307 (line num in coconut source)
            _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #307 (line num in coconut source)
            if (isinstance)(_coconut_match_temp_23, float):  #307 (line num in coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_23  #307 (line num in coconut source)
                if not _coconut_match_kwargs:  #307 (line num in coconut source)
                    _coconut_match_check_10 = True  #307 (line num in coconut source)
        if _coconut_match_check_10:  #307 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #307 (line num in coconut source)
                real = _coconut_match_set_name_real  #307 (line num in coconut source)
        if not _coconut_match_check_10:  #307 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #307 (line num in coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #308 (line num in coconut source)

    @_coconut_addpattern(toRational)  #309 (line num in coconut source)
    @_coconut_tco  #309 (line num in coconut source)
    @_coconut_mark_as_match  #309 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #309 (line num in coconut source)
        _coconut_match_check_11 = False  #309 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #309 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #309 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #309 (line num in coconut source)
            _coconut_match_temp_24 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #309 (line num in coconut source)
            _coconut_match_set_name_real = _coconut_match_temp_24  #309 (line num in coconut source)
            if not _coconut_match_kwargs:  #309 (line num in coconut source)
                _coconut_match_check_11 = True  #309 (line num in coconut source)
        if _coconut_match_check_11:  #309 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #309 (line num in coconut source)
                real = _coconut_match_set_name_real  #309 (line num in coconut source)
        if not _coconut_match_check_11:  #309 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #309 (line num in coconut source)

        return _coconut_tail_call(Rational, real)  #310 (line num in coconut source)

#### Integral:

Integral = int  #313 (line num in coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #315 (line num in coconut source)
    divxy = x // y  #316 (line num in coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #317 (line num in coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #319 (line num in coconut source)
    modxy = x % y  #320 (line num in coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #321 (line num in coconut source)


div: '_coconut.typing.Callable[[int, int], int]'  #323 (line num in coconut source)
div = (_coconut.operator.floordiv)  #324 (line num in coconut source)

mod: '_coconut.typing.Callable[[int, int], int]'  #326 (line num in coconut source)
mod = (_coconut.operator.mod)  #327 (line num in coconut source)

def quotRem(x: 'int', y: 'int') -> 'T.Tuple[int, int]':  #329 (line num in coconut source)
    divxy, modxy = divmod(x, y)  #330 (line num in coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #331 (line num in coconut source)
    return (divxy + adj, modxy - y * adj)  #332 (line num in coconut source)


divMod = divmod  #334 (line num in coconut source)

toInteger: '_coconut.typing.Callable[[Integral], Integer]'  #336 (line num in coconut source)
toInteger = _int  #337 (line num in coconut source)

#### Fractional:
Fractional = Rational  #340 (line num in coconut source)

recip: '_coconut.typing.Callable[[Fractional], Fractional]'  #342 (line num in coconut source)
recip = _coconut.functools.partial((_coconut.operator.truediv), 1)  #343 (line num in coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #345 (line num in coconut source)
    return (x)  #345 (line num in coconut source)

#### Floating:

Floating = float  #348 (line num in coconut source)

from math import pi  #350 (line num in coconut source)
from math import exp  #350 (line num in coconut source)
from math import log  #350 (line num in coconut source)
from math import sqrt  #350 (line num in coconut source)
from math import sin  #350 (line num in coconut source)
from math import cos  #350 (line num in coconut source)
from math import tan  #350 (line num in coconut source)
from math import asin  #350 (line num in coconut source)
from math import acos  #350 (line num in coconut source)
from math import atan  #350 (line num in coconut source)
from math import sinh  #350 (line num in coconut source)
from math import cosh  #350 (line num in coconut source)
from math import tanh  #350 (line num in coconut source)
from math import asinh  #350 (line num in coconut source)
from math import acosh  #350 (line num in coconut source)
from math import atanh  #350 (line num in coconut source)

@_coconut_tco  #369 (line num in coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #369 (line num in coconut source)
    return _coconut_tail_call(log, x, base)  #370 (line num in coconut source)

#### RealFrac:

RealFrac = Rational  #373 (line num in coconut source)

def properFraction(x: 'RealFrac') -> 'T.Tuple[int, RealFrac]':  #375 (line num in coconut source)
    floor_x = floor(x)  #376 (line num in coconut source)
    return (floor_x, x - floor_x)  #377 (line num in coconut source)


truncate: '_coconut.typing.Callable[[RealFrac], int]'  #379 (line num in coconut source)
truncate = _int  #380 (line num in coconut source)

round: '_coconut.typing.Callable[[RealFrac], int]'  #382 (line num in coconut source)
round = _round  #383 (line num in coconut source)

ceiling: '_coconut.typing.Callable[[RealFrac], int]'  #385 (line num in coconut source)
ceiling = _ceil  #386 (line num in coconut source)

floor: '_coconut.typing.Callable[[RealFrac], int]'  #388 (line num in coconut source)
floor = _floor  #389 (line num in coconut source)

#### RealFloat:
RealFloat = float  #392 (line num in coconut source)

def floatRadix(x: 'float') -> 'int':  #394 (line num in coconut source)
    return (2)  #394 (line num in coconut source)


def floatDigits(x: 'float') -> 'int':  #396 (line num in coconut source)
    return (53)  #396 (line num in coconut source)


def floatRange(x: 'float') -> 'T.Tuple[int, int]':  #398 (line num in coconut source)
    return ((-1021, 1024))  #398 (line num in coconut source)


decodeFloat = NotImplemented  #400 (line num in coconut source)

encodeFloat = NotImplemented  #402 (line num in coconut source)

exponent = NotImplemented  #404 (line num in coconut source)

significand = NotImplemented  #406 (line num in coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #408 (line num in coconut source)
    return (x * 2**power)  #409 (line num in coconut source)


from math import isnan as isNaN  #411 (line num in coconut source)
from math import isinf as isInfinite  #411 (line num in coconut source)
from math import atan2  #411 (line num in coconut source)

isDenormalized = NotImplemented  #417 (line num in coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #419 (line num in coconut source)
    return (x == 0 and str(x).startswith("-"))  #420 (line num in coconut source)


def isIEEE(x: 'float') -> 'bool':  #422 (line num in coconut source)
    return (True)  #422 (line num in coconut source)


### Numeric functions:

def subtract(x, y):  #426 (line num in coconut source)
    return (y - x)  #427 (line num in coconut source)


def even(x: 'int') -> 'bool':  #429 (line num in coconut source)
    return (x % 2 == 0)  #430 (line num in coconut source)


def odd(x: 'int') -> 'bool':  #432 (line num in coconut source)
    return (x % 2 == 1)  #433 (line num in coconut source)


gcd: '_coconut.typing.Callable[[int, int], int]'  #435 (line num in coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #436 (line num in coconut source)

if TYPE_CHECKING:  #438 (line num in coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #439 (line num in coconut source)
        ...  #440 (line num in coconut source)

else:  #441 (line num in coconut source)
    @_coconut_mark_as_match  #442 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #442 (line num in coconut source)
        _coconut_match_check_12 = False  #442 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #442 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #442 (line num in coconut source)
            if _coconut_match_args[1] == 0:  #442 (line num in coconut source)
                if not _coconut_match_kwargs:  #442 (line num in coconut source)
                    _coconut_match_check_12 = True  #442 (line num in coconut source)
        if not _coconut_match_check_12:  #442 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #442 (line num in coconut source)

        return (0)  #442 (line num in coconut source)

    @_coconut_addpattern(lcm)  #443 (line num in coconut source)
    @_coconut_mark_as_match  #443 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #443 (line num in coconut source)
        _coconut_match_check_13 = False  #443 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #443 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #443 (line num in coconut source)
            if _coconut_match_args[0] == 0:  #443 (line num in coconut source)
                if not _coconut_match_kwargs:  #443 (line num in coconut source)
                    _coconut_match_check_13 = True  #443 (line num in coconut source)
        if not _coconut_match_check_13:  #443 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #443 (line num in coconut source)

        return (0)  #443 (line num in coconut source)

    @_coconut_addpattern(lcm)  #444 (line num in coconut source)
    @_coconut_mark_as_match  #444 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #444 (line num in coconut source)
        _coconut_match_check_14 = False  #444 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #444 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #444 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #444 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #444 (line num in coconut source)
            _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #444 (line num in coconut source)
            _coconut_match_temp_26 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #444 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_25  #444 (line num in coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_26  #444 (line num in coconut source)
            if not _coconut_match_kwargs:  #444 (line num in coconut source)
                _coconut_match_check_14 = True  #444 (line num in coconut source)
        if _coconut_match_check_14:  #444 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #444 (line num in coconut source)
                x = _coconut_match_set_name_x  #444 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #444 (line num in coconut source)
                y = _coconut_match_set_name_y  #444 (line num in coconut source)
        if not _coconut_match_check_14:  #444 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #444 (line num in coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #445 (line num in coconut source)


fromIntegral: '_coconut.typing.Callable[[Integral], Num]'  #447 (line num in coconut source)
fromIntegral = fromInteger  #448 (line num in coconut source)

realToFrac: '_coconut.typing.Callable[[Real], Fractional]'  #450 (line num in coconut source)
realToFrac = toRational  #451 (line num in coconut source)



## Monoids:
Monoid = T.Iterable  #456 (line num in coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #457 (line num in coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #459 (line num in coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #462 (line num in coconut source)
    _coconut_is_data = True  #463 (line num in coconut source)
    __slots__ = ()  #463 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #463 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #463 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #463 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #463 (line num in coconut source)
    def __eq__(self, other):  #463 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #463 (line num in coconut source)
    def __hash__(self):  #463 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #463 (line num in coconut source)
    __match_args__ = ()  #463 (line num in coconut source)
    @staticmethod  #463 (line num in coconut source)
    @_coconut_tco  #464 (line num in coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #464 (line num in coconut source)
        if (hasattr)(M, "__mempty__"):  #465 (line num in coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #466 (line num in coconut source)
        return _coconut_tail_call(makedata, type(M))  #467 (line num in coconut source)


mempty: 'T.Any' = Mempty()  #469 (line num in coconut source)

@_coconut_tco  #471 (line num in coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #471 (line num in coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #476 (line num in coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #478 (line num in coconut source)
    y = (asTypeOf)(y, x)  #479 (line num in coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #482 (line num in coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #483 (line num in coconut source)

# Default implementation
    if not x:  #486 (line num in coconut source)
        return (y)  #487 (line num in coconut source)
    if not y:  #488 (line num in coconut source)
        return (x)  #489 (line num in coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #490 (line num in coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #491 (line num in coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #492 (line num in coconut source)


@_coconut_tco  #494 (line num in coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #494 (line num in coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #495 (line num in coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #502 (line num in coconut source)

@_coconut_tco  # type: ignore  #504 (line num in coconut source)
def fmap(f: '_coconut.typing.Callable[[Ta], Tb]', xs: 'Functor[Ta]') -> 'Functor[Tb]':  # type: ignore  #504 (line num in coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #507 (line num in coconut source)
    try:  #508 (line num in coconut source)
# Default implementation
        return (_fmap(f, xs))  #510 (line num in coconut source)

    except TypeError:  #512 (line num in coconut source)
# Function instance
        if callable(xs):  #514 (line num in coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #515 (line num in coconut source)

        raise  #517 (line num in coconut source)


@_coconut_tco  #519 (line num in coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #519 (line num in coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #523 (line num in coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #524 (line num in coconut source)

#### Applicative:

Applicative = Functor  #527 (line num in coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #528 (line num in coconut source)

if TYPE_CHECKING:  #530 (line num in coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #531 (line num in coconut source)
        ...  #532 (line num in coconut source)

else:  #533 (line num in coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #534 (line num in coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #538 (line num in coconut source)

        _coconut_is_data = True  #540 (line num in coconut source)
        __slots__ = ()  #540 (line num in coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #540 (line num in coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #540 (line num in coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #540 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #540 (line num in coconut source)
        def __eq__(self, other):  #540 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #540 (line num in coconut source)
        def __hash__(self):  #540 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #540 (line num in coconut source)
        __match_args__ = ('val',)  #540 (line num in coconut source)
        def __join__(self) -> 'T.Any':  #540 (line num in coconut source)
            return (self.val)  #540 (line num in coconut source)


        def __call__(self, arg: 'T.Any') -> 'T.Any':  #542 (line num in coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #543 (line num in coconut source)
            return (self.val)  #544 (line num in coconut source)


        @_coconut_tco  #546 (line num in coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #546 (line num in coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #548 (line num in coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #549 (line num in coconut source)

            try:  #551 (line num in coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #553 (line num in coconut source)

            except TypeError:  #555 (line num in coconut source)
# Check for functions
                if callable(M):  #557 (line num in coconut source)
                    return _coconut_tail_call(const, self.val)  #558 (line num in coconut source)

# Fallback
                raise  #561 (line num in coconut source)


@_coconut_tco  #563 (line num in coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #563 (line num in coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #570 (line num in coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #572 (line num in coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #573 (line num in coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #576 (line num in coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #577 (line num in coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  #580 (line num in coconut source)


@_coconut_tco  #582 (line num in coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #582 (line num in coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #586 (line num in coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #587 (line num in coconut source)


@_coconut_tco  #589 (line num in coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #589 (line num in coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #593 (line num in coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #594 (line num in coconut source)


def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #596 (line num in coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #600 (line num in coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2))  # type: ignore  #601 (line num in coconut source)

#### Monad:

Monad = Applicative  #604 (line num in coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #605 (line num in coconut source)

@_coconut_tco  #607 (line num in coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #607 (line num in coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #612 (line num in coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #613 (line num in coconut source)


@_coconut_tco  #615 (line num in coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #615 (line num in coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #619 (line num in coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #620 (line num in coconut source)


return_ = pure  #622 (line num in coconut source)

if TYPE_CHECKING:  #624 (line num in coconut source)
    def fail(msg: 'str') -> 'T.Any':  #625 (line num in coconut source)
        ...  #626 (line num in coconut source)

else:  #627 (line num in coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #628 (line num in coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #631 (line num in coconut source)

        _coconut_is_data = True  #633 (line num in coconut source)
        __slots__ = ()  #633 (line num in coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #633 (line num in coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #633 (line num in coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #633 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #633 (line num in coconut source)
        def __eq__(self, other):  #633 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #633 (line num in coconut source)
        def __hash__(self):  #633 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #633 (line num in coconut source)
        __match_args__ = ('msg',)  #633 (line num in coconut source)
        @staticmethod  #633 (line num in coconut source)
        def __bool__() -> 'bool':  #634 (line num in coconut source)
            return (False)  #634 (line num in coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #636 (line num in coconut source)
            return (self)  #636 (line num in coconut source)


        @_coconut_tco  #638 (line num in coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #638 (line num in coconut source)
            if (hasattr)(M, "__fail__"):  #639 (line num in coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #640 (line num in coconut source)
            return _coconut_tail_call(makedata, type(M))  #641 (line num in coconut source)

# sequence_ and mapM_ defined in Foldable


@_coconut_tco  #645 (line num in coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #645 (line num in coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #649 (line num in coconut source)
    return _coconut_tail_call((bind), m, func)  #650 (line num in coconut source)


@_coconut_tco  #652 (line num in coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #652 (line num in coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #659 (line num in coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #661 (line num in coconut source)
    _coconut_match_check_15 = False  #661 (line num in coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #661 (line num in coconut source)
        _coconut_match_check_15 = True  #661 (line num in coconut source)
    if _coconut_match_check_15:  #661 (line num in coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #662 (line num in coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #665 (line num in coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #668 (line num in coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #669 (line num in coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  #672 (line num in coconut source)
    _coconut_case_match_check_0 = False  #672 (line num in coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #672 (line num in coconut source)
        _coconut_case_match_check_0 = True  #672 (line num in coconut source)
    if _coconut_case_match_check_0:  #672 (line num in coconut source)
        if not ms:  #676 (line num in coconut source)
            return (ms)  # type: ignore  #677 (line num in coconut source)
        vals = []  # type: ignore  #678 (line num in coconut source)
        fallback = ms  #679 (line num in coconut source)
        for m in ms:  #680 (line num in coconut source)
            if m:  #681 (line num in coconut source)
                vals.extend(m)  # type: ignore  #682 (line num in coconut source)
            else:  #683 (line num in coconut source)
                fallback = m  # type: ignore  #684 (line num in coconut source)
        if not vals:  #685 (line num in coconut source)
            return (fallback)  # type: ignore  #686 (line num in coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  #687 (line num in coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #690 (line num in coconut source)
        _coconut_case_match_check_0 = True  #690 (line num in coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #690 (line num in coconut source)
            _coconut_case_match_check_0 = False  #690 (line num in coconut source)
        if _coconut_case_match_check_0:  #690 (line num in coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #691 (line num in coconut source)

    if not _coconut_case_match_check_0:  #693 (line num in coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #694 (line num in coconut source)


if TYPE_CHECKING:  #696 (line num in coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]') -> 'TMonad':  #697 (line num in coconut source)
        ...  #698 (line num in coconut source)

else:  #699 (line num in coconut source)
    @_coconut_tco  #700 (line num in coconut source)
    @_coconut_mark_as_match  #700 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #700 (line num in coconut source)
        _coconut_match_check_16 = False  #700 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #700 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #700 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #700 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #700 (line num in coconut source)
                _coconut_match_temp_27 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #700 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_27  #700 (line num in coconut source)
                if not _coconut_match_kwargs:  #700 (line num in coconut source)
                    _coconut_match_check_16 = True  #700 (line num in coconut source)
        if _coconut_match_check_16:  #700 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #700 (line num in coconut source)
                func = _coconut_match_set_name_func  #700 (line num in coconut source)
        if not _coconut_match_check_16:  #700 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #700 (line num in coconut source)

        return _coconut_tail_call(func)  #700 (line num in coconut source)

    @_coconut_addpattern(do)  #701 (line num in coconut source)
    @_coconut_tco  #701 (line num in coconut source)
    @_coconut_mark_as_match  #701 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #701 (line num in coconut source)
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
        """  #720 (line num in coconut source)
        _coconut_match_check_17 = False  #721 (line num in coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #721 (line num in coconut source)
        _coconut_match_set_name_ms = _coconut_sentinel  #721 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #721 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #721 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #721 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #721 (line num in coconut source)
                _coconut_match_set_name_m = _coconut_match_args[0][0]  #721 (line num in coconut source)
                _coconut_match_temp_29 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #721 (line num in coconut source)
                _coconut_match_temp_28 = _coconut.list(_coconut_match_args[0][1:])  #721 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_29  #721 (line num in coconut source)
                _coconut_match_set_name_ms = _coconut_match_temp_28  #721 (line num in coconut source)
                if not _coconut_match_kwargs:  #721 (line num in coconut source)
                    _coconut_match_check_17 = True  #721 (line num in coconut source)
        if _coconut_match_check_17:  #721 (line num in coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #721 (line num in coconut source)
                m = _coconut_match_set_name_m  #721 (line num in coconut source)
            if _coconut_match_set_name_ms is not _coconut_sentinel:  #721 (line num in coconut source)
                ms = _coconut_match_set_name_ms  #721 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #721 (line num in coconut source)
                func = _coconut_match_set_name_func  #721 (line num in coconut source)
        if not _coconut_match_check_17:  #721 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #721 (line num in coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))  #721 (line num in coconut source)



## Folds and traversals:

#### Foldable:

Foldable = T.Sequence  #728 (line num in coconut source)

@_coconut_tco  #730 (line num in coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #730 (line num in coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #731 (line num in coconut source)


mapM_: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #733 (line num in coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #734 (line num in coconut source)

@_coconut_tco  #736 (line num in coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #736 (line num in coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #737 (line num in coconut source)


@_coconut_tco  #739 (line num in coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #739 (line num in coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #740 (line num in coconut source)


@_coconut_tco  #742 (line num in coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #742 (line num in coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #743 (line num in coconut source)


foldl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #745 (line num in coconut source)
foldl1 = reduce  #746 (line num in coconut source)

@_coconut_tco  #748 (line num in coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #748 (line num in coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #749 (line num in coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #751 (line num in coconut source)
    return (len(xs) == 0)  #752 (line num in coconut source)


length: '_coconut.typing.Callable[[Foldable], int]'  #754 (line num in coconut source)
length = len  #755 (line num in coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #757 (line num in coconut source)
    return (e in xs)  #758 (line num in coconut source)


maximum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #760 (line num in coconut source)
maximum = _max  #761 (line num in coconut source)

minimum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #763 (line num in coconut source)
minimum = _min  #764 (line num in coconut source)

sum: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #766 (line num in coconut source)
sum = _sum  #767 (line num in coconut source)

product: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #769 (line num in coconut source)
product = _coconut.functools.partial(reduce, _coconut.operator.mul)  #770 (line num in coconut source)

#### Traversable:
Traversable = T.Iterable  #773 (line num in coconut source)

@_coconut_tco  #775 (line num in coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #775 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #776 (line num in coconut source)


@_coconut_tco  #778 (line num in coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #778 (line num in coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #779 (line num in coconut source)


traverse: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #781 (line num in coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  #782 (line num in coconut source)

sequence: '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #784 (line num in coconut source)
sequence = sequenceA  #785 (line num in coconut source)

mapM: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #787 (line num in coconut source)
mapM = traverse  #788 (line num in coconut source)



## Miscellaneous functions:
id: '_coconut.typing.Callable[[Ta], Ta]' = ident  #793 (line num in coconut source)

@_coconut_tco  #795 (line num in coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #795 (line num in coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #799 (line num in coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #800 (line num in coconut source)


if TYPE_CHECKING:  #802 (line num in coconut source)
    @T.overload  #803 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #804 (line num in coconut source)
        ...  #805 (line num in coconut source)

    @T.overload  #806 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #807 (line num in coconut source)
        ...  #808 (line num in coconut source)

    @T.overload  #809 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #810 (line num in coconut source)
        ...  #811 (line num in coconut source)

    @T.overload  #812 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta') -> 'T.Any':  #813 (line num in coconut source)
        ...  #814 (line num in coconut source)

    def apply(func, arg):  #815 (line num in coconut source)
        ...  #816 (line num in coconut source)

else:  #817 (line num in coconut source)
    @_coconut_tco  #818 (line num in coconut source)
    def apply(func, arg):  #818 (line num in coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #824 (line num in coconut source)
        return _coconut_tail_call((of), func, arg)  #825 (line num in coconut source)


@_coconut_tco  #827 (line num in coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #827 (line num in coconut source)
    while True:  #828 (line num in coconut source)
        if cond(x):  #828 (line num in coconut source)
            return (x)  #829 (line num in coconut source)
        try:  # tail recursive  #830 (line num in coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_71  # tail recursive  #830 (line num in coconut source)
        except _coconut.NameError:  # tail recursive  #830 (line num in coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #830 (line num in coconut source)
        if _coconut_tre_check_0:  # tail recursive  #830 (line num in coconut source)
            cond, func, x = cond, func, func(x)  # tail recursive  #830 (line num in coconut source)
            continue  # tail recursive  #830 (line num in coconut source)
        else:  # tail recursive  #830 (line num in coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #831 (line num in coconut source)
        return None  #832 (line num in coconut source)

_coconut_recursive_func_71 = until  #832 (line num in coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #832 (line num in coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #836 (line num in coconut source)
    if TYPE_CHECKING:  #837 (line num in coconut source)
        return (x)  #837 (line num in coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #839 (line num in coconut source)
        for i in (takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count()):  #840 (line num in coconut source)
            if (isinstance)(x, pure):  #841 (line num in coconut source)
                x = x.pure_as(y)  #842 (line num in coconut source)
            elif (isinstance)(x, fail):  #843 (line num in coconut source)
                x = x.fail_as(y)  #844 (line num in coconut source)
            elif (isinstance)(x, Mempty):  #845 (line num in coconut source)
                x = x.mempty_as(y)  #846 (line num in coconut source)
            else:  #847 (line num in coconut source)
                break  #848 (line num in coconut source)
    return (x)  #849 (line num in coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #851 (line num in coconut source)

def error(msg: 'str') -> 'None':  #853 (line num in coconut source)
    raise Exception(msg)  #854 (line num in coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #856 (line num in coconut source)
    raise Exception(msg) from None  #857 (line num in coconut source)


undefined: 'T.Any' = None  #859 (line num in coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #861 (line num in coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #864 (line num in coconut source)
    return (y)  #865 (line num in coconut source)


@_coconut_tco  #867 (line num in coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #867 (line num in coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #872 (line num in coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #873 (line num in coconut source)




# List operations:

@_coconut_tco  #879 (line num in coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #879 (line num in coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #883 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #884 (line num in coconut source)

# type: ignore
map: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #886 (line num in coconut source)
map = _map  # type: ignore  #887 (line num in coconut source)

@_coconut_tco  #889 (line num in coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #889 (line num in coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #893 (line num in coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #894 (line num in coconut source)

# type: ignore
filter: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #896 (line num in coconut source)
filter = _filter  # type: ignore  #897 (line num in coconut source)

head: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #899 (line num in coconut source)
head = _coconut.functools.partial(_coconut_iter_getitem, index=(0))  #900 (line num in coconut source)

last: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #902 (line num in coconut source)
last = _coconut.functools.partial(_coconut_iter_getitem, index=(-1))  #903 (line num in coconut source)

tail: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #905 (line num in coconut source)
tail = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #906 (line num in coconut source)

init: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #908 (line num in coconut source)
init = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #909 (line num in coconut source)

@_coconut_tco  #911 (line num in coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #911 (line num in coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #915 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #916 (line num in coconut source)


reverse: '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #918 (line num in coconut source)
reverse = _reversed  #919 (line num in coconut source)



## Special folds:
and_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #924 (line num in coconut source)
and_ = _all  #925 (line num in coconut source)

or_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #927 (line num in coconut source)
or_ = _any  #928 (line num in coconut source)

any: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #930 (line num in coconut source)
any = _coconut_forward_compose(map, or_)  #931 (line num in coconut source)

all: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #933 (line num in coconut source)
all = _coconut_forward_compose(map, and_)  #934 (line num in coconut source)

@_coconut_tco  #936 (line num in coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #936 (line num in coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #937 (line num in coconut source)


concatMap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #939 (line num in coconut source)
concatMap = _coconut_forward_compose(map, concat)  #940 (line num in coconut source)



## Building lists:

### Scans:
@_coconut_tco  #947 (line num in coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #947 (line num in coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #948 (line num in coconut source)


scanl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #950 (line num in coconut source)
scanl1 = scan  #951 (line num in coconut source)

@_coconut_tco  #953 (line num in coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #953 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #954 (line num in coconut source)


@_coconut_tco  #956 (line num in coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #956 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #957 (line num in coconut source)

### Infinite lists:

@recursive_iterator  #960 (line num in coconut source)
@_coconut_tco  #961 (line num in coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #961 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #962 (line num in coconut source)


@recursive_iterator  #964 (line num in coconut source)
@_coconut_tco  #965 (line num in coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #965 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #966 (line num in coconut source)


@_coconut_tco  #968 (line num in coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #968 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #969 (line num in coconut source)


if TYPE_CHECKING:  #971 (line num in coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #972 (line num in coconut source)
        ...  #973 (line num in coconut source)

else:  #974 (line num in coconut source)
    @recursive_iterator  #975 (line num in coconut source)
    @_coconut_tco  #976 (line num in coconut source)
    @_coconut_mark_as_match  #976 (line num in coconut source)
    def cycle(*_coconut_match_args, **_coconut_match_kwargs):  #976 (line num in coconut source)
        _coconut_match_check_18 = False  #976 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #976 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #976 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #976 (line num in coconut source)
            _coconut_match_temp_30 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #976 (line num in coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_30  #976 (line num in coconut source)
            if not _coconut_match_kwargs:  #976 (line num in coconut source)
                _coconut_match_check_18 = True  #976 (line num in coconut source)
        if _coconut_match_check_18:  #976 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #976 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #976 (line num in coconut source)
        if _coconut_match_check_18 and not (len(xs) > 0):  #976 (line num in coconut source)
            _coconut_match_check_18 = False  #976 (line num in coconut source)
        if not _coconut_match_check_18:  #976 (line num in coconut source)
            raise _coconut_FunctionMatchError('def cycle(xs if len(xs) > 0) =', _coconut_match_args)  #976 (line num in coconut source)

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))  #977 (line num in coconut source)



## Sublists:

@_coconut_tco  #982 (line num in coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #982 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #983 (line num in coconut source)


@_coconut_tco  #985 (line num in coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #985 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #986 (line num in coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> 'T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]':  #988 (line num in coconut source)
    reit = reiterable(xs)  #989 (line num in coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #990 (line num in coconut source)


takeWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #992 (line num in coconut source)
takeWhile = takewhile  #993 (line num in coconut source)

dropWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #995 (line num in coconut source)
dropWhile = dropwhile  #996 (line num in coconut source)

if TYPE_CHECKING:  #998 (line num in coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]':  #999 (line num in coconut source)
        ...  #1000 (line num in coconut source)

else:  #1001 (line num in coconut source)
    @_coconut_mark_as_match  #1002 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1002 (line num in coconut source)
        _coconut_match_check_19 = False  #1002 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1002 (line num in coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #1002 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1002 (line num in coconut source)
                if not _coconut_match_kwargs:  #1002 (line num in coconut source)
                    _coconut_match_check_19 = True  #1002 (line num in coconut source)
        if not _coconut_match_check_19:  #1002 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #1002 (line num in coconut source)

        return (([], []))  #1002 (line num in coconut source)

    @_coconut_addpattern(span)  #1003 (line num in coconut source)
    @_coconut_mark_as_match  #1003 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1003 (line num in coconut source)
        _coconut_match_check_20 = False  #1003 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1003 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #1003 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1003 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1003 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1003 (line num in coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1003 (line num in coconut source)
                _coconut_match_temp_31 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1003 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_args[1][0]  #1003 (line num in coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_31  #1003 (line num in coconut source)
                _coconut_match_temp_32 = _coconut.list(_coconut_match_args[1][1:])  #1003 (line num in coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_32  #1003 (line num in coconut source)
                if not _coconut_match_kwargs:  #1003 (line num in coconut source)
                    _coconut_match_check_20 = True  #1003 (line num in coconut source)
        if _coconut_match_check_20:  #1003 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1003 (line num in coconut source)
                cond = _coconut_match_set_name_cond  #1003 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #1003 (line num in coconut source)
                x = _coconut_match_set_name_x  #1003 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1003 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #1003 (line num in coconut source)
        if _coconut_match_check_20 and not (cond(x)):  #1003 (line num in coconut source)
            _coconut_match_check_20 = False  #1003 (line num in coconut source)
        if not _coconut_match_check_20:  #1003 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #1003 (line num in coconut source)

        ys, zs = span(cond, xs)  #1004 (line num in coconut source)
        return (([x,] + ys, zs))  #1005 (line num in coconut source)

    @_coconut_addpattern(span)  #1006 (line num in coconut source)
    @_coconut_mark_as_match  #1006 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1006 (line num in coconut source)
        _coconut_match_check_21 = False  #1006 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1006 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1006 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1006 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1006 (line num in coconut source)
            _coconut_match_temp_33 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1006 (line num in coconut source)
            _coconut_match_temp_34 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1006 (line num in coconut source)
            _coconut_match_set_name_cond = _coconut_match_temp_33  #1006 (line num in coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_34  #1006 (line num in coconut source)
            if not _coconut_match_kwargs:  #1006 (line num in coconut source)
                _coconut_match_check_21 = True  #1006 (line num in coconut source)
        if _coconut_match_check_21:  #1006 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1006 (line num in coconut source)
                cond = _coconut_match_set_name_cond  #1006 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1006 (line num in coconut source)
                xs = _coconut_match_set_name_xs  #1006 (line num in coconut source)
        if not _coconut_match_check_21:  #1006 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #1006 (line num in coconut source)

        return (([], xs))  #1007 (line num in coconut source)


@_coconut_tco  #1009 (line num in coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #1009 (line num in coconut source)
    """
    break_ = break
    """  #1012 (line num in coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1013 (line num in coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #1018 (line num in coconut source)
    return (e not in xs)  #1019 (line num in coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'Maybe':  #1021 (line num in coconut source)
    try:  #1022 (line num in coconut source)
        return (((Just)((_coconut_iter_getitem((dropwhile)(lambda pair: pair[0] != key, assocs), (0)))[1])))  #1023 (line num in coconut source)
    except IndexError:  #1030 (line num in coconut source)
        return (nothing)  #1031 (line num in coconut source)



## Zipping and unzipping lists:
# type: ignore
zip: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]'  # type: ignore  #1036 (line num in coconut source)
zip = _zip  # type: ignore  #1037 (line num in coconut source)

zip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]'  #1039 (line num in coconut source)
zip3 = _zip  #1040 (line num in coconut source)

@_coconut_tco  #1042 (line num in coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #1042 (line num in coconut source)
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))  #1043 (line num in coconut source)


@_coconut_tco  #1045 (line num in coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1045 (line num in coconut source)
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))  #1046 (line num in coconut source)


@_coconut_tco  #1048 (line num in coconut source)
def unzip(xs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]':  #1048 (line num in coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1049 (line num in coconut source)


unzip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]'  #1051 (line num in coconut source)
unzip3 = unzip  # type: ignore  #1052 (line num in coconut source)



## Functions on strings:
lines: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1057 (line num in coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1058 (line num in coconut source)

words: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1060 (line num in coconut source)
words = _coconut.operator.methodcaller("split")  #1061 (line num in coconut source)

@_coconut_tco  #1063 (line num in coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1063 (line num in coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1064 (line num in coconut source)


unwords: '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1066 (line num in coconut source)
unwords = " ".join  #1067 (line num in coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1075 (line num in coconut source)

Show = T.Any  #1077 (line num in coconut source)

showsPrec = NotImplemented  #1079 (line num in coconut source)

show: '_coconut.typing.Callable[[Ta], str]'  #1081 (line num in coconut source)
show = repr  #1082 (line num in coconut source)

def shows(x: 'Show') -> 'ShowS':  #1084 (line num in coconut source)
    return (lambda s: repr(x) + s)  #1085 (line num in coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1087 (line num in coconut source)
    return (lambda s: repr(list(xs)) + s)  #1088 (line num in coconut source)


def showString(x: 'str') -> 'ShowS':  #1090 (line num in coconut source)
    return (lambda s: x + s)  #1091 (line num in coconut source)


showChar: '_coconut.typing.Callable[[Char], ShowS]'  #1093 (line num in coconut source)
showChar = showString  #1094 (line num in coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1096 (line num in coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1097 (line num in coconut source)



## Converting from String:

ReadS = NotImplemented  #1105 (line num in coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1107 (line num in coconut source)

readsPrec = NotImplemented  #1118 (line num in coconut source)

readList = NotImplemented  #1120 (line num in coconut source)

reads = NotImplemented  #1122 (line num in coconut source)

readParen = NotImplemented  #1124 (line num in coconut source)

@_coconut_tco  #1126 (line num in coconut source)
def read(s: 'str') -> 'Read':  #1126 (line num in coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1127 (line num in coconut source)


lex = NotImplemented  #1129 (line num in coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1137 (line num in coconut source)
    _coconut_is_data = True  #1137 (line num in coconut source)
    __slots__ = ()  #1137 (line num in coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1137 (line num in coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1137 (line num in coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1137 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #1137 (line num in coconut source)
    def __eq__(self, other):  #1137 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1137 (line num in coconut source)
    def __hash__(self):  #1137 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1137 (line num in coconut source)
    __match_args__ = ('io_func',)  #1137 (line num in coconut source)
    @staticmethod  #1138 (line num in coconut source)
    @_coconut_tco  #1139 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1139 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1140 (line num in coconut source)


    @staticmethod  #1142 (line num in coconut source)
    @_coconut_tco  #1143 (line num in coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1143 (line num in coconut source)
        def _coconut_lambda_0():  #1144 (line num in coconut source)
            raise IOError(msg)  #1144 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_lambda_0)  #1144 (line num in coconut source)


    @_coconut_tco  #1146 (line num in coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1146 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1147 (line num in coconut source)


    @_coconut_tco  #1149 (line num in coconut source)
    def __join__(self) -> 'IO':  #1149 (line num in coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1150 (line num in coconut source)


    @staticmethod  #1152 (line num in coconut source)
    @_coconut_tco  #1153 (line num in coconut source)
    def __mempty__() -> 'IO':  #1153 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1154 (line num in coconut source)


    @_coconut_tco  #1156 (line num in coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1156 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1157 (line num in coconut source)


_nullIO: 'IO' = IO(lambda: None)  #1159 (line num in coconut source)

@_coconut_tco  #1161 (line num in coconut source)
def asIO(io: 'IO') -> 'IO':  #1161 (line num in coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1166 (line num in coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1167 (line num in coconut source)


@_coconut_tco  #1169 (line num in coconut source)
def unIO(io: 'IO') -> 'Ta':  #1169 (line num in coconut source)
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
    """  #1183 (line num in coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1184 (line num in coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1192 (line num in coconut source)
def putStr(s: 'str') -> 'IO':  #1192 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))  #1193 (line num in coconut source)


putChar: '_coconut.typing.Callable[[Char], IO]'  #1195 (line num in coconut source)
putChar = putStr  #1196 (line num in coconut source)

@_coconut_tco  #1198 (line num in coconut source)
def putStrLn(s: 'str') -> 'IO':  #1198 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))  #1199 (line num in coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1201 (line num in coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1201 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))  #1202 (line num in coconut source)


### Input functions:

getChar: 'IO' = IO(_coconut.functools.partial(sys.stdin.read, 1))  #1206 (line num in coconut source)

getLine: 'IO' = IO(input)  #1208 (line num in coconut source)

getContents: 'IO' = IO(sys.stdin.read)  #1210 (line num in coconut source)

@_coconut_tco  #1212 (line num in coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1212 (line num in coconut source)
    def do_interact():  #1213 (line num in coconut source)
        while True:  #1214 (line num in coconut source)
            (_print)((func)(input()))  #1215 (line num in coconut source)

    return _coconut_tail_call(IO, do_interact)  #1216 (line num in coconut source)


### Files:

FilePath = str  #1220 (line num in coconut source)

@_coconut_tco  #1222 (line num in coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1222 (line num in coconut source)
    def do_readFile() -> 'str':  #1223 (line num in coconut source)
        with open(fpath, "r+") as f:  #1224 (line num in coconut source)
            return (f.read())  #1225 (line num in coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1226 (line num in coconut source)


@_coconut_tco  #1228 (line num in coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1228 (line num in coconut source)
    def do_writeFile() -> 'None':  #1229 (line num in coconut source)
        with open(fpath, "w+") as f:  #1230 (line num in coconut source)
            f.write(text)  #1231 (line num in coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1232 (line num in coconut source)


@_coconut_tco  #1234 (line num in coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1234 (line num in coconut source)
    def do_appendFile() -> 'None':  #1235 (line num in coconut source)
        with open(fpath, "a+") as f:  #1236 (line num in coconut source)
            f.write(text)  #1237 (line num in coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1238 (line num in coconut source)


@_coconut_tco  #1240 (line num in coconut source)
def readIO(s: 'str') -> 'IO':  #1240 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))  #1241 (line num in coconut source)


@_coconut_tco  #1243 (line num in coconut source)
def readLn() -> 'IO':  #1243 (line num in coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1244 (line num in coconut source)



## Exception handling:

@_coconut_tco  #1249 (line num in coconut source)
def ioError(err: 'IOError') -> 'IO':  #1249 (line num in coconut source)
    def _coconut_lambda_1():  #1250 (line num in coconut source)
        raise err  #1250 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut_lambda_1)  #1250 (line num in coconut source)


@_coconut_tco  #1252 (line num in coconut source)
def userError(msg: 'str') -> 'IOError':  #1252 (line num in coconut source)
    return _coconut_tail_call(IOError, msg)  #1253 (line num in coconut source)
