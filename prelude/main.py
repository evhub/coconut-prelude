#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf3d07e71

# Compiled with Coconut version 2.0.0-a_dev9 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op
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
not_ = _coconut.operator.not_  #42 (line num in coconut source)

otherwise: 'bool' = True  #44 (line num in coconut source)

#### Maybe:
class Maybe:  #47 (line num in coconut source)
    @staticmethod  #48 (line num in coconut source)
    @_coconut_tco  #48 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'Maybe':  #48 (line num in coconut source)
        return _coconut_tail_call(Just, x)  #49 (line num in coconut source)

    @staticmethod  #51 (line num in coconut source)
    def __fail__(msg: 'str') -> 'Maybe':  #51 (line num in coconut source)
        return (nothing)  #52 (line num in coconut source)

    @staticmethod  #54 (line num in coconut source)
    def __mempty__() -> 'Maybe':  #54 (line num in coconut source)
        return (nothing)  #55 (line num in coconut source)

class Nothing(_coconut.collections.namedtuple("Nothing", ()), Maybe):  #57 (line num in coconut source)
    _coconut_is_data = True  #57 (line num in coconut source)
    __slots__ = ()  #57 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #57 (line num in coconut source)
    def __eq__(self, other):  #57 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #57 (line num in coconut source)
    def __hash__(self):  #57 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #57 (line num in coconut source)
    __match_args__ = ()  #57 (line num in coconut source)
nothing: 'Maybe' = Nothing()  #58 (line num in coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #60 (line num in coconut source)
    _coconut_is_data = True  #60 (line num in coconut source)
    __slots__ = ()  #60 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #60 (line num in coconut source)
    def __eq__(self, other):  #60 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #60 (line num in coconut source)
    def __hash__(self):  #60 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #60 (line num in coconut source)
    __match_args__ = ('x',)  #60 (line num in coconut source)

derivingOrd(Nothing, Just)  #62 (line num in coconut source)

if TYPE_CHECKING:  #64 (line num in coconut source)
    def maybe(default: 'Tb', func: '_coconut.typing.Callable[[Ta], Tb]', x: 'Maybe') -> 'Tb':  #65 (line num in coconut source)
        ...  #66 (line num in coconut source)
else:  #67 (line num in coconut source)
    @_coconut_mark_as_match  #68 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #68 (line num in coconut source)
        _coconut_match_check_0 = False  #68 (line num in coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #68 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #68 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #68 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #68 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)   #type: ignore  #68 (line num in coconut source)
            if not _coconut_match_kwargs:  #68 (line num in coconut source)
                _coconut_match_set_name_default = _coconut_match_temp_0  #68 (line num in coconut source)
                _coconut_match_check_0 = True  #68 (line num in coconut source)
        if _coconut_match_check_0:  #68 (line num in coconut source)
            _coconut_match_check_0 = False  #68 (line num in coconut source)
            if not _coconut_match_check_0:  #68 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)) and (_coconut.len(_coconut_match_args[2]) == 0):  #68 (line num in coconut source)
                    _coconut_match_check_0 = True  #68 (line num in coconut source)

            if not _coconut_match_check_0:  #68 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #68 (line num in coconut source)
                    _coconut_match_check_0 = True  #68 (line num in coconut source)
                if _coconut_match_check_0:  #68 (line num in coconut source)
                    _coconut_match_check_0 = False  #68 (line num in coconut source)
                    if not _coconut_match_check_0:  #68 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #68 (line num in coconut source)
                            _coconut_match_check_0 = True  #68 (line num in coconut source)

                    if not _coconut_match_check_0:  #68 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #68 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Nothing, '__match_args__', ())  #68 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #68 (line num in coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #68 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 0:  #68 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #68 (line num in coconut source)
                            _coconut_match_check_0 = True  #68 (line num in coconut source)


        if _coconut_match_check_0:  #68 (line num in coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #68 (line num in coconut source)
                default = _coconut_match_temp_0  #68 (line num in coconut source)
        if not _coconut_match_check_0:  #68 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #68 (line num in coconut source)

        return (default)  #68 (line num in coconut source)
    @_coconut_addpattern(maybe)  #69 (line num in coconut source)
    @_coconut_tco  #69 (line num in coconut source)
    @_coconut_mark_as_match  #69 (line num in coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #69 (line num in coconut source)
        _coconut_match_check_1 = False  #69 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #69 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #69 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #69 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #69 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)   #type: ignore  #69 (line num in coconut source)
            if not _coconut_match_kwargs:  #69 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_0  #69 (line num in coconut source)
                _coconut_match_check_1 = True  #69 (line num in coconut source)
        if _coconut_match_check_1:  #69 (line num in coconut source)
            _coconut_match_check_1 = False  #69 (line num in coconut source)
            if not _coconut_match_check_1:  #69 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #69 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) == 1):  #69 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #69 (line num in coconut source)
                    _coconut_match_check_1 = True  #69 (line num in coconut source)
                if _coconut_match_check_1:  #69 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #69 (line num in coconut source)
                        x = _coconut_match_args[2][0]  #69 (line num in coconut source)

            if not _coconut_match_check_1:  #69 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #69 (line num in coconut source)
                    _coconut_match_check_1 = True  #69 (line num in coconut source)
                if _coconut_match_check_1:  #69 (line num in coconut source)
                    _coconut_match_check_1 = False  #69 (line num in coconut source)
                    if not _coconut_match_check_1:  #69 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #69 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #69 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #69 (line num in coconut source)
                            _coconut_match_check_1 = True  #69 (line num in coconut source)
                        if _coconut_match_check_1:  #69 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #69 (line num in coconut source)
                                x = _coconut_match_args[2]  #69 (line num in coconut source)

                    if not _coconut_match_check_1:  #69 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #69 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #69 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Just, '__match_args__', ())  #69 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #69 (line num in coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #69 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 1:  #69 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #69 (line num in coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_2[0], _coconut_sentinel)  #69 (line num in coconut source)
                            if _coconut_match_temp_3 is not _coconut_sentinel:  #69 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_3  #69 (line num in coconut source)
                                _coconut_match_check_1 = True  #69 (line num in coconut source)
                        if _coconut_match_check_1:  #69 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #69 (line num in coconut source)
                                x = _coconut_match_temp_3  #69 (line num in coconut source)


        if _coconut_match_check_1:  #69 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #69 (line num in coconut source)
                func = _coconut_match_temp_0  #69 (line num in coconut source)
        if not _coconut_match_check_1:  #69 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #69 (line num in coconut source)

        return _coconut_tail_call(func, x)  #69 (line num in coconut source)

#### Either:
class Either:  #72 (line num in coconut source)
    @staticmethod  #73 (line num in coconut source)
    @_coconut_tco  #73 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'Either':  #73 (line num in coconut source)
        return _coconut_tail_call(Right, x)  #74 (line num in coconut source)

    @staticmethod  #76 (line num in coconut source)
    @_coconut_tco  #76 (line num in coconut source)
    def __fail__(msg: 'str') -> 'Either':  #76 (line num in coconut source)
        return _coconut_tail_call(Left, msg)  #77 (line num in coconut source)

class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #79 (line num in coconut source)
    _coconut_is_data = True  #79 (line num in coconut source)
    __slots__ = ()  #79 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #79 (line num in coconut source)
    def __eq__(self, other):  #79 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #79 (line num in coconut source)
    def __hash__(self):  #79 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #79 (line num in coconut source)
    __match_args__ = ('x',)  #79 (line num in coconut source)
    @staticmethod  #79 (line num in coconut source)
    def __bool__() -> 'bool':  #79 (line num in coconut source)
        return (False)  #81 (line num in coconut source)

    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'Either':  #83 (line num in coconut source)
        return (self)  #83 (line num in coconut source)

class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #85 (line num in coconut source)
    _coconut_is_data = True  #85 (line num in coconut source)
    __slots__ = ()  #85 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #85 (line num in coconut source)
    def __eq__(self, other):  #85 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #85 (line num in coconut source)
    def __hash__(self):  #85 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #85 (line num in coconut source)
    __match_args__ = ('x',)  #85 (line num in coconut source)

derivingOrd(Left, Right)  #87 (line num in coconut source)

if TYPE_CHECKING:  #89 (line num in coconut source)
    def either(left_func: '_coconut.typing.Callable[[Ta], Tc]', right_func: '_coconut.typing.Callable[[Tb], Tc]', x: 'Either') -> 'Tc':  #90 (line num in coconut source)
        ...  #91 (line num in coconut source)
else:  #92 (line num in coconut source)
    @_coconut_tco  #93 (line num in coconut source)
    @_coconut_mark_as_match  #93 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #93 (line num in coconut source)
        _coconut_match_check_2 = False  #93 (line num in coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #93 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #93 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #93 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #93 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)   #type: ignore  #93 (line num in coconut source)
            if not _coconut_match_kwargs:  #93 (line num in coconut source)
                _coconut_match_set_name_left_func = _coconut_match_temp_0  #93 (line num in coconut source)
                _coconut_match_check_2 = True  #93 (line num in coconut source)
        if _coconut_match_check_2:  #93 (line num in coconut source)
            _coconut_match_check_2 = False  #93 (line num in coconut source)
            if not _coconut_match_check_2:  #93 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #93 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) == 1):  #93 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #93 (line num in coconut source)
                    _coconut_match_check_2 = True  #93 (line num in coconut source)
                if _coconut_match_check_2:  #93 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #93 (line num in coconut source)
                        x = _coconut_match_args[2][0]  #93 (line num in coconut source)

            if not _coconut_match_check_2:  #93 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #93 (line num in coconut source)
                    _coconut_match_check_2 = True  #93 (line num in coconut source)
                if _coconut_match_check_2:  #93 (line num in coconut source)
                    _coconut_match_check_2 = False  #93 (line num in coconut source)
                    if not _coconut_match_check_2:  #93 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #93 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #93 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #93 (line num in coconut source)
                            _coconut_match_check_2 = True  #93 (line num in coconut source)
                        if _coconut_match_check_2:  #93 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #93 (line num in coconut source)
                                x = _coconut_match_args[2]  #93 (line num in coconut source)

                    if not _coconut_match_check_2:  #93 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #93 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #93 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Left, '__match_args__', ())  #93 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #93 (line num in coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #93 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 1:  #93 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #93 (line num in coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_2[0], _coconut_sentinel)  #93 (line num in coconut source)
                            if _coconut_match_temp_3 is not _coconut_sentinel:  #93 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_3  #93 (line num in coconut source)
                                _coconut_match_check_2 = True  #93 (line num in coconut source)
                        if _coconut_match_check_2:  #93 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #93 (line num in coconut source)
                                x = _coconut_match_temp_3  #93 (line num in coconut source)


        if _coconut_match_check_2:  #93 (line num in coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #93 (line num in coconut source)
                left_func = _coconut_match_temp_0  #93 (line num in coconut source)
        if not _coconut_match_check_2:  #93 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #93 (line num in coconut source)

        return _coconut_tail_call(left_func, x)  #93 (line num in coconut source)
    @_coconut_addpattern(either)  #94 (line num in coconut source)
    @_coconut_tco  #94 (line num in coconut source)
    @_coconut_mark_as_match  #94 (line num in coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #94 (line num in coconut source)
        _coconut_match_check_3 = False  #94 (line num in coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #94 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #94 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #94 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #94 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)   #type: ignore  #94 (line num in coconut source)
            if not _coconut_match_kwargs:  #94 (line num in coconut source)
                _coconut_match_set_name_right_func = _coconut_match_temp_0  #94 (line num in coconut source)
                _coconut_match_check_3 = True  #94 (line num in coconut source)
        if _coconut_match_check_3:  #94 (line num in coconut source)
            _coconut_match_check_3 = False  #94 (line num in coconut source)
            if not _coconut_match_check_3:  #94 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #94 (line num in coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) == 1):  #94 (line num in coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #94 (line num in coconut source)
                    _coconut_match_check_3 = True  #94 (line num in coconut source)
                if _coconut_match_check_3:  #94 (line num in coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #94 (line num in coconut source)
                        x = _coconut_match_args[2][0]  #94 (line num in coconut source)

            if not _coconut_match_check_3:  #94 (line num in coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #94 (line num in coconut source)
                    _coconut_match_check_3 = True  #94 (line num in coconut source)
                if _coconut_match_check_3:  #94 (line num in coconut source)
                    _coconut_match_check_3 = False  #94 (line num in coconut source)
                    if not _coconut_match_check_3:  #94 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #94 (line num in coconut source)
                        if _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #94 (line num in coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #94 (line num in coconut source)
                            _coconut_match_check_3 = True  #94 (line num in coconut source)
                        if _coconut_match_check_3:  #94 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #94 (line num in coconut source)
                                x = _coconut_match_args[2]  #94 (line num in coconut source)

                    if not _coconut_match_check_3:  #94 (line num in coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #94 (line num in coconut source)
                        if not _coconut.isinstance(_coconut_match_args[2], _coconut_self_match_types):  #94 (line num in coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Right, '__match_args__', ())  #94 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #94 (line num in coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #94 (line num in coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 1:  #94 (line num in coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #94 (line num in coconut source)
                            _coconut_match_temp_3 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_2[0], _coconut_sentinel)  #94 (line num in coconut source)
                            if _coconut_match_temp_3 is not _coconut_sentinel:  #94 (line num in coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_3  #94 (line num in coconut source)
                                _coconut_match_check_3 = True  #94 (line num in coconut source)
                        if _coconut_match_check_3:  #94 (line num in coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #94 (line num in coconut source)
                                x = _coconut_match_temp_3  #94 (line num in coconut source)


        if _coconut_match_check_3:  #94 (line num in coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #94 (line num in coconut source)
                right_func = _coconut_match_temp_0  #94 (line num in coconut source)
        if not _coconut_match_check_3:  #94 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #94 (line num in coconut source)

        return _coconut_tail_call(right_func, x)  #94 (line num in coconut source)

#### Ordering:
class Ordering:  #97 (line num in coconut source)
    @staticmethod  #98 (line num in coconut source)
    def __mempty__() -> 'Ordering':  #98 (line num in coconut source)
        return (eq)  #99 (line num in coconut source)

class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #101 (line num in coconut source)
    _coconut_is_data = True  #101 (line num in coconut source)
    __slots__ = ()  #101 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #101 (line num in coconut source)
    def __eq__(self, other):  #101 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #101 (line num in coconut source)
    def __hash__(self):  #101 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #101 (line num in coconut source)
    __match_args__ = ()  #101 (line num in coconut source)
    @staticmethod  #101 (line num in coconut source)
    def __bool__() -> 'bool':  #101 (line num in coconut source)
        return (True)  #103 (line num in coconut source)

class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #105 (line num in coconut source)
    _coconut_is_data = True  #105 (line num in coconut source)
    __slots__ = ()  #105 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #105 (line num in coconut source)
    def __eq__(self, other):  #105 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #105 (line num in coconut source)
    def __hash__(self):  #105 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #105 (line num in coconut source)
    __match_args__ = ()  #105 (line num in coconut source)

class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #107 (line num in coconut source)
    _coconut_is_data = True  #107 (line num in coconut source)
    __slots__ = ()  #107 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #107 (line num in coconut source)
    def __eq__(self, other):  #107 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #107 (line num in coconut source)
    def __hash__(self):  #107 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #107 (line num in coconut source)
    __match_args__ = ()  #107 (line num in coconut source)
    @staticmethod  #107 (line num in coconut source)
    def __bool__() -> 'bool':  #107 (line num in coconut source)
        return (True)  #109 (line num in coconut source)

derivingOrd(LT, EQ, GT)  #111 (line num in coconut source)
derivingBoundedEnum(LT, EQ, GT)  #112 (line num in coconut source)

lt: 'Ordering' = LT()  #114 (line num in coconut source)
eq: 'Ordering' = EQ()  #115 (line num in coconut source)
gt: 'Ordering' = GT()  #116 (line num in coconut source)

#### Char:
Char = T.NewType("Char", str)  #119 (line num in coconut source)

#### String:
String = str  #122 (line num in coconut source)


### Tuples:
fst: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]'  #126 (line num in coconut source)
fst = _coconut.operator.itemgetter((0))  #127 (line num in coconut source)

snd: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]'  #129 (line num in coconut source)
snd = _coconut.operator.itemgetter((1))  #130 (line num in coconut source)

def curry_tuple(func: '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]') -> '_coconut.typing.Callable[[Ta, Tb], Tc]':  #132 (line num in coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #135 (line num in coconut source)
    return (lambda *args: func(args))  # type: ignore  #136 (line num in coconut source)

def uncurry_tuple(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]':  #138 (line num in coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #141 (line num in coconut source)
    return (lambda args: func(*args))  #142 (line num in coconut source)



## Basic type classes:

#### Eq:
Eq = object  #149 (line num in coconut source)

#### Ord:
Ord = Eq  #152 (line num in coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #153 (line num in coconut source)

if TYPE_CHECKING:  #155 (line num in coconut source)
    def compare(x: 'Ord', y: 'Ord') -> 'Ordering':  #156 (line num in coconut source)
        ...  #157 (line num in coconut source)
else:  #158 (line num in coconut source)
    @_coconut_mark_as_match  #159 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #159 (line num in coconut source)
        _coconut_match_check_4 = False  #159 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #159 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #159 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #159 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #159 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #159 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #159 (line num in coconut source)
            if not _coconut_match_kwargs:  #159 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #159 (line num in coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_1  #159 (line num in coconut source)
                _coconut_match_check_4 = True  #159 (line num in coconut source)
        if _coconut_match_check_4:  #159 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #159 (line num in coconut source)
                x = _coconut_match_temp_0  #159 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #159 (line num in coconut source)
                y = _coconut_match_temp_1  #159 (line num in coconut source)
        if _coconut_match_check_4 and not (x == y):  #159 (line num in coconut source)
            _coconut_match_check_4 = False  #159 (line num in coconut source)
        if not _coconut_match_check_4:  #159 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #159 (line num in coconut source)

        return (eq)  #159 (line num in coconut source)
    @_coconut_addpattern(compare)  #160 (line num in coconut source)
    @_coconut_mark_as_match  #160 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #160 (line num in coconut source)
        _coconut_match_check_5 = False  #160 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #160 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #160 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #160 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #160 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #160 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #160 (line num in coconut source)
            if not _coconut_match_kwargs:  #160 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #160 (line num in coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_1  #160 (line num in coconut source)
                _coconut_match_check_5 = True  #160 (line num in coconut source)
        if _coconut_match_check_5:  #160 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #160 (line num in coconut source)
                x = _coconut_match_temp_0  #160 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #160 (line num in coconut source)
                y = _coconut_match_temp_1  #160 (line num in coconut source)
        if _coconut_match_check_5 and not (x < y):  #160 (line num in coconut source)
            _coconut_match_check_5 = False  #160 (line num in coconut source)
        if not _coconut_match_check_5:  #160 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #160 (line num in coconut source)

        return (lt)  #160 (line num in coconut source)
    @_coconut_addpattern(compare)  #161 (line num in coconut source)
    @_coconut_mark_as_match  #161 (line num in coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #161 (line num in coconut source)
        _coconut_match_check_6 = False  #161 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #161 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #161 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #161 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #161 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #161 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #161 (line num in coconut source)
            if not _coconut_match_kwargs:  #161 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #161 (line num in coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_1  #161 (line num in coconut source)
                _coconut_match_check_6 = True  #161 (line num in coconut source)
        if _coconut_match_check_6:  #161 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #161 (line num in coconut source)
                x = _coconut_match_temp_0  #161 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #161 (line num in coconut source)
                y = _coconut_match_temp_1  #161 (line num in coconut source)
        if _coconut_match_check_6 and not (x > y):  #161 (line num in coconut source)
            _coconut_match_check_6 = False  #161 (line num in coconut source)
        if not _coconut_match_check_6:  #161 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #161 (line num in coconut source)

        return (gt)  #161 (line num in coconut source)

max: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #163 (line num in coconut source)
max = _max  #164 (line num in coconut source)

min: '_coconut.typing.Callable[[TOrd, TOrd], TOrd]'  #166 (line num in coconut source)
min = _min  #167 (line num in coconut source)

#### Enum:
Enum = Ord  #170 (line num in coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #171 (line num in coconut source)

succ: '_coconut.typing.Callable[[TEnum], TEnum]'  #173 (line num in coconut source)
succ = _coconut.functools.partial(_coconut.operator.add, 1)  #174 (line num in coconut source)

pred: '_coconut.typing.Callable[[TEnum], TEnum]'  #176 (line num in coconut source)
pred = _coconut_partial(_coconut_minus, {1: 1}, 2)  #177 (line num in coconut source)

toEnum = NotImplemented  #179 (line num in coconut source)

fromEnum: '_coconut.typing.Callable[[Enum], int]'  #181 (line num in coconut source)
fromEnum = _int  #182 (line num in coconut source)

@_coconut_tco  #184 (line num in coconut source)
def enumFrom(first: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #184 (line num in coconut source)
    return _coconut_tail_call(iterate, succ, first)  #185 (line num in coconut source)

def enumFromThen(first: 'TEnum', second: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #187 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #188 (line num in coconut source)
    return (iterate(_coconut.functools.partial(_coconut.operator.add, step), first) if step >= 0 else ())  # type: ignore  #189 (line num in coconut source)

def enumFromTo(first: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #191 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #192 (line num in coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #193 (line num in coconut source)

def enumFromThenTo(first: 'TEnum', second: 'TEnum', last: 'TEnum') -> '_coconut.typing.Iterable[TEnum]':  #195 (line num in coconut source)
    step = fromEnum(second) - fromEnum(first)  #196 (line num in coconut source)
    dist = fromEnum(last) - fromEnum(first)  #197 (line num in coconut source)
    steps = dist / step if step != 0 else 0  #198 (line num in coconut source)
    if steps < 0:  #199 (line num in coconut source)
        return (())  #200 (line num in coconut source)
    counter = iterate(_coconut.functools.partial(_coconut.operator.add, step), first)  #201 (line num in coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #202 (line num in coconut source)


#### Bounded:
Bounded = T.Union[bool, T.Iterable]  #206 (line num in coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #207 (line num in coconut source)

@_coconut_tco  #209 (line num in coconut source)
def minBound(b: 'TBounded') -> 'TBounded':  #209 (line num in coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #213 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #215 (line num in coconut source)
        return (False)  # type: ignore  #216 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #219 (line num in coconut source)
        return _coconut_tail_call(b.__minBound__)  #220 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(_fmap, minBound, b)  #223 (line num in coconut source)

@_coconut_tco  #225 (line num in coconut source)
def maxBound(b: 'TBounded') -> 'TBounded':  #225 (line num in coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #229 (line num in coconut source)
# Check if bool
    if (isinstance)(b, bool):  #231 (line num in coconut source)
        return (True)  # type: ignore  #232 (line num in coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #235 (line num in coconut source)
        return _coconut_tail_call(b.__maxBound__)  #236 (line num in coconut source)

# Default implementation
    return _coconut_tail_call(_fmap, maxBound, b)  #239 (line num in coconut source)



## Numbers:

### Numeric types:

#### Int:
Int = int  #248 (line num in coconut source)

#### Integer:
Integer = int  #251 (line num in coconut source)

#### Float:
Float = float  #254 (line num in coconut source)

#### Double:
Double = float  #257 (line num in coconut source)

#### Rational:
Rational = _fractions.Fraction  #260 (line num in coconut source)

@_coconut_tco  #262 (line num in coconut source)
def over(x, y):  #262 (line num in coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #267 (line num in coconut source)
    return _coconut_tail_call(Rational, x, y)  #268 (line num in coconut source)

#### Word:
Word = Int  #271 (line num in coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #277 (line num in coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #278 (line num in coconut source)

negate: '_coconut.typing.Callable[[TNum], TNum]'  #280 (line num in coconut source)
negate = _coconut_minus  #281 (line num in coconut source)

abs: '_coconut.typing.Callable[[TNum], TNum]'  #283 (line num in coconut source)
abs = _abs  #284 (line num in coconut source)

if TYPE_CHECKING:  #286 (line num in coconut source)
    def signum(x: 'Num') -> 'int':  #287 (line num in coconut source)
        ...  #288 (line num in coconut source)
else:  #289 (line num in coconut source)
    @_coconut_mark_as_match  #290 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #290 (line num in coconut source)
        _coconut_match_check_7 = False  #290 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #290 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 1) and (_coconut_match_args[0] == 0):  #290 (line num in coconut source)
            if not _coconut_match_kwargs:  #290 (line num in coconut source)
                _coconut_match_check_7 = True  #290 (line num in coconut source)
        if not _coconut_match_check_7:  #290 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #290 (line num in coconut source)

        return (0)  #290 (line num in coconut source)
    @_coconut_addpattern(signum)  #291 (line num in coconut source)
    @_coconut_mark_as_match  #291 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #291 (line num in coconut source)
        _coconut_match_check_8 = False  #291 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #291 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #291 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #291 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #291 (line num in coconut source)
            if not _coconut_match_kwargs:  #291 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #291 (line num in coconut source)
                _coconut_match_check_8 = True  #291 (line num in coconut source)
        if _coconut_match_check_8:  #291 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #291 (line num in coconut source)
                x = _coconut_match_temp_0  #291 (line num in coconut source)
        if _coconut_match_check_8 and not (x > 0):  #291 (line num in coconut source)
            _coconut_match_check_8 = False  #291 (line num in coconut source)
        if not _coconut_match_check_8:  #291 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #291 (line num in coconut source)

        return (1)  #291 (line num in coconut source)
    @_coconut_addpattern(signum)  #292 (line num in coconut source)
    @_coconut_mark_as_match  #292 (line num in coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #292 (line num in coconut source)
        _coconut_match_check_9 = False  #292 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #292 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #292 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #292 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #292 (line num in coconut source)
            if not _coconut_match_kwargs:  #292 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #292 (line num in coconut source)
                _coconut_match_check_9 = True  #292 (line num in coconut source)
        if _coconut_match_check_9:  #292 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #292 (line num in coconut source)
                x = _coconut_match_temp_0  #292 (line num in coconut source)
        if _coconut_match_check_9 and not (x < 0):  #292 (line num in coconut source)
            _coconut_match_check_9 = False  #292 (line num in coconut source)
        if not _coconut_match_check_9:  #292 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #292 (line num in coconut source)

        return (-1)  #292 (line num in coconut source)

def fromInteger(x: 'Integer') -> 'Num':  #294 (line num in coconut source)
    return (x)  #294 (line num in coconut source)

#### Real:
Real = Num  #297 (line num in coconut source)

if TYPE_CHECKING:  #299 (line num in coconut source)
    def toRational(real: 'Real') -> 'Rational':  #300 (line num in coconut source)
        ...  #301 (line num in coconut source)
else:  #302 (line num in coconut source)
    @_coconut_tco  #303 (line num in coconut source)
    @_coconut_mark_as_match  #303 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #303 (line num in coconut source)
        _coconut_match_check_10 = False  #303 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #303 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #303 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #303 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #303 (line num in coconut source)
            if ((isinstance)(_coconut_match_temp_0, float)) and (not _coconut_match_kwargs):  #303 (line num in coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_0  #303 (line num in coconut source)
                _coconut_match_check_10 = True  #303 (line num in coconut source)
        if _coconut_match_check_10:  #303 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #303 (line num in coconut source)
                real = _coconut_match_temp_0  #303 (line num in coconut source)
        if not _coconut_match_check_10:  #303 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #303 (line num in coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #304 (line num in coconut source)
    @_coconut_addpattern(toRational)  #305 (line num in coconut source)
    @_coconut_tco  #305 (line num in coconut source)
    @_coconut_mark_as_match  #305 (line num in coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #305 (line num in coconut source)
        _coconut_match_check_11 = False  #305 (line num in coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #305 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #305 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #305 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #305 (line num in coconut source)
            if not _coconut_match_kwargs:  #305 (line num in coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_0  #305 (line num in coconut source)
                _coconut_match_check_11 = True  #305 (line num in coconut source)
        if _coconut_match_check_11:  #305 (line num in coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #305 (line num in coconut source)
                real = _coconut_match_temp_0  #305 (line num in coconut source)
        if not _coconut_match_check_11:  #305 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #305 (line num in coconut source)

        return _coconut_tail_call(Rational, real)  #306 (line num in coconut source)

#### Integral:
Integral = int  #309 (line num in coconut source)

def quot(x: 'int', y: 'int') -> 'int':  #311 (line num in coconut source)
    divxy = x // y  #312 (line num in coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #313 (line num in coconut source)

def rem(x: 'int', y: 'int') -> 'int':  #315 (line num in coconut source)
    modxy = x % y  #316 (line num in coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #317 (line num in coconut source)

div: '_coconut.typing.Callable[[int, int], int]'  #319 (line num in coconut source)
div = _coconut.operator.floordiv  #320 (line num in coconut source)

mod: '_coconut.typing.Callable[[int, int], int]'  #322 (line num in coconut source)
mod = _coconut.operator.mod  #323 (line num in coconut source)

def quotRem(x: 'int', y: 'int') -> 'T.Tuple[int, int]':  #325 (line num in coconut source)
    divxy, modxy = divmod(x, y)  #326 (line num in coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #327 (line num in coconut source)
    return (divxy + adj, modxy - y * adj)  #328 (line num in coconut source)

divMod = divmod  #330 (line num in coconut source)

toInteger: '_coconut.typing.Callable[[Integral], Integer]'  #332 (line num in coconut source)
toInteger = _int  #333 (line num in coconut source)

#### Fractional:
Fractional = Rational  #336 (line num in coconut source)

recip: '_coconut.typing.Callable[[Fractional], Fractional]'  #338 (line num in coconut source)
recip = _coconut.functools.partial(_coconut.operator.truediv, 1)  #339 (line num in coconut source)

def fromRational(x: 'Rational') -> 'Fractional':  #341 (line num in coconut source)
    return (x)  #341 (line num in coconut source)

#### Floating:
Floating = float  #344 (line num in coconut source)

from math import pi  #346 (line num in coconut source)
from math import exp  #346 (line num in coconut source)
from math import log  #346 (line num in coconut source)
from math import sqrt  #346 (line num in coconut source)
from math import sin  #346 (line num in coconut source)
from math import cos  #346 (line num in coconut source)
from math import tan  #346 (line num in coconut source)
from math import asin  #346 (line num in coconut source)
from math import acos  #346 (line num in coconut source)
from math import atan  #346 (line num in coconut source)
from math import sinh  #346 (line num in coconut source)
from math import cosh  #346 (line num in coconut source)
from math import tanh  #346 (line num in coconut source)
from math import asinh  #346 (line num in coconut source)
from math import acosh  #346 (line num in coconut source)
from math import atanh  #346 (line num in coconut source)

@_coconut_tco  #365 (line num in coconut source)
def logBase(base: 'float', x: 'float') -> 'float':  #365 (line num in coconut source)
    return _coconut_tail_call(log, x, base)  #366 (line num in coconut source)

#### RealFrac:
RealFrac = Rational  #369 (line num in coconut source)

def properFraction(x: 'RealFrac') -> 'T.Tuple[int, RealFrac]':  #371 (line num in coconut source)
    floor_x = floor(x)  #372 (line num in coconut source)
    return (floor_x, x - floor_x)  #373 (line num in coconut source)

truncate: '_coconut.typing.Callable[[RealFrac], int]'  #375 (line num in coconut source)
truncate = _int  #376 (line num in coconut source)

round: '_coconut.typing.Callable[[RealFrac], int]'  #378 (line num in coconut source)
round = _round  #379 (line num in coconut source)

ceiling: '_coconut.typing.Callable[[RealFrac], int]'  #381 (line num in coconut source)
ceiling = _ceil  #382 (line num in coconut source)

floor: '_coconut.typing.Callable[[RealFrac], int]'  #384 (line num in coconut source)
floor = _floor  #385 (line num in coconut source)

#### RealFloat:
RealFloat = float  #388 (line num in coconut source)

def floatRadix(x: 'float') -> 'int':  #390 (line num in coconut source)
    return (2)  #390 (line num in coconut source)

def floatDigits(x: 'float') -> 'int':  #392 (line num in coconut source)
    return (53)  #392 (line num in coconut source)

def floatRange(x: 'float') -> 'T.Tuple[int, int]':  #394 (line num in coconut source)
    return ((-1021, 1024))  #394 (line num in coconut source)

decodeFloat = NotImplemented  #396 (line num in coconut source)

encodeFloat = NotImplemented  #398 (line num in coconut source)

exponent = NotImplemented  #400 (line num in coconut source)

significand = NotImplemented  #402 (line num in coconut source)

def scaleFloat(power: 'int', x: 'float') -> 'float':  #404 (line num in coconut source)
    return (x * 2**power)  #405 (line num in coconut source)

from math import isnan as isNaN  #407 (line num in coconut source)
from math import isinf as isInfinite  #407 (line num in coconut source)
from math import atan2  #407 (line num in coconut source)

isDenormalized = NotImplemented  #413 (line num in coconut source)

def isNegativeZero(x: 'float') -> 'bool':  #415 (line num in coconut source)
    return (x == 0 and str(x).startswith("-"))  #416 (line num in coconut source)

def isIEEE(x: 'float') -> 'bool':  #418 (line num in coconut source)
    return (True)  #418 (line num in coconut source)


### Numeric functions:
def subtract(x, y):  #422 (line num in coconut source)
    return (y - x)  #423 (line num in coconut source)

def even(x: 'int') -> 'bool':  #425 (line num in coconut source)
    return (x % 2 == 0)  #426 (line num in coconut source)

def odd(x: 'int') -> 'bool':  #428 (line num in coconut source)
    return (x % 2 == 1)  #429 (line num in coconut source)

gcd: '_coconut.typing.Callable[[int, int], int]'  #431 (line num in coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #432 (line num in coconut source)

if TYPE_CHECKING:  #434 (line num in coconut source)
    def lcm(x: 'int', y: 'int') -> 'int':  #435 (line num in coconut source)
        ...  #436 (line num in coconut source)
else:  #437 (line num in coconut source)
    @_coconut_mark_as_match  #438 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #438 (line num in coconut source)
        _coconut_match_check_12 = False  #438 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #438 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and (_coconut_match_args[1] == 0):  #438 (line num in coconut source)
            if not _coconut_match_kwargs:  #438 (line num in coconut source)
                _coconut_match_check_12 = True  #438 (line num in coconut source)
        if not _coconut_match_check_12:  #438 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #438 (line num in coconut source)

        return (0)  #438 (line num in coconut source)
    @_coconut_addpattern(lcm)  #439 (line num in coconut source)
    @_coconut_mark_as_match  #439 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #439 (line num in coconut source)
        _coconut_match_check_13 = False  #439 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #439 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and (_coconut_match_args[0] == 0):  #439 (line num in coconut source)
            if not _coconut_match_kwargs:  #439 (line num in coconut source)
                _coconut_match_check_13 = True  #439 (line num in coconut source)
        if not _coconut_match_check_13:  #439 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #439 (line num in coconut source)

        return (0)  #439 (line num in coconut source)
    @_coconut_addpattern(lcm)  #440 (line num in coconut source)
    @_coconut_mark_as_match  #440 (line num in coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #440 (line num in coconut source)
        _coconut_match_check_14 = False  #440 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #440 (line num in coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #440 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #440 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #440 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #440 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #440 (line num in coconut source)
            if not _coconut_match_kwargs:  #440 (line num in coconut source)
                _coconut_match_set_name_x = _coconut_match_temp_0  #440 (line num in coconut source)
                _coconut_match_set_name_y = _coconut_match_temp_1  #440 (line num in coconut source)
                _coconut_match_check_14 = True  #440 (line num in coconut source)
        if _coconut_match_check_14:  #440 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #440 (line num in coconut source)
                x = _coconut_match_temp_0  #440 (line num in coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #440 (line num in coconut source)
                y = _coconut_match_temp_1  #440 (line num in coconut source)
        if not _coconut_match_check_14:  #440 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #440 (line num in coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #441 (line num in coconut source)

fromIntegral: '_coconut.typing.Callable[[Integral], Num]'  #443 (line num in coconut source)
fromIntegral = fromInteger  #444 (line num in coconut source)

realToFrac: '_coconut.typing.Callable[[Real], Fractional]'  #446 (line num in coconut source)
realToFrac = toRational  #447 (line num in coconut source)



## Monoids:
Monoid = T.Iterable  #452 (line num in coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #453 (line num in coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #455 (line num in coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #458 (line num in coconut source)
    _coconut_is_data = True  #459 (line num in coconut source)
    __slots__ = ()  #459 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #459 (line num in coconut source)
    def __eq__(self, other):  #459 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #459 (line num in coconut source)
    def __hash__(self):  #459 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #459 (line num in coconut source)
    __match_args__ = ()  #459 (line num in coconut source)
    @staticmethod  #459 (line num in coconut source)
    @_coconut_tco  #459 (line num in coconut source)
    def mempty_as(M: 'TMonoid') -> 'TMonoid':  #460 (line num in coconut source)
        if (hasattr)(M, "__mempty__"):  #461 (line num in coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #462 (line num in coconut source)
        return _coconut_tail_call(makedata, type(M))  #463 (line num in coconut source)

mempty: 'T.Any' = Mempty()  #465 (line num in coconut source)

@_coconut_tco  #467 (line num in coconut source)
def mappend(x: 'TMonoid', y: 'TMonoid') -> 'TMonoid':  #467 (line num in coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #472 (line num in coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #474 (line num in coconut source)
    y = (asTypeOf)(y, x)  #475 (line num in coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #478 (line num in coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #479 (line num in coconut source)

# Default implementation
    if not x:  #482 (line num in coconut source)
        return (y)  #483 (line num in coconut source)
    if not y:  #484 (line num in coconut source)
        return (x)  #485 (line num in coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #486 (line num in coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #487 (line num in coconut source)
    return _coconut_tail_call((makedata), type(x), *_coconut.itertools.chain(x, y))  #488 (line num in coconut source)

@_coconut_tco  #490 (line num in coconut source)
def mconcat(ms: '_coconut.typing.Sequence[TMonoid]') -> 'TMonoid':  #490 (line num in coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #491 (line num in coconut source)



## Monads and functors:

#### Functor:
Functor = T.Iterable  #498 (line num in coconut source)

fmap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], Functor[Ta]], Functor[Tb]]'  # type: ignore  #500 (line num in coconut source)
fmap = _fmap  #501 (line num in coconut source)

@_coconut_tco  #503 (line num in coconut source)
def fmapConst(x: 'Ta', xs: 'Functor') -> 'Functor[Ta]':  #503 (line num in coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #507 (line num in coconut source)
    return _coconut_tail_call(_fmap, lambda _: x, xs)  #508 (line num in coconut source)

#### Applicative:
Applicative = Functor  #511 (line num in coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #512 (line num in coconut source)

if TYPE_CHECKING:  #514 (line num in coconut source)
    def pure(x: 'Ta') -> 'T.Any':  #515 (line num in coconut source)
        ...  #516 (line num in coconut source)
else:  #517 (line num in coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #518 (line num in coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #522 (line num in coconut source)
        _coconut_is_data = True  #523 (line num in coconut source)
        __slots__ = ()  #523 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #523 (line num in coconut source)
        def __eq__(self, other):  #523 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #523 (line num in coconut source)
        def __hash__(self):  #523 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #523 (line num in coconut source)
        __match_args__ = ('val',)  #523 (line num in coconut source)
        def __join__(self) -> 'T.Any':  #523 (line num in coconut source)
            return (self.val)  #523 (line num in coconut source)

        @_coconut_tco  #525 (line num in coconut source)
        def pure_as(self, M: 'TApp') -> 'TApp':  #525 (line num in coconut source)
            if (hasattr)(M, "__pure__"):  #526 (line num in coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #527 (line num in coconut source)
            return _coconut_tail_call(makedata, type(M), self.val)  #528 (line num in coconut source)

@_coconut_tco  #530 (line num in coconut source)
def ap(fs: 'Applicative[_coconut.typing.Callable[[Ta], Tb]]', xs: 'Applicative[Ta]') -> 'Applicative[Tb]':  #530 (line num in coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #537 (line num in coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #539 (line num in coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #540 (line num in coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #543 (line num in coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #544 (line num in coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: _fmap(f, xs))  #547 (line num in coconut source)

@_coconut_tco  #549 (line num in coconut source)
def seqAr(f1: 'Applicative', f2: 'TApp') -> 'TApp':  #549 (line num in coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #553 (line num in coconut source)
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #554 (line num in coconut source)

@_coconut_tco  #556 (line num in coconut source)
def seqAl(f1: 'TApp', f2: 'Applicative') -> 'TApp':  #556 (line num in coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #560 (line num in coconut source)
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #561 (line num in coconut source)

def liftA2(func: '_coconut.typing.Callable[[Ta, Tb], Tc]') -> '_coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]':  #563 (line num in coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #567 (line num in coconut source)
    return (lambda f1, f2: (ap)(_fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2))  #568 (line num in coconut source)

#### Monad:
Monad = Applicative  #571 (line num in coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #572 (line num in coconut source)

@_coconut_tco  #574 (line num in coconut source)
def bind(m: 'Monad[Ta]', func: '_coconut.typing.Callable[[Ta], TMonad]') -> 'TMonad':  #574 (line num in coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #579 (line num in coconut source)
    return _coconut_tail_call(join, _fmap(func, m))  # type: ignore  #580 (line num in coconut source)

@_coconut_tco  #582 (line num in coconut source)
def seqM(m1: 'Monad', m2: 'TMonad') -> 'TMonad':  #582 (line num in coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #586 (line num in coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #587 (line num in coconut source)

return_ = pure  #589 (line num in coconut source)

if TYPE_CHECKING:  #591 (line num in coconut source)
    def fail(msg: 'str') -> 'T.Any':  #592 (line num in coconut source)
        ...  #593 (line num in coconut source)
else:  #594 (line num in coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')])):  #595 (line num in coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #598 (line num in coconut source)
        _coconut_is_data = True  #599 (line num in coconut source)
        __slots__ = ()  #599 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #599 (line num in coconut source)
        def __eq__(self, other):  #599 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #599 (line num in coconut source)
        def __hash__(self):  #599 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #599 (line num in coconut source)
        __match_args__ = ('msg',)  #599 (line num in coconut source)
        @staticmethod  #599 (line num in coconut source)
        def __bool__() -> 'bool':  #599 (line num in coconut source)
            return (False)  #600 (line num in coconut source)

        def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'T.Any':  #602 (line num in coconut source)
            return (self)  #602 (line num in coconut source)

        @_coconut_tco  #604 (line num in coconut source)
        def fail_as(self, M: 'TMonad') -> 'TMonad':  #604 (line num in coconut source)
            if (hasattr)(M, "__fail__"):  #605 (line num in coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #606 (line num in coconut source)
            return _coconut_tail_call(makedata, type(M))  #607 (line num in coconut source)

# sequence_ and mapM_ defined in Foldable

@_coconut_tco  #611 (line num in coconut source)
def bindFrom(func: '_coconut.typing.Callable[[Ta], TMonad]', m: 'Monad[Ta]') -> 'TMonad':  #611 (line num in coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #615 (line num in coconut source)
    return _coconut_tail_call((bind), m, func)  #616 (line num in coconut source)

@_coconut_tco  #618 (line num in coconut source)
def join(ms: 'Monad[TMonad]') -> 'TMonad':  #618 (line num in coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation identifies non-failures using __bool__
    """  #625 (line num in coconut source)
# Resolve ms being pure or fail
    ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #627 (line num in coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #630 (line num in coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #633 (line num in coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #634 (line num in coconut source)

# Default implementation
    if not ms:  #637 (line num in coconut source)
        return (ms)  # type: ignore  #638 (line num in coconut source)
    vals = []  # type: ignore  #639 (line num in coconut source)
    fallback = ms  #640 (line num in coconut source)
    for m in ms:  #641 (line num in coconut source)
        if m:  #642 (line num in coconut source)
            vals.extend(m)  # type: ignore  #643 (line num in coconut source)
        else:  #644 (line num in coconut source)
            fallback = m  # type: ignore  #645 (line num in coconut source)
    if not vals:  #646 (line num in coconut source)
        return (fallback)  # type: ignore  #647 (line num in coconut source)
    return _coconut_tail_call(makedata, type(ms), *vals)  #648 (line num in coconut source)

if TYPE_CHECKING:  #650 (line num in coconut source)
    def do(monads: '_coconut.typing.Sequence[TMonad]', func: '_coconut.typing.Callable[..., TMonad]') -> 'TMonad':  #651 (line num in coconut source)
        ...  #652 (line num in coconut source)
else:  #653 (line num in coconut source)
    @_coconut_tco  #654 (line num in coconut source)
    @_coconut_mark_as_match  #654 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #654 (line num in coconut source)
        _coconut_match_check_15 = False  #654 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #654 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #654 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #654 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #654 (line num in coconut source)
            if not _coconut_match_kwargs:  #654 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_0  #654 (line num in coconut source)
                _coconut_match_check_15 = True  #654 (line num in coconut source)
        if _coconut_match_check_15:  #654 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #654 (line num in coconut source)
                func = _coconut_match_temp_0  #654 (line num in coconut source)
        if not _coconut_match_check_15:  #654 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #654 (line num in coconut source)

        return _coconut_tail_call(func)  #654 (line num in coconut source)
    @_coconut_addpattern(do)  #655 (line num in coconut source)
    @_coconut_tco  #655 (line num in coconut source)
    @_coconut_mark_as_match  #655 (line num in coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #655 (line num in coconut source)
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
        """  #674 (line num in coconut source)
        _coconut_match_check_16 = False  #675 (line num in coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #675 (line num in coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #675 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #675 (line num in coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #675 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #675 (line num in coconut source)
            ms = _coconut.list(_coconut_match_args[0][1:])  #675 (line num in coconut source)
            _coconut_match_set_name_m = _coconut_match_args[0][0]  #675 (line num in coconut source)
            if not _coconut_match_kwargs:  #675 (line num in coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_0  #675 (line num in coconut source)
                _coconut_match_check_16 = True  #675 (line num in coconut source)
        if _coconut_match_check_16:  #675 (line num in coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #675 (line num in coconut source)
                m = _coconut_match_args[0][0]  #675 (line num in coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #675 (line num in coconut source)
                func = _coconut_match_temp_0  #675 (line num in coconut source)
        if not _coconut_match_check_16:  #675 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #675 (line num in coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))  #675 (line num in coconut source)



## Folds and traversals:

#### Foldable:
Foldable = T.Sequence  #682 (line num in coconut source)

@_coconut_tco  #684 (line num in coconut source)
def sequence_(ms: 'Foldable[Monad]') -> 'Monad':  #684 (line num in coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #685 (line num in coconut source)

mapM_: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]'  #687 (line num in coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #688 (line num in coconut source)

@_coconut_tco  #690 (line num in coconut source)
def foldMap(func: '_coconut.typing.Callable[[Ta], TMonoid]', xs: 'Foldable[Ta]') -> 'TMonoid':  #690 (line num in coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #691 (line num in coconut source)

@_coconut_tco  #693 (line num in coconut source)
def foldl(func: '_coconut.typing.Callable[[Tb, Ta], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #693 (line num in coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #694 (line num in coconut source)

@_coconut_tco  #696 (line num in coconut source)
def foldr(func: '_coconut.typing.Callable[[Ta, Tb], Tb]', init: 'Tb', xs: 'Foldable[Ta]') -> 'Tb':  #696 (line num in coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #697 (line num in coconut source)

foldl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]'  #699 (line num in coconut source)
foldl1 = reduce  #700 (line num in coconut source)

@_coconut_tco  #702 (line num in coconut source)
def foldr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: 'Foldable[Ta]') -> 'Ta':  #702 (line num in coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #703 (line num in coconut source)

def null(xs: 'Foldable[Ta]') -> 'bool':  #705 (line num in coconut source)
    return (len(xs) == 0)  #706 (line num in coconut source)

length: '_coconut.typing.Callable[[Foldable], int]'  #708 (line num in coconut source)
length = len  #709 (line num in coconut source)

def elem(e: 'Ta', xs: 'Foldable[Ta]') -> 'bool':  #711 (line num in coconut source)
    return (e in xs)  #712 (line num in coconut source)

maximum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #714 (line num in coconut source)
maximum = _max  #715 (line num in coconut source)

minimum: '_coconut.typing.Callable[[Foldable[TOrd]], TOrd]'  #717 (line num in coconut source)
minimum = _min  #718 (line num in coconut source)

sum: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #720 (line num in coconut source)
sum = _sum  #721 (line num in coconut source)

product: '_coconut.typing.Callable[[Foldable[TNum]], TNum]'  #723 (line num in coconut source)
product = _coconut.functools.partial(reduce, _coconut.operator.mul)  #724 (line num in coconut source)

#### Traversable:
Traversable = T.Iterable  #727 (line num in coconut source)

@_coconut_tco  #729 (line num in coconut source)
def _snoc(xs: '_coconut.typing.Iterable[Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #729 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain, xs, (x, ))  #730 (line num in coconut source)

@_coconut_tco  #732 (line num in coconut source)
def sequenceA(fs: 'Traversable[Applicative[Ta]]') -> 'Applicative[Traversable[Ta]]':  #732 (line num in coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #733 (line num in coconut source)

traverse: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]'  #735 (line num in coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  #736 (line num in coconut source)

sequence: '_coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]'  #738 (line num in coconut source)
sequence = sequenceA  #739 (line num in coconut source)

mapM: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]'  #741 (line num in coconut source)
mapM = traverse  #742 (line num in coconut source)



## Miscellaneous functions:
def id(x: 'Ta') -> 'Ta':  #747 (line num in coconut source)
    return (x)  #747 (line num in coconut source)

@_coconut_tco  #749 (line num in coconut source)
def dot(f: '_coconut.typing.Callable[[Tb], Tc]', g: '_coconut.typing.Callable[[Ta], Tb]') -> '_coconut.typing.Callable[[Ta], Tc]':  #749 (line num in coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #753 (line num in coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #754 (line num in coconut source)

if TYPE_CHECKING:  #756 (line num in coconut source)
    @T.overload  #757 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #758 (line num in coconut source)
        ...  #759 (line num in coconut source)
    @T.overload  #760 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #761 (line num in coconut source)
        ...  #762 (line num in coconut source)
    @T.overload  #763 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', arg: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #764 (line num in coconut source)
        ...  #765 (line num in coconut source)
    @T.overload  #766 (line num in coconut source)
    def apply(func: '_coconut.typing.Callable[..., Tb]', arg: 'Ta') -> 'T.Any':  #767 (line num in coconut source)
        ...  #768 (line num in coconut source)
    def apply(func, arg):  #769 (line num in coconut source)
        ...  #770 (line num in coconut source)
else:  #771 (line num in coconut source)
    @_coconut_tco  #772 (line num in coconut source)
    def apply(func, arg):  #772 (line num in coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #778 (line num in coconut source)
        return _coconut_tail_call((of), func, arg)  #779 (line num in coconut source)

@_coconut_tco  #781 (line num in coconut source)
def until(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> 'Ta':  #781 (line num in coconut source)
    def _coconut_mock_65(cond: '_coconut.typing.Callable[[Ta], bool]', func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta'): return cond, func, x  #782 (line num in coconut source)
    while True:  #782 (line num in coconut source)
        if cond(x):  #782 (line num in coconut source)
            return (x)  #783 (line num in coconut source)
        try:  # tail recursive  #784 (line num in coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_70  # tail recursive  #784 (line num in coconut source)
        except _coconut.NameError:  # tail recursive  #784 (line num in coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #784 (line num in coconut source)
        if _coconut_tre_check_0:  # tail recursive  #784 (line num in coconut source)
            cond, func, x = _coconut_mock_65(cond, func, func(x))  # tail recursive  #784 (line num in coconut source)
            continue  # tail recursive  #784 (line num in coconut source)
        else:  # tail recursive  #784 (line num in coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  # tail recursive  #784 (line num in coconut source)
# tail recursive

        return None  #786 (line num in coconut source)
_coconut_recursive_func_70 = until  #786 (line num in coconut source)
def asTypeOf(x: 'Ta', y: 'Ta') -> 'Ta':  #786 (line num in coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #790 (line num in coconut source)
    if TYPE_CHECKING:  #791 (line num in coconut source)
        return (x)  #791 (line num in coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #793 (line num in coconut source)
        for i in (takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count()):  #794 (line num in coconut source)
            if (isinstance)(x, pure):  #795 (line num in coconut source)
                x = x.pure_as(y)  #796 (line num in coconut source)
            elif (isinstance)(x, fail):  #797 (line num in coconut source)
                x = x.fail_as(y)  #798 (line num in coconut source)
            elif (isinstance)(x, Mempty):  #799 (line num in coconut source)
                x = x.mempty_as(y)  #800 (line num in coconut source)
            else:  #801 (line num in coconut source)
                break  #802 (line num in coconut source)
    return (x)  #803 (line num in coconut source)

asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #805 (line num in coconut source)

def error(msg: 'str') -> 'None':  #807 (line num in coconut source)
    raise Exception(msg)  #808 (line num in coconut source)

def errorWithoutStackTrace(msg: 'str') -> 'None':  #810 (line num in coconut source)
    raise Exception(msg) from None  #811 (line num in coconut source)

undefined: 'T.Any' = None  #813 (line num in coconut source)

def seq(x: 'Ta', y: 'Tb') -> 'Tb':  #815 (line num in coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #818 (line num in coconut source)
    return (y)  #819 (line num in coconut source)

@_coconut_tco  #821 (line num in coconut source)
def cbv(func: '_coconut.typing.Callable[[Ta], Tb]', arg: 'Ta') -> 'Tb':  #821 (line num in coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #826 (line num in coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #827 (line num in coconut source)




# List operations:
@_coconut_tco  #833 (line num in coconut source)
def cons(x: 'Ta', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #833 (line num in coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #837 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain, [x, ], xs)  #838 (line num in coconut source)

map: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]'  # type: ignore  #840 (line num in coconut source)
map = _map  # type: ignore  #841 (line num in coconut source)

@_coconut_tco  #843 (line num in coconut source)
def chain(xs: '_coconut.typing.Iterable[Ta]', ys: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #843 (line num in coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #847 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain, xs, ys)  #848 (line num in coconut source)

filter: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  # type: ignore  #850 (line num in coconut source)
filter = _filter  # type: ignore  #851 (line num in coconut source)

head: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #853 (line num in coconut source)
head = _coconut.functools.partial(_coconut_iter_getitem, index=(0))  #854 (line num in coconut source)

last: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]'  #856 (line num in coconut source)
last = _coconut.functools.partial(_coconut_iter_getitem, index=(-1))  #857 (line num in coconut source)

tail: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #859 (line num in coconut source)
tail = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #860 (line num in coconut source)

init: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #862 (line num in coconut source)
init = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #863 (line num in coconut source)

@_coconut_tco  #865 (line num in coconut source)
def at(xs: '_coconut.typing.Iterable[Ta]', i: 'int') -> 'Ta':  #865 (line num in coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #869 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #870 (line num in coconut source)

reverse: '_coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]'  #872 (line num in coconut source)
reverse = _reversed  #873 (line num in coconut source)



## Special folds:
and_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #878 (line num in coconut source)
and_ = _all  #879 (line num in coconut source)

or_: '_coconut.typing.Callable[[Foldable[bool]], bool]'  #881 (line num in coconut source)
or_ = _any  #882 (line num in coconut source)

any: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #884 (line num in coconut source)
any = _coconut_forward_compose(map, or_)  #885 (line num in coconut source)

all: '_coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]'  #887 (line num in coconut source)
all = _coconut_forward_compose(map, and_)  #888 (line num in coconut source)

@_coconut_tco  #890 (line num in coconut source)
def concat(xs: 'Foldable[_coconut.typing.Iterable[Ta]]') -> '_coconut.typing.Iterable[Ta]':  #890 (line num in coconut source)
    return _coconut_tail_call(_reduce, _coconut.itertools.chain, xs, ())  #891 (line num in coconut source)

concatMap: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]'  #893 (line num in coconut source)
concatMap = _coconut_forward_compose(map, concat)  #894 (line num in coconut source)



## Building lists:

### Scans:
@_coconut_tco  #901 (line num in coconut source)
def scanl(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Ta]':  #901 (line num in coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #902 (line num in coconut source)

scanl1: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #904 (line num in coconut source)
scanl1 = scan  #905 (line num in coconut source)

@_coconut_tco  #907 (line num in coconut source)
def scanr(func: '_coconut.typing.Callable[[Ta, Tb], Ta]', init: 'Ta', xs: '_coconut.typing.Sequence[Tb]') -> '_coconut.typing.Iterable[Ta]':  #907 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #908 (line num in coconut source)

@_coconut_tco  #910 (line num in coconut source)
def scanr1(func: '_coconut.typing.Callable[[Ta, Ta], Ta]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #910 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #911 (line num in coconut source)

### Infinite lists:
@recursive_iterator  #914 (line num in coconut source)
@_coconut_tco  #914 (line num in coconut source)
def iterate(func: '_coconut.typing.Callable[[Ta], Ta]', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #915 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x, ], lambda: iterate(func, func(x)))))  #916 (line num in coconut source)

@recursive_iterator  #918 (line num in coconut source)
@_coconut_tco  #918 (line num in coconut source)
def repeat(x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #919 (line num in coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x, ], lambda: repeat(x))))  #920 (line num in coconut source)

@_coconut_tco  #922 (line num in coconut source)
def replicate(n: 'int', x: 'Ta') -> '_coconut.typing.Iterable[Ta]':  #922 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #923 (line num in coconut source)

if TYPE_CHECKING:  #925 (line num in coconut source)
    def cycle(xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Iterable[Ta]':  #926 (line num in coconut source)
        ...  #927 (line num in coconut source)
else:  #928 (line num in coconut source)
    @recursive_iterator  #929 (line num in coconut source)
    @_coconut_tco  #929 (line num in coconut source)
    @_coconut_mark_as_match  #929 (line num in coconut source)
    def cycle(*_coconut_match_args, **_coconut_match_kwargs):  #929 (line num in coconut source)
        _coconut_match_check_17 = False  #929 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #929 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #929 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #929 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #929 (line num in coconut source)
            if not _coconut_match_kwargs:  #929 (line num in coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_0  #929 (line num in coconut source)
                _coconut_match_check_17 = True  #929 (line num in coconut source)
        if _coconut_match_check_17:  #929 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #929 (line num in coconut source)
                xs = _coconut_match_temp_0  #929 (line num in coconut source)
        if _coconut_match_check_17 and not (len(xs) > 0):  #929 (line num in coconut source)
            _coconut_match_check_17 = False  #929 (line num in coconut source)
        if not _coconut_match_check_17:  #929 (line num in coconut source)
            raise _coconut_FunctionMatchError('def cycle(xs if len(xs) > 0) =', _coconut_match_args)  #929 (line num in coconut source)

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))  #931 (line num in coconut source)



## Sublists:
@_coconut_tco  #936 (line num in coconut source)
def take(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #936 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #937 (line num in coconut source)

@_coconut_tco  #939 (line num in coconut source)
def drop(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> '_coconut.typing.Iterable[Ta]':  #939 (line num in coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #940 (line num in coconut source)

def splitAt(n: 'int', xs: '_coconut.typing.Iterable[Ta]') -> 'T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]':  #942 (line num in coconut source)
    reit = reiterable(xs)  #943 (line num in coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #944 (line num in coconut source)

takeWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #946 (line num in coconut source)
takeWhile = takewhile  #947 (line num in coconut source)

dropWhile: '_coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]'  #949 (line num in coconut source)
dropWhile = dropwhile  #950 (line num in coconut source)

if TYPE_CHECKING:  #952 (line num in coconut source)
    def span(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]':  #953 (line num in coconut source)
        ...  #954 (line num in coconut source)
else:  #955 (line num in coconut source)
    @_coconut_mark_as_match  #956 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #956 (line num in coconut source)
        _coconut_match_check_18 = False  #956 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #956 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #956 (line num in coconut source)
            if not _coconut_match_kwargs:  #956 (line num in coconut source)
                _coconut_match_check_18 = True  #956 (line num in coconut source)
        if not _coconut_match_check_18:  #956 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #956 (line num in coconut source)

        return (([], []))  #956 (line num in coconut source)
    @_coconut_addpattern(span)  #957 (line num in coconut source)
    @_coconut_mark_as_match  #957 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #957 (line num in coconut source)
        _coconut_match_check_19 = False  #957 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #957 (line num in coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #957 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #957 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs) and (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #957 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #957 (line num in coconut source)
            xs = _coconut.list(_coconut_match_args[1][1:])  #957 (line num in coconut source)
            _coconut_match_set_name_x = _coconut_match_args[1][0]  #957 (line num in coconut source)
            if not _coconut_match_kwargs:  #957 (line num in coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_0  #957 (line num in coconut source)
                _coconut_match_check_19 = True  #957 (line num in coconut source)
        if _coconut_match_check_19:  #957 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #957 (line num in coconut source)
                cond = _coconut_match_temp_0  #957 (line num in coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #957 (line num in coconut source)
                x = _coconut_match_args[1][0]  #957 (line num in coconut source)
        if _coconut_match_check_19 and not (cond(x)):  #957 (line num in coconut source)
            _coconut_match_check_19 = False  #957 (line num in coconut source)
        if not _coconut_match_check_19:  #957 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #957 (line num in coconut source)

        ys, zs = span(cond, xs)  #958 (line num in coconut source)
        return (([x, ] + ys, zs))  #959 (line num in coconut source)
    @_coconut_addpattern(span)  #960 (line num in coconut source)
    @_coconut_mark_as_match  #960 (line num in coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #960 (line num in coconut source)
        _coconut_match_check_20 = False  #960 (line num in coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #960 (line num in coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #960 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #960 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #960 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #960 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #960 (line num in coconut source)
            if not _coconut_match_kwargs:  #960 (line num in coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_0  #960 (line num in coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_1  #960 (line num in coconut source)
                _coconut_match_check_20 = True  #960 (line num in coconut source)
        if _coconut_match_check_20:  #960 (line num in coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #960 (line num in coconut source)
                cond = _coconut_match_temp_0  #960 (line num in coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #960 (line num in coconut source)
                xs = _coconut_match_temp_1  #960 (line num in coconut source)
        if not _coconut_match_check_20:  #960 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #960 (line num in coconut source)

        return (([], xs))  #961 (line num in coconut source)

@_coconut_tco  #963 (line num in coconut source)
def break_(cond: '_coconut.typing.Callable[[Ta], bool]', xs: '_coconut.typing.Sequence[Ta]') -> '_coconut.typing.Sequence[Ta]':  #963 (line num in coconut source)
    """
    break_ = break
    """  #966 (line num in coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, _coconut.operator.not_), xs)  # type: ignore  #967 (line num in coconut source)



## Searching lists:
def notElem(e: 'Ta', xs: '_coconut.typing.Sequence[Ta]') -> 'bool':  #972 (line num in coconut source)
    return (e not in xs)  #973 (line num in coconut source)

def lookup(key: 'Ta', assocs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'Maybe':  #975 (line num in coconut source)
    try:  #976 (line num in coconut source)
        return (((Just)((_coconut_iter_getitem((dropwhile)(lambda pair: pair[0] != key, assocs), (0)))[1])))  #977 (line num in coconut source)
    except StopIteration:  #984 (line num in coconut source)
        return (nothing)  #985 (line num in coconut source)



## Zipping and unzipping lists:
zip: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]'  # type: ignore  #990 (line num in coconut source)
zip = _zip  # type: ignore  #991 (line num in coconut source)

zip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]'  #993 (line num in coconut source)
zip3 = _zip  #994 (line num in coconut source)

@_coconut_tco  #996 (line num in coconut source)
def zipWith(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]') -> '_coconut.typing.Iterable[Tc]':  #996 (line num in coconut source)
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))  #997 (line num in coconut source)

@_coconut_tco  #999 (line num in coconut source)
def zipWith3(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', xs1: '_coconut.typing.Iterable[Ta]', xs2: '_coconut.typing.Iterable[Tb]', xs3: '_coconut.typing.Iterable[Tc]') -> '_coconut.typing.Iterable[Td]':  #999 (line num in coconut source)
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))  #1000 (line num in coconut source)

@_coconut_tco  #1002 (line num in coconut source)
def unzip(xs: '_coconut.typing.Iterable[T.Tuple[Ta, Tb]]') -> 'T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]':  #1002 (line num in coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1003 (line num in coconut source)

unzip3: '_coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]'  #1005 (line num in coconut source)
unzip3 = unzip  # type: ignore  #1006 (line num in coconut source)



## Functions on strings:
lines: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1011 (line num in coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1012 (line num in coconut source)

words: '_coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]'  #1014 (line num in coconut source)
words = _coconut.operator.methodcaller("split")  #1015 (line num in coconut source)

@_coconut_tco  #1017 (line num in coconut source)
def unlines(strs: '_coconut.typing.Iterable[str]') -> 'str':  #1017 (line num in coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1018 (line num in coconut source)

unwords: '_coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]'  #1020 (line num in coconut source)
unwords = " ".join  #1021 (line num in coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str, ], str]  #1029 (line num in coconut source)

Show = T.Any  #1031 (line num in coconut source)

showsPrec = NotImplemented  #1033 (line num in coconut source)

show: '_coconut.typing.Callable[[Ta], str]'  #1035 (line num in coconut source)
show = repr  #1036 (line num in coconut source)

def shows(x: 'Show') -> 'ShowS':  #1038 (line num in coconut source)
    return (lambda s: repr(x) + s)  #1039 (line num in coconut source)

def showList(xs: '_coconut.typing.Iterable[Show]') -> 'ShowS':  #1041 (line num in coconut source)
    return (lambda s: repr(list(xs)) + s)  #1042 (line num in coconut source)

def showString(x: 'str') -> 'ShowS':  #1044 (line num in coconut source)
    return (lambda s: x + s)  #1045 (line num in coconut source)

showChar: '_coconut.typing.Callable[[Char], ShowS]'  #1047 (line num in coconut source)
showChar = showString  #1048 (line num in coconut source)

def showParen(parens: 'bool', showFunc: 'ShowS') -> 'ShowS':  #1050 (line num in coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1051 (line num in coconut source)



## Converting from String:
ReadS = NotImplemented  #1059 (line num in coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1061 (line num in coconut source)

readsPrec = NotImplemented  #1072 (line num in coconut source)

readList = NotImplemented  #1074 (line num in coconut source)

reads = NotImplemented  #1076 (line num in coconut source)

readParen = NotImplemented  #1078 (line num in coconut source)

@_coconut_tco  #1080 (line num in coconut source)
def read(s: 'str') -> 'Read':  #1080 (line num in coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1081 (line num in coconut source)

lex = NotImplemented  #1083 (line num in coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1091 (line num in coconut source)
    _coconut_is_data = True  #1091 (line num in coconut source)
    __slots__ = ()  #1091 (line num in coconut source)
    __ne__ = _coconut.object.__ne__  #1091 (line num in coconut source)
    def __eq__(self, other):  #1091 (line num in coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1091 (line num in coconut source)
    def __hash__(self):  #1091 (line num in coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1091 (line num in coconut source)
    __match_args__ = ('io_func',)  #1091 (line num in coconut source)
    @staticmethod  #1091 (line num in coconut source)
    @_coconut_tco  #1091 (line num in coconut source)
    def __pure__(x: 'Ta') -> 'IO':  #1093 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1094 (line num in coconut source)

    @staticmethod  #1096 (line num in coconut source)
    @_coconut_tco  #1096 (line num in coconut source)
    def __fail__(msg: 'str') -> 'IO':  #1097 (line num in coconut source)
        def _coconut_lambda_0():  #1098 (line num in coconut source)
            raise IOError(msg)  #1098 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_lambda_0)  #1098 (line num in coconut source)

    @_coconut_tco  #1100 (line num in coconut source)
    def __fmap__(self, func: '_coconut.typing.Callable[[Ta], Tb]') -> 'IO':  #1100 (line num in coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1101 (line num in coconut source)

    @_coconut_tco  #1103 (line num in coconut source)
    def __join__(self) -> 'IO':  #1103 (line num in coconut source)
        return _coconut_tail_call(_fmap, unIO, self)  #1104 (line num in coconut source)

    @staticmethod  #1106 (line num in coconut source)
    @_coconut_tco  #1106 (line num in coconut source)
    def __mempty__() -> 'IO':  #1107 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1108 (line num in coconut source)

    @_coconut_tco  #1110 (line num in coconut source)
    def __mappend__(self, other: 'IO') -> 'IO':  #1110 (line num in coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1111 (line num in coconut source)

_nullIO: 'IO' = IO(lambda: None)  #1113 (line num in coconut source)

@_coconut_tco  #1115 (line num in coconut source)
def asIO(io: 'IO') -> 'IO':  #1115 (line num in coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1120 (line num in coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1121 (line num in coconut source)

@_coconut_tco  #1123 (line num in coconut source)
def unIO(io: 'IO') -> 'Ta':  #1123 (line num in coconut source)
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
    """  #1137 (line num in coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1138 (line num in coconut source)




## Simple I/O operations:

### Output functions:
@_coconut_tco  #1146 (line num in coconut source)
def putStr(s: 'str') -> 'IO':  #1146 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))  #1147 (line num in coconut source)

putChar: '_coconut.typing.Callable[[Char], IO]'  #1149 (line num in coconut source)
putChar = putStr  #1150 (line num in coconut source)

@_coconut_tco  #1152 (line num in coconut source)
def putStrLn(s: 'str') -> 'IO':  #1152 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))  #1153 (line num in coconut source)

@_coconut_tco  # type: ignore  #1155 (line num in coconut source)
def print(x: 'Ta') -> 'IO':  # type: ignore  #1155 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))  #1156 (line num in coconut source)


### Input functions:
getChar: 'IO' = IO(_coconut.functools.partial(sys.stdin.read, 1))  #1160 (line num in coconut source)

getLine: 'IO' = IO(input)  #1162 (line num in coconut source)

getContents: 'IO' = IO(sys.stdin.read)  #1164 (line num in coconut source)

@_coconut_tco  #1166 (line num in coconut source)
def interact(func: '_coconut.typing.Callable[[str], str]') -> 'IO':  #1166 (line num in coconut source)
    def do_interact():  #1167 (line num in coconut source)
        while True:  #1168 (line num in coconut source)
            (_print)((func)(input()))  #1169 (line num in coconut source)
    return _coconut_tail_call(IO, do_interact)  #1170 (line num in coconut source)


### Files:
FilePath = str  #1174 (line num in coconut source)

@_coconut_tco  #1176 (line num in coconut source)
def readFile(fpath: 'FilePath') -> 'IO':  #1176 (line num in coconut source)
    def do_readFile() -> 'str':  #1177 (line num in coconut source)
        with open(fpath, "r+") as f:  #1178 (line num in coconut source)
            return (f.read())  #1179 (line num in coconut source)
    return _coconut_tail_call(IO, do_readFile)  #1180 (line num in coconut source)

@_coconut_tco  #1182 (line num in coconut source)
def writeFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1182 (line num in coconut source)
    def do_writeFile() -> 'None':  #1183 (line num in coconut source)
        with open(fpath, "w+") as f:  #1184 (line num in coconut source)
            f.write(text)  #1185 (line num in coconut source)
    return _coconut_tail_call(IO, do_writeFile)  #1186 (line num in coconut source)

@_coconut_tco  #1188 (line num in coconut source)
def appendFile(fpath: 'FilePath', text: 'str') -> 'IO':  #1188 (line num in coconut source)
    def do_appendFile() -> 'None':  #1189 (line num in coconut source)
        with open(fpath, "a+") as f:  #1190 (line num in coconut source)
            f.write(text)  #1191 (line num in coconut source)
    return _coconut_tail_call(IO, do_appendFile)  #1192 (line num in coconut source)

@_coconut_tco  #1194 (line num in coconut source)
def readIO(s: 'str') -> 'IO':  #1194 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))  #1195 (line num in coconut source)

@_coconut_tco  #1197 (line num in coconut source)
def readLn() -> 'IO':  #1197 (line num in coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1198 (line num in coconut source)



## Exception handling:
@_coconut_tco  #1203 (line num in coconut source)
def ioError(err: 'IOError') -> 'IO':  #1203 (line num in coconut source)
    def _coconut_lambda_1():  #1204 (line num in coconut source)
        raise err  #1204 (line num in coconut source)
    return _coconut_tail_call(IO, _coconut_lambda_1)  #1204 (line num in coconut source)

@_coconut_tco  #1206 (line num in coconut source)
def userError(msg: 'str') -> 'IOError':  #1206 (line num in coconut source)
    return _coconut_tail_call(IOError, msg)  #1207 (line num in coconut source)
