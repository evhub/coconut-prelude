#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x417f2f6d

# Compiled with Coconut version 1.3.1-post_dev26 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

# Imports:
from prelude import *  # type: ignore


# Tests:
@_coconut_tco
def test_definesBind():
    @definesBind
    class FunctionMonad(_coconut.collections.namedtuple("FunctionMonad", "func"), _coconut.object):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        @staticmethod
        @_coconut_tco
        def __pure__(x  # type: Ta
    ):
# type: (...) -> FunctionMonad
            return _coconut_tail_call(_coconut_tail_call, FunctionMonad, lambda e: x)

        @_coconut_tco
        def __bind__(x,  # type: FunctionMonad
     f  # type: _coconut.typing.Callable[[Ta], FunctionMonad]
    ):
# type: (...) -> FunctionMonad
            return _coconut_tail_call(_coconut_tail_call, FunctionMonad, lambda r: ((f)((x)(r)))(r))

        @_coconut_tco
        def __call__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
            _coconut_match_check = False
            if (_coconut.len(_coconut_match_to_args) >= 1) and (_coconut.isinstance(_coconut_match_to_args[0], FunctionMonad)) and (_coconut.len(_coconut_match_to_args[0]) == 1):
                func = _coconut_match_to_args[0][0]
                args = _coconut_match_to_args[1:]
                kwargs = _coconut_match_to_kwargs
                _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def __call__(FunctionMonad(func), *args, **kwargs) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
                _coconut_match_err.pattern = 'def __call__(FunctionMonad(func), *args, **kwargs) ='
                _coconut_match_err.value = _coconut_match_to_args
                raise _coconut_match_err

            return _coconut_tail_call(func, *args, **kwargs)

    assert 8 == (fmap(_coconut.functools.partial(_coconut.operator.mul, 2), FunctionMonad(_coconut.functools.partial(_coconut.operator.add, 1))))(3)
    assert 6 == ((join)(FunctionMonad(curry(_coconut.operator.add))))(3)
