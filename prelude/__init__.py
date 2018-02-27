#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa7d387cb

# Compiled with Coconut version 1.3.1-post_dev25 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

# Imports:
_sys = _coconut_sys
import typing as _t
import functools as _functools




# Type variables:
_a = _t.TypeVar("_a")
_b = _t.TypeVar("_b")
_c = _t.TypeVar("_c")





# Helper functions:

## Type class helpers:
def derivingEqOrd(*valueConstructors  # type: _t.NamedTuple
    ):
# type: (...) -> None
    """
    The expression
        derivingEqOrd(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for any data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Eq, Ord)
    """
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
def derivingEnum(*valueConstructors  # type: _t.NamedTuple
    ):
# type: (...) -> None
    """
    The expression
        derivingEnum(valueConstructor1, valueConstructor2, ...)
    is equivalent to stating that for any data type defined as
        data dataType = valueConstructor1 ... | valueConstructor2 ... | ...
    we should add
        deriving (Enum)
    """
    ind = _coconut_forward_compose(type, valueConstructors.index)
    for valCon in valueConstructors:
        valCon.__int__ = ind
        def __add__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
            _coconut_match_check = False
            if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "self" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
                _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("self")
                _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
                if (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
                    self = _coconut_match_temp_0
                    x = _coconut_match_temp_1
                    _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def valCon.__add__(self, x is int) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
                _coconut_match_err.pattern = 'def valCon.__add__(self, x is int) ='
                _coconut_match_err.value = _coconut_match_to_args
                raise _coconut_match_err

            return valueConstructors[ind(self) + x]()
        valCon.__add__ = __add__
        def __sub__(*_coconut_match_to_args, **_coconut_match_to_kwargs):
            _coconut_match_check = False
            if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "self" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "x" in _coconut_match_to_kwargs)) == 1):
                _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("self")
                _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("x")
                if (_coconut.isinstance(_coconut_match_temp_1, int)) and (not _coconut_match_to_kwargs):
                    self = _coconut_match_temp_0
                    x = _coconut_match_temp_1
                    _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def valCon.__sub__(self, x is int) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
                _coconut_match_err.pattern = 'def valCon.__sub__(self, x is int) ='
                _coconut_match_err.value = _coconut_match_to_args
                raise _coconut_match_err

            return valueConstructors[ind(self) - x]()




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
        valCon.__sub__ = __sub__
Bool = bool

not_ = None  # type: _coconut.typing.Callable[[bool], bool]
not_ = _coconut.operator.not_

otherwise = True  # type: bool

#### Maybe:
class Maybe(_coconut.object): pass

class Nothing(_coconut.collections.namedtuple("Nothing", ""), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
nothing = Nothing()  # type: Maybe

class Just(_coconut.collections.namedtuple("Just", "x"), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

derivingEqOrd(Nothing, Just)

if TYPE_CHECKING:
    def maybe(default,  # type: _b
     func,  # type: _coconut.typing.Callable[[_t.Any], _b]
     x  # type: Maybe
    ):
# type: (...) -> _b
        return _coconut.Ellipsis  # type: ignore
else:
    def maybe(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 3) and ("default" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Nothing)) and (_coconut.len(_coconut_match_to_args[2]) == 0):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("default")
            if not _coconut_match_to_kwargs:
                default = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def maybe(default, _, Nothing()) = default'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def maybe(default, _, Nothing()) = default'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return default

    @addpattern(maybe)
    def maybe(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 3) and ("func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Just)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def maybe(_, func, Just(x)) = func(x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def maybe(_, func, Just(x)) = func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return func(x)

#### Either:
class Either(_coconut.object): pass

class Left(_coconut.collections.namedtuple("Left", "x"), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

class Right(_coconut.collections.namedtuple("Right", "x"), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

derivingEqOrd(Left, Right)

if TYPE_CHECKING:
    def either(left_func,  # type: _coconut.typing.Callable[[_t.Any], _c]
     right_func,  # type: _coconut.typing.Callable[[_t.Any], _c]
     x  # type: Either
    ):
# type: (...) -> _c
        return _coconut.Ellipsis  # type: ignore
else:
    def either(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 3) and ("left_func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Left)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("left_func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                left_func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def either(left_func, _, Left(x)) = left_func(x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def either(left_func, _, Left(x)) = left_func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return left_func(x)

    @addpattern(either)
    def either(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 3) and ("right_func" not in _coconut_match_to_kwargs) and (_coconut.isinstance(_coconut_match_to_args[2], Right)) and (_coconut.len(_coconut_match_to_args[2]) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("right_func")
            x = _coconut_match_to_args[2][0]
            if not _coconut_match_to_kwargs:
                right_func = _coconut_match_temp_0
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def either(_, right_func, Right(x)) = right_func(x)'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def either(_, right_func, Right(x)) = right_func(x)'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return right_func(x)

#### Ordering:
class Ordering(_coconut.object): pass

class LT(_coconut.collections.namedtuple("LT", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
lt = LT()  # type: Ordering

class EQ(_coconut.collections.namedtuple("EQ", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
eq = EQ()  # type: Ordering

class GT(_coconut.collections.namedtuple("GT", ""), Ordering):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
gt = GT()  # type: Ordering

derivingEqOrd(LT, EQ, GT)
derivingEnum(LT, EQ, GT)

#### Char:
Char = str

#### String:
String = str


### Tuples:
fst = None  # type: _coconut.typing.Callable[[_t.Tuple[_a, _b]], _a]
fst = _coconut.operator.itemgetter(0)

snd = None  # type: _coconut.typing.Callable[[_t.Tuple[_a, _b]], _b]
snd = _coconut.operator.itemgetter(1)

def curry(func  # type: _coconut.typing.Callable[[_a, _b], _c]
    ):
# type: (...) -> _coconut.typing.Callable[[_a], _coconut.typing.Callable[[_b], _c]]
    return _coconut.functools.partial(_coconut.functools.partial, func)  # type: ignore

def uncurry(func  # type: _coconut.typing.Callable[[_a], _coconut.typing.Callable[[_b], _c]]
    ):
# type: (...) -> _coconut.typing.Callable[[_a, _b], _c]
    return lambda x, y: func(x)(y)



## Basic type classes:

#### Eq:
Eq = _t.Any

#### Ord:
Ord = Eq

if TYPE_CHECKING:
    def compare(x,  # type: Ord
     y  # type: Ord
    ):
# type: (...) -> Ordering
        return _coconut.Ellipsis  # type: ignore
else:
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
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
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def compare(x, y if x == y) = eq'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def compare(x, y if x == y) = eq'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return eq

    @addpattern(compare)
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
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
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def compare(x, y if x < y) = lt'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def compare(x, y if x < y) = lt'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return lt

    @addpattern(compare)
    def compare(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
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
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def compare(x, y if x > y) = gt'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def compare(x, y if x > y) = gt'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return gt

max = None  # type: _coconut.typing.Callable[[_a, _a], _a]
max = max  # type: ignore

min = None  # type: _coconut.typing.Callable[[_a, _a], _a]
min = min  # type: ignore

#### Enum:
Enum = _t.SupportsInt
_E = _t.TypeVar("_E", bound=Enum)

succ = None  # type: _coconut.typing.Callable[[_E], _E]
succ = _coconut.functools.partial(_coconut.operator.add, 1)

pred = None  # type: _coconut.typing.Callable[[_E], _E]
pred = _coconut_partial(_coconut_minus, {1: 1}, 2)

toEnum = NotImplemented

fromEnum = None  # type: _coconut.typing.Callable[[Enum], int]
fromEnum = int

def enumFrom(first  # type: _E
    ):
# type: (...) -> _coconut.typing.Iterable[_E]
    return iterate(succ, first)

def enumFromThen(first,  # type: _E
     second  # type: _E
    ):
# type: (...) -> _coconut.typing.Iterable[_E]
    step = fromEnum(second) - fromEnum(first)
    return iterate(_coconut.functools.partial(_coconut.operator.add, step), first)

def enumFromTo(first,  # type: _E
     last  # type: _E
    ):
# type: (...) -> _coconut.typing.Iterable[_E]
    dist = fromEnum(last) - fromEnum(first)
    return _coconut_igetitem(iterate(succ, first), _coconut.slice(None, dist)) if dist >= 0 else _coconut_igetitem(iterate(pred, first), _coconut.slice(None, -dist))

def enumFromThenTo(first,  # type: _E
     second,  # type: _E
     last  # type: _E
    ):
# type: (...) -> _coconut.typing.Iterable[_E]
    step = fromEnum(second) - fromEnum(first)
    return takewhile(lambda _=None: _ <= last if step >= 0 else _ >= last, iterate(_coconut.functools.partial(_coconut.operator.add, step), first))


#### Bounded:
Bounded = NotImplemented

minBound = NotImplemented

maxBound = NotImplemented



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
from fractions import Fraction as Rational

#### Word:
Word = Int


### Numeric type classes:

#### Num:
Num = _t.Union[int, float, Rational]
_N = _t.TypeVar("_N", bound=Num)

negate = _coconut_minus

abs = None  # type: _coconut.typing.Callable[[_a], _a]
abs = abs  # type: ignore

if TYPE_CHECKING:
    def signum(x):
# type: (...) -> int
        return _coconut.Ellipsis  # type: ignore
else:
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 1) and (_coconut_match_to_args[0] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def signum(0) = 0'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def signum(0) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0

    @addpattern(signum)
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (x > 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def signum(x if x > 0) = 1'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def signum(x if x > 0) = 1'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 1

    @addpattern(signum)
    def signum(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "x" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("x")
            if not _coconut_match_to_kwargs:
                x = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (x < 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def signum(x if x < 0) = -1'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def signum(x if x < 0) = -1'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return -1

def fromInteger(x  # type: Integer
    ):
# type: (...) -> Num
    return x

#### Real:
Real = Num

toRational = None  # type: _coconut.typing.Callable[[Real], Rational]
toRational = Rational

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
# type: (...) -> _t.Tuple[int, int]
    divxy, modxy = divmod(x, y)
    return divxy + (1 if modxy < 0 else 0), modxy - (y if modxy < 0 else 0)

divMod = divmod

toInteger = None  # type: _coconut.typing.Callable[[Integral], Integer]
toInteger = int

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

def logBase(base,  # type: Num
     x  # type: Num
    ):
# type: (...) -> float
    return log(x, base)

#### RealFrac:
RealFrac = Rational

def properFraction(x  # type: Rational
    ):
# type: (...) -> (int, Rational)
    floor_x = floor(x)
    return floor_x + (x - floor_x)

truncate = None  # type: _coconut.typing.Callable[[Rational], int]
truncate = int

round = None  # type: _coconut.typing.Callable[[Rational], int]
round = round  # type: ignore

from math import ceil as _ceil
from math import floor as _floor

ceiling = None  # type: _coconut.typing.Callable[[Rational], int]
ceiling = _ceil

floor = None  # type: _coconut.typing.Callable[[Rational], int]
floor = _floor

#### RealFloat:
RealFloat = float

def floatRadix(x  # type: float
    ):
# type: (...) -> int
    return 2

floatDigits = NotImplemented

floatRange = NotImplemented

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

isNegativeZero = NotImplemented

isIEEE = NotImplemented


### Numeric functions:
def subtract(x, y):
    return x - y

def even(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 0

def odd(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 1

from fractions import gcd_

gcd = None  # type: _coconut.typing.Callable[[int, int], int]
gcd = _coconut_forward_compose(gcd_, abs)

if TYPE_CHECKING:
    def lcm(x,  # type: int
     y  # type: int
    ):
# type: (...) -> int
        return _coconut.Ellipsis  # type: ignore
else:
    def lcm(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut_match_to_args[1] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def lcm(_, 0) = 0'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def lcm(_, 0) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0

    @addpattern(lcm)
    def lcm(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut_match_to_args[0] == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def lcm(0, _) = 0'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def lcm(0, _) = 0'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return 0

    @addpattern(lcm)
    def lcm(x, y):
        abs_x = abs(x)
        abs_y = abs(y)
        return abs_y * (abs_x // gcd_(abs_x, abs_y))

fromIntegral = None  # type: _coconut.typing.Callable[[Integral], Num]
fromIntegral = fromInteger

realToFrac = None  # type: _coconut.typing.Callable[[Real], Fractional]
realToFrac = Rational



## Monoids:
Monoid = NotImplemented

mempty = NotImplemented

mappend = NotImplemented

mconcat = NotImplemented



## Monads and functors:

#### Functor:
Functor = _t.Iterable

fmap = fmap  # type: ignore

def fmapConst(x,  # type: _a
     xs  # type: Functor
    ):
# type: (...) -> Functor[_a]
    """
    fmapConst :: Functor f => (a -> b) -> f a -> f b
    fmapConst = (<$)
    """
    return fmap(lambda _=None: x, xs)

#### Applicative:
Applicative = _t.Collection
_A = _t.TypeVar("_A", bound=Applicative)

pure = NotImplemented

def ap(fs,  # type: Applicative[_coconut.typing.Callable[[_a], _b]]
     xs  # type: Applicative[_a]
    ):
# type: (...) -> Applicative[_b]
    """
    ap :: Applicative f => f (a -> b) -> f a -> f b
    ap = (<*>)
    """
    return (bind)(fs, _coconut_partial(fmap, {1: xs}, 2))

def seqAr(f1,  # type: Applicative
     f2  # type: _A
    ):
# type: (...) -> _A
    """
    seqAr :: Applicative f => f a -> f b -> f b
    seqAr = (*>)
    """
    return ap(fmap(lambda x1: lambda x2: x2, f1), f2)

def seqAl(f1,  # type: _A
     f2  # type: Applicative
    ):
# type: (...) -> _A
    """
    seqAl :: Applicative f => f a -> f b -> f a
    seqAl = (<*)
    """
    return ap(fmap(lambda x1: lambda x2: x1, f1), f2)

def liftA2(func,  # type: _coconut.typing.Callable[[_a, _b], _c]
     f1,  # type: Applicative[_a]
     f2  # type: Applicative[_b]
    ):
# type: (...) -> Applicative[_c]
    """Lift a binary function to actions."""
    return ap(fmap(_coconut.functools.partial(_coconut.functools.partial, func), f1), f2)

#### Monad:
Monad = Applicative
_M = _t.TypeVar("_M", bound=Monad)

def bind(m,  # type: Monad[_a]
     func  # type: _coconut.typing.Callable[[_a], _M]
    ):
# type: (...) -> _M
    """
    bind :: Monad m => m a -> (a -> m b) -> m b
    bind = (>>=)
    """
    return join(fmap(func, m))

def seqM(m1,  # type: Monad
     m2  # type: _M
    ):
# type: (...) -> _M
    """
    seqM :: Monad m => m a -> m b -> m b
    seqM = (>>)
    """
    return (bind)(m1, lambda x: m2)

return_ = NotImplemented

fail = NotImplemented

def sequence_(ms  # type: Traversable[Monad[_a]]
    ):
# type: (...) -> None
    reduce(seqM, ms)

mapM_ = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a], Monad[_b]], Traversable[_a]], None]
mapM_ = _coconut_forward_compose(fmap, sequence_)

def bindFrom(func,  # type: _coconut.typing.Callable[[_a], Monad[_b]]
     m  # type: Monad[_a]
    ):
    """
    bindFrom :: Monad m => (a -> m b) -> m a -> m b
    bindFrom = (=<<)
    """
    return (bind)(m, func)

if TYPE_CHECKING:
    def join(m  # type: Monad[_M]
    ):
# type: (...) -> _M
        return _coconut.Ellipsis  # type: ignore
else:
    def join(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "m" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("m")
            if not _coconut_match_to_kwargs:
                m = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (len(m) == 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def join(m if len(m) == 0) = m'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def join(m if len(m) == 0) = m'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return m

    @addpattern(join)
    def join(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "m" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("m")
            if not _coconut_match_to_kwargs:
                m = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (len(m) == 1):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def join(m if len(m) == 1) = m[0]'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def join(m if len(m) == 1) = m[0]'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return m[0]

    @addpattern(join)
    def join(m):
        """The conventional monad join operator."""
        return makedata(type(m), *reduce(_coconut.operator.add, m))

if TYPE_CHECKING:
    def do(func,  # type: _coconut.typing.Callable[..., _M]
     *monads  # type: _M
    ):
# type: (...) -> _M
        return _coconut.Ellipsis  # type: ignore
else:
    def do(func):
        return func()

    @addpattern(do)
    def do(func, m1, *ms):
        """
        The call
            do(func, m1, m2, ...)
        is equivalent to the do notation
            x1 <- m1
            x2 <- m2
            ...
            func(x1, x2, ...)
        which is equivalent to the sequence of binds
            m1 `bind` x1 ->
                m2 `bind` x2 ->
                    ...
                        func(x1, x2, ...)
        """
        return (bind)(m1, lambda x: do(_coconut.functools.partial(func, x), *ms))



## Folds and traversals:

#### Foldable:
Foldable = _t.Sequence

foldMap = NotImplemented

def foldr(func,  # type: _coconut.typing.Callable[[_a, _b], _a]
     init,  # type: _a
     xs  # type: Foldable[_a]
    ):
# type: (...) -> _a
    return reduce(func, xs, init)

def foldl(func,  # type: _coconut.typing.Callable[[_a, _b], _a]
     init,  # type: _a
     xs  # type: Foldable[_a]
    ):
# type: (...) -> _a
    return reduce(func, reversed(xs), init)

foldr1 = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a, _a], _a], Foldable[_a]], _a]
foldr1 = reduce

def foldl1(func,  # type: _coconut.typing.Callable[[_a, _a], _a]
     xs  # type: Foldable[_a]
    ):
# type: (...) -> _a
    return reduce(func, reversed(xs))

def null(xs  # type: Foldable[_a]
    ):
# type: (...) -> bool
    return len(xs) == 0

length = None  # type: _coconut.typing.Callable[[Foldable], int]
length = len

def elem(e,  # type: _a
     xs  # type: Foldable[_a]
    ):
# type: (...) -> bool
    return e in xs

maximum = None  # type: _coconut.typing.Callable[[Foldable[_a]], _a]
maximum = max

minimum = None  # type: _coconut.typing.Callable[[Foldable[_a]], _a]
minimum = min

sum = None  # type: _coconut.typing.Callable[[Foldable[_N]], _N]
sum = sum  # type: ignore

product = None  # type: _coconut.typing.Callable[[Foldable[_N]], _N]
product = _coconut.functools.partial(reduce, _coconut.operator.mul)

#### Traversable:
Traversable = Functor

def sequenceA(t  # type: Traversable[Applicative[_a]]
    ):
# type: (...) -> Applicative[Traversable[_a]]
    return reduce(seqAr, t)

traverse = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a], Applicative[_b]], Traversable[_a]], Applicative[Traversable[_b]]]
traverse = _coconut_forward_compose(fmap, sequenceA)

def sequence(t  # type: Traversable[_M]
    ):
# type: (...) -> _M
    return reduce(seqM, t)

mapM = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a], Monad[_b]], Traversable[_a]], Monad[Traversable[_b]]]
mapM = _coconut_forward_compose(fmap, sequence)



## Miscellaneous functions:
def id(x  # type: _a
    ):
# type: (...) -> _a
    return x

def const(x,  # type: _a
     _):
# type: (...) -> _a
    return x

def dot(f,  # type: _coconut.typing.Callable[[_b], _c]
     g  # type: _coconut.typing.Callable[[_a], _b]
    ):
# type: (...) -> _coconut.typing.Callable[[_a], _c]
    """
    dot :: (b -> c) -> (a -> b) -> a -> c
    dot = (.)
    """
    return _coconut_forward_compose(g, f)

def flip(func  # type: _coconut.typing.Callable[[_a, _b], _c]
    ):
# type: (...) -> _coconut.typing.Callable[[_b, _a], _c]
    return lambda x, y: func(y, x)

def apply(f,  # type: _coconut.typing.Callable[[_a], _b]
     x  # type: _a
    ):
    """
    apply :: (a -> b) -> a -> b
    apply = ($)
    """
    return f(x)

def until(cond,  # type: _coconut.typing.Callable[[_a], bool]
     func,  # type: _coconut.typing.Callable[[_a], _a]
     x  # type: _a
    ):
# type: (...) -> _a
    while True:
        if cond(x):
            return x
        if until is _coconut_recursive_func_62:  # tail recursive
            cond, func, x = cond, func, func(x)  # tail recursive
            continue  # tail recursive
        else:  # tail recursive
            return until(cond, func, func(x))  # tail recursive

        return None
_coconut_recursive_func_62 = until
asTypeOf = None  # type: _coconut.typing.Callable[[_a, _a], _a]
asTypeOf = const

def error(msg  # type: str
    ):
# type: (...) -> None
    raise Exception(msg)

errorWithoutStackTrace = NotImplemented

undefined = None  # type: _t.Any

def seq(x, y  # type: _b
    ):
# type: (...) -> _b
    return y

def cbv(func,  # type: _coconut.typing.Callable[[_a], _b]
     arg  # type: _a
    ):
# type: (...) -> _b
    """
    cbv :: (a -> b) -> a -> b
    cbv = ($!)
    """
    return func(arg)




# List operations:
map = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a], _b], _coconut.typing.Iterable[_a]], _coconut.typing.Iterable[_b]]
map = map  # type: ignore

def append(xs,  # type: _coconut.typing.Iterable[_a]
     ys  # type: _coconut.typing.Iterable[_a]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    """
    append :: [a] -> [a] -> [a]
    append = (++)
    """
    return _coconut.itertools.chain(xs, ys)

filter = None  # type: _coconut.typing.Callable[[_coconut.typing.Callable[[_a], bool], _coconut.typing.Iterable[_a]], _coconut.typing.Iterable[_a]]
filter = filter  # type: ignore

head = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_a]], _a]
head = _coconut.functools.partial(_coconut_igetitem, index=0)

last = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_a]], _a]
last = _coconut.functools.partial(_coconut_igetitem, index=-1)

tail = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_a]], _coconut.typing.Iterable[_a]]
tail = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(1, None))  # type: ignore

init = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_a]], _coconut.typing.Iterable[_a]]
init = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(None, -1))  # type: ignore

def index(xs,  # type: _coconut.typing.Iterable[_a]
     i  # type: int
    ):
# type: (...) -> _a
    return _coconut_igetitem(xs, i)

reverse = None  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[_a]], _coconut.typing.Sequence[_a]]
reverse = reversed



## Special folds:
and_ = None  # type: _coconut.typing.Callable[[Foldable[bool]], bool]
and_ = all  # type: ignore

or_ = None  # type: _coconut.typing.Callable[[Foldable[bool]], bool]
or_ = any  # type: ignore

any = None  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_a], bool]), Foldable[_a]], bool]
any = _coconut_forward_compose(map, or_)

all = None  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_a], bool]), Foldable[_a]], bool]
all = _coconut_forward_compose(map, and_)

concat = None  # type: _coconut.typing.Callable[[Foldable[_coconut.typing.Iterable[_a]]], _coconut.typing.Iterable[_a]]
concat = _coconut.functools.partial(reduce, _coconut.itertools.chain)  # type: ignore

concatMap = None  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_a], _coconut.typing.Iterable[_b]]), Foldable[_a]], _coconut.typing.Iterable[_b]]
concatMap = _coconut_forward_compose(map, concat)



## Building lists:

### Scans:
def scanl(func,  # type: _coconut.typing.Callable[[_a, _b], _a]
     init,  # type: _a
     xs  # type: _coconut.typing.Sequence[_b]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return scan(func, reversed(xs), init)

def scanl1(func,  # type: _coconut.typing.Callable[[_a, _a], _a]
     xs  # type: _coconut.typing.Sequence[_a]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return scan(func, reversed(xs))

def scanr(func,  # type: _coconut.typing.Callable[[_a, _b], _a]
     init,  # type: _a
     xs  # type: _coconut.typing.Iterable[_b]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return scan(func, xs, init)

scanr1 = scan

### Infinite lists:
@recursive_iterator
def iterate(func,  # type: _coconut.typing.Callable[[_a], _a]
     x  # type: _a
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return _coconut.itertools.chain.from_iterable((f() for f in (lambda: [x], lambda: iterate(func, func(x)))))

@recursive_iterator
def repeat(x  # type: _a
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return _coconut.itertools.chain.from_iterable((f() for f in (lambda: [x], lambda: repeat(x))))

def replicate(n,  # type: int
     x  # type: _a
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return _coconut_igetitem(repeat(x), _coconut.slice(None, n))

if TYPE_CHECKING:
    def cycle(xs  # type: _coconut.typing.Iterable[_a]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
        return _coconut.Ellipsis  # type: ignore
else:
    @recursive_iterator
    def cycle(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "xs" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("xs")
            if not _coconut_match_to_kwargs:
                xs = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check and not (len(xs) > 0):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def cycle(xs if len(xs) > 0) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def cycle(xs if len(xs) > 0) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return _coconut.itertools.chain.from_iterable((f() for f in (lambda: xs, lambda: cycle(xs))))



## Sublists:
def take(n,  # type: int
     xs  # type: _coconut.typing.Iterable[_a]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return _coconut_igetitem(xs, _coconut.slice(None, n))

def drop(n,  # type: int
     xs  # type: _coconut.typing.Iterable[_a]
    ):
# type: (...) -> _coconut.typing.Iterable[_a]
    return _coconut_igetitem(xs, _coconut.slice(n, None))

def splitAt(n,  # type: int
     xs  # type: _coconut.typing.Iterable[_a]
    ):
# type: (...) -> _t.Tuple[_coconut.typing.Iterable[_a], _coconut.typing.Iterable[_a]]
    reit = reiterable(xs)
    return _coconut_igetitem(reit, _coconut.slice(None, n)), _coconut_igetitem(reit, _coconut.slice(n, None))

takeWhile = takewhile

dropWhile = dropwhile

if TYPE_CHECKING:
    def span(cond,  # type: _coconut.typing.Callable[[_a], bool]
     xs  # type: _coconut.typing.Sequence[_a]
    ):
# type: (...) -> _coconut.typing.Sequence[_a]
        return _coconut.Ellipsis  # type: ignore
else:
    def span(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) == 2) and (_coconut.isinstance(_coconut_match_to_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to_args[1]) == 0):
            if not _coconut_match_to_kwargs:
                _coconut_match_check = True
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def span(_, []) = ([], [])'" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def span(_, []) = ([], [])'
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        return ([], [])

    @addpattern(span)
    def span(*_coconut_match_to_args, **_coconut_match_to_kwargs):
        _coconut_match_check = False
        if (_coconut.len(_coconut_match_to_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "cond" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "xs" in _coconut_match_to_kwargs)) == 1):
            _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("cond")
            _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("xs")
            if (_coconut.isinstance(_coconut_match_temp_1, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_1) >= 1) and (not _coconut_match_to_kwargs):
                cond = _coconut_match_temp_0
                xs = _coconut_match_temp_1
                t = _coconut.list(_coconut_match_temp_1[1:])
                x = _coconut_match_temp_1[0]
                _coconut_match_check = True
        if _coconut_match_check and not (cond(x)):
            _coconut_match_check = False
        if not _coconut_match_check:
            _coconut_match_err = _coconut_MatchError("pattern-matching failed for " "'def span(cond, [x] + t as xs if cond(x)) ='" " in " + _coconut.repr(_coconut.repr(_coconut_match_to_args)))
            _coconut_match_err.pattern = 'def span(cond, [x] + t as xs if cond(x)) ='
            _coconut_match_err.value = _coconut_match_to_args
            raise _coconut_match_err

        ys, zs = span(cond, t)
        return ([x] + ys, zs)

    @addpattern(span)
    def span(cond, xs):
        return ([], xs)

def break_(cond,  # type: _coconut.typing.Callable[[_a], bool]
     xs  # type: _coconut.typing.Sequence[_a]
    ):
# type: (...) -> _coconut.typing.Sequence[_a]
    return span(_coconut_forward_compose(cond, _coconut.operator.not_), xs)



## Searching lists:
def notElem(e,  # type: _a
     xs  # type: _coconut.typing.Sequence[_a]
    ):
# type: (...) -> bool
    return e not in xs

def lookup(key,  # type: _a
     assocs  # type: _coconut.typing.Iterable[_t.Tuple[_a, _b]]
    ):
# type: (...) -> Maybe
    try:
        return ((Just)((_coconut_igetitem(dropwhile(lambda pair: pair[0] != key, assocs), 0))[1]))
    except StopIteration:
        return nothing



## Zipping and unzipping lists:
zip = zip3 = zip  # type: ignore

def zipWith(func,  # type: _coconut.typing.Callable[..., _a]
     *iters):
# type: (...) -> _coconut.typing.Iterable[_a]
    return starmap(func, zip(*iters))

zipWith3 = zipWith

def unzip(xs  # type: _coconut.typing.Iterable[_coconut.typing.Iterable[_a]]
    ):
# type: (...) -> _coconut.typing.Iterable[_coconut.typing.Iterable[_a]]
    return zip(*xs)

unzip3 = unzip



## Functions on strings:
lines = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
lines = _coconut.operator.methodcaller("split", "\n")  # type: ignore

words = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
words = _coconut.operator.methodcaller("split")  # type: ignore

unlines = None  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[str]], str]
unlines = "\n".join

unwords = None  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[str]], str]
unwords = " ".join




# Converting to and from String:

## Converting to String:
show = str




# Basic input and output:

## Simple I/O operations:

### Output functions:
putStr = _coconut.functools.partial(print, end="")  # type: _coconut.typing.Callable[[str], None]
putChar = putStr

putStrLn = print


### Input functions:
getChar = _coconut.functools.partial(_sys.stdin.read, 1)  # type: _coconut.typing.Callable[[], str]

getLine = input

getContents = _sys.stdin.read  # type: _coconut.typing.Callable[[], str]

def interact(func  # type: _coconut.typing.Callable[[str], str]
    ):
# type: (...) -> None
    while True:
        (print)((func)(input()))


### Files:
FilePath = str

def readFile(fpath  # type: str
    ):
# type: (...) -> str
    with open(fpath, "r+") as f:
        return f.read()

def writeFile(fpath,  # type: str
     fstr  # type: str
    ):
# type: (...) -> None
    with open(fpath, "w+") as f:
        f.write(fstr)  # type: ignore

def appendFile(fpath,  # type: str
     fstr  # type: str
    ):
# type: (...) -> None
    with open(fpath, "a+") as f:
        f.write(fstr)  # type: ignore



## Exception handling:
IOError = IOError  # type: ignore

def ioError():
# type: (...) -> None
    raise IOError()

def userError(msg  # type: str
    ):
# type: (...) -> None
    raise IOError(msg)
