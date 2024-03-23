#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1c35abcb

# Compiled with Coconut version 3.1.0-post_dev7

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.0-post_dev7', '35', True)
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
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op
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
from prelude.typevars import *  # type: ignore  #2 (line in Coconut source)


# Function application:
if _coconut.typing.TYPE_CHECKING:  # type: ignore  #6 (line in Coconut source)
    @_coconut.typing.overload  # type: ignore  #6 (line in Coconut source)
    @_coconut_mark_as_match  # type: ignore  #6 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta], Tb]', _x: 'Ta') -> 'Tb':  # type: ignore  #6 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', _x: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[..., Tb]', _x: 'Ta') -> 'T.Any':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', _x: 'Ta', _y: 'Tb') -> 'Tc':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta', _y: 'Tb') -> '_coconut.typing.Callable[[Tc], Td]':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta', _y: 'Tb', _z: 'Tc') -> 'Td':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut.typing.overload  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(func: '_coconut.typing.Callable[..., T.Any]', *args: 'T.Any', **kwargs: 'T.Any') -> 'T.Any':  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(*_coconut_args, **_coconut_kwargs):  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        return _coconut.typing.cast(_coconut.typing.Any, ...)  #13 (line in Coconut source)
else:  #13 (line in Coconut source)
    @_coconut_mark_as_match  #13 (line in Coconut source)
    def of(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #13 (line in Coconut source)
        """
    of = ($)
    -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
    --  but in case of TypeError curries func$(*args, **kwargs) instead,
    --  as in Haskell function application (see also curry, uncurry)
    """  #12 (line in Coconut source)

        _coconut_match_check_0 = False  #13 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #13 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #13 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #13 (line in Coconut source)
        _coconut_match_kwargs_store = _coconut_match_kwargs  #13 (line in Coconut source)
        if not _coconut_match_check_0:  #13 (line in Coconut source)
            _coconut_match_kwargs = _coconut_match_kwargs_store.copy()  #13 (line in Coconut source)
            _coconut_match_set_name_func = _coconut_sentinel  #13 (line in Coconut source)
            _coconut_match_set_name_args = _coconut_sentinel  #13 (line in Coconut source)
            _coconut_match_set_name_kwargs = _coconut_sentinel  #13 (line in Coconut source)
            if _coconut.sum((_coconut.len(_coconut_match_args) > 0, "func" in _coconut_match_kwargs)) == 1:  #13 (line in Coconut source)
                _coconut_match_set_name_args = _coconut_match_args[1:]  #13 (line in Coconut source)
                _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("func")  #13 (line in Coconut source)
                _coconut_match_set_name_func = _coconut_match_temp_0  #13 (line in Coconut source)
                _coconut_match_set_name_kwargs = _coconut_match_kwargs  #13 (line in Coconut source)
                _coconut_match_check_0 = True  #13 (line in Coconut source)
            if _coconut_match_check_0:  #13 (line in Coconut source)
                if _coconut_match_set_name_func is not _coconut_sentinel:  #13 (line in Coconut source)
                    func = _coconut_match_set_name_func  #13 (line in Coconut source)
                if _coconut_match_set_name_args is not _coconut_sentinel:  #13 (line in Coconut source)
                    args = _coconut_match_set_name_args  #13 (line in Coconut source)
                if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #13 (line in Coconut source)
                    kwargs = _coconut_match_set_name_kwargs  #13 (line in Coconut source)

            if _coconut_match_check_0:  #13 (line in Coconut source)

                    f = _coconut_partial(func, *args, **kwargs)  #22 (line in Coconut source)
                    try:  #23 (line in Coconut source)
                        return (f())  #24 (line in Coconut source)
                    except (TypeError, MatchError):  #25 (line in Coconut source)
                        return (f)  #26 (line in Coconut source)


        if not _coconut_match_check_0:  #28 (line in Coconut source)
            raise _coconut_FunctionMatchError('case def of:  # type: ignore', _coconut_match_args)  #28 (line in Coconut source)


@_coconut_tco  #28 (line in Coconut source)
def curry(func):  #28 (line in Coconut source)
    """
    -- curry a Python-style multi-place function into
    --  a Haskell-style function that returns a function
    --  (see also curry_tuple for functions of tuples)
    """  #33 (line in Coconut source)
    return _coconut_tail_call(_coconut_partial, of, func)  #34 (line in Coconut source)


def uncurry(func):  #36 (line in Coconut source)
    """
    -- uncurry a Haskell-style function that returns a function
    --  into a Python-style multi-place function
    --  (see also uncurry_tuple for functions of tuples)
    """  #41 (line in Coconut source)
    return (lambda *args: reduce(of, args, func))  #42 (line in Coconut source)


# Deriving:

def derivingOrd(*valueConstructors: 'TType') -> 'None':  #46 (line in Coconut source)
    """
    The expression
        derivingOrd(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving Ord
    """  #54 (line in Coconut source)
    if TYPE_CHECKING:  #55 (line in Coconut source)
        return  #55 (line in Coconut source)

    ind = _coconut_forward_compose(type, valueConstructors.index)  #57 (line in Coconut source)
    for valCon in (valueConstructors):  #58 (line in Coconut source)

# Ord
        def _coconut_dotted___lt___0(x, y):  #61 (line in Coconut source)
            return (tuple.__lt__(x, y) if type(x) is type(y) else ind(x) < ind(y))  #62 (line in Coconut source)

        _coconut_dotted___lt___0.__name__ = _coconut_py_str("__lt__")  #63 (line in Coconut source)
        _coconut_qualname_0 = _coconut.getattr(_coconut_dotted___lt___0, "__qualname__", None)  #63 (line in Coconut source)
        if _coconut_qualname_0 is not None:  #63 (line in Coconut source)
            _coconut_dotted___lt___0.__qualname__ = _coconut_py_str("valCon.__lt__" if "." not in _coconut_qualname_0 else _coconut_qualname_0.rsplit(".", 1)[0] + ".valCon.__lt__")  #63 (line in Coconut source)
        valCon.__lt__ = _coconut_dotted___lt___0  #63 (line in Coconut source)

        def _coconut_dotted___le___0(x, y):  #63 (line in Coconut source)
            return (tuple.__le__(x, y) if type(x) is type(y) else ind(x) <= ind(y))  #64 (line in Coconut source)

        _coconut_dotted___le___0.__name__ = _coconut_py_str("__le__")  #65 (line in Coconut source)
        _coconut_qualname_1 = _coconut.getattr(_coconut_dotted___le___0, "__qualname__", None)  #65 (line in Coconut source)
        if _coconut_qualname_1 is not None:  #65 (line in Coconut source)
            _coconut_dotted___le___0.__qualname__ = _coconut_py_str("valCon.__le__" if "." not in _coconut_qualname_1 else _coconut_qualname_1.rsplit(".", 1)[0] + ".valCon.__le__")  #65 (line in Coconut source)
        valCon.__le__ = _coconut_dotted___le___0  #65 (line in Coconut source)

        def _coconut_dotted___ge___0(x, y):  #65 (line in Coconut source)
            return (tuple.__ge__(x, y) if type(x) is type(y) else ind(x) >= ind(y))  #66 (line in Coconut source)

        _coconut_dotted___ge___0.__name__ = _coconut_py_str("__ge__")  #67 (line in Coconut source)
        _coconut_qualname_2 = _coconut.getattr(_coconut_dotted___ge___0, "__qualname__", None)  #67 (line in Coconut source)
        if _coconut_qualname_2 is not None:  #67 (line in Coconut source)
            _coconut_dotted___ge___0.__qualname__ = _coconut_py_str("valCon.__ge__" if "." not in _coconut_qualname_2 else _coconut_qualname_2.rsplit(".", 1)[0] + ".valCon.__ge__")  #67 (line in Coconut source)
        valCon.__ge__ = _coconut_dotted___ge___0  #67 (line in Coconut source)

        def _coconut_dotted___gt___0(x, y):  #67 (line in Coconut source)
            return (tuple.__gt__(x, y) if type(x) is type(y) else ind(x) > ind(y))  #68 (line in Coconut source)


        _coconut_dotted___gt___0.__name__ = _coconut_py_str("__gt__")  #70 (line in Coconut source)
        _coconut_qualname_3 = _coconut.getattr(_coconut_dotted___gt___0, "__qualname__", None)  #70 (line in Coconut source)
        if _coconut_qualname_3 is not None:  #70 (line in Coconut source)
            _coconut_dotted___gt___0.__qualname__ = _coconut_py_str("valCon.__gt__" if "." not in _coconut_qualname_3 else _coconut_qualname_3.rsplit(".", 1)[0] + ".valCon.__gt__")  #70 (line in Coconut source)
        valCon.__gt__ = _coconut_dotted___gt___0  #70 (line in Coconut source)


def derivingBoundedEnum(*valueConstructors: 'TType') -> 'None':  #70 (line in Coconut source)
    """
    The expression
        derivingBoundedEnum(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Bounded, Enum)
    """  #78 (line in Coconut source)
    if TYPE_CHECKING:  #79 (line in Coconut source)
        return  #79 (line in Coconut source)

    ind = _coconut_forward_compose(type, valueConstructors.index)  #81 (line in Coconut source)
    for valCon in (valueConstructors):  #82 (line in Coconut source)

# Bounded
        def _coconut_dotted___minBound___0(self):  #85 (line in Coconut source)
            return _coconut_tail_call(valueConstructors[0])  #86 (line in Coconut source)

        _coconut_dotted___minBound___0.__name__ = _coconut_py_str("__minBound__")  #87 (line in Coconut source)
        _coconut_qualname_4 = _coconut.getattr(_coconut_dotted___minBound___0, "__qualname__", None)  #87 (line in Coconut source)
        if _coconut_qualname_4 is not None:  #87 (line in Coconut source)
            _coconut_dotted___minBound___0.__qualname__ = _coconut_py_str("valCon.__minBound__" if "." not in _coconut_qualname_4 else _coconut_qualname_4.rsplit(".", 1)[0] + ".valCon.__minBound__")  #87 (line in Coconut source)
        valCon.__minBound__ = (_coconut_tco)(_coconut_dotted___minBound___0)  #87 (line in Coconut source)

        def _coconut_dotted___maxBound___0(self):  #87 (line in Coconut source)
            return _coconut_tail_call(valueConstructors[-1])  #88 (line in Coconut source)

# Enum

        _coconut_dotted___maxBound___0.__name__ = _coconut_py_str("__maxBound__")  #91 (line in Coconut source)
        _coconut_qualname_5 = _coconut.getattr(_coconut_dotted___maxBound___0, "__qualname__", None)  #91 (line in Coconut source)
        if _coconut_qualname_5 is not None:  #91 (line in Coconut source)
            _coconut_dotted___maxBound___0.__qualname__ = _coconut_py_str("valCon.__maxBound__" if "." not in _coconut_qualname_5 else _coconut_qualname_5.rsplit(".", 1)[0] + ".valCon.__maxBound__")  #91 (line in Coconut source)
        valCon.__maxBound__ = (_coconut_tco)(_coconut_dotted___maxBound___0)  #91 (line in Coconut source)

        def _coconut_dotted___int___0(x):  #91 (line in Coconut source)
            return _coconut_tail_call(ind, x)  #91 (line in Coconut source)

        _coconut_dotted___int___0.__name__ = _coconut_py_str("__int__")  #92 (line in Coconut source)
        _coconut_qualname_6 = _coconut.getattr(_coconut_dotted___int___0, "__qualname__", None)  #92 (line in Coconut source)
        if _coconut_qualname_6 is not None:  #92 (line in Coconut source)
            _coconut_dotted___int___0.__qualname__ = _coconut_py_str("valCon.__int__" if "." not in _coconut_qualname_6 else _coconut_qualname_6.rsplit(".", 1)[0] + ".valCon.__int__")  #92 (line in Coconut source)
        valCon.__int__ = (_coconut_tco)(_coconut_dotted___int___0)  #92 (line in Coconut source)

        def _coconut_dotted___add___0(x, y):  #92 (line in Coconut source)
            return (valueConstructors[ind(x) + y]() if isinstance(y, int) else tuple.__add__(x, y))  #93 (line in Coconut source)

        _coconut_dotted___add___0.__name__ = _coconut_py_str("__add__")  #94 (line in Coconut source)
        _coconut_qualname_7 = _coconut.getattr(_coconut_dotted___add___0, "__qualname__", None)  #94 (line in Coconut source)
        if _coconut_qualname_7 is not None:  #94 (line in Coconut source)
            _coconut_dotted___add___0.__qualname__ = _coconut_py_str("valCon.__add__" if "." not in _coconut_qualname_7 else _coconut_qualname_7.rsplit(".", 1)[0] + ".valCon.__add__")  #94 (line in Coconut source)
        valCon.__add__ = _coconut_dotted___add___0  #94 (line in Coconut source)

        def _coconut_dotted___radd___0(x, y):  #94 (line in Coconut source)
            return (x + y)  #94 (line in Coconut source)

        _coconut_dotted___radd___0.__name__ = _coconut_py_str("__radd__")  #95 (line in Coconut source)
        _coconut_qualname_8 = _coconut.getattr(_coconut_dotted___radd___0, "__qualname__", None)  #95 (line in Coconut source)
        if _coconut_qualname_8 is not None:  #95 (line in Coconut source)
            _coconut_dotted___radd___0.__qualname__ = _coconut_py_str("valCon.__radd__" if "." not in _coconut_qualname_8 else _coconut_qualname_8.rsplit(".", 1)[0] + ".valCon.__radd__")  #95 (line in Coconut source)
        valCon.__radd__ = _coconut_dotted___radd___0  #95 (line in Coconut source)

        def _coconut_dotted___sub___0(x, y):  #95 (line in Coconut source)
            return (valueConstructors[ind(x) - y]() if isinstance(y, int) else tuple.__sub__(x, y))  #96 (line in Coconut source)


# Monads:

        _coconut_dotted___sub___0.__name__ = _coconut_py_str("__sub__")  #100 (line in Coconut source)
        _coconut_qualname_9 = _coconut.getattr(_coconut_dotted___sub___0, "__qualname__", None)  #100 (line in Coconut source)
        if _coconut_qualname_9 is not None:  #100 (line in Coconut source)
            _coconut_dotted___sub___0.__qualname__ = _coconut_py_str("valCon.__sub__" if "." not in _coconut_qualname_9 else _coconut_qualname_9.rsplit(".", 1)[0] + ".valCon.__sub__")  #100 (line in Coconut source)
        valCon.__sub__ = _coconut_dotted___sub___0  #100 (line in Coconut source)


def definesBind(dataType: 'TType') -> 'TType':  #100 (line in Coconut source)
    """
    Decorator to declare that a data type defines __bind__
    instead of __join__. Will also create an __fmap__ method
    if none exists, though then a __pure__ method is required.
    """  #105 (line in Coconut source)
    if TYPE_CHECKING:  #106 (line in Coconut source)
        return (dataType)  #106 (line in Coconut source)

    if not (hasattr)(dataType, "__fmap__"):  #108 (line in Coconut source)
        if not (hasattr)(dataType, "__pure__"):  #109 (line in Coconut source)
            raise TypeError("data types which define __bind__ must define either __fmap__ or __pure__")  #110 (line in Coconut source)
        def _coconut_dotted___fmap___0(self, func):  #111 (line in Coconut source)
            return _coconut_tail_call(self.__bind__, lambda x: dataType.__pure__(func(x)))  #112 (line in Coconut source)


        _coconut_dotted___fmap___0.__name__ = _coconut_py_str("__fmap__")  #114 (line in Coconut source)
        _coconut_qualname_10 = _coconut.getattr(_coconut_dotted___fmap___0, "__qualname__", None)  #114 (line in Coconut source)
        if _coconut_qualname_10 is not None:  #114 (line in Coconut source)
            _coconut_dotted___fmap___0.__qualname__ = _coconut_py_str("dataType.__fmap__" if "." not in _coconut_qualname_10 else _coconut_qualname_10.rsplit(".", 1)[0] + ".dataType.__fmap__")  #114 (line in Coconut source)
        dataType.__fmap__ = (_coconut_tco)(_coconut_dotted___fmap___0)  #114 (line in Coconut source)

    if (hasattr)(dataType, "__join__"):  #114 (line in Coconut source)
        raise TypeError("data types which define __bind__ cannot define __join__")  #115 (line in Coconut source)
    def _coconut_dotted___join___0(self):  #116 (line in Coconut source)
        return _coconut_tail_call(self.__bind__, lambda x: x)  #117 (line in Coconut source)


    _coconut_dotted___join___0.__name__ = _coconut_py_str("__join__")  #119 (line in Coconut source)
    _coconut_qualname_11 = _coconut.getattr(_coconut_dotted___join___0, "__qualname__", None)  #119 (line in Coconut source)
    if _coconut_qualname_11 is not None:  #119 (line in Coconut source)
        _coconut_dotted___join___0.__qualname__ = _coconut_py_str("dataType.__join__" if "." not in _coconut_qualname_11 else _coconut_qualname_11.rsplit(".", 1)[0] + ".dataType.__join__")  #119 (line in Coconut source)
    dataType.__join__ = (_coconut_tco)(_coconut_dotted___join___0)  #119 (line in Coconut source)

    return (dataType)  #119 (line in Coconut source)


def definesReturn(dataType: 'TType') -> 'TType':  #121 (line in Coconut source)
    """
    A simple decorator to set __pure__ equal to __return__.
    If used with definesBind, definesReturn must be applied
    first (i.e. be a more inner decorator).
    """  #126 (line in Coconut source)
    if (hasattr)(dataType, "__pure__"):  #127 (line in Coconut source)
        raise TypeError("data types which define __return__ cannot define __pure__")  #128 (line in Coconut source)
    dataType.__pure__ = dataType.__return__  #129 (line in Coconut source)
    return (dataType)  #130 (line in Coconut source)
