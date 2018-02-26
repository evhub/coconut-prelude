#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb1559b01

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

if TYPE_CHECKING:
    import typing as _t
    _T = _t.TypeVar("_T")
    _U = _t.TypeVar("_U")
    _V = _t.TypeVar("_V")




# Standard types, classes, and related functions:

## Basic data types:

#### Bool:
Bool = bool

otherwise = True  # type: bool

#### Maybe:
class Maybe(_coconut.object): pass

class Nothing(_coconut.collections.namedtuple("Nothing", ""), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__
nothing = Nothing()  # type: Maybe

class Just(_coconut_NamedTuple("Just", [("x", '_t.Any')]), Maybe):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

if TYPE_CHECKING:
    def maybe(default,  # type: _T
     func,  # type: _coconut.typing.Callable[[_t.Any], _T]
     x  # type: Maybe
    ):
# type: (...) -> _T
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

class Left(_coconut_NamedTuple("Left", [("x", '_t.Any')]), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

class Right(_coconut_NamedTuple("Right", [("x", '_t.Any')]), Either):
    __slots__ = ()
    __ne__ = _coconut.object.__ne__

if TYPE_CHECKING:
    def either(left_func,  # type: _coconut.typing.Callable[[_t.Any], _T]
     right_func,  # type: _coconut.typing.Callable[[_t.Any], _T]
     x  # type: Either
    ):
# type: (...) -> _T
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

#### Char/String:
String = string = str


### Tuples:
fst = _coconut.operator.itemgetter(0)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _T]

snd = _coconut.operator.itemgetter(1)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _T]

def curry(func  # type: _coconut.typing.Callable[[_T, _U], _V]
    ):
# type: (...) -> _coconut.typing.Callable[[_T], _coconut.typing.Callable[[_U], _V]]
    return _coconut.functools.partial(_coconut.functools.partial, func)  # type: ignore

def uncurry(func  # type: _coconut.typing.Callable[[_T], _coconut.typing.Callable[[_U], _V]]
    ):
# type: (...) -> _coconut.typing.Callable[[_T, _U], _V]
    return lambda x, y: func(x)(y)



## Basic type classes:

#### Ord:
if TYPE_CHECKING:
    def compare(x, y):
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

#### Enum:
succ = _coconut.functools.partial(_coconut.operator.add, 1)  # type: _coconut.typing.Callable[[_t.Any], _t.Any]

pred = _coconut_partial(_coconut_minus, {1: 1}, 2)  # type: _coconut.typing.Callable[[_t.Any], _t.Any]



## Numbers:

### Numeric types:
Integer = integer = int

Double = double = float


### Numeric type classes:

#### Num:
if TYPE_CHECKING:
    Num = _t.Union[float, int]
num = (float, int)

negate = _coconut_minus

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

#### Integral:
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

div = _coconut.operator.floordiv  # type: _coconut.typing.Callable[[int, int], int]

mod = _coconut.operator.mod  # type: _coconut.typing.Callable[[int, int], int]

def quotRem(x,  # type: int
     y  # type: int
    ):
# type: (...) -> _t.Tuple[int, int]
    divxy, modxy = divmod(x, y)
    return divxy + (1 if modxy < 0 else 0), modxy - (y if modxy < 0 else 0)

divMod = divmod

#### Fractional:
recip = _coconut.functools.partial(_coconut.operator.truediv, 1)  # type: _coconut.typing.Callable[[Num], Num]

#### Floating:
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
truncate = int

round = round  # type: ignore

from math import ceil as ceiling
from math import floor

#### RealFloat:
from math import isnan as isNaN
from math import isinf as isInfinite
from math import atan2


### Numeric functions:
def even(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 0

def odd(x  # type: int
    ):
# type: (...) -> bool
    return x % 2 == 1

def gcd(x,  # type: int
     y  # type: int
    ):
# type: (...) -> int
    while True:
        if y == 0:
            return abs(x)
        abs_y = abs(y)
        if gcd is _coconut_recursive_func_16:  # tail recursive
            x, y = abs_y, abs(x) % abs_y  # tail recursive
            continue  # tail recursive
        else:  # tail recursive
            return gcd(abs_y, abs(x) % abs_y)  # tail recursive

        return None
_coconut_recursive_func_16 = gcd
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
        return (abs)(((quot)(x, gcd(x, y))) * y)



## Folds and traversals:
def foldr(func,  # type: _coconut.typing.Callable[[_T, _U], _T]
     init,  # type: _T
     xs  # type: _coconut.typing.Iterable[_U]
    ):
# type: (...) -> _T
    return reduce(func, xs, init)

def foldl(func,  # type: _coconut.typing.Callable[[_T, _U], _T]
     init,  # type: _T
     xs  # type: _coconut.typing.Sequence[_U]
    ):
# type: (...) -> _T
    return reduce(func, reversed(xs), init)

foldr1 = reduce

def foldl1(func,  # type: _coconut.typing.Callable[[_T, _T], _T]
     xs  # type: _coconut.typing.Sequence[_T]
    ):
    return reduce(func, reversed(xs))

def null(xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> bool
    return len(xs) == 0

length = len

def elem(e,  # type: _T
     xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> bool
    return e in xs

maximum = max

minimum = min

sum = sum  # type: ignore

product = _coconut.functools.partial(reduce, _coconut.operator.mul)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _T]



## Miscellaneous functions:
def id(x  # type: _T
    ):
# type: (...) -> _T
    return x

def const(x,  # type: _T
     _):
# type: (...) -> _T
    return x

def flip(func  # type: _coconut.typing.Callable[[_T, _U], _V]
    ):
# type: (...) -> _coconut.typing.Callable[[_U, _T], _V]
    return lambda x, y: func(y, x)

def until(cond,  # type: _coconut.typing.Callable[[_T], bool]
     func,  # type: _coconut.typing.Callable[[_T], _T]
     x  # type: _T
    ):
# type: (...) -> _T
    while True:
        if cond(x):
            return x
        if until is _coconut_recursive_func_27:  # tail recursive
            cond, func, x = cond, func, func(x)  # tail recursive
            continue  # tail recursive
        else:  # tail recursive
            return until(cond, func, func(x))  # tail recursive

        return None
_coconut_recursive_func_27 = until
def error(msg  # type: str
    ):
# type: (...) -> None
    raise Exception(msg)

undefined = None  # type: _t.Any




# List operations:
map = map  # type: ignore

filter = filter  # type: ignore

head = _coconut.functools.partial(_coconut_igetitem, index=0)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _T]

last = _coconut.functools.partial(_coconut_igetitem, index=-1)  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _T]

tail = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _coconut.typing.Iterable[_T]]
tail = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(1, None))  # type: ignore

init = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _coconut.typing.Iterable[_T]]
init = _coconut.functools.partial(_coconut_igetitem, index=_coconut.slice(None, -1))  # type: ignore

reverse = reversed



## Special folds:
and_ = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], bool]
and_ = all  # type: ignore

or_ = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_T]], bool]
or_ = any  # type: ignore

any = _coconut_forward_compose(map, or_)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_T], bool]), _coconut.typing.Iterable[_T]], bool]

all = _coconut_forward_compose(map, and_)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_T], bool]), _coconut.typing.Iterable[_T]], bool]

concat = None  # type: _coconut.typing.Callable[[_coconut.typing.Iterable[_coconut.typing.Iterable[_T]]], _coconut.typing.Iterable[_T]]
concat = _coconut.functools.partial(reduce, _coconut.itertools.chain)  # type: ignore

concatMap = _coconut_forward_compose(map, concat)  # type: _coconut.typing.Callable[[(_coconut.typing.Callable[[_coconut.typing.Iterable[_T]], _coconut.typing.Iterable[_U]]), _coconut.typing.Iterable[_coconut.typing.Iterable[_T]]], _coconut.typing.Iterable[_U]]



## Building lists:

### Scans:
def scanl(func,  # type: _coconut.typing.Callable[[_T, _U], _T]
     init,  # type: _T
     xs  # type: _coconut.typing.Sequence[_U]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return scan(func, reversed(xs), init)

def scanl1(func,  # type: _coconut.typing.Callable[[_T, _T], _T]
     xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return scan(func, reversed(xs))

def scanr(func,  # type: _coconut.typing.Callable[[_T, _U], _T]
     init,  # type: _T
     xs  # type: _coconut.typing.Iterable[_U]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return scan(func, xs, init)

scanr1 = scan

### Infinite lists:
@recursive_iterator
def iterate(func,  # type: _coconut.typing.Callable[[_T], _T]
     x  # type: _T
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return _coconut.itertools.chain.from_iterable((f() for f in (lambda: [x], lambda: iterate(func, func(x)))))

@recursive_iterator
def repeat(x  # type: _T
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return _coconut.itertools.chain.from_iterable((f() for f in (lambda: [x], lambda: repeat(x))))

def replicate(n,  # type: int
     x  # type: _T
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return _coconut_igetitem(repeat(x), _coconut.slice(None, n))

if TYPE_CHECKING:
    def cycle(xs  # type: _coconut.typing.Iterable[_T]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
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
     xs  # type: _coconut.typing.Iterable[_T]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return _coconut_igetitem(xs, _coconut.slice(None, n))

def drop(n,  # type: int
     xs  # type: _coconut.typing.Iterable[_T]
    ):
# type: (...) -> _coconut.typing.Iterable[_T]
    return _coconut_igetitem(xs, _coconut.slice(n, None))

def splitAt(n,  # type: int
     xs  # type: _coconut.typing.Iterable[_T]
    ):
# type: (...) -> _t.Tuple[_coconut.typing.Iterable[_T], _coconut.typing.Iterable[_T]]
    reit = reiterable(xs)
    return _coconut_igetitem(reit, _coconut.slice(None, n)), _coconut_igetitem(reit, _coconut.slice(n, None))

takeWhile = takewhile

dropWhile = dropwhile

if TYPE_CHECKING:
    def span(cond,  # type: _coconut.typing.Callable[[_T], bool]
     xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> _coconut.typing.Sequence[_T]
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

def break_(cond,  # type: _coconut.typing.Callable[[_T], bool]
     xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> _coconut.typing.Sequence[_T]
    return span(_coconut_forward_compose(cond, _coconut.operator.not_), xs)



## Searching lists:
def notElem(e,  # type: _T
     xs  # type: _coconut.typing.Sequence[_T]
    ):
# type: (...) -> bool
    return e not in xs

def lookup(key,  # type: _T
     assocs  # type: _coconut.typing.Iterable[_t.Tuple[_T, _U]]
    ):
# type: (...) -> Maybe
    try:
        return ((Just)((_coconut_igetitem(dropwhile(lambda pair: pair[0] != key, assocs), 0))[1]))
    except StopIteration:
        return nothing



## Zipping and unzipping lists:
zip = zip3 = zip  # type: ignore

def zipWith(func,  # type: _coconut.typing.Callable[..., _T]
     *iters):
# type: (...) -> _coconut.typing.Iterable[_T]
    return starmap(func, zip(*iters))

zipWith3 = zipWith

def unzip(xs  # type: _coconut.typing.Iterable[_coconut.typing.Iterable[_T]]
    ):
# type: (...) -> _coconut.typing.Iterable[_coconut.typing.Iterable[_T]]
    return zip(*xs)

unzip3 = unzip



## Functions on strings:
lines = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
lines = _coconut.operator.methodcaller("split", "\n")  # type: ignore

words = None  # type: _coconut.typing.Callable[[str], _coconut.typing.Sequence[str]]
words = _coconut.operator.methodcaller("split")  # type: ignore

unlines = "\n".join  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[str]], str]

unwords = " ".join  # type: _coconut.typing.Callable[[_coconut.typing.Sequence[str]], str]




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
