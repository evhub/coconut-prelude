#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x857f9e52

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
from .typevars import *  # type: ignore


# Deriving:
def derivingEqOrd(*valueConstructors  # type: TType
    ):
# type: (...) -> None
    """
    The expression
        derivingEqOrd(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Eq, Ord)
    """
    if TYPE_CHECKING:
        return

    ind = _coconut_forward_compose(type, valueConstructors.index)
    for valCon in valueConstructors:
        def __eq__(x, y):
            return type(x) is type(y) and tuple.__eq__(x, y)
        valCon.__eq__ = __eq__
        def __lt__(x, y):
            return tuple.__lt__(x, y) if type(x) is type(y) else ind(x) < ind(y)
        valCon.__lt__ = __lt__
        def __le__(x, y):
            return tuple.__le__(x, y) if type(x) is type(y) else ind(x) <= ind(y)
        valCon.__le__ = __le__
        def __ge__(x, y):
            return tuple.__ge__(x, y) if type(x) is type(y) else ind(x) >= ind(y)
        valCon.__ge__ = __ge__
        def __gt__(x, y):
            return tuple.__gt__(x, y) if type(x) is type(y) else ind(x) > ind(y)

        valCon.__gt__ = __gt__
def derivingEnum(*valueConstructors  # type: TType
    ):
# type: (...) -> None
    """
    The expression
        derivingEnum(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for some data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Enum)
    """
    if TYPE_CHECKING:
        return

    ind = _coconut_forward_compose(type, valueConstructors.index)
    for valCon in valueConstructors:
        @_coconut_tco
        def __int__(x):
            return _coconut_tail_call(ind, x)
        valCon.__int__ = __int__
        def __add__(x, y):
            return valueConstructors[ind(x) + y]() if isinstance(y, int) else tuple.__add__(x, y)
        valCon.__add__ = __add__
        def __radd__(x, y):
            return x + y
        valCon.__radd__ = __radd__
        def __sub__(x, y):
            return valueConstructors[ind(x) - y]() if isinstance(y, int) else tuple.__sub__(x, y)


# Monads:
        valCon.__sub__ = __sub__
def definesBind(dataType  # type: TType
    ):
# type: (...) -> TType
    if TYPE_CHECKING:
        return dataType

    if not (hasattr)(dataType, "__fmap__"):
        if not (hasattr)(dataType, "__pure__"):
            raise TypeError("data types which define __bind__ must define either __fmap__ or __pure__")
        @_coconut_tco
        def __fmap__(self, func):
            return _coconut_tail_call(self.__bind__, lambda x: dataType.__pure__(func(x)))

        dataType.__fmap__ = __fmap__
    if (hasattr)(dataType, "__join__"):
        raise TypeError("data types which define __bind__ cannot define __join__")
    @_coconut_tco
    def __join__(self):
        return _coconut_tail_call(self.__bind__, lambda x: x)

    dataType.__join__ = __join__
    return dataType
