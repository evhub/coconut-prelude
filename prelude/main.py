#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfb6725f2

# Compiled with Coconut version 2.0.0-post_dev1 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Helpers:

#### Imports:
sys = _coconut_sys  #4 (line in Coconut source)
import fractions as _fractions  #5 (line in Coconut source)
import math as _math  #6 (line in Coconut source)
import ast as _ast  #7 (line in Coconut source)
from math import gcd as _gcd  #8 (line in Coconut source)

from prelude.util import *  # type: ignore  #10 (line in Coconut source)

#### Untyped built-ins:
_max: '_coconut.typing.Callable[..., T.Any]' = max  #13 (line in Coconut source)
_min: '_coconut.typing.Callable[..., T.Any]' = min  #14 (line in Coconut source)
_zip: '_coconut.typing.Callable[..., T.Any]' = zip  #15 (line in Coconut source)
_abs: '_coconut.typing.Callable[..., T.Any]' = abs  #16 (line in Coconut source)
_round: '_coconut.typing.Callable[..., T.Any]' = round  #17 (line in Coconut source)
_fmap: '_coconut.typing.Callable[..., T.Any]' = fmap  #18 (line in Coconut source)
_reduce: '_coconut.typing.Callable[..., T.Any]' = reduce  #19 (line in Coconut source)
_all: '_coconut.typing.Callable[..., T.Any]' = all  #20 (line in Coconut source)
_any: '_coconut.typing.Callable[..., T.Any]' = any  #21 (line in Coconut source)
_map: '_coconut.typing.Callable[..., T.Any]' = map  #22 (line in Coconut source)
_filter: '_coconut.typing.Callable[..., T.Any]' = filter  #23 (line in Coconut source)
_int: '_coconut.typing.Callable[..., T.Any]' = int  #24 (line in Coconut source)
_sum: '_coconut.typing.Callable[..., T.Any]' = sum  #25 (line in Coconut source)
_reversed: '_coconut.typing.Callable[..., T.Any]' = reversed  #26 (line in Coconut source)
_print: '_coconut.typing.Callable[..., T.Any]' = print  #27 (line in Coconut source)
_ceil: '_coconut.typing.Callable[..., T.Any]' = _math.ceil  #28 (line in Coconut source)
_floor: '_coconut.typing.Callable[..., T.Any]' = _math.floor  #29 (line in Coconut source)




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool  #39 (line in Coconut source)

not_: '_coconut.typing.Callable[[bool], bool]'  #41 (line in Coconut source)
not_ = (_coconut.operator.not_)  #42 (line in Coconut source)

otherwise: 'bool' = True  #44 (line in Coconut source)

#### Maybe:
class Maybe:  #47 (line in Coconut source)
    @staticmethod  #48 (line in Coconut source)
    @_coconut_tco  #49 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'Maybe':  #49 (line in Coconut source)
        return _coconut_tail_call(Just, x)  #49 (line in Coconut source)


    @staticmethod  #51 (line in Coconut source)
    def __fail__(msg: 'str') -> 'Maybe':  #52 (line in Coconut source)
        return (nothing)  #52 (line in Coconut source)


    @staticmethod  #54 (line in Coconut source)
    def __mempty__() -> 'Maybe':  #55 (line in Coconut source)
        return (nothing)  #55 (line in Coconut source)


class Nothing(_coconut.collections.namedtuple("Nothing", ()), Maybe):  #57 (line in Coconut source)
    """
    -- Nothing is the data type; use nothing for the canonical instance
    """  #60 (line in Coconut source)

    _coconut_is_data = True  #62 (line in Coconut source)
    __slots__ = ()  #62 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #62 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #62 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #62 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #62 (line in Coconut source)
    def __eq__(self, other):  #62 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #62 (line in Coconut source)
    def __hash__(self):  #62 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #62 (line in Coconut source)
    __match_args__ = ()  #62 (line in Coconut source)
nothing: 'Maybe' = Nothing()  #62 (line in Coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #64 (line in Coconut source)
    _coconut_is_data = True  #64 (line in Coconut source)
    __slots__ = ()  #64 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #64 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #64 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #64 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #64 (line in Coconut source)
    def __eq__(self, other):  #64 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #64 (line in Coconut source)
    def __hash__(self):  #64 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #64 (line in Coconut source)
    __match_args__ = ('x',)  #64 (line in Coconut source)

derivingOrd(Nothing, Just)  #66 (line in Coconut source)

if TYPE_CHECKING:  #68 (line in Coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #69 (line in Coconut source)
        ...  #70 (line in Coconut source)

else:  #71 (line in Coconut source)
    @_coconut_mark_as_match  #72 (line in Coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #72 (line in Coconut source)
        _coconut_match_check_0 = False  #72 (line in Coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #72 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #72 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #72 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #72 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)  # type: ignore  #72 (line in Coconut source)
            _coconut_match_set_name_default = _coconut_match_temp_0  #72 (line in Coconut source)
            if not _coconut_match_kwargs:  #72 (line in Coconut source)
                _coconut_match_check_0 = True  #72 (line in Coconut source)
        if _coconut_match_check_0:  #72 (line in Coconut source)
            _coconut_match_check_0 = False  #72 (line in Coconut source)
            if not _coconut_match_check_0:  #72 (line in Coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)) and (_coconut.len(_coconut_match_args[2]) == 0):  #72 (line in Coconut source)
                    _coconut_match_check_0 = True  #72 (line in Coconut source)

            if not _coconut_match_check_0:  #72 (line in Coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #72 (line in Coconut source)
                    _coconut_match_check_0 = True  #72 (line in Coconut source)
                if _coconut_match_check_0:  #72 (line in Coconut source)
                    _coconut_match_check_0 = False  #72 (line in Coconut source)
                    if not _coconut_match_check_0:  #72 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #72 (line in Coconut source)
                            _coconut_match_check_0 = True  #72 (line in Coconut source)

                    if not _coconut_match_check_0:  #72 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #72 (line in Coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Nothing, '__match_args__', ())  #72 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #72 (line in Coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #72 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 0:  #72 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #72 (line in Coconut source)
                            _coconut_match_check_0 = True  #72 (line in Coconut source)




        if _coconut_match_check_0:  #72 (line in Coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #72 (line in Coconut source)
                default = _coconut_match_set_name_default  #72 (line in Coconut source)
        if not _coconut_match_check_0:  #72 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #72 (line in Coconut source)

        return (default)  #72 (line in Coconut source)

    @_coconut_addpattern(maybe)  #73 (line in Coconut source)
    @_coconut_tco  #73 (line in Coconut source)
    @_coconut_mark_as_match  #73 (line in Coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #73 (line in Coconut source)
        _coconut_match_check_1 = False  #73 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #73 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #73 (line in Coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #73 (line in Coconut source)
            _coconut_match_temp_4 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)  # type: ignore  #73 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_match_temp_3  #73 (line in Coconut source)
            if not _coconut_match_kwargs:  #73 (line in Coconut source)
                _coconut_match_check_1 = True  #73 (line in Coconut source)
        if _coconut_match_check_1:  #73 (line in Coconut source)
            _coconut_match_check_1 = False  #73 (line in Coconut source)
            if not _coconut_match_check_1:  #73 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #73 (line in Coconut source)
                if (_coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) == 1):  #73 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #73 (line in Coconut source)
                    _coconut_match_check_1 = True  #73 (line in Coconut source)
                if _coconut_match_check_1:  #73 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line in Coconut source)
                        x = _coconut_match_set_name_x  #73 (line in Coconut source)

            if not _coconut_match_check_1:  #73 (line in Coconut source)
                if (not _coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #73 (line in Coconut source)
                    _coconut_match_check_1 = True  #73 (line in Coconut source)
                if _coconut_match_check_1:  #73 (line in Coconut source)
                    _coconut_match_check_1 = False  #73 (line in Coconut source)
                    if not _coconut_match_check_1:  #73 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #73 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #73 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #73 (line in Coconut source)
                            _coconut_match_check_1 = True  #73 (line in Coconut source)
                        if _coconut_match_check_1:  #73 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line in Coconut source)
                                x = _coconut_match_set_name_x  #73 (line in Coconut source)

                    if not _coconut_match_check_1:  #73 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #73 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #73 (line in Coconut source)
                            _coconut_match_temp_5 = _coconut.getattr(Just, '__match_args__', ())  #73 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_5, _coconut.tuple):  #73 (line in Coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #73 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_5) < 1:  #73 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_5),))  #73 (line in Coconut source)
                            _coconut_match_temp_6 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_5[0], _coconut_sentinel)  #73 (line in Coconut source)
                            if _coconut_match_temp_6 is not _coconut_sentinel:  #73 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_6  #73 (line in Coconut source)
                                _coconut_match_check_1 = True  #73 (line in Coconut source)
                        if _coconut_match_check_1:  #73 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #73 (line in Coconut source)
                                x = _coconut_match_set_name_x  #73 (line in Coconut source)




        if _coconut_match_check_1:  #73 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #73 (line in Coconut source)
                func = _coconut_match_set_name_func  #73 (line in Coconut source)
        if not _coconut_match_check_1:  #73 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #73 (line in Coconut source)

        return _coconut_tail_call(func, x)  #73 (line in Coconut source)

#### Either:

class Either:  #76 (line in Coconut source)
    @staticmethod  #77 (line in Coconut source)
    @_coconut_tco  #78 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #78 (line in Coconut source)
        return _coconut_tail_call(Right, x)  #78 (line in Coconut source)


    @staticmethod  #80 (line in Coconut source)
    @_coconut_tco  #81 (line in Coconut source)
    def __fail__(msg: 'str') -> 'Either':  #81 (line in Coconut source)
        return _coconut_tail_call(Left, msg)  #81 (line in Coconut source)


class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #83 (line in Coconut source)
    _coconut_is_data = True  #83 (line in Coconut source)
    __slots__ = ()  #83 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #83 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #83 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #83 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #83 (line in Coconut source)
    def __eq__(self, other):  #83 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #83 (line in Coconut source)
    def __hash__(self):  #83 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #83 (line in Coconut source)
    __match_args__ = ('x',)  #83 (line in Coconut source)
    @staticmethod  #84 (line in Coconut source)
    def __bool__() -> 'bool':  #85 (line in Coconut source)
        return (False)  #85 (line in Coconut source)


    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #87 (line in Coconut source)
        return (self)  #87 (line in Coconut source)


class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #89 (line in Coconut source)
    _coconut_is_data = True  #89 (line in Coconut source)
    __slots__ = ()  #89 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #89 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #89 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #89 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #89 (line in Coconut source)
    def __eq__(self, other):  #89 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #89 (line in Coconut source)
    def __hash__(self):  #89 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #89 (line in Coconut source)
    __match_args__ = ('x',)  #89 (line in Coconut source)

derivingOrd(Left, Right)  #91 (line in Coconut source)

if TYPE_CHECKING:  #93 (line in Coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #94 (line in Coconut source)
        ...  #95 (line in Coconut source)

else:  #96 (line in Coconut source)
    @_coconut_tco  #97 (line in Coconut source)
    @_coconut_mark_as_match  #97 (line in Coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #97 (line in Coconut source)
        _coconut_match_check_2 = False  #97 (line in Coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #97 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #97 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #97 (line in Coconut source)
            _coconut_match_temp_7 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #97 (line in Coconut source)
            _coconut_match_temp_8 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)  # type: ignore  #97 (line in Coconut source)
            _coconut_match_set_name_left_func = _coconut_match_temp_7  #97 (line in Coconut source)
            if not _coconut_match_kwargs:  #97 (line in Coconut source)
                _coconut_match_check_2 = True  #97 (line in Coconut source)
        if _coconut_match_check_2:  #97 (line in Coconut source)
            _coconut_match_check_2 = False  #97 (line in Coconut source)
            if not _coconut_match_check_2:  #97 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #97 (line in Coconut source)
                if (_coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) == 1):  #97 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #97 (line in Coconut source)
                    _coconut_match_check_2 = True  #97 (line in Coconut source)
                if _coconut_match_check_2:  #97 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line in Coconut source)
                        x = _coconut_match_set_name_x  #97 (line in Coconut source)

            if not _coconut_match_check_2:  #97 (line in Coconut source)
                if (not _coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #97 (line in Coconut source)
                    _coconut_match_check_2 = True  #97 (line in Coconut source)
                if _coconut_match_check_2:  #97 (line in Coconut source)
                    _coconut_match_check_2 = False  #97 (line in Coconut source)
                    if not _coconut_match_check_2:  #97 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #97 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #97 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #97 (line in Coconut source)
                            _coconut_match_check_2 = True  #97 (line in Coconut source)
                        if _coconut_match_check_2:  #97 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line in Coconut source)
                                x = _coconut_match_set_name_x  #97 (line in Coconut source)

                    if not _coconut_match_check_2:  #97 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #97 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #97 (line in Coconut source)
                            _coconut_match_temp_9 = _coconut.getattr(Left, '__match_args__', ())  #97 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_9, _coconut.tuple):  #97 (line in Coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #97 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_9) < 1:  #97 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_9),))  #97 (line in Coconut source)
                            _coconut_match_temp_10 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_9[0], _coconut_sentinel)  #97 (line in Coconut source)
                            if _coconut_match_temp_10 is not _coconut_sentinel:  #97 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_10  #97 (line in Coconut source)
                                _coconut_match_check_2 = True  #97 (line in Coconut source)
                        if _coconut_match_check_2:  #97 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #97 (line in Coconut source)
                                x = _coconut_match_set_name_x  #97 (line in Coconut source)




        if _coconut_match_check_2:  #97 (line in Coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #97 (line in Coconut source)
                left_func = _coconut_match_set_name_left_func  #97 (line in Coconut source)
        if not _coconut_match_check_2:  #97 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #97 (line in Coconut source)

        return _coconut_tail_call(left_func, x)  #97 (line in Coconut source)

    @_coconut_addpattern(either)  #98 (line in Coconut source)
    @_coconut_tco  #98 (line in Coconut source)
    @_coconut_mark_as_match  #98 (line in Coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #98 (line in Coconut source)
        _coconut_match_check_3 = False  #98 (line in Coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #98 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #98 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #98 (line in Coconut source)
            _coconut_match_temp_11 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #98 (line in Coconut source)
            _coconut_match_temp_12 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)  # type: ignore  #98 (line in Coconut source)
            _coconut_match_set_name_right_func = _coconut_match_temp_11  #98 (line in Coconut source)
            if not _coconut_match_kwargs:  #98 (line in Coconut source)
                _coconut_match_check_3 = True  #98 (line in Coconut source)
        if _coconut_match_check_3:  #98 (line in Coconut source)
            _coconut_match_check_3 = False  #98 (line in Coconut source)
            if not _coconut_match_check_3:  #98 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #98 (line in Coconut source)
                if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) == 1):  #98 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #98 (line in Coconut source)
                    _coconut_match_check_3 = True  #98 (line in Coconut source)
                if _coconut_match_check_3:  #98 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line in Coconut source)
                        x = _coconut_match_set_name_x  #98 (line in Coconut source)

            if not _coconut_match_check_3:  #98 (line in Coconut source)
                if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #98 (line in Coconut source)
                    _coconut_match_check_3 = True  #98 (line in Coconut source)
                if _coconut_match_check_3:  #98 (line in Coconut source)
                    _coconut_match_check_3 = False  #98 (line in Coconut source)
                    if not _coconut_match_check_3:  #98 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #98 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #98 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #98 (line in Coconut source)
                            _coconut_match_check_3 = True  #98 (line in Coconut source)
                        if _coconut_match_check_3:  #98 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line in Coconut source)
                                x = _coconut_match_set_name_x  #98 (line in Coconut source)

                    if not _coconut_match_check_3:  #98 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #98 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #98 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(Right, '__match_args__', ())  #98 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #98 (line in Coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #98 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #98 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #98 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_13[0], _coconut_sentinel)  #98 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #98 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_14  #98 (line in Coconut source)
                                _coconut_match_check_3 = True  #98 (line in Coconut source)
                        if _coconut_match_check_3:  #98 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #98 (line in Coconut source)
                                x = _coconut_match_set_name_x  #98 (line in Coconut source)




        if _coconut_match_check_3:  #98 (line in Coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #98 (line in Coconut source)
                right_func = _coconut_match_set_name_right_func  #98 (line in Coconut source)
        if not _coconut_match_check_3:  #98 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #98 (line in Coconut source)

        return _coconut_tail_call(right_func, x)  #98 (line in Coconut source)

#### Ordering:

class Ordering:  #101 (line in Coconut source)
    @staticmethod  #102 (line in Coconut source)
    def __mempty__() -> 'Ordering':  #103 (line in Coconut source)
        return (eq)  #103 (line in Coconut source)


class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #105 (line in Coconut source)
    _coconut_is_data = True  #105 (line in Coconut source)
    __slots__ = ()  #105 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #105 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #105 (line in Coconut source)
    def __eq__(self, other):  #105 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #105 (line in Coconut source)
    def __hash__(self):  #105 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #105 (line in Coconut source)
    __match_args__ = ()  #105 (line in Coconut source)
    @staticmethod  #106 (line in Coconut source)
    def __bool__() -> 'bool':  #107 (line in Coconut source)
        return (True)  #107 (line in Coconut source)


class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #109 (line in Coconut source)
    _coconut_is_data = True  #109 (line in Coconut source)
    __slots__ = ()  #109 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #109 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #109 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #109 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #109 (line in Coconut source)
    def __eq__(self, other):  #109 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #109 (line in Coconut source)
    def __hash__(self):  #109 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #109 (line in Coconut source)
    __match_args__ = ()  #109 (line in Coconut source)

class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #111 (line in Coconut source)
    _coconut_is_data = True  #111 (line in Coconut source)
    __slots__ = ()  #111 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #111 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #111 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #111 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #111 (line in Coconut source)
    def __eq__(self, other):  #111 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #111 (line in Coconut source)
    def __hash__(self):  #111 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #111 (line in Coconut source)
    __match_args__ = ()  #111 (line in Coconut source)
    @staticmethod  #112 (line in Coconut source)
    def __bool__() -> 'bool':  #113 (line in Coconut source)
        return (True)  #113 (line in Coconut source)


derivingOrd(LT, EQ, GT)  #115 (line in Coconut source)
derivingBoundedEnum(LT, EQ, GT)  #116 (line in Coconut source)

lt: 'Ordering' = LT()  #118 (line in Coconut source)
eq: 'Ordering' = EQ()  #119 (line in Coconut source)
gt: 'Ordering' = GT()  #120 (line in Coconut source)

#### Char:
Char = T.NewType("Char", str)  #123 (line in Coconut source)

#### String:
String = str  #126 (line in Coconut source)


### Tuples:
fst: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]'  #130 (line in Coconut source)
fst = _coconut.operator.itemgetter((0))  #131 (line in Coconut source)

snd: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]'  #133 (line in Coconut source)
snd = _coconut.operator.itemgetter((1))  #134 (line in Coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #136 (line in Coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #139 (line in Coconut source)
    return (lambda *args: func(args))  # type: ignore  #140 (line in Coconut source)


def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]':  #142 (line in Coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #145 (line in Coconut source)
    return (lambda args: func(*args))  #146 (line in Coconut source)



## Basic type classes:

#### Eq:

Eq = object  #153 (line in Coconut source)

#### Ord:
Ord = Eq  #156 (line in Coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #157 (line in Coconut source)

if TYPE_CHECKING:  #159 (line in Coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #160 (line in Coconut source)
        ...  #161 (line in Coconut source)

else:  #162 (line in Coconut source)
    @_coconut_mark_as_match  #163 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #163 (line in Coconut source)
        _coconut_match_check_4 = False  #163 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #163 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #163 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #163 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #163 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #163 (line in Coconut source)
            _coconut_match_temp_16 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #163 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_15  #163 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_16  #163 (line in Coconut source)
            if not _coconut_match_kwargs:  #163 (line in Coconut source)
                _coconut_match_check_4 = True  #163 (line in Coconut source)
        if _coconut_match_check_4:  #163 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #163 (line in Coconut source)
                x = _coconut_match_set_name_x  #163 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #163 (line in Coconut source)
                y = _coconut_match_set_name_y  #163 (line in Coconut source)
        if _coconut_match_check_4 and not (x == y):  #163 (line in Coconut source)
            _coconut_match_check_4 = False  #163 (line in Coconut source)
        if not _coconut_match_check_4:  #163 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #163 (line in Coconut source)

        return (eq)  #163 (line in Coconut source)

    @_coconut_addpattern(compare)  #164 (line in Coconut source)
    @_coconut_mark_as_match  #164 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #164 (line in Coconut source)
        _coconut_match_check_5 = False  #164 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #164 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #164 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #164 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #164 (line in Coconut source)
            _coconut_match_temp_17 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #164 (line in Coconut source)
            _coconut_match_temp_18 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #164 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_17  #164 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_18  #164 (line in Coconut source)
            if not _coconut_match_kwargs:  #164 (line in Coconut source)
                _coconut_match_check_5 = True  #164 (line in Coconut source)
        if _coconut_match_check_5:  #164 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #164 (line in Coconut source)
                x = _coconut_match_set_name_x  #164 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #164 (line in Coconut source)
                y = _coconut_match_set_name_y  #164 (line in Coconut source)
        if _coconut_match_check_5 and not (x < y):  #164 (line in Coconut source)
            _coconut_match_check_5 = False  #164 (line in Coconut source)
        if not _coconut_match_check_5:  #164 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #164 (line in Coconut source)

        return (lt)  #164 (line in Coconut source)

    @_coconut_addpattern(compare)  #165 (line in Coconut source)
    @_coconut_mark_as_match  #165 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #165 (line in Coconut source)
        _coconut_match_check_6 = False  #165 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #165 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #165 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #165 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #165 (line in Coconut source)
            _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #165 (line in Coconut source)
            _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #165 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_19  #165 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_20  #165 (line in Coconut source)
            if not _coconut_match_kwargs:  #165 (line in Coconut source)
                _coconut_match_check_6 = True  #165 (line in Coconut source)
        if _coconut_match_check_6:  #165 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #165 (line in Coconut source)
                x = _coconut_match_set_name_x  #165 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #165 (line in Coconut source)
                y = _coconut_match_set_name_y  #165 (line in Coconut source)
        if _coconut_match_check_6 and not (x > y):  #165 (line in Coconut source)
            _coconut_match_check_6 = False  #165 (line in Coconut source)
        if not _coconut_match_check_6:  #165 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #165 (line in Coconut source)

        return (gt)  #165 (line in Coconut source)


max: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #167 (line in Coconut source)
max = _max  #168 (line in Coconut source)

min: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #170 (line in Coconut source)
min = _min  #171 (line in Coconut source)

#### Enum:
Enum = Ord  #174 (line in Coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #175 (line in Coconut source)

succ: '_coconut.typing.Callable[[TEnum], TEnum]'  #177 (line in Coconut source)
succ = _coconut.functools.partial((_coconut.operator.add), 1)  #178 (line in Coconut source)

pred: '_coconut.typing.Callable[[TEnum], TEnum]'  #180 (line in Coconut source)
pred = _coconut_partial((_coconut_minus), {1: 1}, 2, ())  #181 (line in Coconut source)

toEnum = NotImplemented  #183 (line in Coconut source)

fromEnum: '_coconut.typing.Callable[[Enum], int]'  #185 (line in Coconut source)
fromEnum = _int  #186 (line in Coconut source)

@_coconut_tco  #188 (line in Coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #188 (line in Coconut source)
    return _coconut_tail_call(iterate, succ, first)  #189 (line in Coconut source)


def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #191 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #192 (line in Coconut source)
    return (iterate(_coconut.functools.partial((_coconut.operator.add), step), first) if step >= 0 else ())  # type: ignore  #193 (line in Coconut source)


def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #195 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #196 (line in Coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #197 (line in Coconut source)


def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #199 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #200 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #201 (line in Coconut source)
    steps = dist / step if step != 0 else 0  #202 (line in Coconut source)
    if steps < 0:  #203 (line in Coconut source)
        return (())  #204 (line in Coconut source)
    counter = iterate(_coconut.functools.partial((_coconut.operator.add), step), first)  #205 (line in Coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #206 (line in Coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #210 (line in Coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #211 (line in Coconut source)

@_coconut_tco  #213 (line in Coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #213 (line in Coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #217 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #219 (line in Coconut source)
        return (False)  # type: ignore  #220 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #223 (line in Coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #224 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #227 (line in Coconut source)


@_coconut_tco  #229 (line in Coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #229 (line in Coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #233 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #235 (line in Coconut source)
        return (True)  # type: ignore  #236 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #239 (line in Coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #240 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #243 (line in Coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #252 (line in Coconut source)

#### Integer:
Integer = int  #255 (line in Coconut source)

#### Float:
Float = float  #258 (line in Coconut source)

#### Double:
Double = float  #261 (line in Coconut source)

#### Rational:
Rational = _fractions.Fraction  #264 (line in Coconut source)

@_coconut_tco  #266 (line in Coconut source)
def over(x, y):  #266 (line in Coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #271 (line in Coconut source)
    return _coconut_tail_call(Rational, x, y)  #272 (line in Coconut source)

#### Word:

Word = Int  #275 (line in Coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #281 (line in Coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #282 (line in Coconut source)

negate: '_coconut.typing.Callable[[TNum], TNum]'  #284 (line in Coconut source)
negate = (_coconut_minus)  #285 (line in Coconut source)

abs: '_coconut.typing.Callable[[TNum], TNum]'  #287 (line in Coconut source)
abs = _abs  #288 (line in Coconut source)

if TYPE_CHECKING:  #290 (line in Coconut source)
    def signum(x: 'Num') -> 'int':  #291 (line in Coconut source)
        ...  #292 (line in Coconut source)

else:  #293 (line in Coconut source)
    @_coconut_mark_as_match  #294 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #294 (line in Coconut source)
        _coconut_match_check_7 = False  #294 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #294 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #294 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #294 (line in Coconut source)
                if not _coconut_match_kwargs:  #294 (line in Coconut source)
                    _coconut_match_check_7 = True  #294 (line in Coconut source)
        if not _coconut_match_check_7:  #294 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #294 (line in Coconut source)

        return (0)  #294 (line in Coconut source)

    @_coconut_addpattern(signum)  #295 (line in Coconut source)
    @_coconut_mark_as_match  #295 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #295 (line in Coconut source)
        _coconut_match_check_8 = False  #295 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #295 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #295 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #295 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #295 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_21  #295 (line in Coconut source)
            if not _coconut_match_kwargs:  #295 (line in Coconut source)
                _coconut_match_check_8 = True  #295 (line in Coconut source)
        if _coconut_match_check_8:  #295 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #295 (line in Coconut source)
                x = _coconut_match_set_name_x  #295 (line in Coconut source)
        if _coconut_match_check_8 and not (x > 0):  #295 (line in Coconut source)
            _coconut_match_check_8 = False  #295 (line in Coconut source)
        if not _coconut_match_check_8:  #295 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #295 (line in Coconut source)

        return (1)  #295 (line in Coconut source)

    @_coconut_addpattern(signum)  #296 (line in Coconut source)
    @_coconut_mark_as_match  #296 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #296 (line in Coconut source)
        _coconut_match_check_9 = False  #296 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #296 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #296 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #296 (line in Coconut source)
            _coconut_match_temp_22 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #296 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_22  #296 (line in Coconut source)
            if not _coconut_match_kwargs:  #296 (line in Coconut source)
                _coconut_match_check_9 = True  #296 (line in Coconut source)
        if _coconut_match_check_9:  #296 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #296 (line in Coconut source)
                x = _coconut_match_set_name_x  #296 (line in Coconut source)
        if _coconut_match_check_9 and not (x < 0):  #296 (line in Coconut source)
            _coconut_match_check_9 = False  #296 (line in Coconut source)
        if not _coconut_match_check_9:  #296 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #296 (line in Coconut source)

        return (-1)  #296 (line in Coconut source)


def fromInteger(x: 'Integer') -> 'Num':  #298 (line in Coconut source)
    return (x)  #298 (line in Coconut source)

#### Real:

Real = Num  #301 (line in Coconut source)

if TYPE_CHECKING:  #303 (line in Coconut source)
    def toRational(real: 'Real') -> 'Rational':  #304 (line in Coconut source)
        ...  #305 (line in Coconut source)

else:  #306 (line in Coconut source)
    @_coconut_tco  #307 (line in Coconut source)
    @_coconut_mark_as_match  #307 (line in Coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #307 (line in Coconut source)
        _coconut_match_check_10 = False  #307 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #307 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #307 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #307 (line in Coconut source)
            _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #307 (line in Coconut source)
            if (isinstance)(_coconut_match_temp_23, float):  #307 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_23  #307 (line in Coconut source)
                if not _coconut_match_kwargs:  #307 (line in Coconut source)
                    _coconut_match_check_10 = True  #307 (line in Coconut source)
        if _coconut_match_check_10:  #307 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #307 (line in Coconut source)
                real = _coconut_match_set_name_real  #307 (line in Coconut source)
        if not _coconut_match_check_10:  #307 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #307 (line in Coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #308 (line in Coconut source)

    @_coconut_addpattern(toRational)  #309 (line in Coconut source)
    @_coconut_tco  #309 (line in Coconut source)
    @_coconut_mark_as_match  #309 (line in Coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #309 (line in Coconut source)
        _coconut_match_check_11 = False  #309 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #309 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #309 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #309 (line in Coconut source)
            _coconut_match_temp_24 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #309 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_match_temp_24  #309 (line in Coconut source)
            if not _coconut_match_kwargs:  #309 (line in Coconut source)
                _coconut_match_check_11 = True  #309 (line in Coconut source)
        if _coconut_match_check_11:  #309 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #309 (line in Coconut source)
                real = _coconut_match_set_name_real  #309 (line in Coconut source)
        if not _coconut_match_check_11:  #309 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #309 (line in Coconut source)

        return _coconut_tail_call(Rational, real)  #310 (line in Coconut source)

#### Integral:

Integral = int  #313 (line in Coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #315 (line in Coconut source)
    divxy = x // y  #316 (line in Coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #317 (line in Coconut source)


def rem(x: 'int', y: 'int') -> 'int':  #319 (line in Coconut source)
    modxy = x % y  #320 (line in Coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #321 (line in Coconut source)


div: '_coconut.typing.Callable[[int, int], int]'  #323 (line in Coconut source)
div = (_coconut.operator.floordiv)  #324 (line in Coconut source)

mod: '_coconut.typing.Callable[[int, int], int]'  #326 (line in Coconut source)
mod = (_coconut.operator.mod)  #327 (line in Coconut source)

def quotRem(x: 'int', y: 'int') -> 'T.Tuple[int, int]':  #329 (line in Coconut source)
    divxy, modxy = divmod(x, y)  #330 (line in Coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #331 (line in Coconut source)
    return (divxy + adj, modxy - y * adj)  #332 (line in Coconut source)


divMod = divmod  #334 (line in Coconut source)

toInteger: '_coconut.typing.Callable[[Integral], Integer]'  #336 (line in Coconut source)
toInteger = _int  #337 (line in Coconut source)

#### Fractional:
Fractional = Rational  #340 (line in Coconut source)

recip: '_coconut.typing.Callable[[Fractional], Fractional]'  #342 (line in Coconut source)
recip = _coconut.functools.partial((_coconut.operator.truediv), 1)  #343 (line in Coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #345 (line in Coconut source)
    return (x)  #345 (line in Coconut source)

#### Floating:

Floating = float  #348 (line in Coconut source)

from math import pi  #350 (line in Coconut source)
from math import exp  #350 (line in Coconut source)
from math import log  #350 (line in Coconut source)
from math import sqrt  #350 (line in Coconut source)
from math import sin  #350 (line in Coconut source)
from math import cos  #350 (line in Coconut source)
from math import tan  #350 (line in Coconut source)
from math import asin  #350 (line in Coconut source)
from math import acos  #350 (line in Coconut source)
from math import atan  #350 (line in Coconut source)
from math import sinh  #350 (line in Coconut source)
from math import cosh  #350 (line in Coconut source)
from math import tanh  #350 (line in Coconut source)
from math import asinh  #350 (line in Coconut source)
from math import acosh  #350 (line in Coconut source)
from math import atanh  #350 (line in Coconut source)

@_coconut_tco  #369 (line in Coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #369 (line in Coconut source)
    return _coconut_tail_call(log, x, base)  #370 (line in Coconut source)

#### RealFrac:

RealFrac = Rational  #373 (line in Coconut source)

def properFraction(x: 'RealFrac') -> 'T.Tuple[int, RealFrac]':  #375 (line in Coconut source)
    floor_x = floor(x)  #376 (line in Coconut source)
    return (floor_x, x - floor_x)  #377 (line in Coconut source)


truncate: '_coconut.typing.Callable[[RealFrac], int]'  #379 (line in Coconut source)
truncate = _int  #380 (line in Coconut source)

round: '_coconut.typing.Callable[[RealFrac], int]'  #382 (line in Coconut source)
round = _round  #383 (line in Coconut source)

ceiling: '_coconut.typing.Callable[[RealFrac], int]'  #385 (line in Coconut source)
ceiling = _ceil  #386 (line in Coconut source)

floor: '_coconut.typing.Callable[[RealFrac], int]'  #388 (line in Coconut source)
floor = _floor  #389 (line in Coconut source)

#### RealFloat:
RealFloat = float  #392 (line in Coconut source)

def floatRadix(x: 'float') -> 'int':  #394 (line in Coconut source)
    return (2)  #394 (line in Coconut source)


def floatDigits(x: 'float') -> 'int':  #396 (line in Coconut source)
    return (53)  #396 (line in Coconut source)


def floatRange(x: 'float') -> 'T.Tuple[int, int]':  #398 (line in Coconut source)
    return ((-1021, 1024))  #398 (line in Coconut source)


decodeFloat = NotImplemented  #400 (line in Coconut source)

encodeFloat = NotImplemented  #402 (line in Coconut source)

exponent = NotImplemented  #404 (line in Coconut source)

significand = NotImplemented  #406 (line in Coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #408 (line in Coconut source)
    return (x * 2**power)  #409 (line in Coconut source)


from math import isnan as isNaN  #411 (line in Coconut source)
from math import isinf as isInfinite  #411 (line in Coconut source)
from math import atan2  #411 (line in Coconut source)

isDenormalized = NotImplemented  #417 (line in Coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #419 (line in Coconut source)
    return (x == 0 and str(x).startswith("-"))  #420 (line in Coconut source)


def isIEEE(x: 'float') -> 'bool':  #422 (line in Coconut source)
    return (True)  #422 (line in Coconut source)


### Numeric functions:

def subtract(x, y):  #426 (line in Coconut source)
    return (y - x)  #427 (line in Coconut source)


def even(x: 'int') -> 'bool':  #429 (line in Coconut source)
    return (x % 2 == 0)  #430 (line in Coconut source)


def odd(x: 'int') -> 'bool':  #432 (line in Coconut source)
    return (x % 2 == 1)  #433 (line in Coconut source)


gcd: '_coconut.typing.Callable[[int, int], int]'  #435 (line in Coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #436 (line in Coconut source)

if TYPE_CHECKING:  #438 (line in Coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #439 (line in Coconut source)
        ...  #440 (line in Coconut source)

else:  #441 (line in Coconut source)
    @_coconut_mark_as_match  #442 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #442 (line in Coconut source)
        _coconut_match_check_12 = False  #442 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #442 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #442 (line in Coconut source)
            if _coconut_match_args[1] == 0:  #442 (line in Coconut source)
                if not _coconut_match_kwargs:  #442 (line in Coconut source)
                    _coconut_match_check_12 = True  #442 (line in Coconut source)
        if not _coconut_match_check_12:  #442 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #442 (line in Coconut source)

        return (0)  #442 (line in Coconut source)

    @_coconut_addpattern(lcm)  #443 (line in Coconut source)
    @_coconut_mark_as_match  #443 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #443 (line in Coconut source)
        _coconut_match_check_13 = False  #443 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #443 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #443 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #443 (line in Coconut source)
                if not _coconut_match_kwargs:  #443 (line in Coconut source)
                    _coconut_match_check_13 = True  #443 (line in Coconut source)
        if not _coconut_match_check_13:  #443 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #443 (line in Coconut source)

        return (0)  #443 (line in Coconut source)

    @_coconut_addpattern(lcm)  #444 (line in Coconut source)
    @_coconut_mark_as_match  #444 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #444 (line in Coconut source)
        _coconut_match_check_14 = False  #444 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #444 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #444 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #444 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #444 (line in Coconut source)
            _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #444 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #444 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_25  #444 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_26  #444 (line in Coconut source)
            if not _coconut_match_kwargs:  #444 (line in Coconut source)
                _coconut_match_check_14 = True  #444 (line in Coconut source)
        if _coconut_match_check_14:  #444 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #444 (line in Coconut source)
                x = _coconut_match_set_name_x  #444 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #444 (line in Coconut source)
                y = _coconut_match_set_name_y  #444 (line in Coconut source)
        if not _coconut_match_check_14:  #444 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #444 (line in Coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #445 (line in Coconut source)


fromIntegral: '_coconut.typing.Callable[[Integral], Num]'  #447 (line in Coconut source)
fromIntegral = fromInteger  #448 (line in Coconut source)

realToFrac: '_coconut.typing.Callable[[Real], Fractional]'  #450 (line in Coconut source)
realToFrac = toRational  #451 (line in Coconut source)



## Monoids:
Monoid = T.Iterable  #456 (line in Coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #457 (line in Coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #459 (line in Coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #462 (line in Coconut source)
    _coconut_is_data = True  #463 (line in Coconut source)
    __slots__ = ()  #463 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #463 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #463 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #463 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #463 (line in Coconut source)
    def __eq__(self, other):  #463 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #463 (line in Coconut source)
    def __hash__(self):  #463 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #463 (line in Coconut source)
    __match_args__ = ()  #463 (line in Coconut source)
    @staticmethod  #463 (line in Coconut source)
    @_coconut_tco  #464 (line in Coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #464 (line in Coconut source)
        if (hasattr)(M, "__mempty__"):  #465 (line in Coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #466 (line in Coconut source)
        return _coconut_tail_call(makedata, type(M))  #467 (line in Coconut source)


mempty: 'T.Any' = Mempty()  #469 (line in Coconut source)

@_coconut_tco  #471 (line in Coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #471 (line in Coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #476 (line in Coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #478 (line in Coconut source)
    y = (asTypeOf)(y, x)  #479 (line in Coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #482 (line in Coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #483 (line in Coconut source)

# Default implementation
    if not x:  #486 (line in Coconut source)
        return (y)  #487 (line in Coconut source)
    if not y:  #488 (line in Coconut source)
        return (x)  #489 (line in Coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #490 (line in Coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #491 (line in Coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #492 (line in Coconut source)


@_coconut_tco  #494 (line in Coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #494 (line in Coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #495 (line in Coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #502 (line in Coconut source)

@_coconut_tco  # type: ignore  #504 (line in Coconut source)
def fmap(f: '_coconut.typing.Callable[[Ta], Tb]', xs: 'Functor[Ta]') -> 'Functor[Tb]':  # type: ignore  #504 (line in Coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #507 (line in Coconut source)
    try:  #508 (line in Coconut source)
# Default implementation
        return (_fmap(f, xs))  #510 (line in Coconut source)

    except TypeError:  #512 (line in Coconut source)
# Function instance
        if callable(xs):  #514 (line in Coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #515 (line in Coconut source)

        raise  #517 (line in Coconut source)


@_coconut_tco  #519 (line in Coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #519 (line in Coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #523 (line in Coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #524 (line in Coconut source)

#### Applicative:

Applicative = Functor  #527 (line in Coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #528 (line in Coconut source)

if TYPE_CHECKING:  #530 (line in Coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #531 (line in Coconut source)
        ...  #532 (line in Coconut source)

else:  #533 (line in Coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #534 (line in Coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #538 (line in Coconut source)

        _coconut_is_data = True  #540 (line in Coconut source)
        __slots__ = ()  #540 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #540 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #540 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #540 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #540 (line in Coconut source)
        def __eq__(self, other):  #540 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #540 (line in Coconut source)
        def __hash__(self):  #540 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #540 (line in Coconut source)
        __match_args__ = ('val',)  #540 (line in Coconut source)
        def __join__(self) -> 'T.Any':  #540 (line in Coconut source)
            return (self.val)  #540 (line in Coconut source)


        def __call__(self, arg: 'T.Any') -> 'T.Any':  #542 (line in Coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #543 (line in Coconut source)
            return (self.val)  #544 (line in Coconut source)


        @_coconut_tco  #546 (line in Coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #546 (line in Coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #548 (line in Coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #549 (line in Coconut source)

            try:  #551 (line in Coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #553 (line in Coconut source)

            except TypeError:  #555 (line in Coconut source)
# Check for functions
                if callable(M):  #557 (line in Coconut source)
                    return _coconut_tail_call(const, self.val)  #558 (line in Coconut source)

# Fallback
                raise  #561 (line in Coconut source)


@_coconut_tco  #563 (line in Coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #563 (line in Coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #570 (line in Coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #572 (line in Coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #573 (line in Coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #576 (line in Coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #577 (line in Coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  #580 (line in Coconut source)


@_coconut_tco  #582 (line in Coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #582 (line in Coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #586 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #587 (line in Coconut source)


@_coconut_tco  #589 (line in Coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #589 (line in Coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #593 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #594 (line in Coconut source)


def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #596 (line in Coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #600 (line in Coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2))  # type: ignore  #601 (line in Coconut source)

#### Monad:

Monad = Applicative  #604 (line in Coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #605 (line in Coconut source)

@_coconut_tco  #607 (line in Coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #607 (line in Coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #612 (line in Coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #613 (line in Coconut source)


@_coconut_tco  #615 (line in Coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #615 (line in Coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #619 (line in Coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #620 (line in Coconut source)


return_ = pure  #622 (line in Coconut source)

if TYPE_CHECKING:  #624 (line in Coconut source)
    def fail(msg: 'str') -> 'T.Any':  #625 (line in Coconut source)
        ...  #626 (line in Coconut source)

else:  #627 (line in Coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #628 (line in Coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #631 (line in Coconut source)

        _coconut_is_data = True  #633 (line in Coconut source)
        __slots__ = ()  #633 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #633 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #633 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #633 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #633 (line in Coconut source)
        def __eq__(self, other):  #633 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #633 (line in Coconut source)
        def __hash__(self):  #633 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #633 (line in Coconut source)
        __match_args__ = ('msg',)  #633 (line in Coconut source)
        @staticmethod  #633 (line in Coconut source)
        def __bool__() -> 'bool':  #634 (line in Coconut source)
            return (False)  #634 (line in Coconut source)


        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #636 (line in Coconut source)
            return (self)  #636 (line in Coconut source)


        @_coconut_tco  #638 (line in Coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #638 (line in Coconut source)
            if (hasattr)(M, "__fail__"):  #639 (line in Coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #640 (line in Coconut source)
            return _coconut_tail_call(makedata, type(M))  #641 (line in Coconut source)

# sequence_ and mapM_ defined in Foldable


@_coconut_tco  #645 (line in Coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #645 (line in Coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #649 (line in Coconut source)
    return _coconut_tail_call((bind), m, func)  #650 (line in Coconut source)


@_coconut_tco  #652 (line in Coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #652 (line in Coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #659 (line in Coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #661 (line in Coconut source)
    _coconut_match_check_15 = False  #661 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #661 (line in Coconut source)
        _coconut_match_check_15 = True  #661 (line in Coconut source)
    if _coconut_match_check_15:  #661 (line in Coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #662 (line in Coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #665 (line in Coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #668 (line in Coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #669 (line in Coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  #672 (line in Coconut source)
    _coconut_case_match_check_0 = False  #672 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #672 (line in Coconut source)
        _coconut_case_match_check_0 = True  #672 (line in Coconut source)
    if _coconut_case_match_check_0:  #672 (line in Coconut source)
        if not ms:  #676 (line in Coconut source)
            return (ms)  # type: ignore  #677 (line in Coconut source)
        vals = []  # type: ignore  #678 (line in Coconut source)
        fallback = ms  #679 (line in Coconut source)
        for m in ms:  #680 (line in Coconut source)
            if m:  #681 (line in Coconut source)
                vals.extend(m)  # type: ignore  #682 (line in Coconut source)
            else:  #683 (line in Coconut source)
                fallback = m  # type: ignore  #684 (line in Coconut source)
        if not vals:  #685 (line in Coconut source)
            return (fallback)  # type: ignore  #686 (line in Coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  # type: ignore  #687 (line in Coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #690 (line in Coconut source)
        _coconut_case_match_check_0 = True  #690 (line in Coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #690 (line in Coconut source)
            _coconut_case_match_check_0 = False  #690 (line in Coconut source)
        if _coconut_case_match_check_0:  #690 (line in Coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #691 (line in Coconut source)

    if not _coconut_case_match_check_0:  #693 (line in Coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #694 (line in Coconut source)


if TYPE_CHECKING:  #696 (line in Coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]') -> 'TMonad':  #697 (line in Coconut source)
        ...  #698 (line in Coconut source)

else:  #699 (line in Coconut source)
    @_coconut_tco  #700 (line in Coconut source)
    @_coconut_mark_as_match  #700 (line in Coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #700 (line in Coconut source)
        _coconut_match_check_16 = False  #700 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #700 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #700 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #700 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #700 (line in Coconut source)
                _coconut_match_temp_27 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #700 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_27  #700 (line in Coconut source)
                if not _coconut_match_kwargs:  #700 (line in Coconut source)
                    _coconut_match_check_16 = True  #700 (line in Coconut source)
        if _coconut_match_check_16:  #700 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #700 (line in Coconut source)
                func = _coconut_match_set_name_func  #700 (line in Coconut source)
        if not _coconut_match_check_16:  #700 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #700 (line in Coconut source)

        return _coconut_tail_call(func)  #700 (line in Coconut source)

    @_coconut_addpattern(do)  #701 (line in Coconut source)
    @_coconut_tco  #701 (line in Coconut source)
    @_coconut_mark_as_match  #701 (line in Coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #701 (line in Coconut source)
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
        """  #720 (line in Coconut source)
        _coconut_match_check_17 = False  #721 (line in Coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #721 (line in Coconut source)
        _coconut_match_set_name_ms = _coconut_sentinel  #721 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #721 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #721 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #721 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #721 (line in Coconut source)
                _coconut_match_set_name_m = _coconut_match_args[0][0]  #721 (line in Coconut source)
                _coconut_match_temp_29 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #721 (line in Coconut source)
                _coconut_match_temp_28 = _coconut.list(_coconut_match_args[0][1:])  #721 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_29  #721 (line in Coconut source)
                _coconut_match_set_name_ms = _coconut_match_temp_28  #721 (line in Coconut source)
                if not _coconut_match_kwargs:  #721 (line in Coconut source)
                    _coconut_match_check_17 = True  #721 (line in Coconut source)
        if _coconut_match_check_17:  #721 (line in Coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #721 (line in Coconut source)
                m = _coconut_match_set_name_m  #721 (line in Coconut source)
            if _coconut_match_set_name_ms is not _coconut_sentinel:  #721 (line in Coconut source)
                ms = _coconut_match_set_name_ms  #721 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #721 (line in Coconut source)
                func = _coconut_match_set_name_func  #721 (line in Coconut source)
        if not _coconut_match_check_17:  #721 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #721 (line in Coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))  #721 (line in Coconut source)



## Folds and traversals:

#### Foldable:

Foldable = T.Sequence  #728 (line in Coconut source)

@_coconut_tco  #730 (line in Coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #730 (line in Coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #731 (line in Coconut source)


mapM_: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #733 (line in Coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #734 (line in Coconut source)

@_coconut_tco  #736 (line in Coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #736 (line in Coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #737 (line in Coconut source)


@_coconut_tco  #739 (line in Coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #739 (line in Coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #740 (line in Coconut source)


@_coconut_tco  #742 (line in Coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #742 (line in Coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #743 (line in Coconut source)


foldl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #745 (line in Coconut source)
foldl1 = reduce  #746 (line in Coconut source)

@_coconut_tco  #748 (line in Coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #748 (line in Coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #749 (line in Coconut source)


def null(xs: 'Foldable[Ta]') -> 'bool':  #751 (line in Coconut source)
    return (len(xs) == 0)  #752 (line in Coconut source)


length: '_coconut.typing.Callable[[Foldable], int]'  #754 (line in Coconut source)
length = len  #755 (line in Coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #757 (line in Coconut source)
    return (e in xs)  #758 (line in Coconut source)


maximum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #760 (line in Coconut source)
maximum = _max  #761 (line in Coconut source)

minimum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #763 (line in Coconut source)
minimum = _min  #764 (line in Coconut source)

sum: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #766 (line in Coconut source)
sum = _sum  #767 (line in Coconut source)

product: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #769 (line in Coconut source)
product = _coconut.functools.partial(reduce, _coconut.operator.mul)  #770 (line in Coconut source)

#### Traversable:
Traversable = T.Iterable  #773 (line in Coconut source)

@_coconut_tco  #775 (line in Coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #775 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #776 (line in Coconut source)


@_coconut_tco  #778 (line in Coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #778 (line in Coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #779 (line in Coconut source)


traverse: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #781 (line in Coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  #782 (line in Coconut source)

sequence: '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #784 (line in Coconut source)
sequence = sequenceA  #785 (line in Coconut source)

mapM: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #787 (line in Coconut source)
mapM = traverse  #788 (line in Coconut source)



## Miscellaneous functions:
id: '_coconut.typing.Callable[[Ta], Ta]' = ident  #793 (line in Coconut source)

@_coconut_tco  #795 (line in Coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #795 (line in Coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #799 (line in Coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #800 (line in Coconut source)


if TYPE_CHECKING:  #802 (line in Coconut source)
    @T.overload  #803 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #804 (line in Coconut source)
        ...  #805 (line in Coconut source)

    @T.overload  #806 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #807 (line in Coconut source)
        ...  #808 (line in Coconut source)

    @T.overload  #809 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #810 (line in Coconut source)
        ...  #811 (line in Coconut source)

    @T.overload  #812 (line in Coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta') -> 'T.Any':  #813 (line in Coconut source)
        ...  #814 (line in Coconut source)

    def apply(func, arg):  #815 (line in Coconut source)
        ...  #816 (line in Coconut source)

else:  #817 (line in Coconut source)
    @_coconut_tco  #818 (line in Coconut source)
    def apply(func, arg):  #818 (line in Coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #824 (line in Coconut source)
        return _coconut_tail_call((of), func, arg)  #825 (line in Coconut source)


@_coconut_tco  #827 (line in Coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #827 (line in Coconut source)
    while True:  #828 (line in Coconut source)
        if cond(x):  #828 (line in Coconut source)
            return (x)  #829 (line in Coconut source)
        try:  # tail recursive  #830 (line in Coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_71  # tail recursive  #830 (line in Coconut source)
        except _coconut.NameError:  # tail recursive  #830 (line in Coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #830 (line in Coconut source)
        if _coconut_tre_check_0:  # tail recursive  #830 (line in Coconut source)
            cond, func, x = cond, func, func(x)  # tail recursive  #830 (line in Coconut source)
            continue  # tail recursive  #830 (line in Coconut source)
        else:  # tail recursive  #830 (line in Coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #831 (line in Coconut source)
        return None  #832 (line in Coconut source)

_coconut_recursive_func_71 = until  #832 (line in Coconut source)

def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #832 (line in Coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #836 (line in Coconut source)
    if TYPE_CHECKING:  #837 (line in Coconut source)
        return (x)  #837 (line in Coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #839 (line in Coconut source)
        for i in (takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count()):  #840 (line in Coconut source)
            if (isinstance)(x, pure):  #841 (line in Coconut source)
                x = x.pure_as(y)  #842 (line in Coconut source)
            elif (isinstance)(x, fail):  #843 (line in Coconut source)
                x = x.fail_as(y)  #844 (line in Coconut source)
            elif (isinstance)(x, Mempty):  #845 (line in Coconut source)
                x = x.mempty_as(y)  #846 (line in Coconut source)
            else:  #847 (line in Coconut source)
                break  #848 (line in Coconut source)
    return (x)  #849 (line in Coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #851 (line in Coconut source)

def error(msg: 'str') -> 'None':  #853 (line in Coconut source)
    raise Exception(msg)  #854 (line in Coconut source)


def errorWithoutStackTrace(msg: 'str') -> 'None':  #856 (line in Coconut source)
    raise Exception(msg) from None  #857 (line in Coconut source)


undefined: 'T.Any' = None  #859 (line in Coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #861 (line in Coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #864 (line in Coconut source)
    return (y)  #865 (line in Coconut source)


@_coconut_tco  #867 (line in Coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #867 (line in Coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #872 (line in Coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #873 (line in Coconut source)




# List operations:

@_coconut_tco  #879 (line in Coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #879 (line in Coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #883 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #884 (line in Coconut source)

# type: ignore
map: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #886 (line in Coconut source)
map = _map  # type: ignore  #887 (line in Coconut source)

@_coconut_tco  #889 (line in Coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #889 (line in Coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #893 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #894 (line in Coconut source)

# type: ignore
filter: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #896 (line in Coconut source)
filter = _filter  # type: ignore  #897 (line in Coconut source)

head: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #899 (line in Coconut source)
head = _coconut.functools.partial(_coconut_iter_getitem, index=(0))  #900 (line in Coconut source)

last: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #902 (line in Coconut source)
last = _coconut.functools.partial(_coconut_iter_getitem, index=(-1))  #903 (line in Coconut source)

tail: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #905 (line in Coconut source)
tail = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #906 (line in Coconut source)

init: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #908 (line in Coconut source)
init = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #909 (line in Coconut source)

@_coconut_tco  #911 (line in Coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #911 (line in Coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #915 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #916 (line in Coconut source)


reverse: '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #918 (line in Coconut source)
reverse = _reversed  #919 (line in Coconut source)



## Special folds:
and_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #924 (line in Coconut source)
and_ = _all  #925 (line in Coconut source)

or_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #927 (line in Coconut source)
or_ = _any  #928 (line in Coconut source)

any: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #930 (line in Coconut source)
any = _coconut_forward_compose(map, or_)  #931 (line in Coconut source)

all: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #933 (line in Coconut source)
all = _coconut_forward_compose(map, and_)  #934 (line in Coconut source)

@_coconut_tco  #936 (line in Coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #936 (line in Coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #937 (line in Coconut source)


concatMap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #939 (line in Coconut source)
concatMap = _coconut_forward_compose(map, concat)  #940 (line in Coconut source)



## Building lists:

### Scans:
@_coconut_tco  #947 (line in Coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #947 (line in Coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #948 (line in Coconut source)


scanl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #950 (line in Coconut source)
scanl1 = scan  #951 (line in Coconut source)

@_coconut_tco  #953 (line in Coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #953 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #954 (line in Coconut source)


@_coconut_tco  #956 (line in Coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #956 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #957 (line in Coconut source)

### Infinite lists:

@recursive_iterator  #960 (line in Coconut source)
@_coconut_tco  #961 (line in Coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #961 (line in Coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #962 (line in Coconut source)


@recursive_iterator  #964 (line in Coconut source)
@_coconut_tco  #965 (line in Coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #965 (line in Coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #966 (line in Coconut source)


@_coconut_tco  #968 (line in Coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #968 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #969 (line in Coconut source)


if TYPE_CHECKING:  #971 (line in Coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #972 (line in Coconut source)
        ...  #973 (line in Coconut source)

else:  #974 (line in Coconut source)
    @recursive_iterator  #975 (line in Coconut source)
    @_coconut_tco  #976 (line in Coconut source)
    @_coconut_mark_as_match  #976 (line in Coconut source)
    def cycle(*_coconut_match_args, **_coconut_match_kwargs):  #976 (line in Coconut source)
        _coconut_match_check_18 = False  #976 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #976 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #976 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #976 (line in Coconut source)
            _coconut_match_temp_30 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #976 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_30  #976 (line in Coconut source)
            if not _coconut_match_kwargs:  #976 (line in Coconut source)
                _coconut_match_check_18 = True  #976 (line in Coconut source)
        if _coconut_match_check_18:  #976 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #976 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #976 (line in Coconut source)
        if _coconut_match_check_18 and not (len(xs) > 0):  #976 (line in Coconut source)
            _coconut_match_check_18 = False  #976 (line in Coconut source)
        if not _coconut_match_check_18:  #976 (line in Coconut source)
            raise _coconut_FunctionMatchError('def cycle(xs if len(xs) > 0) =', _coconut_match_args)  #976 (line in Coconut source)

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))  #977 (line in Coconut source)



## Sublists:

@_coconut_tco  #982 (line in Coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #982 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #983 (line in Coconut source)


@_coconut_tco  #985 (line in Coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #985 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #986 (line in Coconut source)


def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> 'T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]':  #988 (line in Coconut source)
    reit = reiterable(xs)  #989 (line in Coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #990 (line in Coconut source)


takeWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #992 (line in Coconut source)
takeWhile = takewhile  #993 (line in Coconut source)

dropWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #995 (line in Coconut source)
dropWhile = dropwhile  #996 (line in Coconut source)

if TYPE_CHECKING:  #998 (line in Coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]':  #999 (line in Coconut source)
        ...  #1000 (line in Coconut source)

else:  #1001 (line in Coconut source)
    @_coconut_mark_as_match  #1002 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1002 (line in Coconut source)
        _coconut_match_check_19 = False  #1002 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1002 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #1002 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1002 (line in Coconut source)
                if not _coconut_match_kwargs:  #1002 (line in Coconut source)
                    _coconut_match_check_19 = True  #1002 (line in Coconut source)
        if not _coconut_match_check_19:  #1002 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #1002 (line in Coconut source)

        return (([], []))  #1002 (line in Coconut source)

    @_coconut_addpattern(span)  #1003 (line in Coconut source)
    @_coconut_mark_as_match  #1003 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1003 (line in Coconut source)
        _coconut_match_check_20 = False  #1003 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1003 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #1003 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1003 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1003 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1003 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1003 (line in Coconut source)
                _coconut_match_temp_31 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1003 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_args[1][0]  #1003 (line in Coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_31  #1003 (line in Coconut source)
                _coconut_match_temp_32 = _coconut.list(_coconut_match_args[1][1:])  #1003 (line in Coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_32  #1003 (line in Coconut source)
                if not _coconut_match_kwargs:  #1003 (line in Coconut source)
                    _coconut_match_check_20 = True  #1003 (line in Coconut source)
        if _coconut_match_check_20:  #1003 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1003 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1003 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #1003 (line in Coconut source)
                x = _coconut_match_set_name_x  #1003 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1003 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1003 (line in Coconut source)
        if _coconut_match_check_20 and not (cond(x)):  #1003 (line in Coconut source)
            _coconut_match_check_20 = False  #1003 (line in Coconut source)
        if not _coconut_match_check_20:  #1003 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #1003 (line in Coconut source)

        ys, zs = span(cond, xs)  #1004 (line in Coconut source)
        return (([x,] + ys, zs))  #1005 (line in Coconut source)

    @_coconut_addpattern(span)  #1006 (line in Coconut source)
    @_coconut_mark_as_match  #1006 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1006 (line in Coconut source)
        _coconut_match_check_21 = False  #1006 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1006 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1006 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1006 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1006 (line in Coconut source)
            _coconut_match_temp_33 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1006 (line in Coconut source)
            _coconut_match_temp_34 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1006 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_match_temp_33  #1006 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_34  #1006 (line in Coconut source)
            if not _coconut_match_kwargs:  #1006 (line in Coconut source)
                _coconut_match_check_21 = True  #1006 (line in Coconut source)
        if _coconut_match_check_21:  #1006 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1006 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1006 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1006 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1006 (line in Coconut source)
        if not _coconut_match_check_21:  #1006 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #1006 (line in Coconut source)

        return (([], xs))  #1007 (line in Coconut source)


@_coconut_tco  #1009 (line in Coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #1009 (line in Coconut source)
    """
    break_ = break
    """  #1012 (line in Coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1013 (line in Coconut source)



## Searching lists:

def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #1018 (line in Coconut source)
    return (e not in xs)  #1019 (line in Coconut source)


def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'Maybe':  #1021 (line in Coconut source)
    try:  #1022 (line in Coconut source)
        return (((Just)((_coconut_iter_getitem((dropwhile)(lambda pair: pair[0] != key, assocs), (0)))[1])))  #1023 (line in Coconut source)
    except IndexError:  #1030 (line in Coconut source)
        return (nothing)  #1031 (line in Coconut source)



## Zipping and unzipping lists:
# type: ignore
zip: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]'  # type: ignore  #1036 (line in Coconut source)
zip = _zip  # type: ignore  #1037 (line in Coconut source)

zip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]'  #1039 (line in Coconut source)
zip3 = _zip  #1040 (line in Coconut source)

@_coconut_tco  #1042 (line in Coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #1042 (line in Coconut source)
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))  #1043 (line in Coconut source)


@_coconut_tco  #1045 (line in Coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #1045 (line in Coconut source)
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))  #1046 (line in Coconut source)


@_coconut_tco  #1048 (line in Coconut source)
def unzip(xs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]':  #1048 (line in Coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1049 (line in Coconut source)


unzip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]'  #1051 (line in Coconut source)
unzip3 = unzip  # type: ignore  #1052 (line in Coconut source)



## Functions on strings:
lines: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1057 (line in Coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1058 (line in Coconut source)

words: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1060 (line in Coconut source)
words = _coconut.operator.methodcaller("split")  #1061 (line in Coconut source)

@_coconut_tco  #1063 (line in Coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1063 (line in Coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1064 (line in Coconut source)


unwords: '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1066 (line in Coconut source)
unwords = " ".join  #1067 (line in Coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1075 (line in Coconut source)

Show = T.Any  #1077 (line in Coconut source)

showsPrec = NotImplemented  #1079 (line in Coconut source)

show: '_coconut.typing.Callable[[Ta], str]'  #1081 (line in Coconut source)
show = repr  #1082 (line in Coconut source)

def shows(x: 'Show') -> 'ShowS':  #1084 (line in Coconut source)
    return (lambda s: repr(x) + s)  #1085 (line in Coconut source)


def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1087 (line in Coconut source)
    return (lambda s: repr(list(xs)) + s)  #1088 (line in Coconut source)


def showString(x: 'str') -> 'ShowS':  #1090 (line in Coconut source)
    return (lambda s: x + s)  #1091 (line in Coconut source)


showChar: '_coconut.typing.Callable[[Char], ShowS]'  #1093 (line in Coconut source)
showChar = showString  #1094 (line in Coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1096 (line in Coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1097 (line in Coconut source)



## Converting from String:

ReadS = NotImplemented  #1105 (line in Coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1107 (line in Coconut source)

readsPrec = NotImplemented  #1118 (line in Coconut source)

readList = NotImplemented  #1120 (line in Coconut source)

reads = NotImplemented  #1122 (line in Coconut source)

readParen = NotImplemented  #1124 (line in Coconut source)

@_coconut_tco  #1126 (line in Coconut source)
def read(s: 'str') -> 'Read':  #1126 (line in Coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1127 (line in Coconut source)


lex = NotImplemented  #1129 (line in Coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1137 (line in Coconut source)
    _coconut_is_data = True  #1137 (line in Coconut source)
    __slots__ = ()  #1137 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1137 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1137 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1137 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #1137 (line in Coconut source)
    def __eq__(self, other):  #1137 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1137 (line in Coconut source)
    def __hash__(self):  #1137 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1137 (line in Coconut source)
    __match_args__ = ('io_func',)  #1137 (line in Coconut source)
    @staticmethod  #1138 (line in Coconut source)
    @_coconut_tco  #1139 (line in Coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1139 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1140 (line in Coconut source)


    @staticmethod  #1142 (line in Coconut source)
    @_coconut_tco  #1143 (line in Coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1143 (line in Coconut source)
        def _coconut_lambda_0():  #1144 (line in Coconut source)
            raise IOError(msg)  #1144 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_lambda_0)  #1144 (line in Coconut source)


    @_coconut_tco  #1146 (line in Coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1146 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1147 (line in Coconut source)


    @_coconut_tco  #1149 (line in Coconut source)
    def __join__(self) -> 'IO':  #1149 (line in Coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1150 (line in Coconut source)


    @staticmethod  #1152 (line in Coconut source)
    @_coconut_tco  #1153 (line in Coconut source)
    def __mempty__() -> 'IO':  #1153 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1154 (line in Coconut source)


    @_coconut_tco  #1156 (line in Coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1156 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1157 (line in Coconut source)


_nullIO: 'IO' = IO(lambda: None)  #1159 (line in Coconut source)

@_coconut_tco  #1161 (line in Coconut source)
def asIO(io: 'IO') -> 'IO':  #1161 (line in Coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1166 (line in Coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1167 (line in Coconut source)


@_coconut_tco  #1169 (line in Coconut source)
def unIO(io: 'IO') -> 'T.Any':  #1169 (line in Coconut source)
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
    """  #1183 (line in Coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1184 (line in Coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1192 (line in Coconut source)
def putStr(s: 'str') -> 'IO':  #1192 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))  #1193 (line in Coconut source)


putChar: '_coconut.typing.Callable[[Char], IO]'  #1195 (line in Coconut source)
putChar = putStr  #1196 (line in Coconut source)

@_coconut_tco  #1198 (line in Coconut source)
def putStrLn(s: 'str') -> 'IO':  #1198 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))  #1199 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1201 (line in Coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1201 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))  #1202 (line in Coconut source)


### Input functions:

getChar: 'IO' = IO(_coconut.functools.partial(sys.stdin.read, 1))  #1206 (line in Coconut source)

getLine: 'IO' = IO(input)  #1208 (line in Coconut source)

getContents: 'IO' = IO(sys.stdin.read)  #1210 (line in Coconut source)

@_coconut_tco  #1212 (line in Coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1212 (line in Coconut source)
    def do_interact():  #1213 (line in Coconut source)
        while True:  #1214 (line in Coconut source)
            (_print)((func)(input()))  #1215 (line in Coconut source)

    return _coconut_tail_call(IO, do_interact)  #1216 (line in Coconut source)


### Files:

FilePath = str  #1220 (line in Coconut source)

@_coconut_tco  #1222 (line in Coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1222 (line in Coconut source)
    def do_readFile() -> 'str':  #1223 (line in Coconut source)
        with open(fpath, "r+") as f:  #1224 (line in Coconut source)
            return (f.read())  #1225 (line in Coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1226 (line in Coconut source)


@_coconut_tco  #1228 (line in Coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1228 (line in Coconut source)
    def do_writeFile() -> 'None':  #1229 (line in Coconut source)
        with open(fpath, "w+") as f:  #1230 (line in Coconut source)
            f.write(text)  #1231 (line in Coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1232 (line in Coconut source)


@_coconut_tco  #1234 (line in Coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1234 (line in Coconut source)
    def do_appendFile() -> 'None':  #1235 (line in Coconut source)
        with open(fpath, "a+") as f:  #1236 (line in Coconut source)
            f.write(text)  #1237 (line in Coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1238 (line in Coconut source)


@_coconut_tco  #1240 (line in Coconut source)
def readIO(s: 'str') -> 'IO':  #1240 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))  #1241 (line in Coconut source)


@_coconut_tco  #1243 (line in Coconut source)
def readLn() -> 'IO':  #1243 (line in Coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1244 (line in Coconut source)



## Exception handling:

@_coconut_tco  #1249 (line in Coconut source)
def ioError(err: 'IOError') -> 'IO':  #1249 (line in Coconut source)
    def _coconut_lambda_1():  #1250 (line in Coconut source)
        raise err  #1250 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_lambda_1)  #1250 (line in Coconut source)


@_coconut_tco  #1252 (line in Coconut source)
def userError(msg: 'str') -> 'IOError':  #1252 (line in Coconut source)
    return _coconut_tail_call(IOError, msg)  #1253 (line in Coconut source)
