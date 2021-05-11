#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x87982dcf

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
from prelude import *  # type: ignore


# Tests:
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
    assert minBound((False, gt)) == (False, lt)
    assert maxBound((True, lt)) == (True, gt)

def test_Rational():
    assert Rational(1, 3) == (over)(1, 3)

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
    assert mappend(Just([]), mempty) == Just([]) == mappend(mempty, Just([]))
    assert mappend(nothing, Just([])) == Just([]) == mappend(Just([]), nothing)
    assert mappend(nothing, pure(1)) == Just(1)
    assert mappend(fail("derp"), Just(2)) == Just(2)
    assert mappend([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert mappend(Just([1, 2]), Just([3, 4])) == Just([1, 2, 3, 4])
    assert mappend(lt, gt) == lt == mappend(eq, lt)
    assert mappend(gt, lt) == gt == mappend(gt, eq)
    assert mappend(eq, mempty) == eq == mappend(mempty, eq)
    assert mappend(([1], [2]), ([3], [4])) == ([1, 3], [2, 4])
    assert mconcat([[1], [2, 3]]) == [1, 2, 3]

def test_Functor():
    assert (fmap)(error, nothing) == nothing
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), Just(2)) == Just(3)
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), Left(10)) == Left(10)
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), [1, 2, 3]) == [2, 3, 4]
    assert (fmapConst)(10, [1, 2, 3]) == [10, 10, 10]
    assert (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))

def test_Applicative():
    assert pure("12") == (fmap)(lambda s: s + "2", pure("1"))
    assert (ap)(nothing, Just(10)) == nothing
    assert (ap)(Just(_coconut.functools.partial(_coconut.operator.add, 1)), Just(2)) == Just(3)
    assert (ap)([_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 3)], [10, 20, 30]) == [11, 21, 31, 30, 60, 90]
    assert (ap)((_coconut.functools.partial(_coconut.operator.add, 1), _coconut.functools.partial(_coconut.operator.mul, 3)), (10, 20, 30)) == (11, 21, 31, 30, 60, 90)
    assert (ap)(pure(error), nothing) == nothing
    assert (ap)(pure(lambda _=None: _ + 1), Just(2)) == Just(3)
    assert (ap)(pure(lambda _=None: _ + 1), Left(10)) == Left(10)
    assert (ap)(pure(lambda _=None: _ + 1), [1, 2, 3]) == [2, 3, 4]
    assert (ap)(pure(lambda _=None: _ + 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))
    assert (ap)(fail("derp"), Right(1)) == Left("derp")
    assert (seqAr)(nothing, Just(1)) == nothing
    assert (seqAl)(Just(1), nothing) == nothing
    assert (seqAr)(Just(1), Just(2)) == Just(2) == (seqAl)(Just(2), Just(1))
    assert liftA2(_coconut.operator.add)([1, 2, 3], [10, 20, 30]) == [11, 21, 31, 12, 22, 32, 13, 23, 33]

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
    assert fail("derp") == (fmap)(_coconut.functools.partial(_coconut.operator.add, 1), fail("derp"))
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
    assert join(return_(return_(5))) == return_(5)
    assert Just(1) == join(Just(Just(1)))
    assert nothing == join(Just(nothing))
    assert nothing == join(nothing)
    assert [1, 2, 3, 4, 5, 6] == join([[1, 2, 3], [], [4], [5, 6]])
    assert [1] == join([fail("derp"), return_(1)])
    assert Left(3) == do([Right(1), Right(2), Left(3), Right(4),], lambda *xs: error(repr(xs)))
    _coconut_decorator_0 = _coconut.functools.partial(do, [Right(1), Right(2)])
    @_coconut_decorator_0
    @_coconut_tco
    def right3(x, y):
        return _coconut_tail_call(Right, x + y)
    assert right3 == Right(3)
    global glob
    glob = 1
    def _coconut_lambda_0(x):
        global glob
        glob = 2
        return Just(glob)
    assert nothing == (bind)(nothing, (_coconut_lambda_0))
    assert glob == 1

def test_Foldable():
    assert sequence_([[1], [2], [3]]) == [()]
    assert sequence_([[1], [], [3]]) == []
    assert sequence_([Just(1), Just(2), Just(3)]) == Just(())
    assert sequence_([Just(1), nothing, Just(3)]) == nothing
    assert sequence_([Right(1), Right(2), Right(3)]) == Right(())
    assert sequence_([Right(1), Left(2), Right(3)]) == Left(2)
    assert mapM_(Just, [1, 2, 3]) == Just(())
    assert foldMap(lambda x: [x, x], [[1], [2, 3]]) == [[1], [1], [2, 3], [2, 3]]
    assert foldr(_coconut.operator.pow, 2, [1, 2, 3]) == 1
    assert foldl(_coconut.operator.pow, 2, [1, 2, 3]) == 64
    assert (list)(foldr(cons, [], [2, 3, 4])) == [2, 3, 4]
    assert (list)(foldl(flip(cons), [], [2, 3, 4])) == [4, 3, 2]
    assert null([])
    assert not null([1])
    assert length([]) == 0
    assert length([1, 2, 3]) == 3
    assert (elem)(1, [1, 2, 3])
    assert not (elem)(1, [2, 3])
    assert maximum([1, 2, 3]) == 3
    assert minimum([1, 2, 3]) == 1
    assert sum([2, 3, 4]) == 9
    assert product([2, 3, 4]) == 24

def test_Traversable():
    for _sequence in [sequenceA, sequence]:
        assert _sequence([Just(1), nothing, Just(3)]) == nothing
        assert _sequence([Right(1), Right(2), Left(3), Right(4)]) == Left(3)
        assert _sequence([[1, 2, 3], [], [4], [5, 6]]) == []
        assert _sequence([Just(1), Just(2), Just(3)]) == Just([1, 2, 3])
        assert _sequence([Right(1), Right(2), Right(3)]) == Right([1, 2, 3])
        assert _sequence([[1, 2], [3]]) == [[1, 3], [2, 3]]
    for _traverse in [traverse, mapM]:
        assert _traverse(lambda x: [x], [1, 2, 3]) == [[1, 2, 3]]
        assert _traverse(Just, [Just(1), nothing, Just(2)]) == Just([Just(1), nothing, Just(2)])

def test_Miscellaneous_functions():
    assert id(10) == 10
    assert const(10)(5)
    assert ((dot)(abs, _coconut.operator.add))(-2, -3) == 5
    assert flip(_coconut_minus)(10, 5) == -5
    assert (apply)(abs, -2) == 2
    assert ((apply)(_coconut.operator.truediv, 6))(2) == 3
    assert (apply)((apply)((apply)((lambda x, y, z: (x, y, z)), 1), 2), 3) == (1, 2, 3)
    assert until(lambda x: x < 0, _coconut.functools.partial(subtract, 1), 10) == -1
    assert asTypeOf(5, 10) == 5
    assert asTypeOf(pure([]), nothing) == Just([])
    assert asTypeOf(fail("herp"), Right(1)) == Left("herp")
    assert asTypeOf(mempty, Just([])) == nothing
    class Test(_coconut.collections.namedtuple("Test", ('x',))):
        __slots__ = ()
        __ne__ = _coconut.object.__ne__
        def __eq__(self, other):
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
        def __hash__(self):
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
        __match_args__ = ('x',)
        @staticmethod
        @_coconut_tco
        def __mempty__():
            return _coconut_tail_call(pure, 0)

        @staticmethod
        @_coconut_tco
        def __pure__(x):
            return _coconut_tail_call(Test, x)
    assert (asTypeOf)(mempty, Test(1)) == Test(0)
    for _error in [error, errorWithoutStackTrace]:
        try:
            _error("derp")
        except Exception as err:
            assert str(err) == "derp"
        else:
            assert False, "expected error"
    assert undefined == undefined
    assert seq(1, 2) == 2
    assert (cbv)(abs, -2) == 2

def test_List_operations():
    assert (list)((cons)(1, [2, 3])) == [1, 2, 3]
    assert (list)(map(_coconut.functools.partial(_coconut.operator.add, 1), [1, 2, 3])) == [2, 3, 4]
    assert (list)((chain)([1, 2], [3, 4])) == [1, 2, 3, 4]
    assert (list)(filter(lambda x: x > 1, [1, 2, 3])) == [2, 3]
    assert head([1, 2, 3]) == 1
    assert last([1, 2, 3]) == 3
    assert tail([1, 2, 3]) == [2, 3]
    assert init([1, 2, 3]) == [1, 2]
    assert (at)([1, 2, 3], 1) == 2 == (at)(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: 1, lambda: 2, lambda: 3)), 1)
    assert (list)(reverse([1, 2, 3])) == [3, 2, 1]

def test_Special_folds():
    assert and_([True, True])
    assert or_([False, True])
    assert any(_coconut.functools.partial(_coconut.operator.eq, 2), [1, 2, 3])
    assert not all(_coconut.functools.partial(_coconut.operator.eq, 2), [1, 2, 3])
    assert (list)(concat([])) == []
    assert (list)(concat([[]])) == []
    assert (list)(concat([[1], [2, 3]])) == [1, 2, 3]
    assert (list)(concatMap(lambda x: [x, x], [1, 2])) == [1, 1, 2, 2]

def test_Scans():
    assert (list)(scanl(_coconut.operator.add, 0, [1, 2, 3])) == [0, 1, 3, 6]
    assert (list)(scanl1(_coconut.operator.add, [1, 2, 3])) == [1, 3, 6]
    assert (list)(scanr(_coconut.operator.add, 0, [1, 2, 3])) == [6, 5, 3, 0]
    assert (list)(scanr1(_coconut.operator.add, [1, 2, 3])) == [6, 5, 3]

def test_Infinite_lists():
    assert (list)((take)(3, iterate(_coconut.functools.partial(subtract, 1), 3))) == [3, 2, 1]
    assert (list)(_coconut_igetitem(repeat(1), _coconut.slice(None, 3))) == [1, 1, 1] == (list)(replicate(3, 1))
    assert (list)(_coconut_igetitem(cycle([1, 2]), _coconut.slice(None, 4))) == [1, 2, 1, 2]

def test_Sublists():
    assert take(2, [1, 2, 3]) == [1, 2]
    assert drop(2, [1, 2, 3]) == [3]
    assert (fmap)(list, splitAt(2, [1, 2, 3, 4])) == ([1, 2], [3, 4])
    assert (list)(takeWhile((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.gt))(2), [0, 1, 2, 3])) == [0, 1]
    assert (list)(dropWhile((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.gt))(2), [0, 1, 2, 3])) == [2, 3]
    assert span((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.gt))(2), [0, 1, 2, 3]) == ([0, 1], [2, 3])
    assert break_((_coconut.functools.partial(_coconut.functools.partial, _coconut.operator.lt))(2), [1, 2, 3]) == ([1, 2], [3])

def test_Searching_lists():
    assert (notElem)(10, [1, 2, 3])
    assert lookup("b", [("a", 1), ("b", 2), ("c", 3)]) == Just(2)
    assert lookup("b", [("a", 1)]) == nothing
    assert lookup("a", []) == nothing

def test_Zipping_and_unzipping_lists():
    assert (list)(zip([1, 2], [3, 4])) == [(1, 3), (2, 4)]
    assert unzip([(1, 3), (2, 4)]) == ([1, 2], [3, 4])
    assert (list)(zip3([1, 2], [3, 4], [5, 6])) == [(1, 3, 5), (2, 4, 6)]
    assert unzip3([(1, 3, 5), (2, 4, 6)]) == ([1, 2], [3, 4], [5, 6])
    assert (list)(zipWith(_coconut.operator.add, [1, 2], [10, 20])) == [11, 22]
    assert (list)(zipWith3(lambda x, y, z: sum([x, y, z]), [1, 2], [10, 20], [100, 200])) == [111, 222]

def test_Functions_on_strings():
    assert lines("\nabc\ndef\n") == ["", "abc", "def"]
    assert words(" abc def ") == ["abc", "def"]
    assert unlines(["abc", "def"]) == "abc\ndef\n"
    assert unlines(["abc"]) == "abc\n"
    assert unlines([]) == ""
    assert unwords(["abc", "def"]) == "abc def"
    assert unwords(["abc"]) == "abc"
    assert unwords([]) == ""

def test_Converting_to_String():
    assert show(1) == "1"
    assert show("abc") == "'abc'"
    assert ((shows)(3))("abc") == "3abc"
    assert ((showList)([1]))("abc") == "[1]abc"
    assert ((showList)(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: 1, lambda: 2))))("") == "[1, 2]"
    assert ((showString)("abc"))("def") == "abcdef"
    assert ((showChar)("a"))("bcd") == "abcd"
    assert ((showParen)(True, showString("abc")))("def") == "(abc)def"
    assert ((showParen)(False, showString("abc")))("def") == "abcdef"

def test_Converting_from_String():
    assert read("[]") == []
    assert read("10") == 10
    assert read('"abc"') == "abc"

def test_IO():
    assert unIO(pure(5)) == 5
    assert (unIO)(mempty) == mempty
    assert (unIO)(mappend(mempty, asIO(pure(gt)))) == gt
    assert (unIO)((fmap)(lambda _=None: _ * 2, pure(5))) == 10
    try:
        unIO(fail("herp"))
    except IOError as err:
        assert str(err) == "herp"
    else:
        assert False, "expected error"
    assert 6 == (unIO)((bind)(pure(5), lambda x: pure(x + 1)))
    _coconut_decorator_1 = _coconut.functools.partial(do, [asIO(pure(1)), pure(2)])
    @unIO
    @_coconut_decorator_1
    @_coconut_tco
    def three(x1, x2):
        return _coconut_tail_call(pure, x1 + x2)
    assert three == 3

def test_Exception_handling():
    try:
        (unIO)(ioError(IOError("derp")))
    except IOError as err:
        assert str(err) == "derp"
    else:
        assert False, "expected error"
    assert (isinstance)(userError("derp"), IOError)
    assert (str)(userError("derp")) == "derp"


# Run tests:
if __name__ == "__main__":
    for var, val in globals().items():
        if var.startswith("test_"):
            val()
    print("<success>")
