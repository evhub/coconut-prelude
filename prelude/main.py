#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xed3763a5

# Compiled with Coconut version 1.4.1-post_dev8 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_tail_call, _coconut_tco, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Helpers:

#### Imports:
sys = _coconut_sys
import fractions as _fractions
import math as _math
import ast as _ast

from prelude.util import *  # type: ignore

#### Untyped built-ins:
_max = max  # type: _coconut.typing.Callable[..., T.Any]
_min = min  # type: _coconut.typing.Callable[..., T.Any]
_zip = zip  # type: _coconut.typing.Callable[..., T.Any]
_abs = abs  # type: _coconut.typing.Callable[..., T.Any]
_round = round  # type: _coconut.typing.Callable[..., T.Any]
_fmap = fmap  # type: _coconut.typing.Callable[..., T.Any]
_reduce = reduce  # type: _coconut.typing.Callable[..., T.Any]
_all = all  # type: _coconut.typing.Callable[..., T.Any]
_any = any  # type: _coconut.typing.Callable[..., T.Any]
_map = map  # type: _coconut.typing.Callable[..., T.Any]
_filter = filter  # type: _coconut.typing.Callable[..., T.Any]
_int = int  # type: _coconut.typing.Callable[..., T.Any]
_sum = sum  # type: _coconut.typing.Callable[..., T.Any]
_reversed = reversed  # type: _coconut.typing.Callable[..., T.Any]
_print = print  # type: _coconut.typing.Callable[..., T.Any]
_ceil = _math.ceil  # type: _coconut.typing.Callable[..., T.Any]
_floor = _math.floor  # type: _coconut.typing.Callable[..., T.Any]




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool

not_ = None  # type: _coconut.typing.Callable[[bool], bool]
not_ = _coconut.operator.not_

otherwise = True  # type: bool

#### Maybe:
class Maybe(_coconut.object):
    @staticmethod
    @_coconut_tco
    def __pure__(x  # type: Ta
    ):
# type: (...) -> Maybe
        return _coconut_tail_call(Just, x)

    @staticmethod
    def __fail__(msg  # type: str
    ):
# type: (...) -> Maybe
        return nothing

    @staticmethod
    def __mempty__():
# type: (...) -> Maybe
        return nothing

class Nothing(_coconut.collections.namedtuple("Nothing", ""), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)

nothing = Nothing()  # type: Maybe

class Just(_coconut.collections.namedtuple("Just", "x"), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)


derivingOrd(Nothing, Just)

if TYPE_CHECKING:
    def maybe(default,  # type: Tb
     func,  # type: _coconut.typing.Callable[[Ta], Tb]
     x  # type: Maybe
    ):
# type: (...) -> Tb
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_mark_as_match
    def maybe(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 3) and ("default" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Nothing)) and (_coconut.len(_coconut_match_to_args[2]) == 0):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("default")
            if not _coconut_match_to_kwargs:
                default = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def maybe(default, _, Nothing()) = default'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def maybe(default, _, Nothing()) = default'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return default
    @_coconut_addpattern(maybe)
    @_coconut_tco
    @_coconut_mark_as_match
    def maybe(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 3) and ("func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Just)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def maybe(_, func, Just(x)) = func(x)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def maybe(_, func, Just(x)) = func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(func, x)

#### Either:
class Either(_coconut.object):
    @staticmethod
    @_coconut_tco
    def __pure__(x  # type: Ta
    ):
# type: (...) -> Either
        return _coconut_tail_call(Right, x)

    @staticmethod
    @_coconut_tco
    def __fail__(msg  # type: str
    ):
# type: (...) -> Either
        return _coconut_tail_call(Left, msg)

class Left(_coconut.collections.namedtuple("Left", "x"), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @staticmethod
    def __bool__():
# type: (...) -> bool
        return False

    def __fmap__(self, func  # type: _coconut.typing.Callable[[Ta], Tb]
    ):
# type: (...) -> Either
        return self

class Right(_coconut.collections.namedtuple("Right", "x"), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)


derivingOrd(Left, Right)

if TYPE_CHECKING:
    def either(left_func,  # type: _coconut.typing.Callable[[Ta], Tc]
     right_func,  # type: _coconut.typing.Callable[[Tb], Tc]
     x  # type: Either
    ):
# type: (...) -> Tc
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_tco
    @_coconut_mark_as_match
    def either(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 3) and ("left_func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Left)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("left_func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                left_func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def either(left_func, _, Left(x)) = left_func(x)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def either(left_func, _, Left(x)) = left_func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(left_func, x)
    @_coconut_addpattern(either)
    @_coconut_tco
    @_coconut_mark_as_match
    def either(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 3) and ("right_func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Right)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("right_func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                right_func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def either(_, right_func, Right(x)) = right_func(x)'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def either(_, right_func, Right(x)) = right_func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(right_func, x)

#### Ordering:
class Ordering(_coconut.object):
    @staticmethod
    def __mempty__():
# type: (...) -> Ordering
        return eq

class LT(_coconut.collections.namedtuple("LT", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @staticmethod
    def __bool__():
# type: (...) -> bool
        return True

class EQ(_coconut.collections.namedtuple("EQ", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)


class GT(_coconut.collections.namedtuple("GT", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @staticmethod
    def __bool__():
# type: (...) -> bool
        return True

derivingOrd(LT, EQ, GT)
derivingBoundedEnum(LT, EQ, GT)

lt = LT()  # type: Ordering
eq = EQ()  # type: Ordering
gt = GT()  # type: Ordering

#### Char:
Char = T.NewType("Char", str)

#### String:
String = str


### Tuples:
fst = None  # type: _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Ta]
fst = _coconut.operator.itemgetter(0)

snd = None  # type: _coconut.typing.Callable[[T.Tuple[Ta, Tb]], Tb]
snd = _coconut.operator.itemgetter(1)

@_coconut_tco
def curry(func  # type: _coconut.typing.Callable[[Ta, Tb], Tc]
    ):
# type: (...) -> _coconut.typing.Callable[[Ta], _coconut.typing.Callable[[Tb], Tc]]
    return _coconut_tail_call(_coconut.functools.partial, _coconut.functools.partial, func)

def uncurry(func  # type: _coconut.typing.Callable[[Ta], _coconut.typing.Callable[[Tb], Tc]]
    ):
# type: (...) -> _coconut.typing.Callable[[Ta, Tb], Tc]
    return lambda x, y: func(x)(y)



## Basic type classes:

#### Eq:
Eq = object

#### Ord:
Ord = Eq
TOrd = T.TypeVar("TOrd", bound=Ord)

if TYPE_CHECKING:
    def compare(x,  # type: Ord
     y  # type: Ord
    ):
# type: (...) -> Ordering
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_mark_as_match
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                y = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check and not (x == y):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def compare(x, y if x == y) = eq'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def compare(x, y if x == y) = eq'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return eq
    @_coconut_addpattern(compare)
    @_coconut_mark_as_match
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                y = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check and not (x < y):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def compare(x, y if x < y) = lt'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def compare(x, y if x < y) = lt'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return lt
    @_coconut_addpattern(compare)
    @_coconut_mark_as_match
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                y = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check and not (x > y):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def compare(x, y if x > y) = gt'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def compare(x, y if x > y) = gt'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return gt

max = None  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]
max = _max

min = None  # type: _coconut.typing.Callable[[TOrd, TOrd], TOrd]
min = _min

#### Enum:
Enum = Ord
TEnum = T.TypeVar("TEnum", bound=Enum)

succ = None  # type: _coconut.typing.Callable[[TEnum], TEnum]
succ = _coconut.functools.partial(_coconut.operator.add, 1)

pred = None  # type: _coconut.typing.Callable[[TEnum], TEnum]
pred = _coconut_partial(_coconut_minus, {1: 1}, 2)

toEnum = NotImplemented

fromEnum = None  # type: _coconut.typing.Callable[[Enum], int]
fromEnum = _int

@_coconut_tco
def enumFrom(first  # type: TEnum
    ):
# type: (...) -> _coconut.typing.Iterable[TEnum]
    return _coconut_tail_call(iterate, succ, first)

def enumFromThen(first,  # type: TEnum
     second  # type: TEnum
    ):
# type: (...) -> _coconut.typing.Iterable[TEnum]
    step = fromEnum(second) - fromEnum(first)
    return iterate(_coconut.functools.partial(_coconut.operator.add, step), first) if step >= 0 else ()  # type: ignore

def enumFromTo(first,  # type: TEnum
     last  # type: TEnum
    ):
# type: (...) -> _coconut.typing.Iterable[TEnum]
    dist = fromEnum(last) - fromEnum(first)
    return _coconut_igetitem(iterate(succ, first), _coconut.slice(None, dist + 1)) if dist >= 0 else ()  # type: ignore

def enumFromThenTo(first,  # type: TEnum
     second,  # type: TEnum
     last  # type: TEnum
    ):
# type: (...) -> _coconut.typing.Iterable[TEnum]
    step = fromEnum(second) - fromEnum(first)
    dist = fromEnum(last) - fromEnum(first)
    steps = dist / step if step != 0 else 0
    if steps < 0:
        return ()
    counter = iterate(_coconut.functools.partial(_coconut.operator.add, step), first)
    return _coconut_igetitem(counter, _coconut.slice(None, int(steps) + 1)) if steps != 0 else counter


#### Bounded:
Bounded = T.Union[bool, T.Iterable]
TBounded = T.TypeVar("TBounded", bound=Bounded)

@_coconut_tco
def minBound(b  # type: TBounded
    ):
# type: (...) -> TBounded
    """
    -- minBound is overridden by the __minBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with minBound
    """
# Check if bool
    if (isinstance)(b, bool):
        return False  # type: ignore

# Check if overridden
    if (hasattr)(b, "__minBound__"):
        return _coconut_tail_call(b.__minBound__)

# Default implementation
    return _coconut_tail_call(fmap, minBound, b)

@_coconut_tco
def maxBound(b  # type: TBounded
    ):
# type: (...) -> TBounded
    """
    -- maxBound is overridden by the __maxBound__ method
    -- the default implementation recursively calls fmap (__fmap__) with maxBound
    """
# Check if bool
    if (isinstance)(b, bool):
        return True  # type: ignore

# Check if overridden
    if (hasattr)(b, "__maxBound__"):
        return _coconut_tail_call(b.__maxBound__)

# Default implementation
    return _coconut_tail_call(fmap, maxBound, b)



## Numbers:

### Numeric types:

#### Int:
Int = int

#### Integer:
Integer = int

#### Float:
Float = float

#### Double:
Double = float

#### Rational:
Rational = _fractions.Fraction

@_coconut_tco
def over(x, y):
    """
    import Data.Ratio
    over :: Integer -> Integer -> Rational
    over = (%)
    """
    return _coconut_tail_call(Rational, x, y)

#### Word:
Word = Int


### Numeric type classes:

#### Num:
Num = T.Union[int, float, Rational]
TNum = T.TypeVar("TNum", bound=Num)

negate = None  # type: _coconut.typing.Callable[[TNum], TNum]
negate = _coconut_minus

abs = None  # type: _coconut.typing.Callable[[TNum], TNum]
abs = _abs

if TYPE_CHECKING:
    def signum(x  # type: Num
    ):
# type: (...) -> int
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_mark_as_match
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def signum(0) = 0'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def signum(0) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0
    @_coconut_addpattern(signum)
    @_coconut_mark_as_match
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (x > 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def signum(x if x > 0) = 1'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def signum(x if x > 0) = 1'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 1
    @_coconut_addpattern(signum)
    @_coconut_mark_as_match
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (x < 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def signum(x if x < 0) = -1'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def signum(x if x < 0) = -1'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return -1

def fromInteger(x  # type: Integer
    ):
# type: (...) -> Num
    return x

#### Real:
Real = Num

if TYPE_CHECKING:
    def toRational(real  # type: Real
    ):
# type: (...) -> Rational
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_tco
    @_coconut_mark_as_match
    def toRational(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "real" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("real")
            if (_coconut.isinstance(_coconut_match_temp_0, float)) and (not _coconut_match_to_kwargs):
                real = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def toRational(real is float) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def toRational(real is float) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(Rational.from_float, real)
    @_coconut_addpattern(toRational)
    @_coconut_tco
    @_coconut_mark_as_match
    def toRational(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "real" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("real")
            if not _coconut_match_to_kwargs:
                real = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def toRational(real) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def toRational(real) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(Rational, real)

#### Integral:
Integral = int

def quot(x,  # type: int
     y  # type: int
    ):
# type: (...) -> int
    divxy = x // y
    return divxy + (1 if divxy < 0 and x % y != 0 else 0)

def rem(x,  # type: int
     y  # type: int
    ):
# type: (...) -> int
    modxy = x % y
    return modxy - (y if modxy != 0 and x // y < 0 else 0)

div = None  # type: _coconut.typing.Callable[[int, int], int]
div = _coconut.operator.floordiv

mod = None  # type: _coconut.typing.Callable[[int, int], int]
mod = _coconut.operator.mod

def quotRem(x,  # type: int
     y  # type: int
    ):
# type: (...) -> T.Tuple[int, int]
    divxy, modxy = divmod(x, y)
    adj = 1 if divxy < 0 and modxy != 0 else 0
    return divxy + adj, modxy - y * adj

divMod = divmod

toInteger = None  # type: _coconut.typing.Callable[[Integral], Integer]
toInteger = _int

#### Fractional:
Fractional = Rational

recip = None  # type: _coconut.typing.Callable[[Fractional], Fractional]
recip = _coconut.functools.partial(_coconut.operator.truediv, 1)

def fromRational(x  # type: Rational
    ):
# type: (...) -> Fractional
    return x

#### Floating:
Floating = float

from math import pi
from math import exp
from math import log
from math import sqrt
from math import sin
from math import cos
from math import tan
from math import asin
from math import acos
from math import atan
from math import sinh
from math import cosh
from math import tanh
from math import asinh
from math import acosh
from math import atanh

@_coconut_tco
def logBase(base,  # type: float
     x  # type: float
    ):
# type: (...) -> float
    return _coconut_tail_call(log, x, base)

#### RealFrac:
RealFrac = Rational

def properFraction(x  # type: RealFrac
    ):
# type: (...) -> T.Tuple[int, RealFrac]
    floor_x = floor(x)
    return floor_x, x - floor_x

truncate = None  # type: _coconut.typing.Callable[[RealFrac], int]
truncate = _int

round = None  # type: _coconut.typing.Callable[[RealFrac], int]
round = _round

ceiling = None  # type: _coconut.typing.Callable[[RealFrac], int]
ceiling = _ceil

floor = None  # type: _coconut.typing.Callable[[RealFrac], int]
floor = _floor

#### RealFloat:
RealFloat = float

def floatRadix(x  # type: float
    ):
# type: (...) -> int
    return 2

def floatDigits(x  # type: float
    ):
# type: (...) -> int
    return 53

def floatRange(x  # type: float
    ):
# type: (...) -> T.Tuple[int, int]
    return (-1021, 1024)

decodeFloat = NotImplemented

encodeFloat = NotImplemented

exponent = NotImplemented

significand = NotImplemented

def scaleFloat(power,  # type: int
     x  # type: float
    ):
# type: (...) -> float
    return x * 2**power

from math import isnan as isNaN
from math import isinf as isInfinite
from math import atan2

isDenormalized = NotImplemented

def isNegativeZero(x  # type: float
    ):
# type: (...) -> bool
    return x == 0 and str(x).startswith("-")

def isIEEE(x  # type: float
    ):
# type: (...) -> bool
    return True


### Numeric functions:
def subtract(x, y):
    return y - x

def even(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 0

def odd(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 1

gcd = None  # type: _coconut.typing.Callable[[int, int], int]
gcd = _coconut_forward_compose(_fractions.gcd, abs)

if TYPE_CHECKING:
    def lcm(x,  # type: int
     y  # type: int
    ):
# type: (...) -> int
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_mark_as_match
    def lcm(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut_match_to_args[1] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def lcm(_, 0) = 0'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def lcm(_, 0) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0
    @_coconut_addpattern(lcm)
    @_coconut_mark_as_match
    def lcm(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut_match_to_args[0] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def lcm(0, _) = 0'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def lcm(0, _) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0
    @_coconut_addpattern(lcm)
    @_coconut_mark_as_match
    def lcm(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "y" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("y")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                y = _coconut_match_temp_1
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def lcm(x, y) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def lcm(x, y) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return abs(y) * (abs(x) // gcd(x, y))

fromIntegral = None  # type: _coconut.typing.Callable[[Integral], Num]
fromIntegral = fromInteger

realToFrac = None  # type: _coconut.typing.Callable[[Real], Fractional]
realToFrac = toRational



## Monoids:
Monoid = T.Iterable
TMonoid = T.TypeVar("TMonoid", bound=Monoid)

class Mempty(_coconut.collections.namedtuple("Mempty", ""), _coconut.object):
    """
    -- mempty is overridden by the __mempty__ method
    """
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @staticmethod
    @_coconut_tco
    def mempty_as(M  # type: TMonoid
    ):
# type: (...) -> TMonoid
        if (hasattr)(M, "__mempty__"):
            return _coconut_tail_call(M.__mempty__)  # type: ignore
        return _coconut_tail_call(makedata, type(M))

mempty = Mempty()  # type: T.Any

@_coconut_tco
def mappend(x,  # type: TMonoid
     y  # type: TMonoid
    ):
# type: (...) -> TMonoid
    """
    -- mappend is overridden by the __mappend__ method
    -- you may also want to define a __mempty__ method
    -- the default implementation identifies non-identities using __bool__
    """
# Resolve memptys
    x = (asTypeOf)(x, y)
    y = (asTypeOf)(y, x)

# Check if overridden
    if (hasattr)(x, "__mappend__"):
        return _coconut_tail_call(x.__mappend__, y)  # type: ignore

# Default implementation
    if not x:
        return y
    if not y:
        return x
    if (isinstance)(x, tuple) and (isinstance)(y, tuple):
        return _coconut_tail_call(makedata, type(x), *zipWith(mappend, x, y))
    return _coconut_tail_call(makedata, type(x), *_coconut.itertools.chain(x, y))

@_coconut_tco
def mconcat(ms  # type: _coconut.typing.Sequence[TMonoid]
    ):
# type: (...) -> TMonoid
    return _coconut_tail_call(foldr, mappend, mempty, ms)



## Monads and functors:

#### Functor:
Functor = T.Iterable

fmap = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], Functor[Ta]], Functor[Tb]]  # type: ignore
fmap = _fmap

@_coconut_tco
def fmapConst(x,  # type: Ta
     xs  # type: Functor
    ):
# type: (...) -> Functor[Ta]
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """
    return _coconut_tail_call(_fmap, lambda _: x, xs)

#### Applicative:
Applicative = Functor
TApp = T.TypeVar("TApp", bound=Applicative)

if TYPE_CHECKING:
    def pure(x  # type: Ta
    ):
# type: (...) -> T.Any
        return _coconut.Ellipsis  # type: ignore
else:
    class pure(_coconut.collections.namedtuple("pure", "val"), _coconut.object):
        """
        return_ = return
        -- pure/return is overridden by the __pure__ method
        """
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
        def __join__(self):
# type: (...) -> T.Any
            return self.val

        @_coconut_tco
        def pure_as(self, M  # type: TApp
    ):
# type: (...) -> TApp
            if (hasattr)(M, "__pure__"):
                return _coconut_tail_call(M.__pure__, self.val)  # type: ignore
            return _coconut_tail_call(makedata, type(M), self.val)

@_coconut_tco
def ap(fs,  # type: Applicative[_coconut.typing.Callable[[Ta], Tb]]
     xs  # type: Applicative[Ta]
    ):
# type: (...) -> Applicative[Tb]
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    -- ap is overridden by the __ap__ method
    -- you may also want to define a __pure__ method
    -- the default implementation uses join (__join__) and fmap (__fmap__)
    """
# Resolve pures
    fs = (asTypeOf)(fs, xs)  # type: ignore
    xs = (asTypeOf)(xs, fs)  # type: ignore

# Check if overridden
    if (hasattr)(fs, "__ap__"):
        return _coconut_tail_call(fs.__ap__, xs)  # type: ignore

# Default implementation
    return _coconut_tail_call((bind), fs, lambda f: _fmap(f, xs))

@_coconut_tco
def seqAr(f1,  # type: Applicative
     f2  # type: TApp
    ):
# type: (...) -> TApp
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x2, f1), f2)

@_coconut_tco
def seqAl(f1,  # type: TApp
     f2  # type: Applicative
    ):
# type: (...) -> TApp
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """
    return _coconut_tail_call((ap), _fmap(lambda x1: lambda x2: x1, f1), f2)

def liftA2(func  # type: _coconut.typing.Callable[[Ta, Tb], Tc]
    ):
# type: (...) -> _coconut.typing.Callable[[Applicative[Ta], Applicative[Tb]], Applicative[Tc]]
    """
    import Control.Applicative
    liftA2 :: Applicative f => (a -> b -> c) -> f a -> f b -> f c
    """
    return lambda f1, f2: (ap)(_fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2)

#### Monad:
Monad = Applicative
TMonad = T.TypeVar("TMonad", bound=Monad)

@_coconut_tco
def bind(m,  # type: Monad[Ta]
     func  # type: _coconut.typing.Callable[[Ta], TMonad]
    ):
# type: (...) -> TMonad
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    -- bind is overridden by overriding fmap (__fmap__) and join (__join__)
    """
    return _coconut_tail_call(join, _fmap(func, m))

@_coconut_tco
def seqM(m1,  # type: Monad
     m2  # type: TMonad
    ):
# type: (...) -> TMonad
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """
    return _coconut_tail_call((bind), m1, lambda x: m2)

return_ = pure

if TYPE_CHECKING:
    def fail(msg  # type: str
    ):
# type: (...) -> T.Any
        return _coconut.Ellipsis  # type: ignore
else:
    class fail(_coconut.typing.NamedTuple("fail", [("msg", 'str')]), _coconut.object):
        """
        -- fail is overridden by the __fail__ method
        """
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
        @staticmethod
        def __bool__():
# type: (...) -> bool
            return False

        def __fmap__(self, func  # type: _coconut.typing.Callable[[Ta], Tb]
    ):
# type: (...) -> T.Any
            return self

        @_coconut_tco
        def fail_as(self, M  # type: TMonad
    ):
# type: (...) -> TMonad
            if (hasattr)(M, "__fail__"):
                return _coconut_tail_call(M.__fail__, self.msg)  # type: ignore
            return _coconut_tail_call(makedata, type(M))

# sequence_ and mapM_ defined in Foldable

@_coconut_tco
def bindFrom(func,  # type: _coconut.typing.Callable[[Ta], TMonad]
     m  # type: Monad[Ta]
    ):
# type: (...) -> TMonad
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """
    return _coconut_tail_call((bind), m, func)

@_coconut_tco
def join(ms  # type: Monad[TMonad]
    ):
# type: (...) -> TMonad
    """
    import Control.Monad
    join :: Monad m => m (m a) -> m a
    -- join is overridden by the __join__ method
    -- you may also want to define __pure__ and __fail__ methods (pure = return)
    -- the default implementation identifies non-failures using __bool__
    """
# Resolve ms being pure or fail
    ms = reduce(lambda ms, m: (asTypeOf)(ms, m), ms, ms)

# Resolve pures and fails inside of ms
    ms = fmap(lambda m: (asTypeOf)(m, ms), ms)  # type: ignore

# Check if overridden
    if (hasattr)(ms, "__join__"):
        return _coconut_tail_call(ms.__join__)  # type: ignore

# Default implementation
    if not ms:
        return ms  # type: ignore
    vals = []  # type: ignore
    fallback = ms
    for m in ms:
        if m:
            vals.extend(m)
        else:
            fallback = m
    if not vals:
        return fallback  # type: ignore
    return _coconut_tail_call(makedata, type(ms), *vals)

if TYPE_CHECKING:
    def do(monads,  # type: _coconut.typing.Sequence[TMonad]
     func  # type: _coconut.typing.Callable[..., TMonad]
    ):
# type: (...) -> TMonad
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_tco
    @_coconut_mark_as_match
    def do(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "func" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) == 0):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("func")
            if not _coconut_match_to_kwargs:
                func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def do([], func) = func()'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def do([], func) = func()'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(func)
    @_coconut_addpattern(do)
    @_coconut_tco
    @_coconut_mark_as_match
    def do(*_coconut_match_to_args, **_coconut_match_to_kwargs):
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
        """
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (1 <= _coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "func" in _coconut_match_to_kwargs)) == 1) and (_coconut.isinstance(_coconut_match_to_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[0]) >= 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("func")
            ms = _coconut.list(_coconut_match_to_args[0][1:])
            m = _coconut_match_to_args[0][0]
            if not _coconut_match_to_kwargs:
                func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def do([m] + ms, func) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def do([m] + ms, func) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call((bind), m, lambda x: do(ms, _coconut.functools.partial(func, x)))



## Folds and traversals:

#### Foldable:
Foldable = T.Sequence

@_coconut_tco
def sequence_(ms  # type: Foldable[Monad]
    ):
# type: (...) -> Monad
    return _coconut_tail_call(do, ms, lambda *xs: pure(()))

mapM_ = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad], Foldable[Ta]], Monad]
mapM_ = _coconut_forward_compose(fmap, sequence_)

@_coconut_tco
def foldMap(func,  # type: _coconut.typing.Callable[[Ta], TMonoid]
     xs  # type: Foldable[Ta]
    ):
# type: (...) -> TMonoid
    return _coconut_tail_call(mconcat, map(func, xs))

@_coconut_tco
def foldl(func,  # type: _coconut.typing.Callable[[Tb, Ta], Tb]
     init,  # type: Tb
     xs  # type: Foldable[Ta]
    ):
# type: (...) -> Tb
    return _coconut_tail_call(_reduce, func, xs, init)

@_coconut_tco
def foldr(func,  # type: _coconut.typing.Callable[[Ta, Tb], Tb]
     init,  # type: Tb
     xs  # type: Foldable[Ta]
    ):
# type: (...) -> Tb
    return _coconut_tail_call(_reduce, lambda x, y: func(y, x), reversed(xs), init)

foldl1 = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], Foldable[Ta]], Ta]
foldl1 = reduce

@_coconut_tco
def foldr1(func,  # type: _coconut.typing.Callable[[Ta, Ta], Ta]
     xs  # type: Foldable[Ta]
    ):
# type: (...) -> Ta
    return _coconut_tail_call(reduce, lambda x, y: func(y, x), reversed(xs))

def null(xs  # type: Foldable[Ta]
    ):
# type: (...) -> bool
    return len(xs) == 0

length = None  # type: _coconut.typing.Callable[[Foldable], int]
length = len

def elem(e,  # type: Ta
     xs  # type: Foldable[Ta]
    ):
# type: (...) -> bool
    return e in xs

maximum = None  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]
maximum = _max

minimum = None  # type: _coconut.typing.Callable[[Foldable[TOrd]], TOrd]
minimum = _min

sum = None  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]
sum = _sum

product = None  # type: _coconut.typing.Callable[[Foldable[TNum]], TNum]
product = _coconut.functools.partial(reduce, _coconut.operator.mul)

#### Traversable:
Traversable = T.Iterable

@_coconut_tco
def _snoc(xs,  # type: _coconut.typing.Iterable[Ta]
     x  # type: Ta
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut.itertools.chain, xs, (x,))

@_coconut_tco
def sequenceA(fs  # type: Traversable[Applicative[Ta]]
    ):
# type: (...) -> Applicative[Traversable[Ta]]
    return _coconut_tail_call(fmap, lambda xs: makedata(type(fs), *xs), reduce(liftA2(_snoc), fs, pure(())))

traverse = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Applicative[Tb]], Traversable[Ta]], Applicative[Traversable[Tb]]]
traverse = _coconut_forward_compose(fmap, sequenceA)

sequence = None  # type: _coconut.typing.Callable[[Traversable[Monad[Ta]]], Monad[Traversable[Ta]]]
sequence = sequenceA

mapM = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Monad[Tb]], Traversable[Ta]], Monad[Traversable[Tb]]]
mapM = traverse



## Miscellaneous functions:
def id(x  # type: Ta
    ):
# type: (...) -> Ta
    return x

def const(x  # type: Ta
    ):
# type: (...) -> _coconut.typing.Callable[[Tb], Ta]
    return lambda y: x

@_coconut_tco
def dot(f,  # type: _coconut.typing.Callable[[Tb], Tc]
     g  # type: _coconut.typing.Callable[[Ta], Tb]
    ):
# type: (...) -> _coconut.typing.Callable[[Ta], Tc]
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """
    return _coconut_tail_call(_coconut_forward_compose, g, f)

def flip(func  # type: _coconut.typing.Callable[[Ta, Tb], Tc]
    ):
# type: (...) -> _coconut.typing.Callable[[Tb, Ta], Tc]
    return lambda x, y: func(y, x)

@_coconut_tco
def apply(func,  # type: _coconut.typing.Callable[[Ta], Tb]
     arg  # type: Ta
    ):
# type: (...) -> Tb
    """
    apply :: (a -> b) -> a -> b
    apply = ($)
    """
    return _coconut_tail_call(func, arg)

@_coconut_tco
def until(cond,  # type: _coconut.typing.Callable[[Ta], bool]
     func,  # type: _coconut.typing.Callable[[Ta], Ta]
     x  # type: Ta
    ):
# type: (...) -> Ta
    while True:
        if cond(x):
            return x
        try:  # tail recursive
            _coconut_is_recursive = until is _coconut_recursive_func_71  # tail recursive
        except _coconut.NameError:  # tail recursive
            _coconut_is_recursive = False  # tail recursive
        if _coconut_is_recursive:  # tail recursive
            cond, func, x = cond, func, func(x)  # tail recursive
            continue  # tail recursive
        else:  # tail recursive
            return _coconut_tail_call(until, cond, func, func(x))  # tail recursive
# tail recursive

        return None
_coconut_recursive_func_71 = until
def asTypeOf(x,  # type: Ta
     y  # type: Ta
    ):
# type: (...) -> Ta
    """
    -- use asTypeOf to resolve pure, fail, and mempty to the correct type
    -- set asTypeOf.RECURSION_LIMIT to control recursive resolution
    """
    if TYPE_CHECKING:
        return x

    if not (isinstance)(y, (pure, fail, Mempty)):
        for i in takewhile(lambda _=None: _ < asTypeOf.RECURSION_LIMIT, count()):
            if (isinstance)(x, pure):
                x = x.pure_as(y)
            elif (isinstance)(x, fail):
                x = x.fail_as(y)
            elif (isinstance)(x, Mempty):
                x = x.mempty_as(y)
            else:
                break
    return x

asTypeOf.RECURSION_LIMIT = 3  # type: ignore

def error(msg  # type: str
    ):
# type: (...) -> None
    raise Exception(msg)

def errorWithoutStackTrace(msg  # type: str
    ):
# type: (...) -> None
    _coconut_raise_from = Exception(msg)
    _coconut_raise_from.__cause__ = None
    raise _coconut_raise_from

undefined = None  # type: T.Any

def seq(x,  # type: Ta
     y  # type: Tb
    ):
# type: (...) -> Tb
    return y

@_coconut_tco
def cbv(func,  # type: _coconut.typing.Callable[[Ta], Tb]
     arg  # type: Ta
    ):
# type: (...) -> Tb
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    """
    return _coconut_tail_call(func, arg)




# List operations:
@_coconut_tco
def cons(x,  # type: Ta
     xs  # type: _coconut.typing.Iterable[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    """
    cons :: a -> [a] -> [a]
    cons = (:)
    """
    return _coconut_tail_call(_coconut.itertools.chain, [x], xs)

map = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], Tb], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Tb]]
map = _map

@_coconut_tco
def chain(xs,  # type: _coconut.typing.Iterable[Ta]
     ys  # type: _coconut.typing.Iterable[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    """
    chain :: [a] -> [a] -> [a]
    chain = (++)
    """
    return _coconut_tail_call(_coconut.itertools.chain, xs, ys)

filter = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
filter = _filter

head = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]
head = _coconut.functools.partial(_coconut_igetitem, index=0)

last = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], Ta]
last = _coconut.functools.partial(_coconut_igetitem, index=-1)

tail = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
tail = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(1, None))  # type: ignore

init = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
init = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(None, -1))  # type: ignore

@_coconut_tco
def at(xs,  # type: _coconut.typing.Iterable[Ta]
     i  # type: int
    ):
# type: (...) -> Ta
    """
    at :: [a] -> Int -> a
    at = (!!)
    """
    return _coconut_tail_call(_coconut_igetitem, xs, i)

reverse = None  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[Ta]], _coconut.typing.Sequence[Ta]]
reverse = _reversed



## Special folds:
and_ = None  # type: _coconut.typing.Callable[[Foldable[bool]], bool]
and_ = _all

or_ = None  # type: _coconut.typing.Callable[[Foldable[bool]], bool]
or_ = _any

any = None  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]
any = _coconut_forward_compose(map, or_)

all = None  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[Ta], bool]), Foldable[Ta]], bool]
all = _coconut_forward_compose(map, and_)

@_coconut_tco
def concat(xs  # type: Foldable[_coconut.typing.Iterable[Ta]]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_reduce, _coconut.itertools.chain, xs, ())

concatMap = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], _coconut.typing.Iterable[Tb]], Foldable[Ta]], _coconut.typing.Iterable[Tb]]
concatMap = _coconut_forward_compose(map, concat)



## Building lists:

### Scans:
@_coconut_tco
def scanl(func,  # type: _coconut.typing.Callable[[Ta, Tb], Ta]
     init,  # type: Ta
     xs  # type: _coconut.typing.Iterable[Tb]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(scan, func, xs, init)

scanl1 = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta, Ta], Ta], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
scanl1 = scan

@_coconut_tco
def scanr(func,  # type: _coconut.typing.Callable[[Ta, Tb], Ta]
     init,  # type: Ta
     xs  # type: _coconut.typing.Sequence[Tb]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut_igetitem, scan(func, reversed(xs), init), _coconut.slice(None, None, -1))

@_coconut_tco
def scanr1(func,  # type: _coconut.typing.Callable[[Ta, Ta], Ta]
     xs  # type: _coconut.typing.Sequence[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut_igetitem, scan(func, reversed(xs)), _coconut.slice(None, None, -1))

### Infinite lists:
@recursive_iterator
@_coconut_tco
def iterate(func,  # type: _coconut.typing.Callable[[Ta], Ta]
     x  # type: Ta
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [x], lambda: iterate(func, func(x)))))

@recursive_iterator
@_coconut_tco
def repeat(x  # type: Ta
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: [x], lambda: repeat(x))))

@_coconut_tco
def replicate(n,  # type: int
     x  # type: Ta
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut_igetitem, repeat(x), _coconut.slice(None, n))

if TYPE_CHECKING:
    def cycle(xs  # type: _coconut.typing.Sequence[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
        return _coconut.Ellipsis  # type: ignore
else:
    @recursive_iterator
    @_coconut_tco
    @_coconut_mark_as_match
    def cycle(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "xs" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("xs")
            if not _coconut_match_to_kwargs:
                xs = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (len(xs) > 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'def cycle(xs if len(xs) > 0) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'def cycle(xs if len(xs) > 0) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut_tail_call(_coconut.itertools.chain.from_iterable, (_coconut_func() for _coconut_func in (lambda: xs, lambda: cycle(xs))))



## Sublists:
@_coconut_tco
def take(n,  # type: int
     xs  # type: _coconut.typing.Iterable[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut_igetitem, xs, _coconut.slice(None, n))

@_coconut_tco
def drop(n,  # type: int
     xs  # type: _coconut.typing.Iterable[Ta]
    ):
# type: (...) -> _coconut.typing.Iterable[Ta]
    return _coconut_tail_call(_coconut_igetitem, xs, _coconut.slice(n, None))

def splitAt(n,  # type: int
     xs  # type: _coconut.typing.Iterable[Ta]
    ):
# type: (...) -> T.Tuple[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Ta]]
    reit = reiterable(xs)
    return _coconut_igetitem(reit, _coconut.slice(None, n)), _coconut_igetitem(reit, _coconut.slice(n, None))

takeWhile = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
takeWhile = takewhile

dropWhile = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[Ta], bool], _coconut.typing.Iterable[Ta]], _coconut.typing.Iterable[Ta]]
dropWhile = dropwhile

if TYPE_CHECKING:
    def span(cond,  # type: _coconut.typing.Callable[[Ta], bool]
     xs  # type: _coconut.typing.Sequence[Ta]
    ):
# type: (...) -> T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Ta]]
        return _coconut.Ellipsis  # type: ignore
else:
    @_coconut_mark_as_match
    def span(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut.isinstance(_coconut_match_to_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[1]) == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'match def span(_, []) = ([], [])'" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'match def span(_, []) = ([], [])'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return ([], [])
    @_coconut_addpattern(span)
    @_coconut_mark_as_match
    def span(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) == 2) and ("cond" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[1]) >= 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("cond")
            xs = _coconut.list(_coconut_match_to_args[1][1:])
            x = _coconut_match_to_args[1][0]
            if not _coconut_match_to_kwargs:
                cond = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (cond(x)):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def span(cond, [x] + xs if cond(x)) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def span(cond, [x] + xs if cond(x)) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        ys, zs = span(cond, xs)
        return ([x] + ys, zs)
    @_coconut_addpattern(span)
    @_coconut_mark_as_match
    def span(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "cond" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "xs" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("cond")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("xs")
            if not _coconut_match_to_kwargs:
                cond = _coconut_match_temp_0
                xs = _coconut_match_temp_1
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_val_repr = _coconut.repr(_coconut_match_to_args)
            _coconut_match_err = _coconut_FunctionMatchError("pattern-matching failed for " "'addpattern def span(cond, xs) ='" " in " + (_coconut_match_val_repr if _coconut.len(_coconut_match_val_repr) <= 500 else _coconut_match_val_repr[:500] + "..."))
            _coconut_match_err.pattern = 'addpattern def span(cond, xs) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return ([], xs)

@_coconut_tco
def break_(cond,  # type: _coconut.typing.Callable[[Ta], bool]
     xs  # type: _coconut.typing.Sequence[Ta]
    ):
# type: (...) -> _coconut.typing.Sequence[Ta]
    """
    break_ = break
    """
    return _coconut_tail_call(span, _coconut_forward_compose(cond, _coconut.operator.not_), xs)



## Searching lists:
def notElem(e,  # type: Ta
     xs  # type: _coconut.typing.Sequence[Ta]
    ):
# type: (...) -> bool
    return e not in xs

def lookup(key,  # type: Ta
     assocs  # type: _coconut.typing.Iterable[T.Tuple[Ta, Tb]]
    ):
# type: (...) -> Maybe
    try:
        return ((Just)((_coconut_igetitem(dropwhile(lambda pair: pair[0] != key, assocs), 0))[1]))
    except StopIteration:
        return nothing



## Zipping and unzipping lists:
zip = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb]], _coconut.typing.Iterable[T.Tuple[Ta, Tb]]]
zip = _zip

zip3 = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[Ta], _coconut.typing.Iterable[Tb], _coconut.typing.Iterable[Tc]], _coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]]
zip3 = _zip

@_coconut_tco
def zipWith(func,  # type: _coconut.typing.Callable[[Ta, Tb], Tc]
     xs1,  # type: _coconut.typing.Iterable[Ta]
     xs2  # type: _coconut.typing.Iterable[Tb]
    ):
# type: (...) -> _coconut.typing.Iterable[Tc]
    return _coconut_tail_call(starmap, func, zip(xs1, xs2))

@_coconut_tco
def zipWith3(func,  # type: _coconut.typing.Callable[[Ta, Tb, Tc], Td]
     xs1,  # type: _coconut.typing.Iterable[Ta]
     xs2,  # type: _coconut.typing.Iterable[Tb]
     xs3  # type: _coconut.typing.Iterable[Tc]
    ):
# type: (...) -> _coconut.typing.Iterable[Td]
    return _coconut_tail_call(starmap, func, _zip(xs1, xs2, xs3))

@_coconut_tco
def unzip(xs  # type: _coconut.typing.Iterable[T.Tuple[Ta, Tb]]
    ):
# type: (...) -> T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb]]
    return _coconut_tail_call((tuple), map(list, _zip(*xs)))

unzip3 = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[T.Tuple[Ta, Tb, Tc]]], T.Tuple[_coconut.typing.Sequence[Ta], _coconut.typing.Sequence[Tb], _coconut.typing.Sequence[Tc]]]
unzip3 = unzip  # type: ignore



## Functions on strings:
lines = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
lines = _coconut.operator.methodcaller("splitlines")

words = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
words = _coconut.operator.methodcaller("split")

@_coconut_tco
def unlines(strs  # type: _coconut.typing.Iterable[str]
    ):
# type: (...) -> str
    return _coconut_tail_call("".join, (s + "\n" for s in strs))

unwords = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[str]], str]
unwords = " ".join




# Converting to and from String:

## Converting to String:
ShowS = T.Callable[[str], str]

Show = T.Any

showsPrec = NotImplemented

show = None  # type: _coconut.typing.Callable[[Ta], str]
show = repr

def shows(x  # type: Show
    ):
# type: (...) -> ShowS
    return lambda s: repr(x) + s

def showList(xs  # type: _coconut.typing.Iterable[Show]
    ):
# type: (...) -> ShowS
    return lambda s: repr(list(xs)) + s

def showString(x  # type: str
    ):
# type: (...) -> ShowS
    return lambda s: x + s

showChar = None  # type: _coconut.typing.Callable[[Char], ShowS]
showChar = showString

def showParen(parens,  # type: bool
     showFunc  # type: ShowS
    ):
# type: (...) -> ShowS
    return lambda s: ("(" + showFunc("") + ")" + s if parens else showFunc("") + s)



## Converting from String:
ReadS = NotImplemented

Read = T.Union[str, int, float, bool, None, tuple, list, dict,]

readsPrec = NotImplemented

readList = NotImplemented

reads = NotImplemented

readParen = NotImplemented

@_coconut_tco
def read(s  # type: str
    ):
# type: (...) -> Read
    return _coconut_tail_call(_ast.literal_eval, s)

lex = NotImplemented




# Basic input and output:

#### IO:
class IO(_coconut.collections.namedtuple("IO", "io_func"), _coconut.object):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    @staticmethod
    @_coconut_tco
    def __pure__(x  # type: Ta
    ):
# type: (...) -> IO
        return _coconut_tail_call(IO, lambda: x)

    @staticmethod
    @_coconut_tco
    def __fail__(msg  # type: str
    ):
# type: (...) -> IO
        def _coconut_lambda_0():
            raise IOError(msg)
        return _coconut_tail_call(IO, _coconut_lambda_0)

    @_coconut_tco
    def __fmap__(self, func  # type: _coconut.typing.Callable[[Ta], Tb]
    ):
# type: (...) -> IO
        return _coconut_tail_call(IO, _coconut_forward_compose(self.io_func, func))

    @_coconut_tco
    def __join__(self):
# type: (...) -> IO
        return _coconut_tail_call(fmap, unIO, self)

    @staticmethod
    @_coconut_tco
    def __mempty__():
# type: (...) -> IO
        return _coconut_tail_call(IO, lambda: mempty)

    @_coconut_tco
    def __mappend__(self, other  # type: IO
    ):
# type: (...) -> IO
        return _coconut_tail_call(IO, lambda: mappend(self.io_func(), other.io_func()))

_nullIO = IO(lambda: None)  # type: IO

@_coconut_tco
def asIO(io  # type: IO
    ):
# type: (...) -> IO
    """
    asIO :: IO a -> IO a
    asIO = id
    -- asIO(x) is equivalent to x `asTypeOf` IO(...)
    """
    return _coconut_tail_call((asTypeOf), io, _nullIO)

@_coconut_tco
def unIO(io  # type: IO
    ):
# type: (...) -> Ta
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
    """
    return _coconut_tail_call(asIO(io).io_func)




## Simple I/O operations:

### Output functions:
@_coconut_tco
def putStr(s  # type: str
    ):
# type: (...) -> IO
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s, end=""))

putChar = None  # type: _coconut.typing.Callable[[Char], IO]
putChar = putStr

@_coconut_tco
def putStrLn(s  # type: str
    ):
# type: (...) -> IO
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, s))

@_coconut_tco
def print(x  # type: Ta
    ):
# type: (...) -> IO
    return _coconut_tail_call(IO, _coconut.functools.partial(_print, show(x)))


### Input functions:
getChar = IO(_coconut.functools.partial(sys.stdin.read, 1))  # type: IO

getLine = IO(input)  # type: IO

getContents = IO(sys.stdin.read)  # type: IO

@_coconut_tco
def interact(func  # type: _coconut.typing.Callable[[str], str]
    ):
# type: (...) -> IO
    def do_interact():
        while True:
            (_print)((func)(input()))
    return _coconut_tail_call(IO, do_interact)


### Files:
FilePath = str

@_coconut_tco
def readFile(fpath  # type: FilePath
    ):
# type: (...) -> IO
    def do_readFile():
# type: (...) -> str
        with open(fpath, "r+") as f:
            return f.read()
    return _coconut_tail_call(IO, do_readFile)

@_coconut_tco
def writeFile(fpath,  # type: FilePath
     text  # type: str
    ):
# type: (...) -> IO
    def do_writeFile():
# type: (...) -> None
        with open(fpath, "w+") as f:
            f.write(text)
    return _coconut_tail_call(IO, do_writeFile)

@_coconut_tco
def appendFile(fpath,  # type: FilePath
     text  # type: str
    ):
# type: (...) -> IO
    def do_appendFile():
# type: (...) -> None
        with open(fpath, "a+") as f:
            f.write(text)
    return _coconut_tail_call(IO, do_appendFile)

@_coconut_tco
def readIO(s  # type: str
    ):
# type: (...) -> IO
    return _coconut_tail_call(IO, _coconut.functools.partial(read, s))

@_coconut_tco
def readLn():
# type: (...) -> IO
    return _coconut_tail_call((bind), getLine(), readIO)  # type: ignore



## Exception handling:
@_coconut_tco
def ioError(err  # type: IOError
    ):
# type: (...) -> IO
    def _coconut_lambda_1():
        raise err
    return _coconut_tail_call(IO, _coconut_lambda_1)

@_coconut_tco
def userError(msg  # type: str
    ):
# type: (...) -> IOError
    return _coconut_tail_call(IOError, msg)
