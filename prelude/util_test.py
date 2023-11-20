#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x94970d1f

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

# Imports:
from prelude import *  # type: ignore  #2 (line in Coconut source)


# Tests:
def test_FunctionApplication():  #6 (line in Coconut source)
    assert (of)((of)((_coconut.operator.add), 1), 2) == 3  #7 (line in Coconut source)
    assert (of)(of(lambda x, y, z: (x, y, z), 1, 2), 3) == (1, 2, 3)  #8 (line in Coconut source)
    assert (of)(of(lambda x, y: (x, y), y=2), 1) == (1, 2)  #9 (line in Coconut source)
    assert curry(_coconut.operator.add)(1)(2) == 3 == uncurry(_coconut_partial(_coconut_partial, (_coconut.operator.add)))(1, 2)  #10 (line in Coconut source)
    assert uncurry(curry(_coconut.operator.truediv))(6, 2) == 3  #11 (line in Coconut source)


def test_definesBind():  #13 (line in Coconut source)
    @definesBind  #14 (line in Coconut source)
    class FunctionMonad(_coconut.collections.namedtuple("FunctionMonad", ('func',))):  #15 (line in Coconut source)
        __slots__ = ()  #15 (line in Coconut source)
        _coconut_is_data = True  #15 (line in Coconut source)
        __match_args__ = ('func',)  #15 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #15 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #15 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #15 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #15 (line in Coconut source)
        def __eq__(self, other):  #15 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #15 (line in Coconut source)
        def __hash__(self):  #15 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #15 (line in Coconut source)
        @staticmethod  #16 (line in Coconut source)
        @_coconut_tco  #17 (line in Coconut source)
        def __pure__(x: 'Ta') -> 'FunctionMonad':  #17 (line in Coconut source)
            return _coconut_tail_call(FunctionMonad, lambda e: x)  #18 (line in Coconut source)


        @_coconut_tco  #20 (line in Coconut source)
        def __bind__(x: 'FunctionMonad', f: '_coconut.typing.Callable[[Ta], FunctionMonad]') -> 'FunctionMonad':  #20 (line in Coconut source)
            return _coconut_tail_call(FunctionMonad, lambda r: ((f)((x)(r)))(r))  #21 (line in Coconut source)


        @_coconut_tco  #23 (line in Coconut source)
        @_coconut_mark_as_match  #23 (line in Coconut source)
        def __call__(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #23 (line in Coconut source)
            _coconut_match_check_0 = False  #23 (line in Coconut source)
            _coconut_match_set_name_args = _coconut_sentinel  #23 (line in Coconut source)
            _coconut_match_set_name_kwargs = _coconut_sentinel  #23 (line in Coconut source)
            _coconut_FunctionMatchError = _coconut_get_function_match_error()  #23 (line in Coconut source)
            if _coconut_match_first_arg is not _coconut_sentinel:  #23 (line in Coconut source)
                _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #23 (line in Coconut source)
            if _coconut.len(_coconut_match_args) >= 1:  #23 (line in Coconut source)
                _coconut_match_set_name_args = _coconut_match_args[1:]  #23 (line in Coconut source)
                _coconut_match_temp_0 = _coconut.getattr(FunctionMonad, "_coconut_is_data", False) or _coconut.isinstance(FunctionMonad, _coconut.tuple) and _coconut.all(_coconut.getattr(_coconut_x, "_coconut_is_data", False) for _coconut_x in FunctionMonad)  # type: ignore  #23 (line in Coconut source)
                _coconut_match_set_name_kwargs = _coconut_match_kwargs  #23 (line in Coconut source)
                _coconut_match_check_0 = True  #23 (line in Coconut source)
            if _coconut_match_check_0:  #23 (line in Coconut source)
                _coconut_match_check_0 = False  #23 (line in Coconut source)
                if not _coconut_match_check_0:  #23 (line in Coconut source)
                    _coconut_match_set_name_func = _coconut_sentinel  #23 (line in Coconut source)
                    if (_coconut_match_temp_0) and (_coconut.isinstance(_coconut_match_args[0], FunctionMonad)) and (_coconut.len(_coconut_match_args[0]) >= 1):  #23 (line in Coconut source)
                        _coconut_match_set_name_func = _coconut_match_args[0][0]  #23 (line in Coconut source)
                        _coconut_match_temp_1 = _coconut.len(_coconut_match_args[0]) <= _coconut.max(1, _coconut.len(_coconut_match_args[0].__match_args__)) and _coconut.all(i in _coconut.getattr(_coconut_match_args[0], "_coconut_data_defaults", {}) and _coconut_match_args[0][i] == _coconut.getattr(_coconut_match_args[0], "_coconut_data_defaults", {})[i] for i in _coconut.range(1, _coconut.len(_coconut_match_args[0].__match_args__))) if _coconut.hasattr(_coconut_match_args[0], "__match_args__") else _coconut.len(_coconut_match_args[0]) == 1  # type: ignore  #23 (line in Coconut source)
                        if _coconut_match_temp_1:  #23 (line in Coconut source)
                            _coconut_match_check_0 = True  #23 (line in Coconut source)
                    if _coconut_match_check_0:  #23 (line in Coconut source)
                        if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line in Coconut source)
                            func = _coconut_match_set_name_func  #23 (line in Coconut source)

                if not _coconut_match_check_0:  #23 (line in Coconut source)
                    if (not _coconut_match_temp_0) and (_coconut.isinstance(_coconut_match_args[0], FunctionMonad)):  #23 (line in Coconut source)
                        _coconut_match_check_0 = True  #23 (line in Coconut source)
                    if _coconut_match_check_0:  #23 (line in Coconut source)
                        _coconut_match_check_0 = False  #23 (line in Coconut source)
                        if not _coconut_match_check_0:  #23 (line in Coconut source)
                            _coconut_match_set_name_func = _coconut_sentinel  #23 (line in Coconut source)
                            if _coconut.type(_coconut_match_args[0]) in _coconut_self_match_types:  #23 (line in Coconut source)
                                _coconut_match_set_name_func = _coconut_match_args[0]  #23 (line in Coconut source)
                                _coconut_match_check_0 = True  #23 (line in Coconut source)
                            if _coconut_match_check_0:  #23 (line in Coconut source)
                                if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line in Coconut source)
                                    func = _coconut_match_set_name_func  #23 (line in Coconut source)

                        if not _coconut_match_check_0:  #23 (line in Coconut source)
                            _coconut_match_set_name_func = _coconut_sentinel  #23 (line in Coconut source)
                            if not _coconut.type(_coconut_match_args[0]) in _coconut_self_match_types:  #23 (line in Coconut source)
                                _coconut_match_temp_2 = _coconut.getattr(FunctionMonad, '__match_args__', ())  # type: _coconut.typing.Any  # type: ignore  #23 (line in Coconut source)
                                if not _coconut.isinstance(_coconut_match_temp_2, _coconut.tuple):  #23 (line in Coconut source)
                                    raise _coconut.TypeError("FunctionMonad.__match_args__ must be a tuple")  #23 (line in Coconut source)
                                if _coconut.len(_coconut_match_temp_2) < 1:  #23 (line in Coconut source)
                                    raise _coconut.TypeError("too many positional args in class match (pattern requires 1; 'FunctionMonad' only supports %s)" % (_coconut.len(_coconut_match_temp_2),))  #23 (line in Coconut source)
                                _coconut_match_temp_3 = _coconut.getattr(_coconut_match_args[0], _coconut_match_temp_2[0], _coconut_sentinel)  #23 (line in Coconut source)
                                if _coconut_match_temp_3 is not _coconut_sentinel:  #23 (line in Coconut source)
                                    _coconut_match_set_name_func = _coconut_match_temp_3  #23 (line in Coconut source)
                                    _coconut_match_check_0 = True  #23 (line in Coconut source)
                            if _coconut_match_check_0:  #23 (line in Coconut source)
                                if _coconut_match_set_name_func is not _coconut_sentinel:  #23 (line in Coconut source)
                                    func = _coconut_match_set_name_func  #23 (line in Coconut source)




            if _coconut_match_check_0:  #23 (line in Coconut source)
                if _coconut_match_set_name_args is not _coconut_sentinel:  #23 (line in Coconut source)
                    args = _coconut_match_set_name_args  #23 (line in Coconut source)
                if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #23 (line in Coconut source)
                    kwargs = _coconut_match_set_name_kwargs  #23 (line in Coconut source)
            if not _coconut_match_check_0:  #23 (line in Coconut source)
                raise _coconut_FunctionMatchError('def __call__(FunctionMonad(func), *args, **kwargs) =', _coconut_match_args)  #23 (line in Coconut source)

            return _coconut_tail_call(func, *args, **kwargs)  #24 (line in Coconut source)


    _coconut_call_set_names(FunctionMonad)  #26 (line in Coconut source)
    assert 8 == ((fmap)(_coconut_partial((_coconut.operator.mul), 2), FunctionMonad(_coconut_partial((_coconut.operator.add), 1))))(3)  #26 (line in Coconut source)
    assert 6 == ((join)(FunctionMonad(curry(_coconut.operator.add))))(3)  #27 (line in Coconut source)
