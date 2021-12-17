#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8ca42b92

# Compiled with Coconut version 2.0.0-a_dev28 [How Not to Be Seen]

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
from __coconut__ import _coconut_tail_call, _coconut_tco, _namedtuple_of, _coconut, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:
from prelude.typevars import *  # type: ignore  #2 (line num in coconut source)


# Function application:
if TYPE_CHECKING:  #6 (line num in coconut source)
    @T.overload  # type: ignore  #7 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta], Tb]', _x: 'Ta') -> 'Tb':  #8 (line num in coconut source)
        ...  #9 (line num in coconut source)

    @T.overload  #10 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', _x: 'Ta') -> '_coconut.typing.Callable[[Tb], Tc]':  #11 (line num in coconut source)
        ...  #12 (line num in coconut source)

    @T.overload  #13 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta') -> '_coconut.typing.Callable[[Tb, Tc], Td]':  #14 (line num in coconut source)
        ...  #15 (line num in coconut source)

    @T.overload  #16 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[..., Tb]', _x: 'Ta') -> 'T.Any':  #17 (line num in coconut source)
        ...  #18 (line num in coconut source)

    @T.overload  #19 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb], Tc]', _x: 'Ta', _y: 'Tb') -> 'Tc':  #20 (line num in coconut source)
        ...  #21 (line num in coconut source)

    @T.overload  #22 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta', _y: 'Tb') -> '_coconut.typing.Callable[[Tc], Td]':  #23 (line num in coconut source)
        ...  #24 (line num in coconut source)

    @T.overload  #25 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[[Ta, Tb, Tc], Td]', _x: 'Ta', _y: 'Tb', _z: 'Tc') -> 'Td':  #26 (line num in coconut source)
        ...  #27 (line num in coconut source)

    @T.overload  #28 (line num in coconut source)
    def of(func: '_coconut.typing.Callable[..., T.Any]', *args: 'T.Any', **kwargs: 'T.Any') -> 'T.Any':  #29 (line num in coconut source)
        ...  #30 (line num in coconut source)

    def of(func, *args, **kwargs):  #31 (line num in coconut source)
        ...  #32 (line num in coconut source)

else:  #33 (line num in coconut source)
    def of(func, *args, **kwargs):  #34 (line num in coconut source)
        """
        of = ($)
        -- of(func, *args, **kwargs) attempts to call func(*args, **kwargs),
        --  but in case of TypeError curries func$(*args, **kwargs) instead,
        --  as in Haskell function application (see also curry, uncurry)
        """  #40 (line num in coconut source)
        f = _coconut.functools.partial(func, *args, **kwargs)  #41 (line num in coconut source)
        try:  #42 (line num in coconut source)
            return (f())  #43 (line num in coconut source)
        except TypeError:  #44 (line num in coconut source)
            return (f)  #45 (line num in coconut source)


@_coconut_tco  #47 (line num in coconut source)
def curry(func):  #47 (line num in coconut source)
    """
    -- curry a Python-style multi-place function into
    --  a Haskell-style function that returns a function
    --  (see also curry_tuple for functions of tuples)
    """  #52 (line num in coconut source)
    return _coconut_tail_call(_coconut.functools.partial, of, func)  #53 (line num in coconut source)


def uncurry(func):  #55 (line num in coconut source)
    """
    -- uncurry a Haskell-style function that returns a function
    --  into a Python-style multi-place function
    --  (see also uncurry_tuple for functions of tuples)
    """  #60 (line num in coconut source)
    return (lambda *args: reduce(of, args, func))  #61 (line num in coconut source)


# Deriving:

def derivingOrd(*valueConstructors: 'TType') -> 'None':  #65 (line num in coconut source)
    """
    The expression
        derivingOrd(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving Ord
    """  #73 (line num in coconut source)
    if TYPE_CHECKING:  #74 (line num in coconut source)
        return  #74 (line num in coconut source)

    ind = _coconut_forward_compose(type, valueConstructors.index)  #76 (line num in coconut source)
    for valCon in valueConstructors:  #77 (line num in coconut source)

# Ord
        try:  #80 (line num in coconut source)
            _coconut_name_store_0 = __lt__  #80 (line num in coconut source)
        except _coconut.NameError:  #80 (line num in coconut source)
            _coconut_name_store_0 = _coconut_sentinel  #80 (line num in coconut source)
        def __lt__(x, y):  #80 (line num in coconut source)
            return (tuple.__lt__(x, y) if type(x) is type(y) else ind(x) < ind(y))  #81 (line num in coconut source)
        valCon.__lt__ = __lt__  #82 (line num in coconut source)
        if _coconut_name_store_0 is not _coconut_sentinel:  #82 (line num in coconut source)
            __lt__ = _coconut_name_store_0  #82 (line num in coconut source)

        try:  #82 (line num in coconut source)
            _coconut_name_store_1 = __le__  #82 (line num in coconut source)
        except _coconut.NameError:  #82 (line num in coconut source)
            _coconut_name_store_1 = _coconut_sentinel  #82 (line num in coconut source)
        def __le__(x, y):  #82 (line num in coconut source)
            return (tuple.__le__(x, y) if type(x) is type(y) else ind(x) <= ind(y))  #83 (line num in coconut source)
        valCon.__le__ = __le__  #84 (line num in coconut source)
        if _coconut_name_store_1 is not _coconut_sentinel:  #84 (line num in coconut source)
            __le__ = _coconut_name_store_1  #84 (line num in coconut source)

        try:  #84 (line num in coconut source)
            _coconut_name_store_2 = __ge__  #84 (line num in coconut source)
        except _coconut.NameError:  #84 (line num in coconut source)
            _coconut_name_store_2 = _coconut_sentinel  #84 (line num in coconut source)
        def __ge__(x, y):  #84 (line num in coconut source)
            return (tuple.__ge__(x, y) if type(x) is type(y) else ind(x) >= ind(y))  #85 (line num in coconut source)
        valCon.__ge__ = __ge__  #86 (line num in coconut source)
        if _coconut_name_store_2 is not _coconut_sentinel:  #86 (line num in coconut source)
            __ge__ = _coconut_name_store_2  #86 (line num in coconut source)

        try:  #86 (line num in coconut source)
            _coconut_name_store_3 = __gt__  #86 (line num in coconut source)
        except _coconut.NameError:  #86 (line num in coconut source)
            _coconut_name_store_3 = _coconut_sentinel  #86 (line num in coconut source)
        def __gt__(x, y):  #86 (line num in coconut source)
            return (tuple.__gt__(x, y) if type(x) is type(y) else ind(x) > ind(y))  #87 (line num in coconut source)

        valCon.__gt__ = __gt__  #89 (line num in coconut source)
        if _coconut_name_store_3 is not _coconut_sentinel:  #89 (line num in coconut source)
            __gt__ = _coconut_name_store_3  #89 (line num in coconut source)


def derivingBoundedEnum(*valueConstructors: 'TType') -> 'None':  #89 (line num in coconut source)
    """
    The expression
        derivingBoundedEnum(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Bounded, Enum)
    """  #97 (line num in coconut source)
    if TYPE_CHECKING:  #98 (line num in coconut source)
        return  #98 (line num in coconut source)

    ind = _coconut_forward_compose(type, valueConstructors.index)  #100 (line num in coconut source)
    for valCon in valueConstructors:  #101 (line num in coconut source)

# Bounded
        try:  #104 (line num in coconut source)
            _coconut_name_store_4 = __minBound__  #104 (line num in coconut source)
        except _coconut.NameError:  #104 (line num in coconut source)
            _coconut_name_store_4 = _coconut_sentinel  #104 (line num in coconut source)
        @_coconut_tco  #104 (line num in coconut source)
        def __minBound__(self):  #104 (line num in coconut source)
            return _coconut_tail_call(valueConstructors[0])  #105 (line num in coconut source)
        valCon.__minBound__ = __minBound__  #106 (line num in coconut source)
        if _coconut_name_store_4 is not _coconut_sentinel:  #106 (line num in coconut source)
            __minBound__ = _coconut_name_store_4  #106 (line num in coconut source)

        try:  #106 (line num in coconut source)
            _coconut_name_store_5 = __maxBound__  #106 (line num in coconut source)
        except _coconut.NameError:  #106 (line num in coconut source)
            _coconut_name_store_5 = _coconut_sentinel  #106 (line num in coconut source)
        @_coconut_tco  #106 (line num in coconut source)
        def __maxBound__(self):  #106 (line num in coconut source)
            return _coconut_tail_call(valueConstructors[-1])  #107 (line num in coconut source)

# Enum
        valCon.__maxBound__ = __maxBound__  #110 (line num in coconut source)
        if _coconut_name_store_5 is not _coconut_sentinel:  #110 (line num in coconut source)
            __maxBound__ = _coconut_name_store_5  #110 (line num in coconut source)

        try:  #110 (line num in coconut source)
            _coconut_name_store_6 = __int__  #110 (line num in coconut source)
        except _coconut.NameError:  #110 (line num in coconut source)
            _coconut_name_store_6 = _coconut_sentinel  #110 (line num in coconut source)
        @_coconut_tco  #110 (line num in coconut source)
        def __int__(x):  #110 (line num in coconut source)
            return _coconut_tail_call(ind, x)  #110 (line num in coconut source)
        valCon.__int__ = __int__  #111 (line num in coconut source)
        if _coconut_name_store_6 is not _coconut_sentinel:  #111 (line num in coconut source)
            __int__ = _coconut_name_store_6  #111 (line num in coconut source)

        try:  #111 (line num in coconut source)
            _coconut_name_store_7 = __add__  #111 (line num in coconut source)
        except _coconut.NameError:  #111 (line num in coconut source)
            _coconut_name_store_7 = _coconut_sentinel  #111 (line num in coconut source)
        def __add__(x, y):  #111 (line num in coconut source)
            return (valueConstructors[ind(x) + y]() if isinstance(y, int) else tuple.__add__(x, y))  #112 (line num in coconut source)
        valCon.__add__ = __add__  #113 (line num in coconut source)
        if _coconut_name_store_7 is not _coconut_sentinel:  #113 (line num in coconut source)
            __add__ = _coconut_name_store_7  #113 (line num in coconut source)

        try:  #113 (line num in coconut source)
            _coconut_name_store_8 = __radd__  #113 (line num in coconut source)
        except _coconut.NameError:  #113 (line num in coconut source)
            _coconut_name_store_8 = _coconut_sentinel  #113 (line num in coconut source)
        def __radd__(x, y):  #113 (line num in coconut source)
            return (x + y)  #113 (line num in coconut source)
        valCon.__radd__ = __radd__  #114 (line num in coconut source)
        if _coconut_name_store_8 is not _coconut_sentinel:  #114 (line num in coconut source)
            __radd__ = _coconut_name_store_8  #114 (line num in coconut source)

        try:  #114 (line num in coconut source)
            _coconut_name_store_9 = __sub__  #114 (line num in coconut source)
        except _coconut.NameError:  #114 (line num in coconut source)
            _coconut_name_store_9 = _coconut_sentinel  #114 (line num in coconut source)
        def __sub__(x, y):  #114 (line num in coconut source)
            return (valueConstructors[ind(x) - y]() if isinstance(y, int) else tuple.__sub__(x, y))  #115 (line num in coconut source)


# Monads:
        valCon.__sub__ = __sub__  #119 (line num in coconut source)
        if _coconut_name_store_9 is not _coconut_sentinel:  #119 (line num in coconut source)
            __sub__ = _coconut_name_store_9  #119 (line num in coconut source)


def definesBind(dataType: 'TType') -> 'TType':  #119 (line num in coconut source)
    """
    Decorator to declare that a data type defines __bind__
    instead of __join__. Will also create an __fmap__ method
    if none exists, though then a __pure__ method is required.
    """  #124 (line num in coconut source)
    if TYPE_CHECKING:  #125 (line num in coconut source)
        return (dataType)  #125 (line num in coconut source)

    if not (hasattr)(dataType, "__fmap__"):  #127 (line num in coconut source)
        if not (hasattr)(dataType, "__pure__"):  #128 (line num in coconut source)
            raise TypeError("data types which define __bind__ must define either __fmap__ or __pure__")  #129 (line num in coconut source)
        try:  #130 (line num in coconut source)
            _coconut_name_store_10 = __fmap__  #130 (line num in coconut source)
        except _coconut.NameError:  #130 (line num in coconut source)
            _coconut_name_store_10 = _coconut_sentinel  #130 (line num in coconut source)
        @_coconut_tco  #130 (line num in coconut source)
        def __fmap__(self, func):  #130 (line num in coconut source)
            return _coconut_tail_call(self.__bind__, lambda x: dataType.__pure__(func(x)))  #131 (line num in coconut source)

        dataType.__fmap__ = __fmap__  #133 (line num in coconut source)
        if _coconut_name_store_10 is not _coconut_sentinel:  #133 (line num in coconut source)
            __fmap__ = _coconut_name_store_10  #133 (line num in coconut source)

    if (hasattr)(dataType, "__join__"):  #133 (line num in coconut source)
        raise TypeError("data types which define __bind__ cannot define __join__")  #134 (line num in coconut source)
    try:  #135 (line num in coconut source)
        _coconut_name_store_11 = __join__  #135 (line num in coconut source)
    except _coconut.NameError:  #135 (line num in coconut source)
        _coconut_name_store_11 = _coconut_sentinel  #135 (line num in coconut source)
    @_coconut_tco  #135 (line num in coconut source)
    def __join__(self):  #135 (line num in coconut source)
        return _coconut_tail_call(self.__bind__, lambda x: x)  #136 (line num in coconut source)

    dataType.__join__ = __join__  #138 (line num in coconut source)
    if _coconut_name_store_11 is not _coconut_sentinel:  #138 (line num in coconut source)
        __join__ = _coconut_name_store_11  #138 (line num in coconut source)

    return (dataType)  #138 (line num in coconut source)


def definesReturn(dataType: 'TType') -> 'TType':  #140 (line num in coconut source)
    """
    A simple decorator to set __pure__ equal to __return__.
    If used with definesBind, definesReturn must be applied
    first (i.e. be a more inner decorator).
    """  #145 (line num in coconut source)
    if (hasattr)(dataType, "__pure__"):  #146 (line num in coconut source)
        raise TypeError("data types which define __return__ cannot define __pure__")  #147 (line num in coconut source)
    dataType.__pure__ = dataType.__return__  #148 (line num in coconut source)
    return (dataType)  #149 (line num in coconut source)
