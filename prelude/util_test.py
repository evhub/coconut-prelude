#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3197d1e2

# Compiled with Coconut version 1.5.0-post_dev42 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get("__coconut__")
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules["__coconut__"]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:
from prelude import *  # type: ignore  #2 (line in coconut source)


# Tests:
def test_FunctionApplication():  #6 (line in coconut source)
    assert (of)((of)(_coconut.operator.add, 1), 2) == 3  #7 (line in coconut source)
    assert (of)(of(lambda x, y, z: (x, y, z), 1, 2), 3) == (1, 2, 3)  #8 (line in coconut source)
    assert (of)(of(lambda x, y: (x, y), y=2), 1) == (1, 2)  #9 (line in coconut source)
    assert curry(_coconut.operator.add)(1)(2) == 3 == uncurry(_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.add))(1, 2)  #10 (line in coconut source)
    assert uncurry(curry(_coconut.operator.truediv))(6, 2) == 3  #11 (line in coconut source)

def test_definesBind():  #13 (line in coconut source)
    @definesBind  #14 (line in coconut source)
    class FunctionMonad(_coconut.collections.namedtuple("FunctionMonad", ('func',))):  #14 (line in coconut source)
        __slots__ = ()  #14 (line in coconut source)
        __ne__ = _coconut.object.__ne__  #14 (line in coconut source)
        def __eq__(self, other):  #14 (line in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #14 (line in coconut source)
        def __hash__(self):  #14 (line in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #14 (line in coconut source)
        __match_args__ = ('func',)  #14 (line in coconut source)
        @staticmethod  #14 (line in coconut source)
        @_coconut_tco  #14 (line in coconut source)
        def __pure__(x: 'Ta') -> 'FunctionMonad':  #17 (line in coconut source)
            return _coconut_tail_call(FunctionMonad, lambda e: x)  #18 (line in coconut source)

        @_coconut_tco  #20 (line in coconut source)
        def __bind__(x: 'FunctionMonad', f: '_coconut.typing.Callable[[Ta], FunctionMonad]') -> 'FunctionMonad':  #20 (line in coconut source)
            return _coconut_tail_call(FunctionMonad, lambda r: ((f)((x)(r)))(r))  #21 (line in coconut source)

        @_coconut_tco  #23 (line in coconut source)
        @_coconut_mark_as_match  #23 (line in coconut source)
        def __call__(*_coconut_match_to_args, **_coconut_match_to_kwargs):  #23 (line in coconut source)
            _coconut_match_check = False  #23 (line in coconut source)
            _coconut_FunctionMatchError = _coconut_get_function_match_error()  #23 (line in coconut source)
            if (_coconut.len(_coconut_match_to_args) >= 1) and (_coconut.isinstance(_coconut_match_to_args[0], FunctionMonad)) and (_coconut.len(_coconut_match_to_args[0]) == 1):  #23 (line in coconut source)
                func = _coconut_match_to_args[0][0]  #23 (line in coconut source)
                args = _coconut_match_to_args[1:]  #23 (line in coconut source)
                kwargs = _coconut_match_to_kwargs  #23 (line in coconut source)
                _coconut_match_check = True  #23 (line in coconut source)
            if not _coconut_match_check:  #23 (line in coconut source)
                raise _coconut_FunctionMatchError('def __call__(FunctionMonad(func), *args, **kwargs) =', _coconut_match_to_args)  #23 (line in coconut source)

            return _coconut_tail_call(func, *args, **kwargs)  #24 (line in coconut source)

    assert 8 == ((fmap)(_coconut.functools.partial(_coconut.operator.mul, 2), FunctionMonad(_coconut.functools.partial(_coconut.operator.add, 1))))(3)  #26 (line in coconut source)
    assert 6 == ((join)(FunctionMonad(curry(_coconut.operator.add))))(3)  #27 (line in coconut source)
