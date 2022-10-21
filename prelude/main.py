#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6f74bf28

# Compiled with Coconut version 2.0.0-post_dev23 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop, annotations
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

#### Operators:


#### Imports:
sys = _coconut_sys  #18 (line in Coconut source)
import fractions as _fractions  #19 (line in Coconut source)
import math as _math  #20 (line in Coconut source)
import ast as _ast  #21 (line in Coconut source)
from math import gcd as _gcd  #22 (line in Coconut source)

from prelude.util import *  # type: ignore  #24 (line in Coconut source)

#### Untyped built-ins:
_max: _coconut.typing.Callable[..., T.Any] = max  #27 (line in Coconut source)
_min: _coconut.typing.Callable[..., T.Any] = min  #28 (line in Coconut source)
_zip: _coconut.typing.Callable[..., T.Any] = zip  #29 (line in Coconut source)
_abs: _coconut.typing.Callable[..., T.Any] = abs  #30 (line in Coconut source)
_round: _coconut.typing.Callable[..., T.Any] = round  #31 (line in Coconut source)
_fmap: _coconut.typing.Callable[..., T.Any] = fmap  #32 (line in Coconut source)
_reduce: _coconut.typing.Callable[..., T.Any] = reduce  #33 (line in Coconut source)
_all: _coconut.typing.Callable[..., T.Any] = all  #34 (line in Coconut source)
_any: _coconut.typing.Callable[..., T.Any] = any  #35 (line in Coconut source)
_map: _coconut.typing.Callable[..., T.Any] = map  #36 (line in Coconut source)
_filter: _coconut.typing.Callable[..., T.Any] = filter  #37 (line in Coconut source)
_int: _coconut.typing.Callable[..., T.Any] = int  #38 (line in Coconut source)
_sum: _coconut.typing.Callable[..., T.Any] = sum  #39 (line in Coconut source)
_reversed: _coconut.typing.Callable[..., T.Any] = reversed  #40 (line in Coconut source)
_print: _coconut.typing.Callable[..., T.Any] = print  #41 (line in Coconut source)
_ceil: _coconut.typing.Callable[..., T.Any] = _math.ceil  #42 (line in Coconut source)
_floor: _coconut.typing.Callable[..., T.Any] = _math.floor  #43 (line in Coconut source)




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool  #53 (line in Coconut source)

not_: _coconut.typing.Callable[[bool], bool]  #55 (line in Coconut source)
not_ = (_coconut.operator.not_)  #56 (line in Coconut source)

otherwise: bool = True  #58 (line in Coconut source)

#### Maybe:
class Maybe:  #61 (line in Coconut source)
    @staticmethod  #62 (line in Coconut source)
    @_coconut_tco  #63 (line in Coconut source)
    def __pure__(x: Ta) -> Maybe:  #63 (line in Coconut source)
        return _coconut_tail_call(Just, x)  #63 (line in Coconut source)


    @staticmethod  #65 (line in Coconut source)
    def __fail__(msg: str) -> Maybe:  #66 (line in Coconut source)
        return (nothing)  #66 (line in Coconut source)


    @staticmethod  #68 (line in Coconut source)
    def __mempty__() -> Maybe:  #69 (line in Coconut source)
        return (nothing)  #69 (line in Coconut source)


class Nothing(_coconut.collections.namedtuple("Nothing", ()), Maybe):  #71 (line in Coconut source)
    """
    -- Nothing is the data type; use nothing for the canonical instance
    """  #74 (line in Coconut source)

    _coconut_is_data = True  #76 (line in Coconut source)
    __slots__ = ()  #76 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #76 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #76 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #76 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #76 (line in Coconut source)
    def __eq__(self, other):  #76 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #76 (line in Coconut source)
    def __hash__(self):  #76 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #76 (line in Coconut source)
    __match_args__ = ()  #76 (line in Coconut source)
nothing: Maybe = Nothing()  #76 (line in Coconut source)

class Just(_coconut.collections.namedtuple("Just", ('x',)), Maybe):  #78 (line in Coconut source)
    _coconut_is_data = True  #78 (line in Coconut source)
    __slots__ = ()  #78 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #78 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #78 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #78 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #78 (line in Coconut source)
    def __eq__(self, other):  #78 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #78 (line in Coconut source)
    def __hash__(self):  #78 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #78 (line in Coconut source)
    __match_args__ = ('x',)  #78 (line in Coconut source)

derivingOrd(Nothing, Just)  #80 (line in Coconut source)

if TYPE_CHECKING:  #82 (line in Coconut source)
    def maybe(default: Tb, func: _coconut.typing.Callable[[Ta], Tb], x: Maybe) -> Tb:  #83 (line in Coconut source)
        ...  #84 (line in Coconut source)

else:  #85 (line in Coconut source)
    @_coconut_mark_as_match  #86 (line in Coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #86 (line in Coconut source)
        _coconut_match_check_0 = False  #86 (line in Coconut source)
        _coconut_match_set_name_default = _coconut_sentinel  #86 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #86 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("default" not in _coconut_match_kwargs):  #86 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("default")  #86 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.getattr(Nothing, "_coconut_is_data", False) or _coconut.isinstance(Nothing, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Nothing)  # type: ignore  #86 (line in Coconut source)
            _coconut_match_set_name_default = _coconut_match_temp_0  #86 (line in Coconut source)
            if not _coconut_match_kwargs:  #86 (line in Coconut source)
                _coconut_match_check_0 = True  #86 (line in Coconut source)
        if _coconut_match_check_0:  #86 (line in Coconut source)
            _coconut_match_check_0 = False  #86 (line in Coconut source)
            if not _coconut_match_check_0:  #86 (line in Coconut source)
                if (_coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)) and (_coconut.len(_coconut_match_args[2]) == 0):  #86 (line in Coconut source)
                    _coconut_match_check_0 = True  #86 (line in Coconut source)

            if not _coconut_match_check_0:  #86 (line in Coconut source)
                if (not _coconut_match_temp_1) and (_coconut.isinstance(_coconut_match_args[2], Nothing)):  #86 (line in Coconut source)
                    _coconut_match_check_0 = True  #86 (line in Coconut source)
                if _coconut_match_check_0:  #86 (line in Coconut source)
                    _coconut_match_check_0 = False  #86 (line in Coconut source)
                    if not _coconut_match_check_0:  #86 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #86 (line in Coconut source)
                            _coconut_match_check_0 = True  #86 (line in Coconut source)

                    if not _coconut_match_check_0:  #86 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #86 (line in Coconut source)
                            _coconut_match_temp_2 = _coconut.getattr(Nothing, '__match_args__', ())  #86 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #86 (line in Coconut source)
                                raise _coconut.TypeError("Nothing.__match_args__ must be a tuple")  #86 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_2) < 0:  #86 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 0; 'Nothing' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #86 (line in Coconut source)
                            _coconut_match_check_0 = True  #86 (line in Coconut source)




        if _coconut_match_check_0:  #86 (line in Coconut source)
            if _coconut_match_set_name_default is not _coconut_sentinel:  #86 (line in Coconut source)
                default = _coconut_match_set_name_default  #86 (line in Coconut source)
        if not _coconut_match_check_0:  #86 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def maybe(default, _, Nothing()) = default', _coconut_match_args)  #86 (line in Coconut source)

        return (default)  #86 (line in Coconut source)

    @_coconut_addpattern(maybe)  #87 (line in Coconut source)
    @_coconut_tco  #87 (line in Coconut source)
    @_coconut_mark_as_match  #87 (line in Coconut source)
    def maybe(*_coconut_match_args, **_coconut_match_kwargs):  #87 (line in Coconut source)
        _coconut_match_check_1 = False  #87 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #87 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #87 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("func" not in _coconut_match_kwargs):  #87 (line in Coconut source)
            _coconut_match_temp_3 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #87 (line in Coconut source)
            _coconut_match_temp_4 = _coconut.getattr(Just, "_coconut_is_data", False) or _coconut.isinstance(Just, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Just)  # type: ignore  #87 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_match_temp_3  #87 (line in Coconut source)
            if not _coconut_match_kwargs:  #87 (line in Coconut source)
                _coconut_match_check_1 = True  #87 (line in Coconut source)
        if _coconut_match_check_1:  #87 (line in Coconut source)
            _coconut_match_check_1 = False  #87 (line in Coconut source)
            if not _coconut_match_check_1:  #87 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                if (_coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)) and (_coconut.len(_coconut_match_args[2]) == 1):  #87 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #87 (line in Coconut source)
                    _coconut_match_check_1 = True  #87 (line in Coconut source)
                if _coconut_match_check_1:  #87 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                        x = _coconut_match_set_name_x  #87 (line in Coconut source)

            if not _coconut_match_check_1:  #87 (line in Coconut source)
                if (not _coconut_match_temp_4) and (_coconut.isinstance(_coconut_match_args[2], Just)):  #87 (line in Coconut source)
                    _coconut_match_check_1 = True  #87 (line in Coconut source)
                if _coconut_match_check_1:  #87 (line in Coconut source)
                    _coconut_match_check_1 = False  #87 (line in Coconut source)
                    if not _coconut_match_check_1:  #87 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #87 (line in Coconut source)
                            _coconut_match_check_1 = True  #87 (line in Coconut source)
                        if _coconut_match_check_1:  #87 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                                x = _coconut_match_set_name_x  #87 (line in Coconut source)

                    if not _coconut_match_check_1:  #87 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #87 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #87 (line in Coconut source)
                            _coconut_match_temp_5 = _coconut.getattr(Just, '__match_args__', ())  #87 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_5, _coconut.tuple):  #87 (line in Coconut source)
                                raise _coconut.TypeError("Just.__match_args__ must be a tuple")  #87 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_5) < 1:  #87 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Just' only supports %s)" % (_coconut.len(_coconut_match_temp_5),))  #87 (line in Coconut source)
                            _coconut_match_temp_6 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_5[0], _coconut_sentinel)  #87 (line in Coconut source)
                            if _coconut_match_temp_6 is not _coconut_sentinel:  #87 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_6  #87 (line in Coconut source)
                                _coconut_match_check_1 = True  #87 (line in Coconut source)
                        if _coconut_match_check_1:  #87 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #87 (line in Coconut source)
                                x = _coconut_match_set_name_x  #87 (line in Coconut source)




        if _coconut_match_check_1:  #87 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #87 (line in Coconut source)
                func = _coconut_match_set_name_func  #87 (line in Coconut source)
        if not _coconut_match_check_1:  #87 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def maybe(_, func, Just(x)) = func x', _coconut_match_args)  #87 (line in Coconut source)

        return _coconut_tail_call(func, x)  #87 (line in Coconut source)

#### Either:

class Either:  #90 (line in Coconut source)
    @staticmethod  #91 (line in Coconut source)
    @_coconut_tco  #92 (line in Coconut source)
    def __pure__(x: Ta) -> Either:  #92 (line in Coconut source)
        return _coconut_tail_call(Right, x)  #92 (line in Coconut source)


    @staticmethod  #94 (line in Coconut source)
    @_coconut_tco  #95 (line in Coconut source)
    def __fail__(msg: str) -> Either:  #95 (line in Coconut source)
        return _coconut_tail_call(Left, msg)  #95 (line in Coconut source)


class Left(_coconut.collections.namedtuple("Left", ('x',)), Either):  #97 (line in Coconut source)
    _coconut_is_data = True  #97 (line in Coconut source)
    __slots__ = ()  #97 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #97 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #97 (line in Coconut source)
    def __eq__(self, other):  #97 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #97 (line in Coconut source)
    def __hash__(self):  #97 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #97 (line in Coconut source)
    __match_args__ = ('x',)  #97 (line in Coconut source)
    @staticmethod  #98 (line in Coconut source)
    def __bool__() -> bool:  #99 (line in Coconut source)
        return (False)  #99 (line in Coconut source)


    def __fmap__(self, func: _coconut.typing.Callable[[Ta], Tb]) -> Either:  #101 (line in Coconut source)
        return (self)  #101 (line in Coconut source)


class Right(_coconut.collections.namedtuple("Right", ('x',)), Either):  #103 (line in Coconut source)
    _coconut_is_data = True  #103 (line in Coconut source)
    __slots__ = ()  #103 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #103 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #103 (line in Coconut source)
    def __eq__(self, other):  #103 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #103 (line in Coconut source)
    def __hash__(self):  #103 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #103 (line in Coconut source)
    __match_args__ = ('x',)  #103 (line in Coconut source)

derivingOrd(Left, Right)  #105 (line in Coconut source)

if TYPE_CHECKING:  #107 (line in Coconut source)
    def either(left_func: _coconut.typing.Callable[[Ta], Tc], right_func: _coconut.typing.Callable[[Tb], Tc], x: Either) -> Tc:  #108 (line in Coconut source)
        ...  #109 (line in Coconut source)

else:  #110 (line in Coconut source)
    @_coconut_tco  #111 (line in Coconut source)
    @_coconut_mark_as_match  #111 (line in Coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #111 (line in Coconut source)
        _coconut_match_check_2 = False  #111 (line in Coconut source)
        _coconut_match_set_name_left_func = _coconut_sentinel  #111 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #111 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("left_func" not in _coconut_match_kwargs):  #111 (line in Coconut source)
            _coconut_match_temp_7 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("left_func")  #111 (line in Coconut source)
            _coconut_match_temp_8 = _coconut.getattr(Left, "_coconut_is_data", False) or _coconut.isinstance(Left, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Left)  # type: ignore  #111 (line in Coconut source)
            _coconut_match_set_name_left_func = _coconut_match_temp_7  #111 (line in Coconut source)
            if not _coconut_match_kwargs:  #111 (line in Coconut source)
                _coconut_match_check_2 = True  #111 (line in Coconut source)
        if _coconut_match_check_2:  #111 (line in Coconut source)
            _coconut_match_check_2 = False  #111 (line in Coconut source)
            if not _coconut_match_check_2:  #111 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                if (_coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)) and (_coconut.len(_coconut_match_args[2]) == 1):  #111 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #111 (line in Coconut source)
                    _coconut_match_check_2 = True  #111 (line in Coconut source)
                if _coconut_match_check_2:  #111 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                        x = _coconut_match_set_name_x  #111 (line in Coconut source)

            if not _coconut_match_check_2:  #111 (line in Coconut source)
                if (not _coconut_match_temp_8) and (_coconut.isinstance(_coconut_match_args[2], Left)):  #111 (line in Coconut source)
                    _coconut_match_check_2 = True  #111 (line in Coconut source)
                if _coconut_match_check_2:  #111 (line in Coconut source)
                    _coconut_match_check_2 = False  #111 (line in Coconut source)
                    if not _coconut_match_check_2:  #111 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #111 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #111 (line in Coconut source)
                            _coconut_match_check_2 = True  #111 (line in Coconut source)
                        if _coconut_match_check_2:  #111 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                                x = _coconut_match_set_name_x  #111 (line in Coconut source)

                    if not _coconut_match_check_2:  #111 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #111 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #111 (line in Coconut source)
                            _coconut_match_temp_9 = _coconut.getattr(Left, '__match_args__', ())  #111 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_9, _coconut.tuple):  #111 (line in Coconut source)
                                raise _coconut.TypeError("Left.__match_args__ must be a tuple")  #111 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_9) < 1:  #111 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Left' only supports %s)" % (_coconut.len(_coconut_match_temp_9),))  #111 (line in Coconut source)
                            _coconut_match_temp_10 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_9[0], _coconut_sentinel)  #111 (line in Coconut source)
                            if _coconut_match_temp_10 is not _coconut_sentinel:  #111 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_10  #111 (line in Coconut source)
                                _coconut_match_check_2 = True  #111 (line in Coconut source)
                        if _coconut_match_check_2:  #111 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #111 (line in Coconut source)
                                x = _coconut_match_set_name_x  #111 (line in Coconut source)




        if _coconut_match_check_2:  #111 (line in Coconut source)
            if _coconut_match_set_name_left_func is not _coconut_sentinel:  #111 (line in Coconut source)
                left_func = _coconut_match_set_name_left_func  #111 (line in Coconut source)
        if not _coconut_match_check_2:  #111 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def either(left_func, _, Left(x)) = left_func x', _coconut_match_args)  #111 (line in Coconut source)

        return _coconut_tail_call(left_func, x)  #111 (line in Coconut source)

    @_coconut_addpattern(either)  #112 (line in Coconut source)
    @_coconut_tco  #112 (line in Coconut source)
    @_coconut_mark_as_match  #112 (line in Coconut source)
    def either(*_coconut_match_args, **_coconut_match_kwargs):  #112 (line in Coconut source)
        _coconut_match_check_3 = False  #112 (line in Coconut source)
        _coconut_match_set_name_right_func = _coconut_sentinel  #112 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #112 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 3) and ("right_func" not in _coconut_match_kwargs):  #112 (line in Coconut source)
            _coconut_match_temp_11 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("right_func")  #112 (line in Coconut source)
            _coconut_match_temp_12 = _coconut.getattr(Right, "_coconut_is_data", False) or _coconut.isinstance(Right, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in Right)  # type: ignore  #112 (line in Coconut source)
            _coconut_match_set_name_right_func = _coconut_match_temp_11  #112 (line in Coconut source)
            if not _coconut_match_kwargs:  #112 (line in Coconut source)
                _coconut_match_check_3 = True  #112 (line in Coconut source)
        if _coconut_match_check_3:  #112 (line in Coconut source)
            _coconut_match_check_3 = False  #112 (line in Coconut source)
            if not _coconut_match_check_3:  #112 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                if (_coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)) and (_coconut.len(_coconut_match_args[2]) == 1):  #112 (line in Coconut source)
                    _coconut_match_set_name_x = _coconut_match_args[2][0]  #112 (line in Coconut source)
                    _coconut_match_check_3 = True  #112 (line in Coconut source)
                if _coconut_match_check_3:  #112 (line in Coconut source)
                    if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                        x = _coconut_match_set_name_x  #112 (line in Coconut source)

            if not _coconut_match_check_3:  #112 (line in Coconut source)
                if (not _coconut_match_temp_12) and (_coconut.isinstance(_coconut_match_args[2], Right)):  #112 (line in Coconut source)
                    _coconut_match_check_3 = True  #112 (line in Coconut source)
                if _coconut_match_check_3:  #112 (line in Coconut source)
                    _coconut_match_check_3 = False  #112 (line in Coconut source)
                    if not _coconut_match_check_3:  #112 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                        if _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #112 (line in Coconut source)
                            _coconut_match_set_name_x = _coconut_match_args[2]  #112 (line in Coconut source)
                            _coconut_match_check_3 = True  #112 (line in Coconut source)
                        if _coconut_match_check_3:  #112 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                                x = _coconut_match_set_name_x  #112 (line in Coconut source)

                    if not _coconut_match_check_3:  #112 (line in Coconut source)
                        _coconut_match_set_name_x = _coconut_sentinel  #112 (line in Coconut source)
                        if not _coconut.type(_coconut_match_args[2]) in _coconut_self_match_types:  #112 (line in Coconut source)
                            _coconut_match_temp_13 = _coconut.getattr(Right, '__match_args__', ())  #112 (line in Coconut source)
                            if not _coconut.isinstance(_coconut_match_temp_13, _coconut.tuple):  #112 (line in Coconut source)
                                raise _coconut.TypeError("Right.__match_args__ must be a tuple")  #112 (line in Coconut source)
                            if _coconut.len(_coconut_match_temp_13) < 1:  #112 (line in Coconut source)
                                raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'Right' only supports %s)" % (_coconut.len(_coconut_match_temp_13),))  #112 (line in Coconut source)
                            _coconut_match_temp_14 = _coconut.getattr(_coconut_match_args[2], _coconut_match_temp_13[0], _coconut_sentinel)  #112 (line in Coconut source)
                            if _coconut_match_temp_14 is not _coconut_sentinel:  #112 (line in Coconut source)
                                _coconut_match_set_name_x = _coconut_match_temp_14  #112 (line in Coconut source)
                                _coconut_match_check_3 = True  #112 (line in Coconut source)
                        if _coconut_match_check_3:  #112 (line in Coconut source)
                            if _coconut_match_set_name_x is not _coconut_sentinel:  #112 (line in Coconut source)
                                x = _coconut_match_set_name_x  #112 (line in Coconut source)




        if _coconut_match_check_3:  #112 (line in Coconut source)
            if _coconut_match_set_name_right_func is not _coconut_sentinel:  #112 (line in Coconut source)
                right_func = _coconut_match_set_name_right_func  #112 (line in Coconut source)
        if not _coconut_match_check_3:  #112 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def either(_, right_func, Right(x)) = right_func x', _coconut_match_args)  #112 (line in Coconut source)

        return _coconut_tail_call(right_func, x)  #112 (line in Coconut source)

#### Ordering:

class Ordering:  #115 (line in Coconut source)
    @staticmethod  #116 (line in Coconut source)
    def __mempty__() -> Ordering:  #117 (line in Coconut source)
        return (eq)  #117 (line in Coconut source)


class LT(_coconut.collections.namedtuple("LT", ()), Ordering):  #119 (line in Coconut source)
    _coconut_is_data = True  #119 (line in Coconut source)
    __slots__ = ()  #119 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #119 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #119 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #119 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #119 (line in Coconut source)
    def __eq__(self, other):  #119 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #119 (line in Coconut source)
    def __hash__(self):  #119 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #119 (line in Coconut source)
    __match_args__ = ()  #119 (line in Coconut source)
    @staticmethod  #120 (line in Coconut source)
    def __bool__() -> bool:  #121 (line in Coconut source)
        return (True)  #121 (line in Coconut source)


class EQ(_coconut.collections.namedtuple("EQ", ()), Ordering):  #123 (line in Coconut source)
    _coconut_is_data = True  #123 (line in Coconut source)
    __slots__ = ()  #123 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #123 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #123 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #123 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #123 (line in Coconut source)
    def __eq__(self, other):  #123 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #123 (line in Coconut source)
    def __hash__(self):  #123 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #123 (line in Coconut source)
    __match_args__ = ()  #123 (line in Coconut source)

class GT(_coconut.collections.namedtuple("GT", ()), Ordering):  #125 (line in Coconut source)
    _coconut_is_data = True  #125 (line in Coconut source)
    __slots__ = ()  #125 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #125 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #125 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #125 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #125 (line in Coconut source)
    def __eq__(self, other):  #125 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #125 (line in Coconut source)
    def __hash__(self):  #125 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #125 (line in Coconut source)
    __match_args__ = ()  #125 (line in Coconut source)
    @staticmethod  #126 (line in Coconut source)
    def __bool__() -> bool:  #127 (line in Coconut source)
        return (True)  #127 (line in Coconut source)


derivingOrd(LT, EQ, GT)  #129 (line in Coconut source)
derivingBoundedEnum(LT, EQ, GT)  #130 (line in Coconut source)

lt: Ordering = LT()  #132 (line in Coconut source)
eq: Ordering = EQ()  #133 (line in Coconut source)
gt: Ordering = GT()  #134 (line in Coconut source)

#### Char:
Char = T.NewType("Char", str)  #137 (line in Coconut source)

#### String:
String = str  #140 (line in Coconut source)


### Tuples:
fst: _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]  #144 (line in Coconut source)
fst = _coconut.operator.itemgetter((0))  #145 (line in Coconut source)

snd: _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]  #147 (line in Coconut source)
snd = _coconut.operator.itemgetter((1))  #148 (line in Coconut source)

def curry_tuple(func: _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]) -> _coconut.typing.Callable[[Ta, Tb], Tc]:  #150 (line in Coconut source)
    """
    -- curry a function of a tuple into a Python-style multi-place function
    """  #153 (line in Coconut source)
    return (lambda *args: func(args))  # type: ignore  #154 (line in Coconut source)


def uncurry_tuple(func: _coconut.typing.Callable[[Ta, Tb], Tc]) -> _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tc]:  #156 (line in Coconut source)
    """
    -- uncurry a Python-style multi-place function into a function of a tuple
    """  #159 (line in Coconut source)
    return (lambda args: func(*args))  #160 (line in Coconut source)



## Basic type classes:

#### Eq:

Eq = object  #167 (line in Coconut source)

#### Ord:
Ord = Eq  #170 (line in Coconut source)
TOrd = T.TypeVar("TOrd", bound=Ord)  #171 (line in Coconut source)

if TYPE_CHECKING:  #173 (line in Coconut source)
    def compare(x: Ord, y: Ord) -> Ordering:  #174 (line in Coconut source)
        ...  #175 (line in Coconut source)

else:  #176 (line in Coconut source)
    @_coconut_mark_as_match  #177 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #177 (line in Coconut source)
        _coconut_match_check_4 = False  #177 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #177 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #177 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #177 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #177 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #177 (line in Coconut source)
            _coconut_match_temp_16 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #177 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_15  #177 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_16  #177 (line in Coconut source)
            if not _coconut_match_kwargs:  #177 (line in Coconut source)
                _coconut_match_check_4 = True  #177 (line in Coconut source)
        if _coconut_match_check_4:  #177 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #177 (line in Coconut source)
                x = _coconut_match_set_name_x  #177 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #177 (line in Coconut source)
                y = _coconut_match_set_name_y  #177 (line in Coconut source)
        if _coconut_match_check_4 and not (x == y):  #177 (line in Coconut source)
            _coconut_match_check_4 = False  #177 (line in Coconut source)
        if not _coconut_match_check_4:  #177 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def compare(x, y if x == y) = eq', _coconut_match_args)  #177 (line in Coconut source)

        return (eq)  #177 (line in Coconut source)

    @_coconut_addpattern(compare)  #178 (line in Coconut source)
    @_coconut_mark_as_match  #178 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #178 (line in Coconut source)
        _coconut_match_check_5 = False  #178 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #178 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #178 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #178 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #178 (line in Coconut source)
            _coconut_match_temp_17 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #178 (line in Coconut source)
            _coconut_match_temp_18 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #178 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_17  #178 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_18  #178 (line in Coconut source)
            if not _coconut_match_kwargs:  #178 (line in Coconut source)
                _coconut_match_check_5 = True  #178 (line in Coconut source)
        if _coconut_match_check_5:  #178 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #178 (line in Coconut source)
                x = _coconut_match_set_name_x  #178 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #178 (line in Coconut source)
                y = _coconut_match_set_name_y  #178 (line in Coconut source)
        if _coconut_match_check_5 and not (x < y):  #178 (line in Coconut source)
            _coconut_match_check_5 = False  #178 (line in Coconut source)
        if not _coconut_match_check_5:  #178 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x < y) = lt', _coconut_match_args)  #178 (line in Coconut source)

        return (lt)  #178 (line in Coconut source)

    @_coconut_addpattern(compare)  #179 (line in Coconut source)
    @_coconut_mark_as_match  #179 (line in Coconut source)
    def compare(*_coconut_match_args, **_coconut_match_kwargs):  #179 (line in Coconut source)
        _coconut_match_check_6 = False  #179 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #179 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #179 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #179 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #179 (line in Coconut source)
            _coconut_match_temp_19 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #179 (line in Coconut source)
            _coconut_match_temp_20 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #179 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_19  #179 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_20  #179 (line in Coconut source)
            if not _coconut_match_kwargs:  #179 (line in Coconut source)
                _coconut_match_check_6 = True  #179 (line in Coconut source)
        if _coconut_match_check_6:  #179 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #179 (line in Coconut source)
                x = _coconut_match_set_name_x  #179 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #179 (line in Coconut source)
                y = _coconut_match_set_name_y  #179 (line in Coconut source)
        if _coconut_match_check_6 and not (x > y):  #179 (line in Coconut source)
            _coconut_match_check_6 = False  #179 (line in Coconut source)
        if not _coconut_match_check_6:  #179 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def compare(x, y if x > y) = gt', _coconut_match_args)  #179 (line in Coconut source)

        return (gt)  #179 (line in Coconut source)


max: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  #181 (line in Coconut source)
max = _max  #182 (line in Coconut source)

min: _coconut.typing.Callable[[TOrd, TOrd], TOrd]  #184 (line in Coconut source)
min = _min  #185 (line in Coconut source)

#### Enum:
Enum = Ord  #188 (line in Coconut source)
TEnum = T.TypeVar("TEnum", bound=Enum)  #189 (line in Coconut source)

succ: _coconut.typing.Callable[[TEnum], TEnum]  #191 (line in Coconut source)
succ = _coconut.functools.partial((_coconut.operator.add), 1)  #192 (line in Coconut source)

pred: _coconut.typing.Callable[[TEnum], TEnum]  #194 (line in Coconut source)
pred = _coconut_partial((_coconut_minus), {1: 1}, 2, ())  #195 (line in Coconut source)

toEnum = NotImplemented  #197 (line in Coconut source)

fromEnum: _coconut.typing.Callable[[Enum], int]  #199 (line in Coconut source)
fromEnum = _int  #200 (line in Coconut source)

@_coconut_tco  #202 (line in Coconut source)
def enumFrom(first: TEnum) -> _coconut.typing.Iterable[TEnum]:  #202 (line in Coconut source)
    return _coconut_tail_call(iterate, succ, first)  #203 (line in Coconut source)


def enumFromThen(first: TEnum, second: TEnum) -> _coconut.typing.Iterable[TEnum]:  #205 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #206 (line in Coconut source)
    return (iterate(_coconut.functools.partial((_coconut.operator.add), step), first) if step >= 0 else ())  # type: ignore  #207 (line in Coconut source)


def enumFromTo(first: TEnum, last: TEnum) -> _coconut.typing.Iterable[TEnum]:  #209 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #210 (line in Coconut source)
    return (_coconut_iter_getitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ())  # type: ignore  #211 (line in Coconut source)


def enumFromThenTo(first: TEnum, second: TEnum, last: TEnum) -> _coconut.typing.Iterable[TEnum]:  #213 (line in Coconut source)
    step = fromEnum(second) - fromEnum(first)  #214 (line in Coconut source)
    dist = fromEnum(last) - fromEnum(first)  #215 (line in Coconut source)
    steps = dist / step if step != 0 else 0  #216 (line in Coconut source)
    if steps < 0:  #217 (line in Coconut source)
        return (())  #218 (line in Coconut source)
    counter = iterate(_coconut.functools.partial((_coconut.operator.add), step), first)  #219 (line in Coconut source)
    return (_coconut_iter_getitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter)  #220 (line in Coconut source)


#### Bounded:

Bounded = T.Union[bool, T.Iterable]  #224 (line in Coconut source)
TBounded = T.TypeVar("TBounded", bound=Bounded)  #225 (line in Coconut source)

@_coconut_tco  #227 (line in Coconut source)
def minBound(b: TBounded) -> TBounded:  #227 (line in Coconut source)
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """  #231 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #233 (line in Coconut source)
        return (False)  # type: ignore  #234 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__minBound__"):  #237 (line in Coconut source)
        return _coconut_tail_call(b.__minBound__)  # type: ignore  #238 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)  # type: ignore  #241 (line in Coconut source)


@_coconut_tco  #243 (line in Coconut source)
def maxBound(b: TBounded) -> TBounded:  #243 (line in Coconut source)
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """  #247 (line in Coconut source)
# Check if bool
    if (isinstance)(b, bool):  #249 (line in Coconut source)
        return (True)  # type: ignore  #250 (line in Coconut source)

# Check if overridden
    if (hasattr)(b, "__maxBound__"):  #253 (line in Coconut source)
        return _coconut_tail_call(b.__maxBound__)  # type: ignore  #254 (line in Coconut source)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)  # type: ignore  #257 (line in Coconut source)



## Numbers:

### Numeric types:

#### Int:

Int = int  #266 (line in Coconut source)

#### Integer:
Integer = int  #269 (line in Coconut source)

#### Float:
Float = float  #272 (line in Coconut source)

#### Double:
Double = float  #275 (line in Coconut source)

#### Rational:
Rational = _fractions.Fraction  #278 (line in Coconut source)

@_coconut_tco  #280 (line in Coconut source)
def over(x, y):  #280 (line in Coconut source)
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """  #285 (line in Coconut source)
    return _coconut_tail_call(Rational, x, y)  #286 (line in Coconut source)

_coconut_op_U25_U25 = over  #287 (line in Coconut source)

#### Word:
Word = Int  #290 (line in Coconut source)


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]  #296 (line in Coconut source)
TNum = T.TypeVar("TNum", bound=Num)  #297 (line in Coconut source)

negate: _coconut.typing.Callable[[TNum], TNum]  #299 (line in Coconut source)
negate = (_coconut_minus)  #300 (line in Coconut source)

abs: _coconut.typing.Callable[[TNum], TNum]  #302 (line in Coconut source)
abs = _abs  #303 (line in Coconut source)

if TYPE_CHECKING:  #305 (line in Coconut source)
    def signum(x: Num) -> int:  #306 (line in Coconut source)
        ...  #307 (line in Coconut source)

else:  #308 (line in Coconut source)
    @_coconut_mark_as_match  #309 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #309 (line in Coconut source)
        _coconut_match_check_7 = False  #309 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #309 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #309 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #309 (line in Coconut source)
                if not _coconut_match_kwargs:  #309 (line in Coconut source)
                    _coconut_match_check_7 = True  #309 (line in Coconut source)
        if not _coconut_match_check_7:  #309 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def signum(0) = 0', _coconut_match_args)  #309 (line in Coconut source)

        return (0)  #309 (line in Coconut source)

    @_coconut_addpattern(signum)  #310 (line in Coconut source)
    @_coconut_mark_as_match  #310 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #310 (line in Coconut source)
        _coconut_match_check_8 = False  #310 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #310 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #310 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #310 (line in Coconut source)
            _coconut_match_temp_21 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #310 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_21  #310 (line in Coconut source)
            if not _coconut_match_kwargs:  #310 (line in Coconut source)
                _coconut_match_check_8 = True  #310 (line in Coconut source)
        if _coconut_match_check_8:  #310 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #310 (line in Coconut source)
                x = _coconut_match_set_name_x  #310 (line in Coconut source)
        if _coconut_match_check_8 and not (x > 0):  #310 (line in Coconut source)
            _coconut_match_check_8 = False  #310 (line in Coconut source)
        if not _coconut_match_check_8:  #310 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x > 0) = 1', _coconut_match_args)  #310 (line in Coconut source)

        return (1)  #310 (line in Coconut source)

    @_coconut_addpattern(signum)  #311 (line in Coconut source)
    @_coconut_mark_as_match  #311 (line in Coconut source)
    def signum(*_coconut_match_args, **_coconut_match_kwargs):  #311 (line in Coconut source)
        _coconut_match_check_9 = False  #311 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #311 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #311 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1):  #311 (line in Coconut source)
            _coconut_match_temp_22 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #311 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_22  #311 (line in Coconut source)
            if not _coconut_match_kwargs:  #311 (line in Coconut source)
                _coconut_match_check_9 = True  #311 (line in Coconut source)
        if _coconut_match_check_9:  #311 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #311 (line in Coconut source)
                x = _coconut_match_set_name_x  #311 (line in Coconut source)
        if _coconut_match_check_9 and not (x < 0):  #311 (line in Coconut source)
            _coconut_match_check_9 = False  #311 (line in Coconut source)
        if not _coconut_match_check_9:  #311 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def signum(x if x < 0) = -1', _coconut_match_args)  #311 (line in Coconut source)

        return (-1)  #311 (line in Coconut source)


def fromInteger(x: Integer) -> Num:  #313 (line in Coconut source)
    return (x)  #313 (line in Coconut source)

#### Real:

Real = Num  #316 (line in Coconut source)

if TYPE_CHECKING:  #318 (line in Coconut source)
    def toRational(real: Real) -> Rational:  #319 (line in Coconut source)
        ...  #320 (line in Coconut source)

else:  #321 (line in Coconut source)
    @_coconut_tco  #322 (line in Coconut source)
    @_coconut_mark_as_match  #322 (line in Coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #322 (line in Coconut source)
        _coconut_match_check_10 = False  #322 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #322 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #322 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #322 (line in Coconut source)
            _coconut_match_temp_23 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #322 (line in Coconut source)
            if (isinstance)(_coconut_match_temp_23, float):  #322 (line in Coconut source)
                _coconut_match_set_name_real = _coconut_match_temp_23  #322 (line in Coconut source)
                if not _coconut_match_kwargs:  #322 (line in Coconut source)
                    _coconut_match_check_10 = True  #322 (line in Coconut source)
        if _coconut_match_check_10:  #322 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #322 (line in Coconut source)
                real = _coconut_match_set_name_real  #322 (line in Coconut source)
        if not _coconut_match_check_10:  #322 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def toRational(real `isinstance` float) =', _coconut_match_args)  #322 (line in Coconut source)

        return _coconut_tail_call(Rational.from_float, real)  #323 (line in Coconut source)

    @_coconut_addpattern(toRational)  #324 (line in Coconut source)
    @_coconut_tco  #324 (line in Coconut source)
    @_coconut_mark_as_match  #324 (line in Coconut source)
    def toRational(*_coconut_match_args, **_coconut_match_kwargs):  #324 (line in Coconut source)
        _coconut_match_check_11 = False  #324 (line in Coconut source)
        _coconut_match_set_name_real = _coconut_sentinel  #324 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #324 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "real" in _coconut_match_kwargs)) == 1):  #324 (line in Coconut source)
            _coconut_match_temp_24 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("real")  #324 (line in Coconut source)
            _coconut_match_set_name_real = _coconut_match_temp_24  #324 (line in Coconut source)
            if not _coconut_match_kwargs:  #324 (line in Coconut source)
                _coconut_match_check_11 = True  #324 (line in Coconut source)
        if _coconut_match_check_11:  #324 (line in Coconut source)
            if _coconut_match_set_name_real is not _coconut_sentinel:  #324 (line in Coconut source)
                real = _coconut_match_set_name_real  #324 (line in Coconut source)
        if not _coconut_match_check_11:  #324 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def toRational(real) =', _coconut_match_args)  #324 (line in Coconut source)

        return _coconut_tail_call(Rational, real)  #325 (line in Coconut source)

#### Integral:

Integral = int  #328 (line in Coconut source)

def quot(x: int, y: int) -> int:  #330 (line in Coconut source)
    divxy = x // y  #331 (line in Coconut source)
    return (divxy + (1 if divxy < 0 and x % y != 0 else 0))  #332 (line in Coconut source)


def rem(x: int, y: int) -> int:  #334 (line in Coconut source)
    modxy = x % y  #335 (line in Coconut source)
    return (modxy - (y if modxy != 0 and x // y < 0 else 0))  #336 (line in Coconut source)


div: _coconut.typing.Callable[[int, int], int]  #338 (line in Coconut source)
div = (_coconut.operator.floordiv)  #339 (line in Coconut source)

mod: _coconut.typing.Callable[[int, int], int]  #341 (line in Coconut source)
mod = (_coconut.operator.mod)  #342 (line in Coconut source)

def quotRem(x: int, y: int) -> T.Tuple[int, int]:  #344 (line in Coconut source)
    divxy, modxy = divmod(x, y)  #345 (line in Coconut source)
    adj = 1 if divxy < 0 and modxy != 0 else 0  #346 (line in Coconut source)
    return (divxy + adj, modxy - y * adj)  #347 (line in Coconut source)


divMod = divmod  #349 (line in Coconut source)

toInteger: _coconut.typing.Callable[[Integral], Integer]  #351 (line in Coconut source)
toInteger = _int  #352 (line in Coconut source)

#### Fractional:
Fractional = Rational  #355 (line in Coconut source)

recip: _coconut.typing.Callable[[Fractional], Fractional]  #357 (line in Coconut source)
recip = _coconut.functools.partial((_coconut.operator.truediv), 1)  #358 (line in Coconut source)

def fromRational(x: Rational) -> Fractional:  #360 (line in Coconut source)
    return (x)  #360 (line in Coconut source)

#### Floating:

Floating = float  #363 (line in Coconut source)

from math import pi  # NOQA  #365 (line in Coconut source)
from math import exp  # NOQA  #365 (line in Coconut source)
from math import log  # NOQA  #365 (line in Coconut source)
from math import sqrt  # NOQA  #365 (line in Coconut source)
from math import sin  # NOQA  #365 (line in Coconut source)
from math import cos  # NOQA  #365 (line in Coconut source)
from math import tan  # NOQA  #365 (line in Coconut source)
from math import asin  # NOQA  #365 (line in Coconut source)
from math import acos  # NOQA  #365 (line in Coconut source)
from math import atan  # NOQA  #365 (line in Coconut source)
from math import sinh  # NOQA  #365 (line in Coconut source)
from math import cosh  # NOQA  #365 (line in Coconut source)
from math import tanh  # NOQA  #365 (line in Coconut source)
from math import asinh  # NOQA  #365 (line in Coconut source)
from math import acosh  # NOQA  #365 (line in Coconut source)
from math import atanh  # NOQA  #365 (line in Coconut source)

@_coconut_tco  #384 (line in Coconut source)
def logBase(base: float, x: float) -> float:  #384 (line in Coconut source)
    return _coconut_tail_call(log, x, base)  #385 (line in Coconut source)

#### RealFrac:

RealFrac = Rational  #388 (line in Coconut source)

def properFraction(x: RealFrac) -> T.Tuple[int, RealFrac]:  #390 (line in Coconut source)
    floor_x = floor(x)  #391 (line in Coconut source)
    return (floor_x, x - floor_x)  #392 (line in Coconut source)


truncate: _coconut.typing.Callable[[RealFrac], int]  #394 (line in Coconut source)
truncate = _int  #395 (line in Coconut source)

round: _coconut.typing.Callable[[RealFrac], int]  #397 (line in Coconut source)
round = _round  #398 (line in Coconut source)

ceiling: _coconut.typing.Callable[[RealFrac], int]  #400 (line in Coconut source)
ceiling = _ceil  #401 (line in Coconut source)

floor: _coconut.typing.Callable[[RealFrac], int]  #403 (line in Coconut source)
floor = _floor  #404 (line in Coconut source)

#### RealFloat:
RealFloat = float  #407 (line in Coconut source)

def floatRadix(x: float) -> int:  #409 (line in Coconut source)
    return (2)  #409 (line in Coconut source)


def floatDigits(x: float) -> int:  #411 (line in Coconut source)
    return (53)  #411 (line in Coconut source)


def floatRange(x: float) -> T.Tuple[int, int]:  #413 (line in Coconut source)
    return ((-1021, 1024))  #413 (line in Coconut source)


decodeFloat = NotImplemented  #415 (line in Coconut source)

encodeFloat = NotImplemented  #417 (line in Coconut source)

exponent = NotImplemented  #419 (line in Coconut source)

significand = NotImplemented  #421 (line in Coconut source)

def scaleFloat(power: int, x: float) -> float:  #423 (line in Coconut source)
    return (x * 2**power)  #424 (line in Coconut source)

# NOQA
from math import isnan as isNaN  # NOQA  #426 (line in Coconut source)
from math import isinf as isInfinite  # NOQA  #426 (line in Coconut source)
from math import atan2  # NOQA  #426 (line in Coconut source)

isDenormalized = NotImplemented  #432 (line in Coconut source)

def isNegativeZero(x: float) -> bool:  #434 (line in Coconut source)
    return (x == 0 and str(x).startswith("-"))  #435 (line in Coconut source)


def isIEEE(x: float) -> bool:  #437 (line in Coconut source)
    return (True)  #437 (line in Coconut source)


### Numeric functions:

def subtract(x, y):  #441 (line in Coconut source)
    return (y - x)  #442 (line in Coconut source)


def even(x: int) -> bool:  #444 (line in Coconut source)
    return (x % 2 == 0)  #445 (line in Coconut source)


def odd(x: int) -> bool:  #447 (line in Coconut source)
    return (x % 2 == 1)  #448 (line in Coconut source)


gcd: _coconut.typing.Callable[[int, int], int]  #450 (line in Coconut source)
gcd = _coconut_forward_compose(_gcd, abs)  #451 (line in Coconut source)

if TYPE_CHECKING:  #453 (line in Coconut source)
    def lcm(x: int, y: int) -> int:  #454 (line in Coconut source)
        ...  #455 (line in Coconut source)

else:  #456 (line in Coconut source)
    @_coconut_mark_as_match  #457 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #457 (line in Coconut source)
        _coconut_match_check_12 = False  #457 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #457 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #457 (line in Coconut source)
            if _coconut_match_args[1] == 0:  #457 (line in Coconut source)
                if not _coconut_match_kwargs:  #457 (line in Coconut source)
                    _coconut_match_check_12 = True  #457 (line in Coconut source)
        if not _coconut_match_check_12:  #457 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def lcm(_, 0) = 0', _coconut_match_args)  #457 (line in Coconut source)

        return (0)  #457 (line in Coconut source)

    @_coconut_addpattern(lcm)  #458 (line in Coconut source)
    @_coconut_mark_as_match  #458 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #458 (line in Coconut source)
        _coconut_match_check_13 = False  #458 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #458 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #458 (line in Coconut source)
            if _coconut_match_args[0] == 0:  #458 (line in Coconut source)
                if not _coconut_match_kwargs:  #458 (line in Coconut source)
                    _coconut_match_check_13 = True  #458 (line in Coconut source)
        if not _coconut_match_check_13:  #458 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(0, _) = 0', _coconut_match_args)  #458 (line in Coconut source)

        return (0)  #458 (line in Coconut source)

    @_coconut_addpattern(lcm)  #459 (line in Coconut source)
    @_coconut_mark_as_match  #459 (line in Coconut source)
    def lcm(*_coconut_match_args, **_coconut_match_kwargs):  #459 (line in Coconut source)
        _coconut_match_check_14 = False  #459 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #459 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #459 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #459 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "x" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "y" in _coconut_match_kwargs)) == 1):  #459 (line in Coconut source)
            _coconut_match_temp_25 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("x")  #459 (line in Coconut source)
            _coconut_match_temp_26 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("y")  #459 (line in Coconut source)
            _coconut_match_set_name_x = _coconut_match_temp_25  #459 (line in Coconut source)
            _coconut_match_set_name_y = _coconut_match_temp_26  #459 (line in Coconut source)
            if not _coconut_match_kwargs:  #459 (line in Coconut source)
                _coconut_match_check_14 = True  #459 (line in Coconut source)
        if _coconut_match_check_14:  #459 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #459 (line in Coconut source)
                x = _coconut_match_set_name_x  #459 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #459 (line in Coconut source)
                y = _coconut_match_set_name_y  #459 (line in Coconut source)
        if not _coconut_match_check_14:  #459 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def lcm(x, y) =', _coconut_match_args)  #459 (line in Coconut source)

        return (abs(y) * (abs(x) // gcd(x, y)))  #460 (line in Coconut source)


fromIntegral: _coconut.typing.Callable[[Integral], Num]  #462 (line in Coconut source)
fromIntegral = fromInteger  #463 (line in Coconut source)

realToFrac: _coconut.typing.Callable[[Real], Fractional]  #465 (line in Coconut source)
realToFrac = toRational  #466 (line in Coconut source)



## Monoids:
Monoid = T.Iterable  #471 (line in Coconut source)
TMonoid = T.TypeVar("TMonoid", bound=Monoid)  #472 (line in Coconut source)

class Mempty(_coconut.collections.namedtuple("Mempty", ())):  #474 (line in Coconut source)
    """
    -- mempty is overridden by the __mempty__ method
    """  #477 (line in Coconut source)
    _coconut_is_data = True  #478 (line in Coconut source)
    __slots__ = ()  #478 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #478 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #478 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #478 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #478 (line in Coconut source)
    def __eq__(self, other):  #478 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #478 (line in Coconut source)
    def __hash__(self):  #478 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #478 (line in Coconut source)
    __match_args__ = ()  #478 (line in Coconut source)
    @staticmethod  #478 (line in Coconut source)
    @_coconut_tco  #479 (line in Coconut source)
    def mempty_as(M: TMonoid) -> TMonoid:  #479 (line in Coconut source)
        if (hasattr)(M, "__mempty__"):  #480 (line in Coconut source)
            return _coconut_tail_call(M.__mempty__)  # type: ignore  #481 (line in Coconut source)
        return _coconut_tail_call(makedata, type(M))  #482 (line in Coconut source)


mempty: T.Any = Mempty()  #484 (line in Coconut source)

@_coconut_tco  #486 (line in Coconut source)
def mappend(x: TMonoid, y: TMonoid) -> TMonoid:  #486 (line in Coconut source)
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """  #491 (line in Coconut source)
# Resolve memptys
    x = (asTypeOf)(x, y)  #493 (line in Coconut source)
    y = (asTypeOf)(y, x)  #494 (line in Coconut source)

# Check if overridden
    if (hasattr)(x, "__mappend__"):  #497 (line in Coconut source)
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore  #498 (line in Coconut source)

# Default implementation
    if not x:  #501 (line in Coconut source)
        return (y)  #502 (line in Coconut source)
    if not y:  #503 (line in Coconut source)
        return (x)  #504 (line in Coconut source)
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):  #505 (line in Coconut source)
        return _coconut_tail_call((makedata), type(x), *zipWith(mappend, x, y))  #506 (line in Coconut source)
    return _coconut_tail_call((makedata), type(x), *(_coconut.itertools.chain)(x, y))  #507 (line in Coconut source)


@_coconut_tco  #509 (line in Coconut source)
def mconcat(ms: _coconut.typing.Sequence[TMonoid]) -> TMonoid:  #509 (line in Coconut source)
    return _coconut_tail_call(foldr, mappend, mempty, ms)  # type: ignore  #510 (line in Coconut source)



## Monads and functors:

#### Functor:

Functor = T.Iterable  #517 (line in Coconut source)

@_coconut_tco  # type: ignore  #519 (line in Coconut source)
def fmap(f: _coconut.typing.Callable[[Ta], Tb], xs: Functor[Ta]) -> Functor[Tb]:  # type: ignore  #519 (line in Coconut source)
    """
    -- fmap is overridden by the __fmap__ method
    """  #522 (line in Coconut source)
    try:  #523 (line in Coconut source)
# Default implementation
        return (_fmap(f, xs))  #525 (line in Coconut source)

    except TypeError:  #527 (line in Coconut source)
# Function instance
        if callable(xs):  #529 (line in Coconut source)
            return _coconut_tail_call(_coconut_forward_compose, xs, f)  # type: ignore  #530 (line in Coconut source)

        raise  #532 (line in Coconut source)


@_coconut_tco  #534 (line in Coconut source)
def fmapConst(x: Ta, xs: Functor) -> Functor[Ta]:  #534 (line in Coconut source)
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """  #538 (line in Coconut source)
    return _coconut_tail_call(fmap, lambda _: x, xs)  #539 (line in Coconut source)

_coconut_op_U3c_U24 = fmapConst  #540 (line in Coconut source)

#### Applicative:
Applicative = Functor  #543 (line in Coconut source)
TApp = T.TypeVar("TApp", bound=Applicative)  #544 (line in Coconut source)

if TYPE_CHECKING:  #546 (line in Coconut source)
    def pure(x: Ta) -> T.Any:  #547 (line in Coconut source)
        ...  #548 (line in Coconut source)

else:  #549 (line in Coconut source)
    class pure(_coconut.collections.namedtuple("pure", ('val',))):  #550 (line in Coconut source)
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """  #554 (line in Coconut source)

        _coconut_is_data = True  #556 (line in Coconut source)
        __slots__ = ()  #556 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #556 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #556 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #556 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #556 (line in Coconut source)
        def __eq__(self, other):  #556 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #556 (line in Coconut source)
        def __hash__(self):  #556 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #556 (line in Coconut source)
        __match_args__ = ('val',)  #556 (line in Coconut source)
        def __join__(self) -> T.Any:  #556 (line in Coconut source)
            return (self.val)  #556 (line in Coconut source)


        def __call__(self, arg: T.Any) -> T.Any:  #558 (line in Coconut source)
            """Implicitly casts pure to the Applicative function instance."""  #559 (line in Coconut source)
            return (self.val)  #560 (line in Coconut source)


        @_coconut_tco  #562 (line in Coconut source)
        def pure_as(self, M: TApp) -> TApp:  #562 (line in Coconut source)
# Check if overridden
            if (hasattr)(M, "__pure__"):  #564 (line in Coconut source)
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore  #565 (line in Coconut source)

            try:  #567 (line in Coconut source)
# Default implementation
                return (makedata(type(M), self.val))  #569 (line in Coconut source)

            except TypeError:  #571 (line in Coconut source)
# Check for functions
                if callable(M):  #573 (line in Coconut source)
                    return _coconut_tail_call(const, self.val)  #574 (line in Coconut source)

# Fallback
                raise  #577 (line in Coconut source)


@_coconut_tco  #579 (line in Coconut source)
def ap(fs: Applicative[_coconut.typing.Callable[[Ta], Tb]], xs: Applicative[Ta]) -> Applicative[Tb]:  #579 (line in Coconut source)
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """  #586 (line in Coconut source)
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore  #588 (line in Coconut source)
    xs = (asTypeOf)(xs, fs)  # type: ignore  #589 (line in Coconut source)

# Check if overridden
    if (hasattr)(fs, "__ap__"):  #592 (line in Coconut source)
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore  #593 (line in Coconut source)

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: fmap(f, xs))  #596 (line in Coconut source)

_coconut_op_U3c_U2a_U3e = ap  #597 (line in Coconut source)

@_coconut_tco  #599 (line in Coconut source)
def seqAr(f1: Applicative, f2: TApp) -> TApp:  #599 (line in Coconut source)
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """  #603 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x2, f1), f2)  # type: ignore  #604 (line in Coconut source)

_coconut_op_U2a_U3e = seqAr  #605 (line in Coconut source)

@_coconut_tco  #607 (line in Coconut source)
def seqAl(f1: TApp, f2: Applicative) -> TApp:  #607 (line in Coconut source)
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """  #611 (line in Coconut source)
    return _coconut_tail_call((ap), fmap(lambda x1: lambda x2: x1, f1), f2)  # type: ignore  #612 (line in Coconut source)

_coconut_op_U3c_U2a = seqAl  #613 (line in Coconut source)

def liftA2(func: _coconut.typing.Callable[[Ta, Tb], Tc]) -> _coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]:  #615 (line in Coconut source)
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """  #619 (line in Coconut source)
    return (lambda f1, f2: (ap)(fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2))  # type: ignore  #620 (line in Coconut source)

#### Monad:

Monad = Applicative  #623 (line in Coconut source)
TMonad = T.TypeVar("TMonad", bound=Monad)  #624 (line in Coconut source)

@_coconut_tco  #626 (line in Coconut source)
def bind(m: Monad[Ta], func: _coconut.typing.Callable[[Ta], TMonad]) -> TMonad:  #626 (line in Coconut source)
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """  #631 (line in Coconut source)
    return _coconut_tail_call(join, fmap(func, m))  # type: ignore  #632 (line in Coconut source)

_coconut_op_U3e_U3e_U3e_U3d = bind  #633 (line in Coconut source)

@_coconut_tco  #635 (line in Coconut source)
def seqM(m1: Monad, m2: TMonad) -> TMonad:  #635 (line in Coconut source)
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """  #639 (line in Coconut source)
    return _coconut_tail_call((bind), m1, lambda x: m2)  # type: ignore  #640 (line in Coconut source)

_coconut_op_U3e_U3e_U3e = seqM  #641 (line in Coconut source)

return_ = pure  #643 (line in Coconut source)

if TYPE_CHECKING:  #645 (line in Coconut source)
    def fail(msg: str) -> T.Any:  #646 (line in Coconut source)
        ...  #647 (line in Coconut source)

else:  #648 (line in Coconut source)
    class fail(_coconut.typing.NamedTuple("fail", [("msg", str)])):  #649 (line in Coconut source)
        """
        -- fail is overridden by the __fail__ method
        """  #652 (line in Coconut source)

        _coconut_is_data = True  #654 (line in Coconut source)
        __slots__ = ()  #654 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #654 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #654 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #654 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #654 (line in Coconut source)
        def __eq__(self, other):  #654 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #654 (line in Coconut source)
        def __hash__(self):  #654 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #654 (line in Coconut source)
        __match_args__ = ('msg',)  #654 (line in Coconut source)
        @staticmethod  #654 (line in Coconut source)
        def __bool__() -> bool:  #655 (line in Coconut source)
            return (False)  #655 (line in Coconut source)


        def __fmap__(self, func: _coconut.typing.Callable[[Ta], Tb]) -> T.Any:  #657 (line in Coconut source)
            return (self)  #657 (line in Coconut source)


        @_coconut_tco  #659 (line in Coconut source)
        def fail_as(self, M: TMonad) -> TMonad:  #659 (line in Coconut source)
            if (hasattr)(M, "__fail__"):  #660 (line in Coconut source)
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore  #661 (line in Coconut source)
            return _coconut_tail_call(makedata, type(M))  #662 (line in Coconut source)

# sequence_ and mapM_ defined in Foldable


@_coconut_tco  #666 (line in Coconut source)
def bindFrom(func: _coconut.typing.Callable[[Ta], TMonad], m: Monad[Ta]) -> TMonad:  #666 (line in Coconut source)
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """  #670 (line in Coconut source)
    return _coconut_tail_call((bind), m, func)  #671 (line in Coconut source)

_coconut_op_U3d_U3c_U3c_U3c = bindFrom  #672 (line in Coconut source)

@_coconut_tco  #674 (line in Coconut source)
def join(ms: Monad[TMonad]) -> TMonad:  #674 (line in Coconut source)
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation uses __bool__ and __iter__
    """  #681 (line in Coconut source)
# Resolve ms being pure or fail
    _coconut_match_to_0 = ms  #683 (line in Coconut source)
    _coconut_match_check_15 = False  #683 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Iterable):  #683 (line in Coconut source)
        _coconut_match_check_15 = True  #683 (line in Coconut source)
    if _coconut_match_check_15:  #683 (line in Coconut source)
        ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)  #684 (line in Coconut source)

# Resolve pures and fails inside of ms
    ms = (fmap)(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore  #687 (line in Coconut source)

# Check if overridden
    if (hasattr)(ms, "__join__"):  #690 (line in Coconut source)
        return _coconut_tail_call(ms.__join__)  # type: ignore  #691 (line in Coconut source)

# Default implementation
    _coconut_case_match_to_0 = ms  #694 (line in Coconut source)
    _coconut_case_match_check_0 = False  #694 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #694 (line in Coconut source)
        _coconut_case_match_check_0 = True  #694 (line in Coconut source)
    if _coconut_case_match_check_0:  #694 (line in Coconut source)
        if not ms:  #698 (line in Coconut source)
            return (ms)  # type: ignore  #699 (line in Coconut source)
        vals = []  # type: ignore  #700 (line in Coconut source)
        fallback = ms  #701 (line in Coconut source)
        for m in (ms):  #702 (line in Coconut source)
            if m:  #703 (line in Coconut source)
                vals.extend(m)  # type: ignore  #704 (line in Coconut source)
            else:  #705 (line in Coconut source)
                fallback = m  # type: ignore  #706 (line in Coconut source)
        if not vals:  #707 (line in Coconut source)
            return (fallback)  # type: ignore  #708 (line in Coconut source)
        return _coconut_tail_call(makedata, type(ms), *vals)  # type: ignore  #709 (line in Coconut source)

# Function instance
    if not _coconut_case_match_check_0:  #712 (line in Coconut source)
        _coconut_case_match_check_0 = True  #712 (line in Coconut source)
        if _coconut_case_match_check_0 and not (callable(ms)):  #712 (line in Coconut source)
            _coconut_case_match_check_0 = False  #712 (line in Coconut source)
        if _coconut_case_match_check_0:  #712 (line in Coconut source)
            return (lambda r: ms(r)(r))  # type: ignore  #713 (line in Coconut source)

    if not _coconut_case_match_check_0:  #715 (line in Coconut source)
        raise TypeError("cannot join non-monad type " + str(type(ms)))  #716 (line in Coconut source)


if TYPE_CHECKING:  #718 (line in Coconut source)
    def do(monads: _coconut.typing.Sequence[TMonad], func: _coconut.typing.Callable[..., TMonad]) -> TMonad:  #719 (line in Coconut source)
        ...  #720 (line in Coconut source)

else:  #721 (line in Coconut source)
    @_coconut_tco  #722 (line in Coconut source)
    @_coconut_mark_as_match  #722 (line in Coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #722 (line in Coconut source)
        _coconut_match_check_16 = False  #722 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #722 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #722 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #722 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 0):  #722 (line in Coconut source)
                _coconut_match_temp_27 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #722 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_27  #722 (line in Coconut source)
                if not _coconut_match_kwargs:  #722 (line in Coconut source)
                    _coconut_match_check_16 = True  #722 (line in Coconut source)
        if _coconut_match_check_16:  #722 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #722 (line in Coconut source)
                func = _coconut_match_set_name_func  #722 (line in Coconut source)
        if not _coconut_match_check_16:  #722 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def do([], func) = func()', _coconut_match_args)  #722 (line in Coconut source)

        return _coconut_tail_call(func)  #722 (line in Coconut source)

    @_coconut_addpattern(do)  #723 (line in Coconut source)
    @_coconut_tco  #723 (line in Coconut source)
    @_coconut_mark_as_match  #723 (line in Coconut source)
    def do(*_coconut_match_args, **_coconut_match_kwargs):  #723 (line in Coconut source)
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
        """  #742 (line in Coconut source)
        _coconut_match_check_17 = False  #743 (line in Coconut source)
        _coconut_match_set_name_m = _coconut_sentinel  #743 (line in Coconut source)
        _coconut_match_set_name_ms = _coconut_sentinel  #743 (line in Coconut source)
        _coconut_match_set_name_func = _coconut_sentinel  #743 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #743 (line in Coconut source)
        if (1 <= _coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "func" in _coconut_match_kwargs)) == 1):  #743 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #743 (line in Coconut source)
                _coconut_match_set_name_m = _coconut_match_args[0][0]  #743 (line in Coconut source)
                _coconut_match_temp_29 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("func")  #743 (line in Coconut source)
                _coconut_match_temp_28 = _coconut.list(_coconut_match_args[0][1:])  #743 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_29  #743 (line in Coconut source)
                _coconut_match_set_name_ms = _coconut_match_temp_28  #743 (line in Coconut source)
                if not _coconut_match_kwargs:  #743 (line in Coconut source)
                    _coconut_match_check_17 = True  #743 (line in Coconut source)
        if _coconut_match_check_17:  #743 (line in Coconut source)
            if _coconut_match_set_name_m is not _coconut_sentinel:  #743 (line in Coconut source)
                m = _coconut_match_set_name_m  #743 (line in Coconut source)
            if _coconut_match_set_name_ms is not _coconut_sentinel:  #743 (line in Coconut source)
                ms = _coconut_match_set_name_ms  #743 (line in Coconut source)
            if _coconut_match_set_name_func is not _coconut_sentinel:  #743 (line in Coconut source)
                func = _coconut_match_set_name_func  #743 (line in Coconut source)
        if not _coconut_match_check_17:  #743 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def do([m] + ms, func) =', _coconut_match_args)  #743 (line in Coconut source)

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))  #743 (line in Coconut source)



## Folds and traversals:

#### Foldable:

Foldable = T.Sequence  #750 (line in Coconut source)

@_coconut_tco  #752 (line in Coconut source)
def sequence_(ms: Foldable[Monad]) -> Monad:  #752 (line in Coconut source)
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))  #753 (line in Coconut source)


mapM_: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]  #755 (line in Coconut source)
mapM_ = _coconut_forward_compose(fmap, sequence_)  #756 (line in Coconut source)

@_coconut_tco  #758 (line in Coconut source)
def foldMap(func: _coconut.typing.Callable[[Ta], TMonoid], xs: Foldable[Ta]) -> TMonoid:  #758 (line in Coconut source)
    return _coconut_tail_call(mconcat, _map(func, xs))  # type: ignore  #759 (line in Coconut source)


@_coconut_tco  #761 (line in Coconut source)
def foldl(func: _coconut.typing.Callable[[Tb, Ta], Tb], init: Tb, xs: Foldable[Ta]) -> Tb:  #761 (line in Coconut source)
    return _coconut_tail_call(_reduce, func, xs, init)  #762 (line in Coconut source)


@_coconut_tco  #764 (line in Coconut source)
def foldr(func: _coconut.typing.Callable[[Ta, Tb], Tb], init: Tb, xs: Foldable[Ta]) -> Tb:  #764 (line in Coconut source)
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)  #765 (line in Coconut source)


foldl1: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]  #767 (line in Coconut source)
foldl1 = reduce  #768 (line in Coconut source)

@_coconut_tco  #770 (line in Coconut source)
def foldr1(func: _coconut.typing.Callable[[Ta, Ta], Ta], xs: Foldable[Ta]) -> Ta:  #770 (line in Coconut source)
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))  #771 (line in Coconut source)


def null(xs: Foldable[Ta]) -> bool:  #773 (line in Coconut source)
    return (len(xs) == 0)  #774 (line in Coconut source)


length: _coconut.typing.Callable[[Foldable], int]  #776 (line in Coconut source)
length = len  #777 (line in Coconut source)

def elem(e: Ta, xs: Foldable[Ta]) -> bool:  #779 (line in Coconut source)
    return (e in xs)  #780 (line in Coconut source)


maximum: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #782 (line in Coconut source)
maximum = _max  #783 (line in Coconut source)

minimum: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]  #785 (line in Coconut source)
minimum = _min  #786 (line in Coconut source)

sum: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #788 (line in Coconut source)
sum = _sum  #789 (line in Coconut source)

product: _coconut.typing.Callable[[Foldable[TNum]], TNum]  #791 (line in Coconut source)
product = _coconut.functools.partial(reduce, _coconut.operator.mul)  #792 (line in Coconut source)

#### Traversable:
Traversable = T.Iterable  #795 (line in Coconut source)

@_coconut_tco  #797 (line in Coconut source)
def _snoc(xs: _coconut.typing.Iterable[Ta], x: Ta) -> _coconut.typing.Iterable[Ta]:  #797 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, (x,))  #798 (line in Coconut source)


@_coconut_tco  #800 (line in Coconut source)
def sequenceA(fs: Traversable[Applicative[Ta]]) -> Applicative[Traversable[Ta]]:  #800 (line in Coconut source)
    return _coconut_tail_call((fmap), lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))  #801 (line in Coconut source)


traverse: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]  #803 (line in Coconut source)
traverse = _coconut_forward_compose(fmap, sequenceA)  #804 (line in Coconut source)

sequence: _coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]  #806 (line in Coconut source)
sequence = sequenceA  #807 (line in Coconut source)

mapM: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]  #809 (line in Coconut source)
mapM = traverse  #810 (line in Coconut source)



## Miscellaneous functions:
id: _coconut.typing.Callable[[Ta], Ta] = ident  #815 (line in Coconut source)

@_coconut_tco  #817 (line in Coconut source)
def dot(f: _coconut.typing.Callable[[Tb], Tc], g: _coconut.typing.Callable[[Ta], Tb]) -> _coconut.typing.Callable[[Ta], Tc]:  #817 (line in Coconut source)
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """  #821 (line in Coconut source)
    return _coconut_tail_call(_coconut_forward_compose, g, f)  # type: ignore  #822 (line in Coconut source)


if TYPE_CHECKING:  #824 (line in Coconut source)
    @T.overload  #825 (line in Coconut source)
    def apply(func: _coconut.typing.Callable[[Ta], Tb], arg: Ta) -> Tb:  #826 (line in Coconut source)
        ...  #827 (line in Coconut source)

    @T.overload  #828 (line in Coconut source)
    def apply(func: _coconut.typing.Callable[[Ta, Tb], Tc], arg: Ta) -> _coconut.typing.Callable[[Tb], Tc]:  #829 (line in Coconut source)
        ...  #830 (line in Coconut source)

    @T.overload  #831 (line in Coconut source)
    def apply(func: _coconut.typing.Callable[[Ta, Tb, Tc], Td], arg: Ta) -> _coconut.typing.Callable[[Tb, Tc], Td]:  #832 (line in Coconut source)
        ...  #833 (line in Coconut source)

    @T.overload  #834 (line in Coconut source)
    def apply(func: _coconut.typing.Callable[..., Tb], arg: Ta) -> T.Any:  #835 (line in Coconut source)
        ...  #836 (line in Coconut source)

    def apply(func, arg):  #837 (line in Coconut source)
        ...  #838 (line in Coconut source)

else:  #839 (line in Coconut source)
    @_coconut_tco  #840 (line in Coconut source)
    def apply(func, arg):  #840 (line in Coconut source)
        """
        apply :: (a -> b) -> a -> b
        apply = ($)
        -- apply will automatically curry functions as in Haskell function
        --  application (see also `of` for the more general version)
        """  #846 (line in Coconut source)
        return _coconut_tail_call((of), func, arg)  #847 (line in Coconut source)

_coconut_op_U24_U24 = apply  #848 (line in Coconut source)

@_coconut_tco  #850 (line in Coconut source)
def until(cond: _coconut.typing.Callable[[Ta], bool], func: _coconut.typing.Callable[[Ta], Ta], x: Ta) -> Ta:  #850 (line in Coconut source)
    while True:  #851 (line in Coconut source)
        if cond(x):  #851 (line in Coconut source)
            return (x)  #852 (line in Coconut source)
        try:  # tail recursive  #853 (line in Coconut source)
            _coconut_tre_check_0 = until is _coconut_recursive_func_71  # tail recursive  #853 (line in Coconut source)
        except _coconut.NameError:  # tail recursive  #853 (line in Coconut source)
            _coconut_tre_check_0 = False  # tail recursive  #853 (line in Coconut source)
        if _coconut_tre_check_0:  # tail recursive  #853 (line in Coconut source)
            cond, func, x = cond, func, func(x)  # tail recursive  #853 (line in Coconut source)
            continue  # tail recursive  #853 (line in Coconut source)
        else:  # tail recursive  #853 (line in Coconut source)
            return _coconut_tail_call(until, cond, func, func(x))  #854 (line in Coconut source)
        return None  #855 (line in Coconut source)

_coconut_recursive_func_71 = until  #855 (line in Coconut source)

def asTypeOf(x: Ta, y: Ta) -> Ta:  #855 (line in Coconut source)
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """  #859 (line in Coconut source)
    if TYPE_CHECKING:  #860 (line in Coconut source)
        return (x)  #860 (line in Coconut source)

    if not (isinstance)(y, (pure, fail, Mempty)):  #862 (line in Coconut source)
        for i in ((takewhile)(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count())):  #863 (line in Coconut source)
            if (isinstance)(x, pure):  #864 (line in Coconut source)
                x = x.pure_as(y)  #865 (line in Coconut source)
            elif (isinstance)(x, fail):  #866 (line in Coconut source)
                x = x.fail_as(y)  #867 (line in Coconut source)
            elif (isinstance)(x, Mempty):  #868 (line in Coconut source)
                x = x.mempty_as(y)  #869 (line in Coconut source)
            else:  #870 (line in Coconut source)
                break  #871 (line in Coconut source)
    return (x)  #872 (line in Coconut source)

# type: ignore
asTypeOf.RECURSION_LIMIT = 3  # type: ignore  #874 (line in Coconut source)

def error(msg: str) -> None:  #876 (line in Coconut source)
    raise Exception(msg)  #877 (line in Coconut source)


def errorWithoutStackTrace(msg: str) -> None:  #879 (line in Coconut source)
    raise Exception(msg) from None  #880 (line in Coconut source)


undefined: T.Any = None  #882 (line in Coconut source)

def seq(x: Ta, y: Tb) -> Tb:  #884 (line in Coconut source)
    """
    -- seq doesn't actually do anything here, since Python isn't lazy
    """  #887 (line in Coconut source)
    return (y)  #888 (line in Coconut source)


@_coconut_tco  #890 (line in Coconut source)
def cbv(func: _coconut.typing.Callable[[Ta], Tb], arg: Ta) -> Tb:  #890 (line in Coconut source)
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    -- cbv is just an apply that doesn't curry the provided function
    """  #895 (line in Coconut source)
    return _coconut_tail_call((seq), arg, func(arg))  #896 (line in Coconut source)




# List operations:

@_coconut_tco  #902 (line in Coconut source)
def cons(x: Ta, xs: _coconut.typing.Iterable[Ta]) -> _coconut.typing.Iterable[Ta]:  #902 (line in Coconut source)
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """  #906 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), [x,], xs)  #907 (line in Coconut source)

# type: ignore
map: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]  # type: ignore  #909 (line in Coconut source)
map = _map  # type: ignore  #910 (line in Coconut source)

@_coconut_tco  #912 (line in Coconut source)
def chain(xs: _coconut.typing.Iterable[Ta], ys: _coconut.typing.Iterable[Ta]) -> _coconut.typing.Iterable[Ta]:  #912 (line in Coconut source)
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """  #916 (line in Coconut source)
    return _coconut_tail_call((_coconut.itertools.chain), xs, ys)  #917 (line in Coconut source)

_coconut_op_U2b_U2b = chain  #918 (line in Coconut source)

filter: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  # type: ignore  #920 (line in Coconut source)
filter = _filter  # type: ignore  #921 (line in Coconut source)

head: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #923 (line in Coconut source)
head = _coconut.functools.partial(_coconut_iter_getitem, index=(0))  #924 (line in Coconut source)

last: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]  #926 (line in Coconut source)
last = _coconut.functools.partial(_coconut_iter_getitem, index=(-1))  #927 (line in Coconut source)

tail: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #929 (line in Coconut source)
tail = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(1, None)))  # type: ignore  #930 (line in Coconut source)

init: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #932 (line in Coconut source)
init = _coconut.functools.partial(_coconut_iter_getitem, index=(_coconut.slice(None, -1)))  # type: ignore  #933 (line in Coconut source)

@_coconut_tco  #935 (line in Coconut source)
def at(xs: _coconut.typing.Iterable[Ta], i: int) -> Ta:  #935 (line in Coconut source)
    """
    at :: [a] -> Int -> a
    at = (!!)
    """  #939 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, i)  #940 (line in Coconut source)

_coconut_op_U21_U21 = at  #941 (line in Coconut source)

reverse: _coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]  #943 (line in Coconut source)
reverse = _reversed  #944 (line in Coconut source)



## Special folds:
and_: _coconut.typing.Callable[[Foldable[bool]], bool]  #949 (line in Coconut source)
and_ = _all  #950 (line in Coconut source)

or_: _coconut.typing.Callable[[Foldable[bool]], bool]  #952 (line in Coconut source)
or_ = _any  #953 (line in Coconut source)

any: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #955 (line in Coconut source)
any = _coconut_forward_compose(map, or_)  #956 (line in Coconut source)

all: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]  #958 (line in Coconut source)
all = _coconut_forward_compose(map, and_)  #959 (line in Coconut source)

@_coconut_tco  #961 (line in Coconut source)
def concat(xs: Foldable[_coconut.typing.Iterable[Ta]]) -> _coconut.typing.Iterable[Ta]:  #961 (line in Coconut source)
    return _coconut_tail_call(_reduce, (_coconut.itertools.chain), xs, ())  #962 (line in Coconut source)


concatMap: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]  #964 (line in Coconut source)
concatMap = _coconut_forward_compose(map, concat)  #965 (line in Coconut source)



## Building lists:

### Scans:
@_coconut_tco  #972 (line in Coconut source)
def scanl(func: _coconut.typing.Callable[[Ta, Tb], Ta], init: Ta, xs: _coconut.typing.Iterable[Tb]) -> _coconut.typing.Iterable[Ta]:  #972 (line in Coconut source)
    return _coconut_tail_call(scan, func, xs, init)  #973 (line in Coconut source)


scanl1: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #975 (line in Coconut source)
scanl1 = scan  #976 (line in Coconut source)

@_coconut_tco  #978 (line in Coconut source)
def scanr(func: _coconut.typing.Callable[[Ta, Tb], Ta], init: Ta, xs: _coconut.typing.Sequence[Tb]) -> _coconut.typing.Iterable[Ta]:  #978 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))  #979 (line in Coconut source)


@_coconut_tco  #981 (line in Coconut source)
def scanr1(func: _coconut.typing.Callable[[Ta, Ta], Ta], xs: _coconut.typing.Sequence[Ta]) -> _coconut.typing.Iterable[Ta]:  #981 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))  #982 (line in Coconut source)

### Infinite lists:

@recursive_iterator  #985 (line in Coconut source)
@_coconut_tco  #986 (line in Coconut source)
def iterate(func: _coconut.typing.Callable[[Ta], Ta], x: Ta) -> _coconut.typing.Iterable[Ta]:  #986 (line in Coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: iterate(func, func(x)))))  #987 (line in Coconut source)


@recursive_iterator  #989 (line in Coconut source)
@_coconut_tco  #990 (line in Coconut source)
def repeat(x: Ta) -> _coconut.typing.Iterable[Ta]:  #990 (line in Coconut source)
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: [x,], lambda: repeat(x))))  #991 (line in Coconut source)


@_coconut_tco  #993 (line in Coconut source)
def replicate(n: int, x: Ta) -> _coconut.typing.Iterable[Ta]:  #993 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, repeat(x), _coconut.slice(None, n))  #994 (line in Coconut source)


if TYPE_CHECKING:  #996 (line in Coconut source)
    def cycle(xs: _coconut.typing.Sequence[Ta]) -> _coconut.typing.Iterable[Ta]:  #997 (line in Coconut source)
        ...  #998 (line in Coconut source)

else:  #999 (line in Coconut source)
    @recursive_iterator  #1000 (line in Coconut source)
    @_coconut_tco  #1001 (line in Coconut source)
    @_coconut_mark_as_match  #1001 (line in Coconut source)
    def cycle(*_coconut_match_args, **_coconut_match_kwargs):  #1001 (line in Coconut source)
        _coconut_match_check_18 = False  #1001 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1001 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1001 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "xs" in _coconut_match_kwargs)) == 1):  #1001 (line in Coconut source)
            _coconut_match_temp_30 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("xs")  #1001 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_30  #1001 (line in Coconut source)
            if not _coconut_match_kwargs:  #1001 (line in Coconut source)
                _coconut_match_check_18 = True  #1001 (line in Coconut source)
        if _coconut_match_check_18:  #1001 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1001 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1001 (line in Coconut source)
        if _coconut_match_check_18 and not (len(xs) > 0):  #1001 (line in Coconut source)
            _coconut_match_check_18 = False  #1001 (line in Coconut source)
        if not _coconut_match_check_18:  #1001 (line in Coconut source)
            raise _coconut_FunctionMatchError('def cycle(xs if len(xs) > 0) =', _coconut_match_args)  #1001 (line in Coconut source)

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, _coconut_reiterable(_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))  #1002 (line in Coconut source)



## Sublists:

@_coconut_tco  #1007 (line in Coconut source)
def take(n: int, xs: _coconut.typing.Iterable[Ta]) -> _coconut.typing.Iterable[Ta]:  #1007 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(None, n))  #1008 (line in Coconut source)


@_coconut_tco  #1010 (line in Coconut source)
def drop(n: int, xs: _coconut.typing.Iterable[Ta]) -> _coconut.typing.Iterable[Ta]:  #1010 (line in Coconut source)
    return _coconut_tail_call(_coconut_iter_getitem, xs, _coconut.slice(n, None))  #1011 (line in Coconut source)


def splitAt(n: int, xs: _coconut.typing.Iterable[Ta]) -> T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]:  #1013 (line in Coconut source)
    reit = reiterable(xs)  #1014 (line in Coconut source)
    return (_coconut_iter_getitem(reit, _coconut.slice(None, n)), _coconut_iter_getitem(reit, _coconut.slice(n, None)))  #1015 (line in Coconut source)


takeWhile: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1017 (line in Coconut source)
takeWhile = takewhile  #1018 (line in Coconut source)

dropWhile: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]  #1020 (line in Coconut source)
dropWhile = dropwhile  #1021 (line in Coconut source)

if TYPE_CHECKING:  #1023 (line in Coconut source)
    def span(cond: _coconut.typing.Callable[[Ta], bool], xs: _coconut.typing.Sequence[Ta]) -> T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]:  #1024 (line in Coconut source)
        ...  #1025 (line in Coconut source)

else:  #1026 (line in Coconut source)
    @_coconut_mark_as_match  #1027 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1027 (line in Coconut source)
        _coconut_match_check_19 = False  #1027 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1027 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 2:  #1027 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 0):  #1027 (line in Coconut source)
                if not _coconut_match_kwargs:  #1027 (line in Coconut source)
                    _coconut_match_check_19 = True  #1027 (line in Coconut source)
        if not _coconut_match_check_19:  #1027 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def span(_, []) = ([], [])', _coconut_match_args)  #1027 (line in Coconut source)

        return (([], []))  #1027 (line in Coconut source)

    @_coconut_addpattern(span)  #1028 (line in Coconut source)
    @_coconut_mark_as_match  #1028 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1028 (line in Coconut source)
        _coconut_match_check_20 = False  #1028 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1028 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #1028 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1028 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1028 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) == 2) and ("cond" not in _coconut_match_kwargs):  #1028 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) >= 1):  #1028 (line in Coconut source)
                _coconut_match_temp_31 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1028 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_args[1][0]  #1028 (line in Coconut source)
                _coconut_match_set_name_cond = _coconut_match_temp_31  #1028 (line in Coconut source)
                _coconut_match_temp_32 = _coconut.list(_coconut_match_args[1][1:])  #1028 (line in Coconut source)
                _coconut_match_set_name_xs = _coconut_match_temp_32  #1028 (line in Coconut source)
                if not _coconut_match_kwargs:  #1028 (line in Coconut source)
                    _coconut_match_check_20 = True  #1028 (line in Coconut source)
        if _coconut_match_check_20:  #1028 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1028 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1028 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #1028 (line in Coconut source)
                x = _coconut_match_set_name_x  #1028 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1028 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1028 (line in Coconut source)
        if _coconut_match_check_20 and not (cond(x)):  #1028 (line in Coconut source)
            _coconut_match_check_20 = False  #1028 (line in Coconut source)
        if not _coconut_match_check_20:  #1028 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, [x] + xs if cond(x)) =', _coconut_match_args)  #1028 (line in Coconut source)

        ys, zs = span(cond, xs)  #1029 (line in Coconut source)
        return (([x,] + ys, zs))  #1030 (line in Coconut source)

    @_coconut_addpattern(span)  #1031 (line in Coconut source)
    @_coconut_mark_as_match  #1031 (line in Coconut source)
    def span(*_coconut_match_args, **_coconut_match_kwargs):  #1031 (line in Coconut source)
        _coconut_match_check_21 = False  #1031 (line in Coconut source)
        _coconut_match_set_name_cond = _coconut_sentinel  #1031 (line in Coconut source)
        _coconut_match_set_name_xs = _coconut_sentinel  #1031 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #1031 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "cond" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "xs" in _coconut_match_kwargs)) == 1):  #1031 (line in Coconut source)
            _coconut_match_temp_33 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("cond")  #1031 (line in Coconut source)
            _coconut_match_temp_34 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("xs")  #1031 (line in Coconut source)
            _coconut_match_set_name_cond = _coconut_match_temp_33  #1031 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_34  #1031 (line in Coconut source)
            if not _coconut_match_kwargs:  #1031 (line in Coconut source)
                _coconut_match_check_21 = True  #1031 (line in Coconut source)
        if _coconut_match_check_21:  #1031 (line in Coconut source)
            if _coconut_match_set_name_cond is not _coconut_sentinel:  #1031 (line in Coconut source)
                cond = _coconut_match_set_name_cond  #1031 (line in Coconut source)
            if _coconut_match_set_name_xs is not _coconut_sentinel:  #1031 (line in Coconut source)
                xs = _coconut_match_set_name_xs  #1031 (line in Coconut source)
        if not _coconut_match_check_21:  #1031 (line in Coconut source)
            raise _coconut_FunctionMatchError('addpattern def span(cond, xs) =', _coconut_match_args)  #1031 (line in Coconut source)

        return (([], xs))  #1032 (line in Coconut source)


@_coconut_tco  #1034 (line in Coconut source)
def break_(cond: _coconut.typing.Callable[[Ta], bool], xs: _coconut.typing.Sequence[Ta]) -> _coconut.typing.Sequence[Ta]:  #1034 (line in Coconut source)
    """
    break_ = break
    """  #1037 (line in Coconut source)
    return _coconut_tail_call(span, _coconut_forward_compose(cond, (_coconut.operator.not_)), xs)  # type: ignore  #1038 (line in Coconut source)



## Searching lists:

def notElem(e: Ta, xs: _coconut.typing.Sequence[Ta]) -> bool:  #1043 (line in Coconut source)
    return (e not in xs)  #1044 (line in Coconut source)


def lookup(key: Ta, assocs: _coconut.typing.Iterable[T.Tuple[Ta, Tb]]) -> Maybe:  #1046 (line in Coconut source)
    try:  #1047 (line in Coconut source)
        return (((Just)((_coconut_iter_getitem((dropwhile)(lambda pair: pair[0] != key, assocs), (0)))[1])))  #1048 (line in Coconut source)
    except IndexError:  #1055 (line in Coconut source)
        return (nothing)  #1056 (line in Coconut source)



## Zipping and unzipping lists:
# type: ignore
zip: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]  # type: ignore  #1061 (line in Coconut source)
zip = _zip  # type: ignore  #1062 (line in Coconut source)

zip3: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]  #1064 (line in Coconut source)
zip3 = _zip  #1065 (line in Coconut source)

@_coconut_tco  #1067 (line in Coconut source)
def zipWith(func: _coconut.typing.Callable[[Ta, Tb], Tc], xs1: _coconut.typing.Iterable[Ta], xs2: _coconut.typing.Iterable[Tb]) -> _coconut.typing.Iterable[Tc]:  #1067 (line in Coconut source)
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))  #1068 (line in Coconut source)


@_coconut_tco  #1070 (line in Coconut source)
def zipWith3(func: _coconut.typing.Callable[[Ta, Tb, Tc], Td], xs1: _coconut.typing.Iterable[Ta], xs2: _coconut.typing.Iterable[Tb], xs3: _coconut.typing.Iterable[Tc]) -> _coconut.typing.Iterable[Td]:  #1070 (line in Coconut source)
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))  #1071 (line in Coconut source)


@_coconut_tco  #1073 (line in Coconut source)
def unzip(xs: _coconut.typing.Iterable[T.Tuple[Ta, Tb]]) -> T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]:  #1073 (line in Coconut source)
    return _coconut_tail_call((tuple), (_map)(list, _zip(*xs)))  # type: ignore  #1074 (line in Coconut source)


unzip3: _coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]  #1076 (line in Coconut source)
unzip3 = unzip  # type: ignore  #1077 (line in Coconut source)



## Functions on strings:
lines: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1082 (line in Coconut source)
lines = _coconut.operator.methodcaller("splitlines")  #1083 (line in Coconut source)

words: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]  #1085 (line in Coconut source)
words = _coconut.operator.methodcaller("split")  #1086 (line in Coconut source)

@_coconut_tco  #1088 (line in Coconut source)
def unlines(strs: _coconut.typing.Iterable[str]) -> str:  #1088 (line in Coconut source)
    return _coconut_tail_call("".join, (s + "\n" for s in strs))  #1089 (line in Coconut source)


unwords: _coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]  #1091 (line in Coconut source)
unwords = " ".join  #1092 (line in Coconut source)




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str,], str]  #1100 (line in Coconut source)

Show = T.Any  #1102 (line in Coconut source)

showsPrec = NotImplemented  #1104 (line in Coconut source)

show: _coconut.typing.Callable[[Ta], str]  #1106 (line in Coconut source)
show = repr  #1107 (line in Coconut source)

def shows(x: Show) -> ShowS:  #1109 (line in Coconut source)
    return (lambda s: repr(x) + s)  #1110 (line in Coconut source)


def showList(xs: _coconut.typing.Iterable[Show]) -> ShowS:  #1112 (line in Coconut source)
    return (lambda s: repr(list(xs)) + s)  #1113 (line in Coconut source)


def showString(x: str) -> ShowS:  #1115 (line in Coconut source)
    return (lambda s: x + s)  #1116 (line in Coconut source)


showChar: _coconut.typing.Callable[[Char], ShowS]  #1118 (line in Coconut source)
showChar = showString  #1119 (line in Coconut source)

def showParen(parens: bool, showFunc: ShowS) -> ShowS:  #1121 (line in Coconut source)
    return (lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s))  #1122 (line in Coconut source)



## Converting from String:

ReadS = NotImplemented  #1130 (line in Coconut source)

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]  #1132 (line in Coconut source)

readsPrec = NotImplemented  #1143 (line in Coconut source)

readList = NotImplemented  #1145 (line in Coconut source)

reads = NotImplemented  #1147 (line in Coconut source)

readParen = NotImplemented  #1149 (line in Coconut source)

@_coconut_tco  #1151 (line in Coconut source)
def read(s: str) -> Read:  #1151 (line in Coconut source)
    return _coconut_tail_call(_ast.literal_eval, s)  #1152 (line in Coconut source)


lex = NotImplemented  #1154 (line in Coconut source)




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", ('io_func',))):  #1162 (line in Coconut source)
    _coconut_is_data = True  #1162 (line in Coconut source)
    __slots__ = ()  #1162 (line in Coconut source)
    def __add__(self, other): return _coconut.NotImplemented  #1162 (line in Coconut source)
    def __mul__(self, other): return _coconut.NotImplemented  #1162 (line in Coconut source)
    def __rmul__(self, other): return _coconut.NotImplemented  #1162 (line in Coconut source)
    __ne__ = _coconut.object.__ne__  #1162 (line in Coconut source)
    def __eq__(self, other):  #1162 (line in Coconut source)
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #1162 (line in Coconut source)
    def __hash__(self):  #1162 (line in Coconut source)
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #1162 (line in Coconut source)
    __match_args__ = ('io_func',)  #1162 (line in Coconut source)
    @staticmethod  #1163 (line in Coconut source)
    @_coconut_tco  #1164 (line in Coconut source)
    def __pure__(x: Ta) -> IO:  #1164 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: x)  #1165 (line in Coconut source)


    @staticmethod  #1167 (line in Coconut source)
    @_coconut_tco  #1168 (line in Coconut source)
    def __fail__(msg: str) -> IO:  #1168 (line in Coconut source)
        def _coconut_lambda_0():  #1169 (line in Coconut source)
            raise IOError(msg)  #1169 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_lambda_0)  #1169 (line in Coconut source)


    @_coconut_tco  #1171 (line in Coconut source)
    def __fmap__(self, func: _coconut.typing.Callable[[Ta], Tb]) -> IO:  #1171 (line in Coconut source)
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))  #1172 (line in Coconut source)


    @_coconut_tco  #1174 (line in Coconut source)
    def __join__(self) -> IO:  #1174 (line in Coconut source)
        return _coconut_tail_call(fmap, unIO, self)  # type: ignore  #1175 (line in Coconut source)


    @staticmethod  #1177 (line in Coconut source)
    @_coconut_tco  #1178 (line in Coconut source)
    def __mempty__() -> IO:  #1178 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mempty)  #1179 (line in Coconut source)


    @_coconut_tco  #1181 (line in Coconut source)
    def __mappend__(self, other: IO) -> IO:  #1181 (line in Coconut source)
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))  #1182 (line in Coconut source)


_nullIO: IO = IO(lambda: None)  #1184 (line in Coconut source)

@_coconut_tco  #1186 (line in Coconut source)
def asIO(io: IO) -> IO:  #1186 (line in Coconut source)
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """  #1191 (line in Coconut source)
    return _coconut_tail_call((asTypeOf), io, _nullIO)  # type: ignore  #1192 (line in Coconut source)


@_coconut_tco  #1194 (line in Coconut source)
def unIO(io: IO) -> T.Any:  #1194 (line in Coconut source)
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
    """  #1208 (line in Coconut source)
    return _coconut_tail_call(asIO(io).io_func)  #1209 (line in Coconut source)




## Simple I/O operations:

### Output functions:

@_coconut_tco  #1217 (line in Coconut source)
def putStr(s: str) -> IO:  #1217 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))  #1218 (line in Coconut source)


putChar: _coconut.typing.Callable[[Char], IO]  #1220 (line in Coconut source)
putChar = putStr  #1221 (line in Coconut source)

@_coconut_tco  #1223 (line in Coconut source)
def putStrLn(s: str) -> IO:  #1223 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))  #1224 (line in Coconut source)

# type: ignore
@_coconut_tco  # type: ignore  #1226 (line in Coconut source)
def print(x: Ta) -> IO:  # type: ignore  #1226 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))  #1227 (line in Coconut source)


### Input functions:

getChar: IO = IO(_coconut.functools.partial(sys.stdin.read, 1))  #1231 (line in Coconut source)

getLine: IO = IO(input)  #1233 (line in Coconut source)

getContents: IO = IO(sys.stdin.read)  #1235 (line in Coconut source)

@_coconut_tco  #1237 (line in Coconut source)
def interact(func: _coconut.typing.Callable[[str], str]) -> IO:  #1237 (line in Coconut source)
    def do_interact():  #1238 (line in Coconut source)
        while True:  #1239 (line in Coconut source)
            (_print)((func)(input()))  #1240 (line in Coconut source)

    return _coconut_tail_call(IO, do_interact)  #1241 (line in Coconut source)


### Files:

FilePath = str  #1245 (line in Coconut source)

@_coconut_tco  #1247 (line in Coconut source)
def readFile(fpath: FilePath) -> IO:  #1247 (line in Coconut source)
    def do_readFile() -> str:  #1248 (line in Coconut source)
        with open(fpath, "r+") as f:  #1249 (line in Coconut source)
            return (f.read())  #1250 (line in Coconut source)

    return _coconut_tail_call(IO, do_readFile)  #1251 (line in Coconut source)


@_coconut_tco  #1253 (line in Coconut source)
def writeFile(fpath: FilePath, text: str) -> IO:  #1253 (line in Coconut source)
    def do_writeFile() -> None:  #1254 (line in Coconut source)
        with open(fpath, "w+") as f:  #1255 (line in Coconut source)
            f.write(text)  #1256 (line in Coconut source)

    return _coconut_tail_call(IO, do_writeFile)  #1257 (line in Coconut source)


@_coconut_tco  #1259 (line in Coconut source)
def appendFile(fpath: FilePath, text: str) -> IO:  #1259 (line in Coconut source)
    def do_appendFile() -> None:  #1260 (line in Coconut source)
        with open(fpath, "a+") as f:  #1261 (line in Coconut source)
            f.write(text)  #1262 (line in Coconut source)

    return _coconut_tail_call(IO, do_appendFile)  #1263 (line in Coconut source)


@_coconut_tco  #1265 (line in Coconut source)
def readIO(s: str) -> IO:  #1265 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))  #1266 (line in Coconut source)


@_coconut_tco  #1268 (line in Coconut source)
def readLn() -> IO:  #1268 (line in Coconut source)
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore  #1269 (line in Coconut source)



## Exception handling:

@_coconut_tco  #1274 (line in Coconut source)
def ioError(err: IOError) -> IO:  #1274 (line in Coconut source)
    def _coconut_lambda_1():  #1275 (line in Coconut source)
        raise err  #1275 (line in Coconut source)
    return _coconut_tail_call(IO, _coconut_lambda_1)  #1275 (line in Coconut source)


@_coconut_tco  #1277 (line in Coconut source)
def userError(msg: str) -> IOError:  #1277 (line in Coconut source)
    return _coconut_tail_call(IOError, msg)  #1278 (line in Coconut source)
