#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2a7e8320

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

# Imports:
from prelude import *  # type: ignore  #2 (line num in coconut source)


# Tests:
def test_FunctionApplication():  #6 (line num in coconut source)
    assert (of)((of)(_coconut.operator.add, 1), 2) == 3  #7 (line num in coconut source)
    assert (of)(of(lambda x, y, z: (x, y, z), 1, 2), 3) == (1, 2, 3)  #8 (line num in coconut source)
    assert (of)(of(lambda x, y: (x, y), y=2), 1) == (1, 2)  #9 (line num in coconut source)
    assert curry(_coconut.operator.add)(1)(2) == 3 == uncurry(_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.add))(1, 2)  #10 (line num in coconut source)
    assert uncurry(curry(_coconut.operator.truediv))(6, 2) == 3  #11 (line num in coconut source)

def test_definesBind():  #13 (line num in coconut source)
    @definesBind  #14 (line num in coconut source)
    class FunctionMonad(_coconut.collections.namedtuple("FunctionMonad", ('func',))):  #14 (line num in coconut source)
        _coconut_is_data = True  #14 (line num in coconut source)
        __slots__ = ()  #14 (line num in coconut source)
        __ne__ = _coconut.object.__ne__  #14 (line num in coconut source)
        def __eq__(self, other):  #14 (line num in coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #14 (line num in coconut source)
        def __hash__(self):  #14 (line num in coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #14 (line num in coconut source)
        __match_args__ = ('func',)  #14 (line num in coconut source)
        @staticmethod  #14 (line num in coconut source)
        @_coconut_tco  #14 (line num in coconut source)
        def __pure__(x: 'Ta') -> 'FunctionMonad':  #17 (line num in coconut source)
            return _coconut_tail_call(FunctionMonad, lambda e: x)  #18 (line num in coconut source)

        @_coconut_tco  #20 (line num in coconut source)
        def __bind__(x: 'FunctionMonad', f: '_coconut.typing.Callable[[Ta], FunctionMonad]') -> 'FunctionMonad':  #20 (line num in coconut source)
            return _coconut_tail_call(FunctionMonad, lambda r: ((f)((x)(r)))(r))  #21 (line num in coconut source)

        @_coconut_tco  #23 (line num in coconut source)
        @_coconut_mark_as_match  #23 (line num in coconut source)
        def __call__(*_coconut_match_args, **_coconut_match_kwargs):  #23 (line num in coconut source)
            _coconut_match_check_0 = False  #23 (line num in coconut source)
            _coconut_match_set_name_args = _coconut_sentinel  #23 (line num in coconut source)
            _coconut_match_set_name_kwargs = _coconut_sentinel  #23 (line num in coconut source)
            _coconut_FunctionMatchError = _coconut_get_function_match_error()  #23 (line num in coconut source)
            if _coconut.len(_coconut_match_args) >= 1:  #23 (line num in coconut source)
                _coconut_match_temp_0 = _coconut.getattr(FunctionMonad, "_coconut_is_data", False) or _coconut.isinstance(FunctionMonad, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in FunctionMonad)   #type: ignore  #23 (line num in coconut source)
                _coconut_match_set_name_args = _coconut_match_args[1:]  #23 (line num in coconut source)
                _coconut_match_set_name_kwargs = _coconut_match_kwargs  #23 (line num in coconut source)
                _coconut_match_check_0 = True  #23 (line num in coconut source)
            if _coconut_match_check_0:  #23 (line num in coconut source)
                _coconut_match_check_0 = False  #23 (line num in coconut source)
                if not _coconut_match_check_0:  #23 (line num in coconut source)
                    _coconut_match_set_name_func = _coconut_sentinel  #23 (line num in coconut source)
                    if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_match_args[0], FunctionMonad)) and (_coconut.len(_coconut_match_args[0]) == 1):  #23 (line num in coconut source)
                        _coconut_match_set_name_func = _coconut_match_args[0][0]  #23 (line num in coconut source)
                        _coconut_match_check_0 = True  #23 (line num in coconut source)
                    if _coconut_match_check_0:  #23 (line num in coconut source)
                        if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line num in coconut source)
                            func = _coconut_match_args[0][0]  #23 (line num in coconut source)

                if not _coconut_match_check_0:  #23 (line num in coconut source)
                    if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_match_args[0], FunctionMonad)):  #23 (line num in coconut source)
                        _coconut_match_check_0 = True  #23 (line num in coconut source)
                    if _coconut_match_check_0:  #23 (line num in coconut source)
                        _coconut_match_check_0 = False  #23 (line num in coconut source)
                        if not _coconut_match_check_0:  #23 (line num in coconut source)
                            _coconut_match_set_name_func = _coconut_sentinel  #23 (line num in coconut source)
                            if _coconut.isinstance(_coconut_match_args[0], _coconut_self_match_types):  #23 (line num in coconut source)
                                _coconut_match_set_name_func = _coconut_match_args[0]  #23 (line num in coconut source)
                                _coconut_match_check_0 = True  #23 (line num in coconut source)
                            if _coconut_match_check_0:  #23 (line num in coconut source)
                                if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line num in coconut source)
                                    func = _coconut_match_args[0]  #23 (line num in coconut source)

                        if not _coconut_match_check_0:  #23 (line num in coconut source)
                            _coconut_match_set_name_func = _coconut_sentinel  #23 (line num in coconut source)
                            if not _coconut.isinstance(_coconut_match_args[0], _coconut_self_match_types):  #23 (line num in coconut source)
                                _coconut_match_temp_1 = _coconut.getattr(FunctionMonad, '__match_args__', ())  #23 (line num in coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_1, _coconut.tuple):  #23 (line num in coconut source)
                                    raise _coconut.TypeError("FunctionMonad.__match_args__ must be a tuple")  #23 (line num in coconut source)
                                if _coconut.len(_coconut_match_temp_1) < 1:  #23 (line num in coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'FunctionMonad' only supports %s)" % (_coconut.len(_coconut_match_temp_1),))  #23 (line num in coconut source)
                                _coconut_match_temp_2 = _coconut.getattr(_coconut_match_args[0], _coconut_match_temp_1[0], _coconut_sentinel)  #23 (line num in coconut source)
                                if _coconut_match_temp_2 is not _coconut_sentinel:  #23 (line num in coconut source)
                                    _coconut_match_set_name_func = _coconut_match_temp_2  #23 (line num in coconut source)
                                    _coconut_match_check_0 = True  #23 (line num in coconut source)
                            if _coconut_match_check_0:  #23 (line num in coconut source)
                                if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line num in coconut source)
                                    func = _coconut_match_temp_2  #23 (line num in coconut source)


            if _coconut_match_check_0:  #23 (line num in coconut source)
                if _coconut_match_set_name_args is not _coconut_sentinel:  #23 (line num in coconut source)
                    args = _coconut_match_args[1:]  #23 (line num in coconut source)
                if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #23 (line num in coconut source)
                    kwargs = _coconut_match_kwargs  #23 (line num in coconut source)
            if not _coconut_match_check_0:  #23 (line num in coconut source)
                raise _coconut_FunctionMatchError('def __call__(FunctionMonad(func), *args, **kwargs) =', _coconut_match_args)  #23 (line num in coconut source)

            return _coconut_tail_call(func, *args, **kwargs)  #24 (line num in coconut source)

    assert 8 == ((fmap)(_coconut.functools.partial(_coconut.operator.mul, 2), FunctionMonad(_coconut.functools.partial(_coconut.operator.add, 1))))(3)  #26 (line num in coconut source)
    assert 6 == ((join)(FunctionMonad(curry(_coconut.operator.add))))(3)  #27 (line num in coconut source)
