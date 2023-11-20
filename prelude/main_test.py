#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8c39a9f6

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
def test_Bool():  #6 (line in Coconut source)
    assert (isinstance)(True, Bool)  #7 (line in Coconut source)
    assert (not_)(True) == False  #8 (line in Coconut source)
    assert otherwise == True  #9 (line in Coconut source)


def test_Maybe():  #11 (line in Coconut source)
    assert (isinstance)(nothing, Maybe)  #12 (line in Coconut source)
    assert (isinstance)(Just(2), Maybe)  #13 (line in Coconut source)
    assert nothing == Nothing()  #14 (line in Coconut source)
    assert nothing < Just(1) < Just(2)  #15 (line in Coconut source)
    assert nothing <= Just(1) <= Just(1)  #16 (line in Coconut source)
    assert Just(2) > Just(1) > nothing  #17 (line in Coconut source)
    assert Just(1) >= Just(1) >= nothing  #18 (line in Coconut source)
    assert Just(1) == Just(1)  #19 (line in Coconut source)
    assert maybe(1, _coconut_partial((_coconut.operator.add), 1), nothing) == 1  #20 (line in Coconut source)
    assert maybe(1, _coconut_partial((_coconut.operator.add), 1), Just(1)) == 2  #21 (line in Coconut source)


def test_Either():  #23 (line in Coconut source)
    assert (isinstance)(Left(1), Either)  #24 (line in Coconut source)
    assert (isinstance)(Right(1), Either)  #25 (line in Coconut source)
    assert Left(10) < Right(1)  #26 (line in Coconut source)
    assert Left(1) != Right(1)  #27 (line in Coconut source)
    assert Left(1) < Left(2) < Right(0) < Right(1)  #28 (line in Coconut source)
    assert Left(2) == Left(2)  #29 (line in Coconut source)
    assert either(lambda _=None: _ + 1, lambda _=None: _ * 2, Left(2)) == 3  #30 (line in Coconut source)
    assert either(lambda _=None: _ + 1, lambda _=None: _ * 2, Right(2)) == 4  #31 (line in Coconut source)


def test_Ordering():  #33 (line in Coconut source)
    assert and_(((isinstance)(x, Ordering) for x in (lt, eq, gt)))  #34 (line in Coconut source)
    assert lt == LT()  #35 (line in Coconut source)
    assert eq == EQ()  #36 (line in Coconut source)
    assert gt == GT()  #37 (line in Coconut source)
    assert lt < eq < gt  #38 (line in Coconut source)
    assert [fromEnum(x) for x in (lt, eq, gt)] == [0, 1, 2]  #39 (line in Coconut source)
    assert (succ)(lt) == eq == (pred)(gt)  #40 (line in Coconut source)
    assert (succ)(eq) == gt  #41 (line in Coconut source)
    assert (pred)(eq) == lt  #42 (line in Coconut source)


def test_Tuples():  #44 (line in Coconut source)
    assert (fst)((1, 2)) == 1 == (snd)((2, 1))  #45 (line in Coconut source)
    @_coconut_mark_as_match  #46 (line in Coconut source)
    @_coconut_mark_as_match  #46 (line in Coconut source)
    def _coconut_lambda_0(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #46 (line in Coconut source)
        _coconut_match_check_0 = False  #46 (line in Coconut source)
        _coconut_match_set_name_x = _coconut_sentinel  #46 (line in Coconut source)
        _coconut_match_set_name_y = _coconut_sentinel  #46 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #46 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #46 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #46 (line in Coconut source)
        if _coconut.len(_coconut_match_args) == 1:  #46 (line in Coconut source)
            if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 2):  #46 (line in Coconut source)
                _coconut_match_set_name_x = _coconut_match_args[0][0]  #46 (line in Coconut source)
                _coconut_match_set_name_y = _coconut_match_args[0][1]  #46 (line in Coconut source)
                if not _coconut_match_kwargs:  #46 (line in Coconut source)
                    _coconut_match_check_0 = True  #46 (line in Coconut source)
        if _coconut_match_check_0:  #46 (line in Coconut source)
            if _coconut_match_set_name_x is not _coconut_sentinel:  #46 (line in Coconut source)
                x = _coconut_match_set_name_x  #46 (line in Coconut source)
            if _coconut_match_set_name_y is not _coconut_sentinel:  #46 (line in Coconut source)
                y = _coconut_match_set_name_y  #46 (line in Coconut source)
        if not _coconut_match_check_0:  #46 (line in Coconut source)
            raise _coconut_FunctionMatchError('assert uncurry_tuple(+)((1, 2),) == 3 == curry_tuple(def ((x, y),) -> x + y)(1, 2)', _coconut_match_args)  #46 (line in Coconut source)
        return (x + y)  #46 (line in Coconut source)

    assert uncurry_tuple(_coconut.operator.add)((1, 2)) == 3 == curry_tuple(_coconut_lambda_0)(1, 2)  #46 (line in Coconut source)
    assert curry_tuple(uncurry_tuple(_coconut_minus))(3, 2) == 1  #47 (line in Coconut source)


def test_Ord():  #49 (line in Coconut source)
    assert and_(((isinstance)(x, Ord) and (isinstance)(x, Eq) for x in (True, nothing, Left(3), lt, 5, (1, 2))))  #50 (line in Coconut source)
    assert compare(1, 2) == lt == compare(nothing, Just(1))  #53 (line in Coconut source)
    assert compare(2, 2) == eq == compare(Left(2), Left(2))  #54 (line in Coconut source)
    assert compare(2, 1) == gt == compare(Right(1), Left(0))  #55 (line in Coconut source)
    assert max(1, 2) == 2 == min(2, 3)  #56 (line in Coconut source)
    assert min(eq, gt) == eq == max(lt, eq)  #57 (line in Coconut source)


def test_Enum():  #59 (line in Coconut source)
    assert and_(((isinstance)(x, Enum) for x in (True, lt, 5)))  #60 (line in Coconut source)
    assert (succ)(5) == 6 == (pred)(7)  #63 (line in Coconut source)
    assert fromEnum(10) == 10  #64 (line in Coconut source)
    assert (list)(_coconut_iter_getitem(enumFrom(2), _coconut.slice(None, 2))) == [2, 3]  #65 (line in Coconut source)
    assert (list)(_coconut_iter_getitem(enumFromThen(2, 4), _coconut.slice(None, 3))) == [2, 4, 6]  #66 (line in Coconut source)
    assert (list)(enumFromTo(2, 4)) == [2, 3, 4]  #67 (line in Coconut source)
    assert (list)(enumFromThenTo(2, 4, 8)) == [2, 4, 6, 8] == (list)(enumFromThenTo(2, 4, 9))  #68 (line in Coconut source)
    assert (list)(enumFromThenTo(2, 4, 1)) == []  #69 (line in Coconut source)
    assert (list)(enumFromThen(10, 1)) == []  #70 (line in Coconut source)
    assert (list)(enumFromThenTo(4, 3, 1)) == [4, 3, 2, 1]  #71 (line in Coconut source)
    assert (list)(_coconut_iter_getitem(enumFromThen(1, 1), _coconut.slice(None, 3))) == [1, 1, 1] == (list)(_coconut_iter_getitem(enumFromThenTo(1, 1, 1), _coconut.slice(None, 3)))  #72 (line in Coconut source)
    assert (list)(enumFromTo(1, 1)) == [1,]  #73 (line in Coconut source)


def test_Bounded():  #75 (line in Coconut source)
    assert minBound(True) is False  #76 (line in Coconut source)
    assert maxBound(False) is True  #77 (line in Coconut source)
    assert minBound(eq) == lt  #78 (line in Coconut source)
    assert maxBound(eq) == gt  #79 (line in Coconut source)
    assert minBound((False, gt)) == (False, lt)  #80 (line in Coconut source)
    assert maxBound((True, lt)) == (True, gt)  #81 (line in Coconut source)


def test_Rational():  #83 (line in Coconut source)
    assert Rational(1, 3) == (over)(1, 3)  #84 (line in Coconut source)


def test_Num():  #86 (line in Coconut source)
    assert negate(2) == -2 == negate((over)(2, 1))  #87 (line in Coconut source)
    assert abs(-10) == 10 == abs((over)(10, 1))  #88 (line in Coconut source)
    assert signum(0) == 0  #89 (line in Coconut source)
    assert signum(-2) == -1 == signum(-2.5)  #90 (line in Coconut source)
    assert signum(10) == 1 == signum((over)(2, 2))  #91 (line in Coconut source)
    assert fromInteger(10) == 10  #92 (line in Coconut source)


def test_Real():  #94 (line in Coconut source)
    assert toRational(10) == (over)(10, 1)  #95 (line in Coconut source)
    assert toRational((over)(1, 3)) == (over)(1, 3)  #96 (line in Coconut source)
    assert toRational(1.5) == (over)(3, 2)  #97 (line in Coconut source)


def test_Integral():  #99 (line in Coconut source)
    assert (isinstance)(10, Integral)  #100 (line in Coconut source)
    assert quot(10, 3) == 3 == div(10, 3)  #101 (line in Coconut source)
    assert rem(10, 3) == 1 == mod(10, 3)  #102 (line in Coconut source)
    assert div(-10, 3) == -4 == div(10, -3)  #103 (line in Coconut source)
    assert quot(-10, 3) == -3 == quot(10, -3)  #104 (line in Coconut source)
    assert mod(-10, 3) == 2  #105 (line in Coconut source)
    assert mod(10, -3) == -2  #106 (line in Coconut source)
    assert rem(-10, 3) == -1  #107 (line in Coconut source)
    assert rem(10, -3) == 1  #108 (line in Coconut source)
    assert quotRem(-10, -3) == (3, -1) == divMod(-10, -3)  #109 (line in Coconut source)
    assert quotRem(10, -3) == (-3, 1)  #110 (line in Coconut source)
    assert quotRem(-10, 3) == (-3, -1)  #111 (line in Coconut source)
    assert toInteger(10) == 10  #112 (line in Coconut source)


def test_Fractional():  #114 (line in Coconut source)
    assert (recip)((over)(2, 3)) == (over)(3, 2)  #115 (line in Coconut source)
    assert (fromRational)((over)(1, 3)) == (over)(1, 3)  #116 (line in Coconut source)


def test_RealFrac():  #118 (line in Coconut source)
    assert properFraction((over)(10, 3)) == (3, (over)(1, 3))  #119 (line in Coconut source)
    assert (truncate)((over)(4, 3)) == 1  #120 (line in Coconut source)
    assert (round)((over)(5, 3)) == 2  #121 (line in Coconut source)
    assert (truncate)((over)(-4, 3)) == -1  #122 (line in Coconut source)
    assert (floor)((over)(-4, 3)) == -2  #123 (line in Coconut source)
    assert (round)((over)(-4, 3)) == -1  #124 (line in Coconut source)
    assert (ceiling)((over)(-4, 3)) == -1  #125 (line in Coconut source)
    assert (ceiling)((over)(4, 3)) == 2  #126 (line in Coconut source)
    assert (floor)((over)(4, 3)) == 1  #127 (line in Coconut source)


def test_RealFloat():  #129 (line in Coconut source)
    assert floatRadix(1.2) == 2  #130 (line in Coconut source)
    assert floatDigits(0.5) == 53  #131 (line in Coconut source)
    assert floatRange(0.1) == (-1021, 1024)  #132 (line in Coconut source)
    assert scaleFloat(1, 1.5) == 3  #133 (line in Coconut source)
    assert not isNegativeZero(0.0)  #134 (line in Coconut source)
    assert isNegativeZero(float("-0"))  #135 (line in Coconut source)
    assert isIEEE(0.9) is True  #136 (line in Coconut source)


def test_Numeric_functions():  #138 (line in Coconut source)
    assert subtract(2, 1) == -1  #139 (line in Coconut source)
    assert even(2)  #140 (line in Coconut source)
    assert not even(3)  #141 (line in Coconut source)
    assert odd(3)  #142 (line in Coconut source)
    assert not odd(2)  #143 (line in Coconut source)
    assert gcd(4, 6) == 2 == gcd(-4, -6)  #144 (line in Coconut source)
    assert lcm(0, 2) == 0 == lcm(2, 0)  #145 (line in Coconut source)
    assert lcm(4, 6) == 12 == lcm(-4, -6)  #146 (line in Coconut source)
    assert fromIntegral(10) == 10  #147 (line in Coconut source)
    assert realToFrac(0.5) == (over)(1, 2)  #148 (line in Coconut source)


def test_Monoids():  #150 (line in Coconut source)
    assert mappend(Just([]), mempty) == Just([]) == mappend(mempty, Just([]))  #151 (line in Coconut source)
    assert mappend(nothing, Just([])) == Just([]) == mappend(Just([]), nothing)  #152 (line in Coconut source)
    assert mappend(nothing, pure(1)) == Just(1)  #153 (line in Coconut source)
    assert mappend(fail("derp"), Just(2)) == Just(2)  #154 (line in Coconut source)
    assert mappend([1, 2], [3, 4]) == [1, 2, 3, 4]  #155 (line in Coconut source)
    assert mappend(Just([1, 2]), Just([3, 4])) == Just([1, 2, 3, 4])  #156 (line in Coconut source)
    assert mappend(lt, gt) == lt == mappend(eq, lt)  #157 (line in Coconut source)
    assert mappend(gt, lt) == gt == mappend(gt, eq)  #158 (line in Coconut source)
    assert mappend(eq, mempty) == eq == mappend(mempty, eq)  #159 (line in Coconut source)
    assert mappend(([1,], [2,]), ([3,], [4,])) == ([1, 3], [2, 4])  #160 (line in Coconut source)
    assert mconcat([[1,], [2, 3]]) == [1, 2, 3]  #161 (line in Coconut source)


def test_Functor():  #163 (line in Coconut source)
    assert (fmap)(error, nothing) == nothing  #164 (line in Coconut source)
    assert (fmap)(_coconut_partial((_coconut.operator.add), 1), Just(2)) == Just(3)  #165 (line in Coconut source)
    assert (fmap)(_coconut_partial((_coconut.operator.add), 1), Left(10)) == Left(10)  #166 (line in Coconut source)
    assert (fmap)(_coconut_partial((_coconut.operator.add), 1), [1, 2, 3]) == [2, 3, 4]  #167 (line in Coconut source)
    assert (fmapConst)(10, [1, 2, 3]) == [10, 10, 10]  #168 (line in Coconut source)
    assert (fmap)(_coconut_partial((_coconut.operator.add), 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))  #169 (line in Coconut source)


def test_Applicative():  #171 (line in Coconut source)
    assert pure("12") == (fmap)(lambda s: s + "2", pure("1"))  #172 (line in Coconut source)
    assert (ap)(nothing, Just(10)) == nothing  #173 (line in Coconut source)
    assert (ap)(Just(_coconut_partial((_coconut.operator.add), 1)), Just(2)) == Just(3)  #174 (line in Coconut source)
    assert (ap)([_coconut_partial((_coconut.operator.add), 1), _coconut_partial((_coconut.operator.mul), 3)], [10, 20, 30]) == [11, 21, 31, 30, 60, 90]  #175 (line in Coconut source)
    assert (ap)((_coconut_partial((_coconut.operator.add), 1), _coconut_partial((_coconut.operator.mul), 3)), (10, 20, 30)) == (11, 21, 31, 30, 60, 90)  #176 (line in Coconut source)
    assert (ap)(pure(error), nothing) == nothing  #177 (line in Coconut source)
    assert (ap)(pure(lambda _=None: _ + 1), Just(2)) == Just(3)  #178 (line in Coconut source)
    assert (ap)(pure(lambda _=None: _ + 1), Left(10)) == Left(10)  #179 (line in Coconut source)
    assert (ap)(pure(lambda _=None: _ + 1), [1, 2, 3]) == [2, 3, 4]  #180 (line in Coconut source)
    assert (ap)(pure(lambda _=None: _ + 1), _coconut.frozenset((1, 2))) == _coconut.frozenset((2, 3))  #181 (line in Coconut source)
    assert (ap)(fail("derp"), Right(1)) == Left("derp")  #182 (line in Coconut source)
    assert (seqAr)(nothing, Just(1)) == nothing  #183 (line in Coconut source)
    assert (seqAl)(Just(1), nothing) == nothing  #184 (line in Coconut source)
    assert (seqAr)(Just(1), Just(2)) == Just(2) == (seqAl)(Just(2), Just(1))  #185 (line in Coconut source)
    assert liftA2((_coconut.operator.add))([1, 2, 3], [10, 20, 30]) == [11, 21, 31, 12, 22, 32, 13, 23, 33]  #186 (line in Coconut source)


def test_Monad():  #188 (line in Coconut source)
    assert nothing == (bind)(nothing, Just)  #189 (line in Coconut source)
    assert nothing == (bindFrom)(Just, nothing)  #190 (line in Coconut source)
    assert Just(2) == (bind)(Just(1), lambda x: Just(x + 1))  #191 (line in Coconut source)
    assert Left(2) == (bind)(Left(2), Right)  #192 (line in Coconut source)
    assert Left(2) == (bindFrom)(Right, Left(2))  #193 (line in Coconut source)
    assert Left(2) == (bind)(Right(2), Left)  #194 (line in Coconut source)
    assert Left(2) == (bindFrom)(Left, Right(2))  #195 (line in Coconut source)
    assert Just(2) == (seqM)(Just(1), Just(2))  #196 (line in Coconut source)
    assert nothing == (seqM)(nothing, Just(2))  #197 (line in Coconut source)
    assert Right(2) == (seqM)(Right(1), Right(2))  #198 (line in Coconut source)
    assert Left(1) == (seqM)(Left(1), Right(2))  #199 (line in Coconut source)
    assert [] == (seqM)([], [1,])  #200 (line in Coconut source)
    assert fail("derp") == (fmap)(_coconut_partial((_coconut.operator.add), 1), fail("derp"))  #201 (line in Coconut source)
    assert nothing == (bind)(Just(1), _coconut_forward_compose(str, fail))  #202 (line in Coconut source)
    assert Left(1) == (bind)(Left(1), _coconut_forward_compose(str, fail))  #203 (line in Coconut source)
    assert Left("1") == (bind)(Right(1), _coconut_forward_compose(str, fail))  #204 (line in Coconut source)
    assert [] == (bind)([1, 2], _coconut_forward_compose(str, fail))  #205 (line in Coconut source)
    assert Just(1) == (bind)(Just(1), return_)  #206 (line in Coconut source)
    assert Just(2) == (bind)(Just(1), lambda _=None: return_(2))  #207 (line in Coconut source)
    assert nothing == (bind)(nothing, return_)  #208 (line in Coconut source)
    assert [1,] == (bind)([1,], return_)  #209 (line in Coconut source)
    assert [2, 3] == (bind)([1, 2], lambda x: return_(x + 1))  #210 (line in Coconut source)
    assert [] == (bind)([], return_)  #211 (line in Coconut source)
    assert Right(1) == (bind)(Right(1), return_)  #212 (line in Coconut source)
    assert Left(1) == (bind)(Left(1), return_(2))  #213 (line in Coconut source)
    assert Right(2) == (bind)(Right(1), lambda x: return_(x + 1))  #214 (line in Coconut source)
    assert join(return_(return_(5))) == return_(5)  #215 (line in Coconut source)
    assert Just(1) == join(Just(Just(1)))  #216 (line in Coconut source)
    assert nothing == join(Just(nothing))  #217 (line in Coconut source)
    assert nothing == join(nothing)  #218 (line in Coconut source)
    assert [1, 2, 3, 4, 5, 6] == join([[1, 2, 3], [], [4,], [5, 6]])  #219 (line in Coconut source)
    assert [1,] == join([fail("derp"), return_(1)])  #220 (line in Coconut source)
    assert Left(3) == do([Right(1), Right(2), Left(3), Right(4)], lambda *xs: error(repr(xs)))  #221 (line in Coconut source)
    _coconut_decorator_0 = _coconut_partial(do, [Right(1), Right(2)])  #227 (line in Coconut source)
    @_coconut_decorator_0  #228 (line in Coconut source)
    @_coconut_tco  #228 (line in Coconut source)
    def right3(x, y):  #228 (line in Coconut source)
        return _coconut_tail_call(Right, x + y)  #228 (line in Coconut source)

    assert right3 == Right(3)  #229 (line in Coconut source)
    global glob  #230 (line in Coconut source)
    glob = 1  #230 (line in Coconut source)
    @_coconut_tco  #231 (line in Coconut source)
    def _coconut_lambda_1(x):  #231 (line in Coconut source)
        global glob  #231 (line in Coconut source)
        glob = 2  #231 (line in Coconut source)
        return _coconut_tail_call(Just, glob)  #231 (line in Coconut source)

    assert nothing == (bind)(nothing, (_coconut_lambda_1))  #231 (line in Coconut source)
    assert glob == 1  #232 (line in Coconut source)


def test_Foldable():  #234 (line in Coconut source)
    assert sequence_([[1,], [2,], [3,]]) == [(),]  #235 (line in Coconut source)
    assert sequence_([[1,], [], [3,]]) == []  #236 (line in Coconut source)
    assert sequence_([Just(1), Just(2), Just(3)]) == Just(())  #237 (line in Coconut source)
    assert sequence_([Just(1), nothing, Just(3)]) == nothing  #238 (line in Coconut source)
    assert sequence_([Right(1), Right(2), Right(3)]) == Right(())  #239 (line in Coconut source)
    assert sequence_([Right(1), Left(2), Right(3)]) == Left(2)  #240 (line in Coconut source)
    assert mapM_(Just, [1, 2, 3]) == Just(())  #241 (line in Coconut source)
    assert foldMap(lambda x: [x, x], [[1,], [2, 3]]) == [[1,], [1,], [2, 3], [2, 3]]  #242 (line in Coconut source)
    assert foldr((_coconut.operator.pow), 2, [1, 2, 3]) == 1  #243 (line in Coconut source)
    assert foldl((_coconut.operator.pow), 2, [1, 2, 3]) == 64  #244 (line in Coconut source)
    assert (list)(foldr(cons, [], [2, 3, 4])) == [2, 3, 4]  #245 (line in Coconut source)
    assert (list)(foldl(flip(cons), [], [2, 3, 4])) == [4, 3, 2]  #246 (line in Coconut source)
    assert null([])  #247 (line in Coconut source)
    assert not null([1,])  #248 (line in Coconut source)
    assert length([]) == 0  #249 (line in Coconut source)
    assert length([1, 2, 3]) == 3  #250 (line in Coconut source)
    assert (elem)(1, [1, 2, 3])  #251 (line in Coconut source)
    assert not (elem)(1, [2, 3])  #252 (line in Coconut source)
    assert maximum([1, 2, 3]) == 3  #253 (line in Coconut source)
    assert minimum([1, 2, 3]) == 1  #254 (line in Coconut source)
    assert sum([2, 3, 4]) == 9  #255 (line in Coconut source)
    assert product([2, 3, 4]) == 24  #256 (line in Coconut source)


def test_Traversable():  #258 (line in Coconut source)
    for _sequence in ([sequenceA, sequence]):  #259 (line in Coconut source)
        assert _sequence([Just(1), nothing, Just(3)]) == nothing  #260 (line in Coconut source)
        assert _sequence([Right(1), Right(2), Left(3), Right(4)]) == Left(3)  #261 (line in Coconut source)
        assert _sequence([[1, 2, 3], [], [4,], [5, 6]]) == []  #262 (line in Coconut source)
        assert _sequence([Just(1), Just(2), Just(3)]) == Just([1, 2, 3])  #263 (line in Coconut source)
        assert _sequence([Right(1), Right(2), Right(3)]) == Right([1, 2, 3])  #264 (line in Coconut source)
        assert _sequence([[1, 2], [3,]]) == [[1, 3], [2, 3]]  #265 (line in Coconut source)
    for _traverse in ([traverse, mapM]):  #266 (line in Coconut source)
        assert _traverse(lambda x: [x,], [1, 2, 3]) == [[1, 2, 3],]  #267 (line in Coconut source)
        assert _traverse(Just, [Just(1), nothing, Just(2)]) == Just([Just(1), nothing, Just(2)])  #268 (line in Coconut source)


def test_Miscellaneous_functions():  #270 (line in Coconut source)
    assert id(10) == 10  #271 (line in Coconut source)
    assert const(10)(5)  #272 (line in Coconut source)
    assert ((dot)(abs, (_coconut.operator.add)))(-2, -3) == 5  #273 (line in Coconut source)
    assert flip((_coconut_minus))(10, 5) == -5  #274 (line in Coconut source)
    assert (apply)(abs, -2) == 2  #275 (line in Coconut source)
    assert ((apply)((_coconut.operator.truediv), 6))(2) == 3  #276 (line in Coconut source)
    assert (apply)((apply)((apply)((lambda x, y, z: (x, y, z)), 1), 2), 3) == (1, 2, 3)  #277 (line in Coconut source)
    assert until(lambda x: x < 0, _coconut_partial(subtract, 1), 10) == -1  #278 (line in Coconut source)
    assert asTypeOf(5, 10) == 5  #279 (line in Coconut source)
    assert asTypeOf(pure([]), nothing) == Just([])  #280 (line in Coconut source)
    assert asTypeOf(fail("herp"), Right(1)) == Left("herp")  #281 (line in Coconut source)
    assert asTypeOf(mempty, Just([])) == nothing  #282 (line in Coconut source)
    class Test(_coconut.collections.namedtuple("Test", ('x',))):  #283 (line in Coconut source)
        __slots__ = ()  #283 (line in Coconut source)
        _coconut_is_data = True  #283 (line in Coconut source)
        __match_args__ = ('x',)  #283 (line in Coconut source)
        def __add__(self, other): return _coconut.NotImplemented  #283 (line in Coconut source)
        def __mul__(self, other): return _coconut.NotImplemented  #283 (line in Coconut source)
        def __rmul__(self, other): return _coconut.NotImplemented  #283 (line in Coconut source)
        __ne__ = _coconut.object.__ne__  #283 (line in Coconut source)
        def __eq__(self, other):  #283 (line in Coconut source)
            return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)  #283 (line in Coconut source)
        def __hash__(self):  #283 (line in Coconut source)
            return _coconut.tuple.__hash__(self) ^ hash(self.__class__)  #283 (line in Coconut source)
        @staticmethod  #284 (line in Coconut source)
        @_coconut_tco  #285 (line in Coconut source)
        def __mempty__():  #285 (line in Coconut source)
            return _coconut_tail_call(pure, 0)  #285 (line in Coconut source)


        @staticmethod  #287 (line in Coconut source)
        @_coconut_tco  #288 (line in Coconut source)
        def __pure__(x):  #288 (line in Coconut source)
            return _coconut_tail_call(Test, x)  #288 (line in Coconut source)

    _coconut_call_set_names(Test)  #289 (line in Coconut source)
    assert (asTypeOf)(mempty, Test(1)) == Test(0)  #289 (line in Coconut source)
    for _error in ([error, errorWithoutStackTrace]):  #290 (line in Coconut source)
        try:  #291 (line in Coconut source)
            _error("derp")  #292 (line in Coconut source)
        except Exception as err:  #293 (line in Coconut source)
            assert str(err) == "derp"  #294 (line in Coconut source)
        else:  #295 (line in Coconut source)
            assert False, "expected error"  #296 (line in Coconut source)
    assert undefined == undefined  #297 (line in Coconut source)
    assert seq(1, 2) == 2  #298 (line in Coconut source)
    assert (cbv)(abs, -2) == 2  #299 (line in Coconut source)


def test_List_operations():  #301 (line in Coconut source)
    assert (list)((cons)(1, [2, 3])) == [1, 2, 3]  #302 (line in Coconut source)
    assert (list)(map(_coconut_partial((_coconut.operator.add), 1), [1, 2, 3])) == [2, 3, 4]  #303 (line in Coconut source)
    assert (list)((chain)([1, 2], [3, 4])) == [1, 2, 3, 4]  #304 (line in Coconut source)
    assert (list)(filter(lambda x: x > 1, [1, 2, 3])) == [2, 3]  #305 (line in Coconut source)
    assert head([1, 2, 3]) == 1  #306 (line in Coconut source)
    assert last([1, 2, 3]) == 3  #307 (line in Coconut source)
    assert tail([1, 2, 3]) == [2, 3]  #308 (line in Coconut source)
    assert init([1, 2, 3]) == [1, 2]  #309 (line in Coconut source)
    assert (at)([1, 2, 3], 1) == 2 == (at)(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: 1, lambda: 2, lambda: 3)), 1)  #310 (line in Coconut source)
    assert (list)(reverse([1, 2, 3])) == [3, 2, 1]  #311 (line in Coconut source)


def test_Special_folds():  #313 (line in Coconut source)
    assert and_([True, True])  #314 (line in Coconut source)
    assert or_([False, True])  #315 (line in Coconut source)
    assert any(_coconut_partial((_coconut.operator.eq), 2), [1, 2, 3])  #316 (line in Coconut source)
    assert not all(_coconut_partial((_coconut.operator.eq), 2), [1, 2, 3])  #317 (line in Coconut source)
    assert (list)(concat([])) == []  #318 (line in Coconut source)
    assert (list)(concat([[],])) == []  #319 (line in Coconut source)
    assert (list)(concat([[1,], [2, 3]])) == [1, 2, 3]  #320 (line in Coconut source)
    assert (list)(concatMap(lambda x: [x, x], [1, 2])) == [1, 1, 2, 2]  #321 (line in Coconut source)


def test_Scans():  #323 (line in Coconut source)
    assert (list)(scanl((_coconut.operator.add), 0, [1, 2, 3])) == [0, 1, 3, 6]  #324 (line in Coconut source)
    assert (list)(scanl1((_coconut.operator.add), [1, 2, 3])) == [1, 3, 6]  #325 (line in Coconut source)
    assert (list)(scanr((_coconut.operator.add), 0, [1, 2, 3])) == [6, 5, 3, 0]  #326 (line in Coconut source)
    assert (list)(scanr1((_coconut.operator.add), [1, 2, 3])) == [6, 5, 3]  #327 (line in Coconut source)


def test_Infinite_lists():  #329 (line in Coconut source)
    assert (list)((take)(3, iterate(_coconut_partial(subtract, 1), 3))) == [3, 2, 1]  #330 (line in Coconut source)
    assert (list)(_coconut_iter_getitem(repeat(1), _coconut.slice(None, 3))) == [1, 1, 1] == (list)(replicate(3, 1))  #331 (line in Coconut source)
    assert (list)(_coconut_iter_getitem(cycle([1, 2]), _coconut.slice(None, 4))) == [1, 2, 1, 2]  #332 (line in Coconut source)


def test_Sublists():  #334 (line in Coconut source)
    assert take(2, [1, 2, 3]) == [1, 2]  #335 (line in Coconut source)
    assert drop(2, [1, 2, 3]) == [3,]  #336 (line in Coconut source)
    assert (fmap)(list, splitAt(2, [1, 2, 3, 4])) == ([1, 2], [3, 4])  #337 (line in Coconut source)
    assert (list)(takeWhile((_coconut_partial(_coconut_partial, (_coconut.operator.gt)))(2), [0, 1, 2, 3])) == [0, 1]  #338 (line in Coconut source)
    assert (list)(dropWhile((_coconut_partial(_coconut_partial, (_coconut.operator.gt)))(2), [0, 1, 2, 3])) == [2, 3]  #339 (line in Coconut source)
    assert span((_coconut_partial(_coconut_partial, (_coconut.operator.gt)))(2), [0, 1, 2, 3]) == ([0, 1], [2, 3])  #340 (line in Coconut source)
    assert break_((_coconut_partial(_coconut_partial, (_coconut.operator.lt)))(2), [1, 2, 3]) == ([1, 2], [3,])  #341 (line in Coconut source)


def test_Searching_lists():  #343 (line in Coconut source)
    assert (notElem)(10, [1, 2, 3])  #344 (line in Coconut source)
    assert lookup("b", [("a", 1), ("b", 2), ("c", 3)]) == Just(2)  #345 (line in Coconut source)
    assert lookup("b", [("a", 1),]) == nothing  #346 (line in Coconut source)
    assert lookup("a", []) == nothing  #347 (line in Coconut source)


def test_Zipping_and_unzipping_lists():  #349 (line in Coconut source)
    assert (list)(zip([1, 2], [3, 4])) == [(1, 3), (2, 4)]  #350 (line in Coconut source)
    assert unzip([(1, 3), (2, 4)]) == ([1, 2], [3, 4])  #351 (line in Coconut source)
    assert (list)(zip3([1, 2], [3, 4], [5, 6])) == [(1, 3, 5), (2, 4, 6)]  #352 (line in Coconut source)
    assert unzip3([(1, 3, 5), (2, 4, 6)]) == ([1, 2], [3, 4], [5, 6])  #353 (line in Coconut source)
    assert (list)(zipWith((_coconut.operator.add), [1, 2], [10, 20])) == [11, 22]  #354 (line in Coconut source)
    assert (list)(zipWith3(lambda x, y, z: sum([x, y, z]), [1, 2], [10, 20], [100, 200])) == [111, 222]  #355 (line in Coconut source)


def test_Functions_on_strings():  #357 (line in Coconut source)
    assert lines("\nabc\ndef\n") == ["", "abc", "def"]  #358 (line in Coconut source)
    assert words(" abc def ") == ["abc", "def"]  #359 (line in Coconut source)
    assert unlines(["abc", "def"]) == "abc\ndef\n"  #360 (line in Coconut source)
    assert unlines(["abc",]) == "abc\n"  #361 (line in Coconut source)
    assert unlines([]) == ""  #362 (line in Coconut source)
    assert unwords(["abc", "def"]) == "abc def"  #363 (line in Coconut source)
    assert unwords(["abc",]) == "abc"  #364 (line in Coconut source)
    assert unwords([]) == ""  #365 (line in Coconut source)


def test_Converting_to_String():  #367 (line in Coconut source)
    assert show(1) == "1"  #368 (line in Coconut source)
    assert show("abc") == "'abc'"  #369 (line in Coconut source)
    assert ((shows)(3))("abc") == "3abc"  #370 (line in Coconut source)
    assert ((showList)([1,]))("abc") == "[1]abc"  #371 (line in Coconut source)
    assert ((showList)(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: 1, lambda: 2))))("") == "[1, 2]"  #372 (line in Coconut source)
    assert ((showString)("abc"))("def") == "abcdef"  #373 (line in Coconut source)
    assert ((showChar)("a"))("bcd") == "abcd"  #374 (line in Coconut source)
    assert ((showParen)(True, showString("abc")))("def") == "(abc)def"  #375 (line in Coconut source)
    assert ((showParen)(False, showString("abc")))("def") == "abcdef"  #376 (line in Coconut source)


def test_Converting_from_String():  #378 (line in Coconut source)
    assert read("[]") == []  #379 (line in Coconut source)
    assert read("10") == 10  #380 (line in Coconut source)
    assert read('"abc"') == "abc"  #381 (line in Coconut source)


def test_IO():  #383 (line in Coconut source)
    assert unIO(pure(5)) == 5  #384 (line in Coconut source)
    assert (unIO)(mempty) == mempty  #385 (line in Coconut source)
    assert (unIO)(mappend(mempty, asIO(pure(gt)))) == gt  #386 (line in Coconut source)
    assert (unIO)((fmap)(lambda _=None: _ * 2, pure(5))) == 10  #387 (line in Coconut source)
    try:  #388 (line in Coconut source)
        unIO(fail("herp"))  #389 (line in Coconut source)
    except IOError as err:  #390 (line in Coconut source)
        assert str(err) == "herp"  #391 (line in Coconut source)
    else:  #392 (line in Coconut source)
        assert False, "expected error"  #393 (line in Coconut source)
    assert 6 == (unIO)((bind)(pure(5), lambda x: pure(x + 1)))  #394 (line in Coconut source)
    _coconut_decorator_1 = _coconut_partial(do, [asIO(pure(1)), pure(2)])  #396 (line in Coconut source)
    @unIO  #395 (line in Coconut source)
    @_coconut_decorator_1  #396 (line in Coconut source)
    @_coconut_tco  #396 (line in Coconut source)
    def three(x1, x2):  #396 (line in Coconut source)
        return _coconut_tail_call(pure, x1 + x2)  #397 (line in Coconut source)

    assert three == 3  #398 (line in Coconut source)


def test_Exception_handling():  #400 (line in Coconut source)
    try:  #401 (line in Coconut source)
        (unIO)(ioError(IOError("derp")))  #402 (line in Coconut source)
    except IOError as err:  #403 (line in Coconut source)
        assert str(err) == "derp"  #404 (line in Coconut source)
    else:  #405 (line in Coconut source)
        assert False, "expected error"  #406 (line in Coconut source)
    assert (isinstance)(userError("derp"), IOError)  #407 (line in Coconut source)
    assert (str)(userError("derp")) == "derp"  #408 (line in Coconut source)


def test_function_monad():  #410 (line in Coconut source)
    assert liftA2(_coconut_comma_op)(id, id)(1) == (1, 1) == lift(_coconut_comma_op)(ident, ident)(1)  #411 (line in Coconut source)
    assert ((fmap)((_coconut_complex_partial(_coconut.operator.add, {1: 1}, 2, ())), (_coconut_complex_partial(_coconut.operator.mul, {1: 2}, 2, ()))))(3) == 7  #412 (line in Coconut source)
    assert pure(5)(10) == 5  #413 (line in Coconut source)
    assert ((ap)(_coconut_partial(_coconut_partial, (_coconut.operator.mul)), (_coconut_complex_partial(_coconut.operator.add, {1: 1}, 2, ()))))(3) == 12 == ((bind)((_coconut_complex_partial(_coconut.operator.add, {1: 1}, 2, ())), _coconut_partial(_coconut_partial, (_coconut.operator.mul))))(3)  #414 (line in Coconut source)


# Run tests:

if __name__ == "__main__":  #418 (line in Coconut source)
    for var, val in (globals().items()):  #419 (line in Coconut source)
        if var.startswith("test_"):  #420 (line in Coconut source)
            val()  #421 (line in Coconut source)
    print("<success>")  #422 (line in Coconut source)
