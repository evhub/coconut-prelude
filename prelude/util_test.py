#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x387be82e

# Compiled with Coconut version 1.5.0-post_dev37 [Fish License]

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
from prelude import *  # type: ignore


# Tests:
def test_definesBind():
    @definesBind
    class FunctionMonad(_coconut.collections.namedtuple("FunctionMonad", ('func',))):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
        __match_args__ = ('func',)
        @staticmethod
        @_coconut_tco
        def __pure__(x: 'Ta') -> 'FunctionMonad':
            return _coconut_tail_call(FunctionMonad, lambda e: x)

        @_coconut_tco
        def __bind__(x: 'FunctionMonad', f: '_coconut.typing.Callable[[Ta], FunctionMonad]') -> 'FunctionMonad':
            return _coconut_tail_call(FunctionMonad, lambda r: ((f)((x)(r)))(r))

        @_coconut_tco
        @_coconut_mark_as_match
        def __call__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
            _coconut_match_check = False
            _coconut_FunctionMatchError = _coconut_get_function_match_error()
            if (_coconut.len(_coconut_match_to_args) >= 1) and (_coconut.isinstance(_coconut_match_to_args[0], FunctionMonad)) and (_coconut.len(_coconut_match_to_args[0]) == 1):
                func = _coconut_match_to_args[0][0]
                args = _coconut_match_to_args[1:]
                kwargs = _coconut_match_to_kwargs
                _coconut_match_check = True
            if not _coconut_match_check:
                raise _coconut_FunctionMatchError('def __call__(FunctionMonad(func), *args, **kwargs) =', _coconut_match_to_args)

            return _coconut_tail_call(func, *args, **kwargs)

    assert 8 == ((fmap)(_coconut.functools.partial(_coconut.operator.mul, 2), FunctionMonad(_coconut.functools.partial(_coconut.operator.add, 1))))(3)
    assert 6 == ((join)(FunctionMonad(curry(_coconut.operator.add))))(3)
