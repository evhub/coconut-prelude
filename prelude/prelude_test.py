#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd7b16ad3

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

from prelude import *  # type: ignore

def test_Bool():
    assert (isinstance)(True, Bool)
    assert (not_)(True) == False
    assert otherwise == True

def test_Maybe():
    assert (isinstance)(nothing, Maybe)
    assert (isinstance)(Just(2), Maybe)
    assert nothing == Nothing()
    assert nothing < Just(1) < Just(2)
    assert nothing <= Just(1) <= Just(1)
    assert Just(2) > Just(1) > nothing
    assert Just(1) >= Just(1) >= nothing
    assert Just(1) == Just(1)
    assert maybe(1, _coconut.functools.partial(_coconut.operator.add, 1), nothing) == 1
    assert maybe(1, _coconut.functools.partial(_coconut.operator.add, 1), Just(1)) == 2

def test_Either():
    assert (isinstance)(Left(1), Either)
    assert (isinstance)(Right(1), Either)
    assert Left(10) < Right(1)
    assert Left(1) != Right(1)
    assert Left(1) < Left(2) < Right(0) < Right(1)
    assert Left(2) == Left(2)
    assert either(lambda _=None: _ + 1, lambda _=None: _ * 2, Left(2)) == 3
    assert either(lambda _=None: _ + 1, lambda _=None: _ * 2, Right(2)) == 4

def test_Ordering():
    assert and_(((isinstance)(x, Ordering) for x in (lt, eq, gt)))
    assert lt == LT()
    assert eq == EQ()
    assert gt == GT()
    assert lt < eq < gt
    assert [fromEnum(x) for x in (lt, eq, gt)] == [0, 1, 2]
    assert (succ)(lt) == eq == (pred)(gt)
    assert (succ)(eq) == gt
    assert (pred)(eq) == lt

def test_Tuples():
    assert (fst)((1, 2)) == 1 == (snd)((2, 1))
    assert curry(_coconut.operator.add)(1)(2) == 3 == uncurry(_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.add))(1, 2)
    assert uncurry(curry(_coconut_minus))(3, 2) == 1

def test_Ord():
    assert and_(((isinstance)(x, Ord) and (isinstance)(x, Eq) for x in (True, nothing, Left(3), lt, 5, (1, 2),)))
    assert compare(1, 2) == lt == compare(nothing, Just(1))
    assert compare(2, 2) == eq == compare(Left(2), Left(2))
    assert compare(2, 1) == gt == compare(Right(1), Left(0))
    assert max(1, 2) == 2 == min(2, 3)
    assert min(eq, gt) == eq == max(lt, eq)

def test_Enum():
    assert and_(((isinstance)(x, Enum) for x in (True, lt, 5,)))
    assert (succ)(5) == 6 == (pred)(7)
    assert fromEnum(10) == 10
    assert (list)(_coconut_igetitem(enumFrom(2), _coconut.slice(None, 2))) == [2, 3]
    assert (list)(_coconut_igetitem(enumFromThen(2, 4), _coconut.slice(None, 3))) == [2, 4, 6]
    assert (list)(enumFromTo(2, 4)) == [2, 3, 4]
    assert (list)(enumFromThenTo(2, 4, 8)) == [2, 4, 6, 8] == (list)(enumFromThenTo(2, 4, 9))
    assert (list)(enumFromThenTo(2, 4, 1)) == []
    assert (list)(enumFromThen(10, 1)) == []
    assert (list)(enumFromThenTo(4, 3, 1)) == [4, 3, 2, 1]
    assert (list)(_coconut_igetitem(enumFromThen(1, 1), _coconut.slice(None, 3))) == [1, 1, 1] == (list)(_coconut_igetitem(enumFromThenTo(1, 1, 1), _coconut.slice(None, 3)))
    assert (list)(enumFromTo(1, 1)) == [1]

def test_Bounded():
    assert minBound(True) is False
    assert maxBound(False) is True
    assert minBound(eq) == lt
    assert maxBound(eq) == gt

def test_Num():
    assert negate(2) == -2 == negate((over)(2, 1))
    assert abs(-10) == 10 == abs((over)(10, 1))
    assert signum(0) == 0
    assert signum(-2) == -1 == signum(-2.5)
    assert signum(10) == 1 == signum((over)(2, 2))
    assert fromInteger(10) == 10

def test_Real():
    assert toRational(10) == (over)(10, 1)
    assert toRational((over)(1, 3)) == (over)(1, 3)
    assert toRational(1.5) == (over)(3, 2)

def test_Integral():
    assert (isinstance)(10, Integral)
    assert quot(10, 3) == 3 == div(10, 3)
    assert rem(10, 3) == 1 == mod(10, 3)
    assert div(-10, 3) == -4 == div(10, -3)
    assert quot(-10, 3) == -3 == quot(10, -3)
    assert mod(-10, 3) == 2
    assert mod(10, -3) == -2
    assert rem(-10, 3) == -1
    assert rem(10, -3) == 1
    assert quotRem(-10, -3) == (3, -1) == divMod(-10, -3)
    assert quotRem(10, -3) == (-3, 1)
    assert quotRem(-10, 3) == (-3, -1)
    assert toInteger(10) == 10

def test_Fractional():
    assert (recip)((over)(2, 3)) == (over)(3, 2)
    assert (fromRational)((over)(1, 3)) == (over)(1, 3)

def test_RealFrac():
    assert properFraction((over)(10, 3)) == (3, (over)(1, 3))
    assert (truncate)((over)(4, 3)) == 1
    assert (round)((over)(5, 3)) == 2
    assert (truncate)((over)(-4, 3)) == -1
    assert (floor)((over)(-4, 3)) == -2
    assert (round)((over)(-4, 3)) == -1
    assert (ceiling)((over)(-4, 3)) == -1
    assert (ceiling)((over)(4, 3)) == 2
    assert (floor)((over)(4, 3)) == 1

def test_RealFloat():
    assert floatRadix(1.2) == 2
    assert floatDigits(0.5) == 53
    assert floatRange(0.1) == (-1021, 1024)
    assert scaleFloat(1, 1.5) == 3
    assert not isNegativeZero(0.0)
    assert isNegativeZero(float("-0"))
    assert isIEEE(0.9) is True

def test_Numeric_functions():
    assert subtract(2, 1) == -1
    assert even(2)
    assert not even(3)
    assert odd(3)
    assert not odd(2)
    assert gcd(4, 6) == 2 == gcd(-4, -6)
    assert lcm(0, 2) == 0 == lcm(2, 0)
    assert lcm(4, 6) == 12 == lcm(-4, -6)
    assert fromIntegral(10) == 10
    assert realToFrac(0.5) == (over)(1, 2)

def test_Monoids():
    pass

def test_Functor():
    assert (fmap)(error, nothing) == nothing
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), Just(2)) == Just(3)
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), Left(10)) == Left(10)
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), [1, 2, 3]) == [2, 3, 4]
    assert (fmapConst)(10, [1, 2, 3]) == [10, 10, 10]
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))

def test_Applicative():
    assert (ap)(nothing, Just(10)) == nothing
    assert (ap)(Just(_coconut.functools.partial(_coconut.operator.add, 1)), Just(2)) == Just(3)
    assert (ap)([_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 3)], [10, 20, 30]) == [11, 21, 31, 30, 60, 90]
    assert (ap)((_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 3)), (10, 20, 30)) == (11, 21, 31, 30, 60, 90)
    assert (ap)((_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 3)), _coconut.frozenset((10, 20, 30))) == _coconut.frozenset((11, 21, 31, 30, 60, 90))
    assert (seqAr)(nothing, Just(1)) == nothing
    assert (seqAl)(Just(1), nothing) == nothing
    assert (seqAr)(Just(1), Just(2)) == Just(2) == (seqAl)(Just(2), Just(1))
    assert liftA2(_coconut.operator.add, [1, 2, 3], [10, 20, 30]) == [11, 21, 31, 12, 22, 32, 13, 23, 33]
    assert (ap)(pure(error), nothing) == nothing
    assert (ap)(pure(lambda _=None: _ + 1), Just(2)) == Just(3)
    assert (ap)(pure(lambda _=None: _ + 1), Left(10)) == Left(10)
    assert (ap)(pure(lambda _=None: _ + 1), [1, 2, 3]) == [2, 3, 4]
    assert (ap)(pure(lambda _=None: _ + 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))

def test_Monad():
    assert nothing == (bind)(nothing, Just)
    assert nothing == (bindFrom)(Just, nothing)
    assert Just(2) == (bind)(Just(1), lambda x: Just(x + 1))
    assert Left(2) == (bind)(Left(2), Right)
    assert Left(2) == (bindFrom)(Right, Left(2))
    assert Left(2) == (bind)(Right(2), Left)
    assert Left(2) == (bindFrom)(Left, Right(2))
    assert Just(2) == (seqM)(Just(1), Just(2))
    assert nothing == (seqM)(nothing, Just(2))
    assert Right(2) == (seqM)(Right(1), Right(2))
    assert Left(1) == (seqM)(Left(1), Right(2))
    assert [] == (seqM)([], [1])
    assert nothing == (bind)(Just(1), _coconut_forward_compose(str, fail))
    assert Left(1) == (bind)(Left(1), _coconut_forward_compose(str, fail))
    assert Left("1") == (bind)(Right(1), _coconut_forward_compose(str, fail))
    assert [] == (bind)([1, 2], _coconut_forward_compose(str, fail))
    assert Just(1) == (bind)(Just(1), return_)
    assert Just(2) == (bind)(Just(1), lambda _=None: return_(2))
    assert nothing == (bind)(nothing, return_)
    assert [1] == (bind)([1], return_)
    assert [2, 3] == (bind)([1, 2], lambda x: return_(x + 1))
    assert [] == (bind)([], return_)
    assert Right(1) == (bind)(Right(1), return_)
    assert Left(1) == (bind)(Left(1), return_(2))
    assert Right(2) == (bind)(Right(1), lambda x: return_(x + 1))
    assert Just(1) == join(Just(Just(1)))
    assert nothing == join(Just(nothing))
    assert nothing == join(nothing)
    assert [1, 2, 3, 4, 5, 6] == join([[1, 2, 3], [], [4], [5, 6]])
    assert Left(3) == do([Right(1), Right(2), Left(3), Right(4),], lambda *xs: error(repr(xs)))

def test_Foldable():
    assert sequence_([[1], [2], [3]]) == [()]
    assert sequence_([[1], [], [3]]) == []
    assert sequence_([Just(1), Just(2), Just(3)]) == Just(())
    assert sequence_([Just(1), nothing, Just(3)]) == nothing
    assert sequence_([Right(1), Right(2), Right(3)]) == Right(())
    assert sequence_([Right(1), Left(2), Right(3)]) == Left(2)
    assert foldr(_coconut.operator.pow, 2, [1, 2, 3]) == 1
    assert foldl(_coconut.operator.pow, 2, [1, 2, 3]) == 64
    assert (list)(foldr(cons, [], [2, 3, 4])) == [2, 3, 4]
    assert (list)(foldl(flip(cons), [], [2, 3, 4])) == [4, 3, 2]

def test_Traversable():
    assert sequenceA([Right(1), Right(2), Left(3), Right(4)]) == Left(3)
    assert sequenceA([[1, 2, 3], [], [4], [5, 6]]) == []

if __name__ == "__main__":
    for var, val in globals().items():
        if var.startswith("test_"):
            val()
    print("<success>")
