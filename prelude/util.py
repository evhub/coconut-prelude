#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9ddc6a5b

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
from prelude.typevars import *  # type: ignore


# Deriving:
def derivingOrd(*valueConstructors: 'TType') -> 'None':
    """
    The expression
        derivingOrd(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving Ord
    """
    if TYPE_CHECKING:
        return

    ind = _coconut_forward_compose(type, valueConstructors.index)
    for valCon in valueConstructors:

# Ord
        try:
            _coconut_dotted_func_name_store_0 = __lt__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_0 = _coconut_sentinel
        def __lt__(x, y):
            return tuple.__lt__(x, y) if type(x) is type(y) else ind(x) < ind(y)
        valCon.__lt__ = __lt__
        if _coconut_dotted_func_name_store_0 is not _coconut_sentinel:
            __lt__ = _coconut_dotted_func_name_store_0
        try:
            _coconut_dotted_func_name_store_1 = __le__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_1 = _coconut_sentinel
        def __le__(x, y):
            return tuple.__le__(x, y) if type(x) is type(y) else ind(x) <= ind(y)
        valCon.__le__ = __le__
        if _coconut_dotted_func_name_store_1 is not _coconut_sentinel:
            __le__ = _coconut_dotted_func_name_store_1
        try:
            _coconut_dotted_func_name_store_2 = __ge__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_2 = _coconut_sentinel
        def __ge__(x, y):
            return tuple.__ge__(x, y) if type(x) is type(y) else ind(x) >= ind(y)
        valCon.__ge__ = __ge__
        if _coconut_dotted_func_name_store_2 is not _coconut_sentinel:
            __ge__ = _coconut_dotted_func_name_store_2
        try:
            _coconut_dotted_func_name_store_3 = __gt__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_3 = _coconut_sentinel
        def __gt__(x, y):
            return tuple.__gt__(x, y) if type(x) is type(y) else ind(x) > ind(y)

        valCon.__gt__ = __gt__
        if _coconut_dotted_func_name_store_3 is not _coconut_sentinel:
            __gt__ = _coconut_dotted_func_name_store_3
def derivingBoundedEnum(*valueConstructors: 'TType') -> 'None':
    """
    The expression
        derivingBoundedEnum(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Bounded, Enum)
    """
    if TYPE_CHECKING:
        return

    ind = _coconut_forward_compose(type, valueConstructors.index)
    for valCon in valueConstructors:

# Bounded
        try:
            _coconut_dotted_func_name_store_4 = __minBound__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_4 = _coconut_sentinel
        @_coconut_tco
        def __minBound__(self):
            return _coconut_tail_call(valueConstructors[0])
        valCon.__minBound__ = __minBound__
        if _coconut_dotted_func_name_store_4 is not _coconut_sentinel:
            __minBound__ = _coconut_dotted_func_name_store_4
        try:
            _coconut_dotted_func_name_store_5 = __maxBound__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_5 = _coconut_sentinel
        @_coconut_tco
        def __maxBound__(self):
            return _coconut_tail_call(valueConstructors[-1])

# Enum
        valCon.__maxBound__ = __maxBound__
        if _coconut_dotted_func_name_store_5 is not _coconut_sentinel:
            __maxBound__ = _coconut_dotted_func_name_store_5
        try:
            _coconut_dotted_func_name_store_6 = __int__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_6 = _coconut_sentinel
        @_coconut_tco
        def __int__(x):
            return _coconut_tail_call(ind, x)
        valCon.__int__ = __int__
        if _coconut_dotted_func_name_store_6 is not _coconut_sentinel:
            __int__ = _coconut_dotted_func_name_store_6
        try:
            _coconut_dotted_func_name_store_7 = __add__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_7 = _coconut_sentinel
        def __add__(x, y):
            return valueConstructors[ind(x) + y]() if isinstance(y, int) else tuple.__add__(x, y)
        valCon.__add__ = __add__
        if _coconut_dotted_func_name_store_7 is not _coconut_sentinel:
            __add__ = _coconut_dotted_func_name_store_7
        try:
            _coconut_dotted_func_name_store_8 = __radd__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_8 = _coconut_sentinel
        def __radd__(x, y):
            return x + y
        valCon.__radd__ = __radd__
        if _coconut_dotted_func_name_store_8 is not _coconut_sentinel:
            __radd__ = _coconut_dotted_func_name_store_8
        try:
            _coconut_dotted_func_name_store_9 = __sub__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_9 = _coconut_sentinel
        def __sub__(x, y):
            return valueConstructors[ind(x) - y]() if isinstance(y, int) else tuple.__sub__(x, y)


# Monads:
        valCon.__sub__ = __sub__
        if _coconut_dotted_func_name_store_9 is not _coconut_sentinel:
            __sub__ = _coconut_dotted_func_name_store_9
def definesBind(dataType: 'TType') -> 'TType':
    """
    Decorator to declare that a data type defines __bind__
    instead of __join__. Will also create an __fmap__ method
    if none exists, though then a __pure__ method is required.
    """
    if TYPE_CHECKING:
        return dataType

    if not (hasattr)(dataType, "__fmap__"):
        if not (hasattr)(dataType, "__pure__"):
            raise TypeError("data types which define __bind__ must define either __fmap__ or __pure__")
        try:
            _coconut_dotted_func_name_store_10 = __fmap__
        except _coconut.NameError:
            _coconut_dotted_func_name_store_10 = _coconut_sentinel
        @_coconut_tco
        def __fmap__(self, func):
            return _coconut_tail_call(self.__bind__, lambda x: dataType.__pure__(func(x)))

        dataType.__fmap__ = __fmap__
        if _coconut_dotted_func_name_store_10 is not _coconut_sentinel:
            __fmap__ = _coconut_dotted_func_name_store_10
    if (hasattr)(dataType, "__join__"):
        raise TypeError("data types which define __bind__ cannot define __join__")
    try:
        _coconut_dotted_func_name_store_11 = __join__
    except _coconut.NameError:
        _coconut_dotted_func_name_store_11 = _coconut_sentinel
    @_coconut_tco
    def __join__(self):
        return _coconut_tail_call(self.__bind__, lambda x: x)

    dataType.__join__ = __join__
    if _coconut_dotted_func_name_store_11 is not _coconut_sentinel:
        __join__ = _coconut_dotted_func_name_store_11
    return dataType

def definesReturn(dataType: 'TType') -> 'TType':
    """
    A simple decorator to set __pure__ equal to __return__.
    If used with definesBind, definesReturn must be applied
    first (i.e. be a more inner decorator).
    """
    dataType.__pure__ = dataType.__return__
    return dataType
