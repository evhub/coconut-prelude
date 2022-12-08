#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2fe46f21

# Compiled with Coconut version 2.1.1-post_dev27 [The Spanish Inquisition]

# Coconut Header: -------------------------------------------------------------

from __future__ import generator_stop
import sys as _coconut_sys
from builtins import chr, hex, input, int, map, object, oct, open, print, range, str, super, zip, filter, reversed, enumerate, repr
py_chr, py_hex, py_input, py_int, py_map, py_object, py_oct, py_open, py_print, py_range, py_str, py_super, py_zip, py_filter, py_reversed, py_enumerate, py_repr = chr, hex, input, int, map, object, oct, open, print, range, str, super, zip, filter, reversed, enumerate, repr
_coconut_py_str, _coconut_py_super = str, super
from functools import wraps as _coconut_wraps
exec("_coconut_exec = exec")
if _coconut_sys.version_info < (3, 7):
    def _coconut_default_breakpointhook(*args, **kwargs):
        hookname = _coconut.os.getenv("PYTHONBREAKPOINT")
        if hookname != "0":
            if not hookname:
                hookname = "pdb.set_trace"
            modname, dot, funcname = hookname.rpartition(".")
            if not dot:
                modname = "builtins" if _coconut_sys.version_info >= (3,) else "__builtin__"
            if _coconut_sys.version_info >= (2, 7):
                import importlib
                module = importlib.import_module(modname)
            else:
                import imp
                module = imp.load_module(modname, *imp.find_module(modname))
            hook = _coconut.getattr(module, funcname)
            return hook(*args, **kwargs)
    if not hasattr(_coconut_sys, "__breakpointhook__"):
        _coconut_sys.__breakpointhook__ = _coconut_default_breakpointhook
    def breakpoint(*args, **kwargs):
        return _coconut.getattr(_coconut_sys, "breakpointhook", _coconut_default_breakpointhook)(*args, **kwargs)
else:
    py_breakpoint = breakpoint
@_coconut_wraps(_coconut_py_super)
def _coconut_super(type=None, object_or_type=None):
    if type is None:
        if object_or_type is not None:
            raise _coconut.TypeError("invalid use of super()")
        frame = _coconut_sys._getframe(1)
        try:
            cls = frame.f_locals["__class__"]
        except _coconut.AttributeError:
            raise _coconut.RuntimeError("super(): __class__ cell not found")
        self = frame.f_locals[frame.f_code.co_varnames[0]]
        return _coconut_py_super(cls, self)
    return _coconut_py_super(type, object_or_type)
super = _coconut_super
class _coconut:
    import collections, copy, functools, types, itertools, operator, threading, os, warnings, contextlib, traceback, weakref, multiprocessing, math
    from multiprocessing import dummy as multiprocessing_dummy
    import copyreg
    import asyncio
    import pickle
    OrderedDict = collections.OrderedDict
    import collections.abc as abc
    import typing
    if _coconut_sys.version_info < (3, 6):
        def NamedTuple(name, fields):
            return _coconut.collections.namedtuple(name, [x for x, t in fields])
        typing.NamedTuple = NamedTuple
        NamedTuple = staticmethod(NamedTuple)
    if _coconut_sys.version_info < (3, 10):
        try:
            from typing_extensions import TypeAlias, ParamSpec, Concatenate
        except ImportError:
            class you_need_to_install_typing_extensions:
                __slots__ = ()
            TypeAlias = ParamSpec = Concatenate = you_need_to_install_typing_extensions()
        typing.TypeAlias = TypeAlias
        typing.ParamSpec = ParamSpec
        typing.Concatenate = Concatenate
    if _coconut_sys.version_info < (3, 11):
        try:
            from typing_extensions import TypeVarTuple, Unpack
        except ImportError:
            class you_need_to_install_typing_extensions:
                __slots__ = ()
            TypeVarTuple = Unpack = you_need_to_install_typing_extensions()
        typing.TypeVarTuple = TypeVarTuple
        typing.Unpack = Unpack
    zip_longest = itertools.zip_longest
    try:
        import numpy
    except ImportError:
        class you_need_to_install_numpy:
            __slots__ = ()
        numpy = you_need_to_install_numpy()
    else:
        abc.Sequence.register(numpy.ndarray)
    numpy_modules = ('numpy', 'pandas', 'jaxlib.xla_extension')
    jax_numpy_modules = ('jaxlib.xla_extension',)
    tee_type = type(itertools.tee((), 1)[0])
    reiterables = abc.Sequence, abc.Mapping, abc.Set
    abc.Sequence.register(collections.deque)
    Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, all, any, bytes, callable, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, setattr, slice, str, sum, super, tuple, type, vars, zip, repr, print = Ellipsis, NotImplemented, NotImplementedError, Exception, AttributeError, ImportError, IndexError, KeyError, NameError, TypeError, ValueError, StopIteration, RuntimeError, all, any, bytes, callable, classmethod, dict, enumerate, filter, float, frozenset, getattr, hasattr, hash, id, int, isinstance, issubclass, iter, len, list, locals, map, min, max, next, object, property, range, reversed, set, setattr, slice, str, sum, super, tuple, type, vars, zip, repr, print
class _coconut_sentinel:
    __slots__ = ()
class _coconut_base_hashable:
    __slots__ = ()
    def __reduce_ex__(self, _):
        return self.__reduce__()
    def __eq__(self, other):
        return self.__class__ is other.__class__ and self.__reduce__() == other.__reduce__()
    def __hash__(self):
        return _coconut.hash(self.__reduce__())
    def __setstate__(self, setvars):
        for k, v in setvars.items():
            _coconut.setattr(self, k, v)
class MatchError(_coconut_base_hashable, Exception):
    """Pattern-matching error. Has attributes .pattern, .value, and .message."""
    __slots__ = ("pattern", "value", "_message")
    max_val_repr_len = 500
    def __init__(self, pattern=None, value=None):
        self.pattern = pattern
        self.value = value
        self._message = None
    @property
    def message(self):
        if self._message is None:
            value_repr = _coconut.repr(self.value)
            self._message = "pattern-matching failed for %s in %s" % (_coconut.repr(self.pattern), value_repr if _coconut.len(value_repr) <= self.max_val_repr_len else value_repr[:self.max_val_repr_len] + "...")
            Exception.__init__(self, self._message)
        return self._message
    def __repr__(self):
        self.message
        return Exception.__repr__(self)
    def __str__(self):
        self.message
        return Exception.__str__(self)
    def __unicode__(self):
        self.message
        return Exception.__unicode__(self)
    def __reduce__(self):
        return (self.__class__, (self.pattern, self.value))
class _coconut_tail_call:
    __slots__ = ("func", "args", "kwargs")
    def __init__(self, _coconut_func, *args, **kwargs):
        self.func = _coconut_func
        self.args = args
        self.kwargs = kwargs
_coconut_tco_func_dict = {}
def _coconut_tco(func):
    @_coconut.functools.wraps(func)
    def tail_call_optimized_func(*args, **kwargs):
        call_func = func
        while True:
            if _coconut.isinstance(call_func, _coconut_base_pattern_func):
                call_func = call_func._coconut_tco_func
            elif _coconut.isinstance(call_func, _coconut.types.MethodType):
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func.__func__))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func.__func__:
                    if call_func.__self__ is None:
                        call_func = call_func._coconut_tco_func
                    else:
                        call_func = _coconut.functools.partial(call_func._coconut_tco_func, call_func.__self__)
            else:
                wkref = _coconut_tco_func_dict.get(_coconut.id(call_func))
                wkref_func = None if wkref is None else wkref()
                if wkref_func is call_func:
                    call_func = call_func._coconut_tco_func
            result = call_func(*args, **kwargs)  # use 'coconut --no-tco' to clean up your traceback
            if not isinstance(result, _coconut_tail_call):
                return result
            call_func, args, kwargs = result.func, result.args, result.kwargs
    tail_call_optimized_func._coconut_tco_func = func
    tail_call_optimized_func.__module__ = _coconut.getattr(func, "__module__", None)
    tail_call_optimized_func.__name__ = _coconut.getattr(func, "__name__", None)
    tail_call_optimized_func.__qualname__ = _coconut.getattr(func, "__qualname__", None)
    _coconut_tco_func_dict[_coconut.id(tail_call_optimized_func)] = _coconut.weakref.ref(tail_call_optimized_func)
    return tail_call_optimized_func
@_coconut.functools.wraps(_coconut.itertools.tee)
def tee(iterable, n=2):
    if n < 0:
        raise ValueError("n must be >= 0")
    elif n == 0:
        return ()
    elif n == 1:
        return (iterable,)
    elif _coconut.isinstance(iterable, _coconut.reiterables):
        return (iterable,) * n
    else:
        if _coconut.getattr(iterable, "__getitem__", None) is not None or _coconut.isinstance(iterable, (_coconut.tee_type, _coconut.abc.Sized, _coconut.abc.Container)):
            existing_copies = [iterable]
            while _coconut.len(existing_copies) < n:
                try:
                    copy = _coconut.copy.copy(iterable)
                except _coconut.TypeError:
                    break
                else:
                    existing_copies.append(copy)
            else:
                return _coconut.tuple(existing_copies)
        return _coconut.itertools.tee(iterable, n)
class _coconut_has_iter(_coconut_base_hashable):
    __slots__ = ("lock", "iter")
    def __new__(cls, iterable):
        self = _coconut.object.__new__(cls)
        self.lock = _coconut.threading.Lock()
        self.iter = iterable
        return self
    def get_new_iter(self):
        """Tee the underlying iterator."""
        with self.lock:
            self.iter = _coconut_reiterable(self.iter)
        return self.iter
    def __fmap__(self, func):
        return _coconut_map(func, self)
class reiterable(_coconut_has_iter):
    """Allow an iterator to be iterated over multiple times with the same results."""
    __slots__ = ()
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut.reiterables):
            return iterable
        return _coconut_has_iter.__new__(cls, iterable)
    def get_new_iter(self):
        """Tee the underlying iterator."""
        with self.lock:
            self.iter, new_iter = _coconut_tee(self.iter)
        return new_iter
    def __iter__(self):
        return _coconut.iter(self.get_new_iter())
    def __repr__(self):
        return "reiterable(%s)" % (_coconut.repr(self.get_new_iter()),)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    def __getitem__(self, index):
        return _coconut_iter_getitem(self.get_new_iter(), index)
    def __reversed__(self):
        return _coconut_reversed(self.get_new_iter())
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.len(self.get_new_iter())
    def __contains__(self, elem):
        return elem in self.get_new_iter()
    def count(self, elem):
        """Count the number of times elem appears in the iterable."""
        return self.get_new_iter().count(elem)
    def index(self, elem):
        """Find the index of elem in the iterable."""
        return self.get_new_iter().index(elem)
_coconut.reiterables = (reiterable,) + _coconut.reiterables
def _coconut_iter_getitem_special_case(iterable, start, stop, step):
    iterable = _coconut.itertools.islice(iterable, start, None)
    cache = _coconut.collections.deque(_coconut.itertools.islice(iterable, -stop), maxlen=-stop)
    for index, item in _coconut.enumerate(iterable):
        cached_item = cache.popleft()
        if index % step == 0:
            yield cached_item
        cache.append(item)
def _coconut_iter_getitem(iterable, index):
    """Iterator slicing works just like sequence slicing, including support for negative indices and slices, and support for `slice` objects in the same way as can be done with normal slicing.

    Coconut's iterator slicing is very similar to Python's `itertools.islice`, but unlike `itertools.islice`, Coconut's iterator slicing supports negative indices, and will preferentially call an object's `__iter_getitem__` (Coconut-specific magic method, preferred) or `__getitem__` (general Python magic method), if they exist. Coconut's iterator slicing is also optimized to work well with all of Coconut's built-in objects, only computing the elements of each that are actually necessary to extract the desired slice.

    Some code taken from more_itertools under the terms of its MIT license.
    """
    obj_iter_getitem = _coconut.getattr(iterable, "__iter_getitem__", None)
    if obj_iter_getitem is None:
        obj_iter_getitem = _coconut.getattr(iterable, "__getitem__", None)
    if obj_iter_getitem is not None:
        try:
            result = obj_iter_getitem(index)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if not _coconut.isinstance(index, _coconut.slice):
        index = _coconut.operator.index(index)
        if index < 0:
            return _coconut.collections.deque(iterable, maxlen=-index)[0]
        result = _coconut.next(_coconut.itertools.islice(iterable, index, index + 1), _coconut_sentinel)
        if result is _coconut_sentinel:
            raise _coconut.IndexError(".$[] index out of range")
        return result
    start = _coconut.operator.index(index.start) if index.start is not None else None
    stop = _coconut.operator.index(index.stop) if index.stop is not None else None
    step = _coconut.operator.index(index.step) if index.step is not None else 1
    if step == 0:
        raise _coconut.ValueError("slice step cannot be zero")
    if start is None and stop is None and step == -1:
        obj_reversed = _coconut.getattr(iterable, "__reversed__", None)
        if obj_reversed is not None:
            try:
                result = obj_reversed()
            except _coconut.NotImplementedError:
                pass
            else:
                if result is not _coconut.NotImplemented:
                    return result
    if step >= 0:
        start = 0 if start is None else start
        if start < 0:
            cache = _coconut.collections.deque(_coconut.enumerate(iterable, 1), maxlen=-start)
            len_iter = cache[-1][0] if cache else 0
            i = _coconut.max(len_iter + start, 0)
            if stop is None:
                j = len_iter
            elif stop >= 0:
                j = _coconut.min(stop, len_iter)
            else:
                j = _coconut.max(len_iter + stop, 0)
            n = j - i
            if n <= 0:
                return ()
            if n < -start or step != 1:
                cache = _coconut.itertools.islice(cache, 0, n, step)
            return _coconut_map(_coconut.operator.itemgetter(1), cache)
        elif stop is None or stop >= 0:
            return _coconut.itertools.islice(iterable, start, stop, step)
        else:
            return _coconut_iter_getitem_special_case(iterable, start, stop, step)
    else:
        start = -1 if start is None else start
        if stop is not None and stop < 0:
            n = -stop - 1
            cache = _coconut.collections.deque(_coconut.enumerate(iterable, 1), maxlen=n)
            len_iter = cache[-1][0] if cache else 0
            if start < 0:
                i, j = start, stop
            else:
                i, j = _coconut.min(start - len_iter, -1), None
            return _coconut_map(_coconut.operator.itemgetter(1), _coconut.tuple(cache)[i:j:step])
        else:
            if stop is not None:
                m = stop + 1
                iterable = _coconut.itertools.islice(iterable, m, None)
            if start < 0:
                i = start
                n = None
            elif stop is None:
                i = None
                n = start + 1
            else:
                i = None
                n = start - stop
            if n is not None:
                if n <= 0:
                    return ()
                iterable = _coconut.itertools.islice(iterable, 0, n)
            return _coconut.tuple(iterable)[i::step]
class _coconut_base_compose(_coconut_base_hashable):
    __slots__ = ("func", "funcstars")
    def __init__(self, func, *funcstars):
        self.func = func
        self.funcstars = []
        for f, stars in funcstars:
            if _coconut.isinstance(f, _coconut_base_compose):
                self.funcstars.append((f.func, stars))
                self.funcstars += f.funcstars
            else:
                self.funcstars.append((f, stars))
        self.funcstars = _coconut.tuple(self.funcstars)
    def __call__(self, *args, **kwargs):
        arg = self.func(*args, **kwargs)
        for f, stars in self.funcstars:
            if stars == 0:
                arg = f(arg)
            elif stars == 1:
                arg = f(*arg)
            elif stars == 2:
                arg = f(**arg)
            else:
                raise _coconut.ValueError("invalid arguments to " + _coconut.repr(self))
        return arg
    def __repr__(self):
        return _coconut.repr(self.func) + " " + " ".join(("..*> " if star == 1 else "..**>" if star == 2 else "..> ") + _coconut.repr(f) for f, star in self.funcstars)
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.funcstars)
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.types.MethodType(self, obj)
def _coconut_forward_compose(func, *funcs):
    """Forward composition operator (..>).

    (..>)(f, g) is effectively equivalent to (*args, **kwargs) -> g(f(*args, **kwargs))."""
    return _coconut_base_compose(func, *((f, 0) for f in funcs))
def _coconut_back_compose(*funcs):
    """Backward composition operator (<..).

    (<..)(f, g) is effectively equivalent to (*args, **kwargs) -> f(g(*args, **kwargs))."""
    return _coconut_forward_compose(*_coconut.reversed(funcs))
def _coconut_forward_star_compose(func, *funcs):
    """Forward star composition operator (..*>).

    (..*>)(f, g) is effectively equivalent to (*args, **kwargs) -> g(*f(*args, **kwargs))."""
    return _coconut_base_compose(func, *((f, 1) for f in funcs))
def _coconut_back_star_compose(*funcs):
    """Backward star composition operator (<*..).

    (<*..)(f, g) is effectively equivalent to (*args, **kwargs) -> f(*g(*args, **kwargs))."""
    return _coconut_forward_star_compose(*_coconut.reversed(funcs))
def _coconut_forward_dubstar_compose(func, *funcs):
    """Forward double star composition operator (..**>).

    (..**>)(f, g) is effectively equivalent to (*args, **kwargs) -> g(**f(*args, **kwargs))."""
    return _coconut_base_compose(func, *((f, 2) for f in funcs))
def _coconut_back_dubstar_compose(*funcs):
    """Backward double star composition operator (<**..).

    (<**..)(f, g) is effectively equivalent to (*args, **kwargs) -> f(**g(*args, **kwargs))."""
    return _coconut_forward_dubstar_compose(*_coconut.reversed(funcs))
def _coconut_pipe(x, f):
    """Pipe operator (|>). Equivalent to (x, f) -> f(x)."""
    return f(x)
def _coconut_star_pipe(xs, f):
    """Star pipe operator (*|>). Equivalent to (xs, f) -> f(*xs)."""
    return f(*xs)
def _coconut_dubstar_pipe(kws, f):
    """Double star pipe operator (**|>). Equivalent to (kws, f) -> f(**kws)."""
    return f(**kws)
def _coconut_back_pipe(f, x):
    """Backward pipe operator (<|). Equivalent to (f, x) -> f(x)."""
    return f(x)
def _coconut_back_star_pipe(f, xs):
    """Backward star pipe operator (<*|). Equivalent to (f, xs) -> f(*xs)."""
    return f(*xs)
def _coconut_back_dubstar_pipe(f, kws):
    """Backward double star pipe operator (<**|). Equivalent to (f, kws) -> f(**kws)."""
    return f(**kws)
def _coconut_none_pipe(x, f):
    """Nullable pipe operator (|?>). Equivalent to (x, f) -> f(x) if x is not None else None."""
    return None if x is None else f(x)
def _coconut_none_star_pipe(xs, f):
    """Nullable star pipe operator (|?*>). Equivalent to (xs, f) -> f(*xs) if xs is not None else None."""
    return None if xs is None else f(*xs)
def _coconut_none_dubstar_pipe(kws, f):
    """Nullable double star pipe operator (|?**>). Equivalent to (kws, f) -> f(**kws) if kws is not None else None."""
    return None if kws is None else f(**kws)
def _coconut_assert(cond, msg=None):
    """Assert operator (assert). Asserts condition with optional message."""
    if not cond:
        assert False, msg if msg is not None else "(assert) got falsey value " + _coconut.repr(cond)
def _coconut_raise(exc=None, from_exc=None):
    """Raise operator (raise). Raises exception with optional cause."""
    if exc is None:
        raise
    if from_exc is not None:
        exc.__cause__ = from_exc
    raise exc
def _coconut_bool_and(a, b):
    """Boolean and operator (and). Equivalent to (a, b) -> a and b."""
    return a and b
def _coconut_bool_or(a, b):
    """Boolean or operator (or). Equivalent to (a, b) -> a or b."""
    return a or b
def _coconut_none_coalesce(a, b):
    """None coalescing operator (??). Equivalent to (a, b) -> a if a is not None else b."""
    return b if a is None else a
def _coconut_minus(a, b=_coconut_sentinel):
    """Minus operator (-). Effectively equivalent to (a, b=None) -> a - b if b is not None else -a."""
    if b is _coconut_sentinel:
        return -a
    return a - b
def _coconut_comma_op(*args):
    """Comma operator (,). Equivalent to (*args) -> args."""
    return args
_coconut_matmul = _coconut.operator.matmul
class scan(_coconut_has_iter):
    """Reduce func over iterable, yielding intermediate results,
    optionally starting from initial."""
    __slots__ = ("func", "initial")
    def __new__(cls, function, iterable, initial=_coconut_sentinel):
        self = _coconut_has_iter.__new__(cls, iterable)
        self.func = function
        self.initial = initial
        return self
    def __repr__(self):
        return "scan(%r, %s%s)" % (self.func, _coconut.repr(self.iter), "" if self.initial is _coconut_sentinel else ", " + _coconut.repr(self.initial))
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter, self.initial))
    def __copy__(self):
        return self.__class__(self.func, self.get_new_iter(), self.initial)
    def __iter__(self):
        acc = self.initial
        if acc is not _coconut_sentinel:
            yield acc
        for item in self.iter:
            if acc is _coconut_sentinel:
                acc = item
            else:
                acc = self.func(acc, item)
            yield acc
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.len(self.iter)
class reversed(_coconut_has_iter):
    __slots__ = ()
    __doc__ = getattr(_coconut.reversed, "__doc__", "<see help(py_reversed)>")
    def __new__(cls, iterable):
        if _coconut.isinstance(iterable, _coconut.range):
            return iterable[::-1]
        if _coconut.getattr(iterable, "__reversed__", None) is None or _coconut.isinstance(iterable, (_coconut.list, _coconut.tuple)):
            self = _coconut_has_iter.__new__(cls, iterable)
            return self
        return _coconut.reversed(iterable)
    def __repr__(self):
        return "reversed(%s)" % (_coconut.repr(self.iter),)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    def __iter__(self):
        return _coconut.iter(_coconut.reversed(self.iter))
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return _coconut_iter_getitem(self.iter, _coconut.slice(-(index.start + 1) if index.start is not None else None, -(index.stop + 1) if index.stop else None, -(index.step if index.step is not None else 1)))
        return _coconut_iter_getitem(self.iter, -(index + 1))
    def __reversed__(self):
        return self.iter
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.len(self.iter)
    def __contains__(self, elem):
        return elem in self.iter
    def count(self, elem):
        """Count the number of times elem appears in the reversed iterable."""
        return self.iter.count(elem)
    def index(self, elem):
        """Find the index of elem in the reversed iterable."""
        return _coconut.len(self.iter) - self.iter.index(elem) - 1
    def __fmap__(self, func):
        return self.__class__(_coconut_map(func, self.iter))
class flatten(_coconut_has_iter):
    """Flatten an iterable of iterables into a single iterable.
    Flattens the first axis of numpy arrays."""
    __slots__ = ()
    def __new__(cls, iterable):
        if iterable.__class__.__module__ in _coconut.numpy_modules:
            if len(iterable.shape) < 2:
                raise _coconut.TypeError("flatten() on numpy arrays requires two or more dimensions")
            return iterable.reshape(-1, *iterable.shape[2:])
        self = _coconut_has_iter.__new__(cls, iterable)
        return self
    def get_new_iter(self):
        """Tee the underlying iterator."""
        with self.lock:
            if not (_coconut.isinstance(self.iter, _coconut_reiterable) and _coconut.isinstance(self.iter.iter, _coconut_map) and self.iter.iter.func is _coconut_reiterable):
                self.iter = _coconut_map(_coconut_reiterable, self.iter)
            self.iter = _coconut_reiterable(self.iter)
        return self.iter
    def __iter__(self):
        return _coconut.itertools.chain.from_iterable(self.iter)
    def __reversed__(self):
        return self.__class__(_coconut_reversed(_coconut_map(_coconut_reversed, self.get_new_iter())))
    def __repr__(self):
        return "flatten(%s)" % (_coconut.repr(self.iter),)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    def __contains__(self, elem):
        return _coconut.any(elem in it for it in self.get_new_iter())
    def count(self, elem):
        """Count the number of times elem appears in the flattened iterable."""
        return _coconut.sum(it.count(elem) for it in self.get_new_iter())
    def index(self, elem):
        """Find the index of elem in the flattened iterable."""
        ind = 0
        for it in self.get_new_iter():
            try:
                return ind + it.index(elem)
            except _coconut.ValueError:
                ind += _coconut.len(it)
        raise ValueError("%r not in %r" % (elem, self))
    def __fmap__(self, func):
        return self.__class__(_coconut_map(_coconut.functools.partial(_coconut_map, func), self.get_new_iter()))
class cartesian_product(_coconut_base_hashable):
    __slots__ = ("iters", "repeat")
    __doc__ = getattr(_coconut.itertools.product, "__doc__", "Cartesian product of input iterables.") + """

Additionally supports Cartesian products of numpy arrays."""
    def __new__(cls, *iterables, **kwargs):
        repeat = kwargs.pop("repeat", 1)
        if kwargs:
            raise _coconut.TypeError("cartesian_product() got unexpected keyword arguments " + _coconut.repr(kwargs))
        if iterables and _coconut.all(it.__class__.__module__ in _coconut.numpy_modules for it in iterables):
            if _coconut.any(it.__class__.__module__ in _coconut.jax_numpy_modules for it in iterables):
                from jax import numpy
            else:
                numpy = _coconut.numpy
            iterables *= repeat
            la = _coconut.len(iterables)
            dtype = numpy.result_type(*iterables)
            arr = numpy.empty([_coconut.len(a) for a in iterables] + [la], dtype=dtype)
            for i, a in _coconut.enumerate(numpy.ix_(*iterables)):
                arr[...,i] = a
            return arr.reshape(-1, la)
        self = _coconut.object.__new__(cls)
        self.iters = iterables
        self.repeat = repeat
        return self
    def __iter__(self):
        return _coconut.itertools.product(*self.iters, repeat=self.repeat)
    def __repr__(self):
        return "cartesian_product(" + ", ".join(_coconut.repr(it) for it in self.iters) + (", repeat=" + _coconut.repr(self.repeat) if self.repeat != 1 else "") + ")"
    def __reduce__(self):
        return (self.__class__, self.iters, {"repeat": self.repeat})
    def __copy__(self):
        self.iters = _coconut.tuple(_coconut_reiterable(it) for it in self.iters)
        return self.__class__(*self.iters, repeat=self.repeat)
    @property
    def all_iters(self):
        return _coconut.itertools.chain.from_iterable(_coconut.itertools.repeat(self.iters, self.repeat))
    def __len__(self):
        total_len = 1
        for it in self.iters:
            if not _coconut.isinstance(it, _coconut.abc.Sized):
                return _coconut.NotImplemented
            total_len *= _coconut.len(it)
        return total_len ** self.repeat
    def __contains__(self, elem):
        for e, it in _coconut.zip_longest(elem, self.all_iters, fillvalue=_coconut_sentinel):
            if e is _coconut_sentinel or it is _coconut_sentinel or e not in it:
                return False
        return True
    def count(self, elem):
        """Count the number of times elem appears in the product."""
        total_count = 1
        for e, it in _coconut.zip_longest(elem, self.all_iters, fillvalue=_coconut_sentinel):
            if e is _coconut_sentinel or it is _coconut_sentinel:
                return 0
            total_count *= it.count(e)
            if not total_count:
                return total_count
        return total_count
    def __fmap__(self, func):
        return _coconut_map(func, self)
class map(_coconut_base_hashable, _coconut.map):
    __slots__ = ("func", "iters")
    __doc__ = getattr(_coconut.map, "__doc__", "<see help(py_map)>")
    def __new__(cls, function, *iterables):
        self = _coconut.map.__new__(cls, function, *iterables)
        self.func = function
        self.iters = iterables
        return self
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, *(_coconut_iter_getitem(it, index) for it in self.iters))
        return self.func(*(_coconut_iter_getitem(it, index) for it in self.iters))
    def __reversed__(self):
        return self.__class__(self.func, *(_coconut_reversed(it) for it in self.iters))
    def __len__(self):
        if not _coconut.all(_coconut.isinstance(it, _coconut.abc.Sized) for it in self.iters):
            return _coconut.NotImplemented
        return _coconut.min(_coconut.len(it) for it in self.iters)
    def __repr__(self):
        return "map(%r, %s)" % (self.func, ", ".join((_coconut.repr(i) for i in self.iters)))
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.iters)
    def __copy__(self):
        self.iters = _coconut.tuple(_coconut_reiterable(it) for it in self.iters)
        return self.__class__(self.func, *self.iters)
    def __iter__(self):
        return _coconut.iter(_coconut.map(self.func, *self.iters))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), *self.iters)
class _coconut_parallel_concurrent_map_func_wrapper(_coconut_base_hashable):
    __slots__ = ("map_cls", "func", "star")
    def __init__(self, map_cls, func, star):
        self.map_cls = map_cls
        self.func = func
        self.star = star
    def __reduce__(self):
        return (self.__class__, (self.map_cls, self.func, self.star))
    def __call__(self, *args, **kwargs):
        self.map_cls.get_pool_stack().append(None)
        try:
            if self.star:
                assert _coconut.len(args) == 1, "internal parallel/concurrent map error (you should report this at https://github.com/evhub/coconut/issues/new)"
                return self.func(*args[0], **kwargs)
            else:
                return self.func(*args, **kwargs)
        except:
            _coconut.print(self.map_cls.__name__ + " error:")
            _coconut.traceback.print_exc()
            raise
        finally:
            assert self.map_cls.get_pool_stack().pop() is None, "internal parallel/concurrent map error (you should report this at https://github.com/evhub/coconut/issues/new)"
class _coconut_base_parallel_concurrent_map(map):
    __slots__ = ("result", "chunksize")
    @classmethod
    def get_pool_stack(cls):
        return cls.threadlocal_ns.__dict__.setdefault("pool_stack", [None])
    def __new__(cls, function, *iterables, **kwargs):
        self = _coconut_map.__new__(cls, function, *iterables)
        self.result = None
        self.chunksize = kwargs.pop("chunksize", 1)
        if kwargs:
            raise _coconut.TypeError(cls.__name__ + "() got unexpected keyword arguments " + _coconut.repr(kwargs))
        if cls.get_pool_stack()[-1] is not None:
            return self.get_list()
        return self
    @classmethod
    @_coconut.contextlib.contextmanager
    def multiple_sequential_calls(cls, max_workers=None):
        """Context manager that causes nested calls to use the same pool."""
        if cls.get_pool_stack()[-1] is None:
            cls.get_pool_stack()[-1] = cls.make_pool(max_workers)
            try:
                yield
            finally:
                cls.get_pool_stack()[-1].terminate()
                cls.get_pool_stack()[-1] = None
        else:
            yield
    def get_list(self):
        if self.result is None:
            with self.multiple_sequential_calls():
                if _coconut.len(self.iters) == 1:
                    self.result = _coconut.list(self.get_pool_stack()[-1].imap(_coconut_parallel_concurrent_map_func_wrapper(self.__class__, self.func, False), self.iters[0], self.chunksize))
                else:
                    self.result = _coconut.list(self.get_pool_stack()[-1].imap(_coconut_parallel_concurrent_map_func_wrapper(self.__class__, self.func, True), _coconut.zip(*self.iters), self.chunksize))
            self.func = _coconut_ident
            self.iters = (self.result,)
        return self.result
    def __iter__(self):
        return _coconut.iter(self.get_list())
class parallel_map(_coconut_base_parallel_concurrent_map):
    """Multi-process implementation of map. Requires arguments to be pickleable.

    For multiple sequential calls, use:
        with parallel_map.multiple_sequential_calls():
            ...
    """
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_pool(max_workers=None):
        return _coconut.multiprocessing.Pool(max_workers)
    def __repr__(self):
        return "parallel_" + _coconut_map.__repr__(self)
class concurrent_map(_coconut_base_parallel_concurrent_map):
    """Multi-thread implementation of map.

    For multiple sequential calls, use:
        with concurrent_map.multiple_sequential_calls():
            ...
    """
    __slots__ = ()
    threadlocal_ns = _coconut.threading.local()
    @staticmethod
    def make_pool(max_workers=None):
        return _coconut.multiprocessing_dummy.Pool(_coconut.multiprocessing.cpu_count() * 5 if max_workers is None else max_workers)
    def __repr__(self):
        return "concurrent_" + _coconut_map.__repr__(self)
class filter(_coconut_base_hashable, _coconut.filter):
    __slots__ = ("func", "iter")
    __doc__ = getattr(_coconut.filter, "__doc__", "<see help(py_filter)>")
    def __new__(cls, function, iterable):
        self = _coconut.filter.__new__(cls, function, iterable)
        self.func = function
        self.iter = iterable
        return self
    def __reversed__(self):
        return self.__class__(self.func, _coconut_reversed(self.iter))
    def __repr__(self):
        return "filter(%r, %s)" % (self.func, _coconut.repr(self.iter))
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __copy__(self):
        self.iter = _coconut_reiterable(self.iter)
        return self.__class__(self.func, self.iter)
    def __iter__(self):
        return _coconut.iter(_coconut.filter(self.func, self.iter))
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip(_coconut_base_hashable, _coconut.zip):
    __slots__ = ("iters", "strict")
    __doc__ = getattr(_coconut.zip, "__doc__", "<see help(py_zip)>")
    def __new__(cls, *iterables, **kwargs):
        self = _coconut.zip.__new__(cls, *iterables)
        self.iters = iterables
        self.strict = kwargs.pop("strict", False)
        if kwargs:
            raise _coconut.TypeError("zip() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return self
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(*(_coconut_iter_getitem(i, index) for i in self.iters), strict=self.strict)
        return _coconut.tuple(_coconut_iter_getitem(i, index) for i in self.iters)
    def __reversed__(self):
        return self.__class__(*(_coconut_reversed(i) for i in self.iters), strict=self.strict)
    def __len__(self):
        if not _coconut.all(_coconut.isinstance(it, _coconut.abc.Sized) for it in self.iters):
            return _coconut.NotImplemented
        return _coconut.min(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip(%s%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), ", strict=True" if self.strict else "")
    def __reduce__(self):
        return (self.__class__, self.iters, {"strict": self.strict})
    def __copy__(self):
        self.iters = _coconut.tuple(_coconut_reiterable(it) for it in self.iters)
        return self.__class__(*self.iters, strict=self.strict)
    def __iter__(self):
        for items in _coconut.iter(_coconut.zip_longest(*self.iters, fillvalue=_coconut_sentinel) if self.strict else _coconut.zip(*self.iters)):
            if self.strict and _coconut.any(x is _coconut_sentinel for x in items):
                raise _coconut.ValueError("zip(..., strict=True) arguments have mismatched lengths")
            yield items
    def __fmap__(self, func):
        return _coconut_map(func, self)
class zip_longest(zip):
    __slots__ = ("fillvalue",)
    __doc__ = getattr(_coconut.zip_longest, "__doc__", "Version of zip that fills in missing values with fillvalue.")
    def __new__(cls, *iterables, **kwargs):
        self = _coconut_zip.__new__(cls, *iterables, strict=False)
        self.fillvalue = kwargs.pop("fillvalue", None)
        if kwargs:
            raise _coconut.TypeError("zip_longest() got unexpected keyword arguments " + _coconut.repr(kwargs))
        return self
    def __getitem__(self, index):
        self_len = None
        if _coconut.isinstance(index, _coconut.slice):
            if self_len is None:
                self_len = self.__len__()
                if self_len is _coconut.NotImplemented:
                    return self_len
            new_ind = _coconut.slice(index.start + self_len if index.start is not None and index.start < 0 else index.start, index.stop + self_len if index.stop is not None and index.stop < 0 else index.stop, index.step)
            return self.__class__(*(_coconut_iter_getitem(i, new_ind) for i in self.iters))
        if index < 0:
            if self_len is None:
                self_len = self.__len__()
                if self_len is _coconut.NotImplemented:
                    return self_len
            index += self_len
        result = []
        got_non_default = False
        for it in self.iters:
            try:
                result.append(_coconut_iter_getitem(it, index))
            except _coconut.IndexError:
                result.append(self.fillvalue)
            else:
                got_non_default = True
        if not got_non_default:
            raise _coconut.IndexError("zip_longest index out of range")
        return _coconut.tuple(result)
    def __len__(self):
        if not _coconut.all(_coconut.isinstance(it, _coconut.abc.Sized) for it in self.iters):
            return _coconut.NotImplemented
        return _coconut.max(_coconut.len(i) for i in self.iters)
    def __repr__(self):
        return "zip_longest(%s, fillvalue=%s)" % (", ".join((_coconut.repr(i) for i in self.iters)), _coconut.repr(self.fillvalue))
    def __reduce__(self):
        return (self.__class__, self.iters, {"fillvalue": self.fillvalue})
    def __copy__(self):
        self.iters = _coconut.tuple(_coconut_reiterable(it) for it in self.iters)
        return self.__class__(*self.iters, fillvalue=self.fillvalue)
    def __iter__(self):
        return _coconut.iter(_coconut.zip_longest(*self.iters, fillvalue=self.fillvalue))
class enumerate(_coconut_base_hashable, _coconut.enumerate):
    __slots__ = ("iter", "start")
    __doc__ = getattr(_coconut.enumerate, "__doc__", "<see help(py_enumerate)>")
    def __new__(cls, iterable, start=0):
        self = _coconut.enumerate.__new__(cls, iterable, start)
        self.iter = iterable
        self.start = start
        return self
    def __repr__(self):
        return "enumerate(%s, %r)" % (_coconut.repr(self.iter), self.start)
    def __fmap__(self, func):
        return _coconut_map(func, self)
    def __reduce__(self):
        return (self.__class__, (self.iter, self.start))
    def __copy__(self):
        self.iter = _coconut_reiterable(self.iter)
        return self.__class__(self.iter, self.start)
    def __iter__(self):
        return _coconut.iter(_coconut.enumerate(self.iter, self.start))
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(_coconut_iter_getitem(self.iter, index), self.start + (0 if index.start is None else index.start if index.start >= 0 else _coconut.len(self.iter) + index.start))
        return (self.start + index, _coconut_iter_getitem(self.iter, index))
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.len(self.iter)
class multi_enumerate(_coconut_has_iter):
    """Enumerate an iterable of iterables. Works like enumerate, but indexes
    through inner iterables and produces a tuple index representing the index
    in each inner iterable. Supports indexing.

    For numpy arrays, effectively equivalent to:
        it = np.nditer(iterable, flags=["multi_index"])
        for x in it:
            yield it.multi_index, x

    Also supports len for numpy arrays.
    """
    __slots__ = ()
    def __repr__(self):
        return "multi_enumerate(%s)" % (_coconut.repr(self.iter),)
    def __reduce__(self):
        return (self.__class__, (self.iter,))
    def __copy__(self):
        return self.__class__(self.get_new_iter())
    @property
    def is_numpy(self):
        return self.iter.__class__.__module__ in _coconut.numpy_modules
    def __iter__(self):
        if self.is_numpy:
            it = _coconut.numpy.nditer(self.iter, flags=["multi_index"])
            for x in it:
                yield it.multi_index, x
        else:
            ind = [-1]
            its = [_coconut.iter(self.iter)]
            while its:
                ind[-1] += 1
                try:
                    x = _coconut.next(its[-1])
                except _coconut.StopIteration:
                    ind.pop()
                    its.pop()
                else:
                    if _coconut.isinstance(x, _coconut.abc.Iterable):
                        ind.append(-1)
                        its.append(_coconut.iter(x))
                    else:
                        yield _coconut.tuple(ind), x
    def __getitem__(self, index):
        if self.is_numpy and not _coconut.isinstance(index, _coconut.slice):
            multi_ind = []
            for i in _coconut.reversed(self.iter.shape):
                multi_ind.append(index % i)
                index //= i
            multi_ind = _coconut.tuple(_coconut.reversed(multi_ind))
            return multi_ind, self.iter[multi_ind]
        return _coconut_iter_getitem(_coconut.iter(self), index)
    def __len__(self):
        if self.is_numpy:
            return self.iter.size
        return _coconut.NotImplemented
class count(_coconut_base_hashable):
    __slots__ = ("start", "step")
    __doc__ = getattr(_coconut.itertools.count, "__doc__", "count(start, step) returns an infinite iterator starting at start and increasing by step.")
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
    def __reduce__(self):
        return (self.__class__, (self.start, self.step))
    def __repr__(self):
        return "count(%s, %s)" % (_coconut.repr(self.start), _coconut.repr(self.step))
    def __iter__(self):
        while True:
            yield self.start
            if self.step:
                self.start += self.step
    def __fmap__(self, func):
        return _coconut_map(func, self)
    def __contains__(self, elem):
        if not self.step:
            return elem == self.start
        if self.step > 0 and elem < self.start or self.step < 0 and elem > self.start:
            return False
        return (elem - self.start) % self.step == 0
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            if (index.start is None or index.start >= 0) and (index.stop is None or index.stop >= 0):
                new_start, new_step = self.start, self.step
                if self.step and index.start is not None:
                    new_start += self.step * index.start
                if self.step and index.step is not None:
                    new_step *= index.step
                if index.stop is None:
                    return self.__class__(new_start, new_step)
                if self.step and _coconut.isinstance(self.start, _coconut.int) and _coconut.isinstance(self.step, _coconut.int):
                    return _coconut.range(new_start, self.start + self.step * index.stop, new_step)
                return _coconut_map(self.__getitem__, _coconut.range(index.start if index.start is not None else 0, index.stop, index.step if index.step is not None else 1))
            raise _coconut.IndexError("count() indices must be positive")
        if index < 0:
            raise _coconut.IndexError("count() indices must be positive")
        return self.start + self.step * index if self.step else self.start
    def count(self, elem):
        """Count the number of times elem appears in the count."""
        if not self.step:
            return _coconut.float("inf") if elem == self.start else 0
        return _coconut.int(elem in self)
    def index(self, elem):
        """Find the index of elem in the count."""
        if elem not in self:
            raise _coconut.ValueError(_coconut.repr(elem) + " not in " + _coconut.repr(self))
        return (elem - self.start) // self.step if self.step else 0
    def __reversed__(self):
        if not self.step:
            return self
        raise _coconut.TypeError(_coconut.repr(self) + " object is not reversible")
class cycle(_coconut_has_iter):
    __slots__ = ("times",)
    def __new__(cls, iterable, times=None):
        if times is not None:
            if iterable.__class__.__module__ in _coconut.numpy_modules:
                return _coconut.numpy.concatenate((iterable,) * times)
            if iterable.__class__.__module__ in _coconut.jax_numpy_modules:
                import jax.numpy as jnp
                return jnp.concatenate((iterable,) * times)
        self = _coconut_has_iter.__new__(cls, iterable)
        self.times = times
        return self
    def __reduce__(self):
        return (self.__class__, (self.iter, self.times))
    def __copy__(self):
        return self.__class__(self.get_new_iter(), self.times)
    def __repr__(self):
        return "cycle(%s, %r)" % (_coconut.repr(self.iter), self.times)
    def __iter__(self):
        i = 0
        while self.times is None or i < self.times:
            for x in self.get_new_iter():
                yield x
            i += 1
    def __contains__(self, elem):
        return elem in self.iter
    def __getitem__(self, index):
        if not _coconut.isinstance(index, _coconut.slice):
            if self.times is not None and index // _coconut.len(self.iter) >= self.times:
                raise _coconut.IndexError("cycle index out of range")
            return self.iter[index % _coconut.len(self.iter)]
        if self.times is None:
            return _coconut_map(self.__getitem__, _coconut_count()[index])
        else:
            return _coconut_map(self.__getitem__, _coconut_range(0, _coconut.len(self))[index])
    def __len__(self):
        if self.times is None:
            return _coconut.NotImplemented
        return _coconut.len(self.iter) * self.times
    def __reversed__(self):
        if self.times is None:
            raise _coconut.TypeError(_coconut.repr(self) + " object is not reversible")
        return self.__class__(_coconut_reversed(self.get_new_iter()), self.times)
    def count(self, elem):
        """Count the number of times elem appears in the cycle."""
        return self.iter.count(elem) * (float("inf") if self.times is None else self.times)
    def index(self, elem):
        """Find the index of elem in the cycle."""
        if elem not in self.iter:
            raise _coconut.ValueError(_coconut.repr(elem) + " not in " + _coconut.repr(self))
        return self.iter.index(elem)
class groupsof(_coconut_has_iter):
    """groupsof(n, iterable) splits iterable into groups of size n.

    If the length of the iterable is not divisible by n, the last group will be of size < n.
    """
    __slots__ = ("group_size",)
    def __new__(cls, n, iterable):
        self = _coconut_has_iter.__new__(cls, iterable)
        self.group_size = _coconut.operator.index(n)
        if self.group_size <= 0:
            raise _coconut.ValueError("group size must be > 0; not %r" % (self.group_size,))
        return self
    def __iter__(self):
        iterator = _coconut.iter(self.iter)
        loop = True
        while loop:
            group = []
            for _ in _coconut.range(self.group_size):
                try:
                    group.append(_coconut.next(iterator))
                except _coconut.StopIteration:
                    loop = False
                    break
            if group:
                yield _coconut.tuple(group)
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.int(_coconut.math.ceil(_coconut.len(self.iter) / self.group_size))
    def __repr__(self):
        return "groupsof(%r, %s)" % (self.group_size, _coconut.repr(self.iter))
    def __reduce__(self):
        return (self.__class__, (self.group_size, self.iter))
    def __copy__(self):
        return self.__class__(self.group_size, self.get_new_iter())
class recursive_iterator(_coconut_base_hashable):
    """Decorator that optimizes a recursive function that returns an iterator (e.g. a recursive generator)."""
    __slots__ = ("func", "reit_store", "backup_reit_store")
    def __init__(self, func):
        self.func = func
        self.reit_store = {}
        self.backup_reit_store = []
    def __call__(self, *args, **kwargs):
        key = (args, _coconut.frozenset(kwargs.items()))
        use_backup = False
        try:
            _coconut.hash(key)
        except _coconut.Exception:
            try:
                key = _coconut.pickle.dumps(key, -1)
            except _coconut.Exception:
                use_backup = True
        if use_backup:
            for k, v in self.backup_reit_store:
                if k == key:
                    return reit
            reit = _coconut_reiterable(self.func(*args, **kwargs))
            self.backup_reit_store.append([key, reit])
            return reit
        else:
            reit = self.reit_store.get(key)
            if reit is None:
                reit = _coconut_reiterable(self.func(*args, **kwargs))
                self.reit_store[key] = reit
            return reit
    def __repr__(self):
        return "recursive_iterator(%r)" % (self.func,)
    def __reduce__(self):
        return (self.__class__, (self.func,))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.types.MethodType(self, obj)
class _coconut_FunctionMatchErrorContext:
    __slots__ = ("exc_class", "taken")
    threadlocal_ns = _coconut.threading.local()
    def __init__(self, exc_class):
        self.exc_class = exc_class
        self.taken = False
    @classmethod
    def get_contexts(cls):
        try:
            return cls.threadlocal_ns.contexts
        except _coconut.AttributeError:
            cls.threadlocal_ns.contexts = []
            return cls.threadlocal_ns.contexts
    def __enter__(self):
        self.get_contexts().append(self)
    def __exit__(self, type, value, traceback):
        self.get_contexts().pop()
def _coconut_get_function_match_error():
    try:
        ctx = _coconut_FunctionMatchErrorContext.get_contexts()[-1]
    except _coconut.IndexError:
        return _coconut_MatchError
    if ctx.taken:
        return _coconut_MatchError
    ctx.taken = True
    return ctx.exc_class
class _coconut_base_pattern_func(_coconut_base_hashable):
    _coconut_is_match = True
    def __init__(self, *funcs):
        self.FunctionMatchError = _coconut.type(_coconut_py_str("MatchError"), (_coconut_MatchError,), {})
        self.patterns = []
        self.__doc__ = None
        self.__name__ = None
        if _coconut_sys.version_info >= (3, 7):
            self.__qualname__ = None
        for func in funcs:
            self.add_pattern(func)
    def add_pattern(self, func):
        if _coconut.isinstance(func, _coconut_base_pattern_func):
            self.patterns += func.patterns
        else:
            self.patterns.append(func)
        self.__doc__ = _coconut.getattr(func, "__doc__", self.__doc__)
        self.__name__ = _coconut.getattr(func, "__name__", self.__name__)
        if _coconut_sys.version_info >= (3, 7):
            self.__qualname__ = _coconut.getattr(func, "__qualname__", self.__qualname__)
    def __call__(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return self.patterns[-1](*args, **kwargs)
    def _coconut_tco_func(self, *args, **kwargs):
        for func in self.patterns[:-1]:
            try:
                with _coconut_FunctionMatchErrorContext(self.FunctionMatchError):
                    return func(*args, **kwargs)
            except self.FunctionMatchError:
                pass
        return _coconut_tail_call(self.patterns[-1], *args, **kwargs)
    def __repr__(self):
        return "addpattern(%r)(*%r)" % (self.patterns[0], self.patterns[1:])
    def __reduce__(self):
        return (self.__class__, _coconut.tuple(self.patterns))
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return _coconut.types.MethodType(self, obj)
def _coconut_mark_as_match(base_func):
    base_func._coconut_is_match = True
    return base_func
def addpattern(base_func, new_pattern=None, **kwargs):
    """Decorator to add a new case to a pattern-matching function (where the new case is checked last).

    Pass allow_any_func=True to allow any object as the base_func rather than just pattern-matching functions.
    If new_pattern is passed, addpattern(base_func, new_pattern) is equivalent to addpattern(base_func)(new_pattern).
    """
    allow_any_func = kwargs.pop("allow_any_func", False)
    if not allow_any_func and not _coconut.getattr(base_func, "_coconut_is_match", False):
        _coconut.warnings.warn("Possible misuse of addpattern with non-pattern-matching function " + _coconut.repr(base_func) + " (pass allow_any_func=True to dismiss)", stacklevel=2)
    if kwargs:
        raise _coconut.TypeError("addpattern() got unexpected keyword arguments " + _coconut.repr(kwargs))
    if new_pattern is not None:
        return _coconut_base_pattern_func(base_func, new_pattern)
    return _coconut.functools.partial(_coconut_base_pattern_func, base_func)
_coconut_addpattern = addpattern
def prepattern(*args, **kwargs):
    """Deprecated built-in 'prepattern' disabled by --strict compilation; use 'addpattern' instead."""
    raise _coconut.NameError("deprecated built-in 'prepattern' disabled by --strict compilation; use 'addpattern' instead")
class _coconut_partial(_coconut_base_hashable):
    __slots__ = ("func", "_argdict", "_arglen", "_pos_kwargs", "_stargs", "keywords")
    def __init__(self, _coconut_func, _coconut_argdict, _coconut_arglen, _coconut_pos_kwargs, *args, **kwargs):
        self.func = _coconut_func
        self._argdict = _coconut_argdict
        self._arglen = _coconut_arglen
        self._pos_kwargs = _coconut_pos_kwargs
        self._stargs = args
        self.keywords = kwargs
    def __reduce__(self):
        return (self.__class__, (self.func, self._argdict, self._arglen, self._pos_kwargs) + self._stargs, {"keywords": self.keywords})
    @property
    def args(self):
        return _coconut.tuple(self._argdict.get(i) for i in _coconut.range(self._arglen)) + self._stargs
    @property
    def required_nargs(self):
        return self._arglen - _coconut.len(self._argdict) + len(self._pos_kwargs)
    def __call__(self, *args, **kwargs):
        callargs = []
        argind = 0
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                callargs.append(self._argdict[i])
            elif argind >= _coconut.len(args):
                raise _coconut.TypeError("expected at least " + _coconut.str(self.required_nargs) + " argument(s) to " + _coconut.repr(self))
            else:
                callargs.append(args[argind])
                argind += 1
        for k in self._pos_kwargs:
            if k in kwargs:
                raise _coconut.TypeError(_coconut.repr(k) + " is an invalid keyword argument for " + _coconut.repr(self))
            elif argind >= _coconut.len(args):
                raise _coconut.TypeError("expected at least " + _coconut.str(self.required_nargs) + " argument(s) to " + _coconut.repr(self))
            else:
                kwargs[k] = args[argind]
                argind += 1
        callargs += self._stargs
        callargs += args[argind:]
        callkwargs = self.keywords.copy()
        callkwargs.update(kwargs)
        return self.func(*callargs, **callkwargs)
    def __repr__(self):
        args = []
        for i in _coconut.range(self._arglen):
            if i in self._argdict:
                args.append(_coconut.repr(self._argdict[i]))
            else:
                args.append("?")
        for arg in self._stargs:
            args.append(_coconut.repr(arg))
        for k in self._pos_kwargs:
            args.append(k + "=?")
        for k, v in self.keywords.items():
            args.append(k + "=" + _coconut.repr(v))
        return "%r$(%s)" % (self.func, ", ".join(args))
def consume(iterable, keep_last=0):
    """consume(iterable, keep_last) fully exhausts iterable and returns the last keep_last elements."""
    return _coconut.collections.deque(iterable, maxlen=keep_last)
class starmap(_coconut_base_hashable, _coconut.itertools.starmap):
    __slots__ = ("func", "iter")
    __doc__ = getattr(_coconut.itertools.starmap, "__doc__", "starmap(func, iterable) = (func(*args) for args in iterable)")
    def __new__(cls, function, iterable):
        self = _coconut.itertools.starmap.__new__(cls, function, iterable)
        self.func = function
        self.iter = iterable
        return self
    def __getitem__(self, index):
        if _coconut.isinstance(index, _coconut.slice):
            return self.__class__(self.func, _coconut_iter_getitem(self.iter, index))
        return self.func(*_coconut_iter_getitem(self.iter, index))
    def __reversed__(self):
        return self.__class__(self.func, *_coconut_reversed(self.iter))
    def __len__(self):
        if not _coconut.isinstance(self.iter, _coconut.abc.Sized):
            return _coconut.NotImplemented
        return _coconut.len(self.iter)
    def __repr__(self):
        return "starmap(%r, %s)" % (self.func, _coconut.repr(self.iter))
    def __reduce__(self):
        return (self.__class__, (self.func, self.iter))
    def __copy__(self):
        self.iter = _coconut_reiterable(self.iter)
        return self.__class__(self.func, self.iter)
    def __iter__(self):
        return _coconut.iter(_coconut.itertools.starmap(self.func, self.iter))
    def __fmap__(self, func):
        return self.__class__(_coconut_forward_compose(self.func, func), self.iter)
class multiset(_coconut.collections.Counter):
    __slots__ = ()
    __doc__ = getattr(_coconut.collections.Counter, "__doc__", "multiset is a version of set that counts the number of times each element is added.")
    def add(self, item):
        """Add an element to a multiset."""
        self[item] += 1
    def discard(self, item):
        """Remove an element from a multiset if it is a member."""
        item_count = self[item]
        if item_count > 0:
            self[item] = item_count - 1
            if item_count - 1 <= 0:
                del self[item]
    def remove(self, item):
        """Remove an element from a multiset; it must be a member."""
        item_count = self[item]
        if item_count > 0:
            self[item] = item_count - 1
            if item_count - 1 <= 0:
                del self[item]
        else:
            raise _coconut.KeyError(item)
    def isdisjoint(self, other):
        """Return True if two multisets have a null intersection."""
        return not self & other
    def __xor__(self, other):
        return self - other | other - self
    def count(self, item):
        """Return the number of times an element occurs in a multiset.
        Equivalent to multiset[item], but additionally verifies the count is non-negative."""
        result = self[item]
        if result < 0:
            raise _coconut.ValueError("multiset has negative count for " + _coconut.repr(item))
        return result
    if _coconut_sys.version_info < (3, 10):
        def total(self):
            """Compute the sum of the counts in a multiset.
            Note that total_size is different from len(multiset), which only counts the unique elements."""
            return _coconut.sum(self.values())
        def __eq__(self, other):
            if not _coconut.isinstance(other, _coconut.dict):
                return False
            if not _coconut.isinstance(other, _coconut.collections.Counter):
                return _coconut.NotImplemented
            for k, v in self.items():
                if other[k] != v:
                    return False
            for k, v in other.items():
                if self[k] != v:
                    return False
            return True
        __ne__ = _coconut.object.__ne__
        def __le__(self, other):
            if not _coconut.isinstance(other, _coconut.collections.Counter):
                return _coconut.NotImplemented
            for k, v in self.items():
                if not (v <= other[k]):
                    return False
            for k, v in other.items():
                if not (self[k] <= v):
                    return False
            return True
        def __lt__(self, other):
            if not _coconut.isinstance(other, _coconut.collections.Counter):
                return _coconut.NotImplemented
            found_diff = False
            for k, v in self.items():
                if not (v <= other[k]):
                    return False
                found_diff = found_diff or v != other[k]
            for k, v in other.items():
                if not (self[k] <= v):
                    return False
                found_diff = found_diff or self[k] != v
            return found_diff
_coconut.abc.MutableSet.register(multiset)
def _coconut_base_makedata(data_type, args):
    if _coconut.hasattr(data_type, "_make") and _coconut.issubclass(data_type, _coconut.tuple):
        return data_type._make(args)
    if _coconut.issubclass(data_type, (_coconut.range, _coconut.abc.Iterator)):
        return args
    if _coconut.issubclass(data_type, _coconut.str):
        return "".join(args)
    return data_type(args)
def makedata(data_type, *args):
    """Construct an object of the given data_type containing the given arguments."""
    return _coconut_base_makedata(data_type, args)
def datamaker(*args, **kwargs):
    """Deprecated built-in 'datamaker' disabled by --strict compilation; use 'makedata' instead."""
    raise _coconut.NameError("deprecated built-in 'datamaker' disabled by --strict compilation; use 'makedata' instead")
class _coconut_amap(_coconut_base_hashable):
    __slots__ = ("func", "aiter")
    def __init__(self, func, aiter):
        self.func = func
        self.aiter = aiter
    def __reduce__(self):
        return (self.__class__, (self.func, self.aiter))
    def __repr__(self):
        return "fmap(" + _coconut.repr(self.func) + ", " + _coconut.repr(self.aiter) + ")"
    def __aiter__(self):
        return self
    async def __anext__(self):
        return self.func(await self.aiter.__anext__())
def fmap(func, obj, **kwargs):
    """fmap(func, obj) creates a copy of obj with func applied to its contents.
    Supports asynchronous iterables, mappings (maps over .items()), and numpy arrays (uses np.vectorize).

    Override by defining obj.__fmap__(func).
    """
    starmap_over_mappings = kwargs.pop("starmap_over_mappings", False)
    if kwargs:
        raise _coconut.TypeError("fmap() got unexpected keyword arguments " + _coconut.repr(kwargs))
    if obj is None:
        return None
    obj_fmap = _coconut.getattr(obj, "__fmap__", None)
    if obj_fmap is not None:
        try:
            result = obj_fmap(func)
        except _coconut.NotImplementedError:
            pass
        else:
            if result is not _coconut.NotImplemented:
                return result
    if obj.__class__.__module__ in _coconut.jax_numpy_modules:
        import jax.numpy as jnp
        return jnp.vectorize(func)(obj)
    if obj.__class__.__module__ in _coconut.numpy_modules:
        return _coconut.numpy.vectorize(func)(obj)
    obj_aiter = _coconut.getattr(obj, "__aiter__", None)
    if obj_aiter is not None and _coconut_amap is not None:
        try:
            aiter = obj_aiter()
        except _coconut.NotImplementedError:
            pass
        else:
            if aiter is not _coconut.NotImplemented:
                return _coconut_amap(func, aiter)
    if starmap_over_mappings:
        return _coconut_base_makedata(obj.__class__, _coconut_starmap(func, obj.items()) if _coconut.isinstance(obj, _coconut.abc.Mapping) else _coconut_map(func, obj))
    else:
        return _coconut_base_makedata(obj.__class__, _coconut_map(func, obj.items() if _coconut.isinstance(obj, _coconut.abc.Mapping) else obj))
def _coconut_memoize_helper(maxsize=None, typed=False):
    return maxsize, typed
def memoize(*args, **kwargs):
    """Decorator that memoizes a function, preventing it from being recomputed
    if it is called multiple times with the same arguments."""
    if not kwargs and _coconut.len(args) == 1 and _coconut.callable(args[0]):
        return _coconut.functools.lru_cache(maxsize=None)(args[0])
    if _coconut.len(kwargs) == 1 and "user_function" in kwargs and _coconut.callable(kwargs["user_function"]):
        return _coconut.functools.lru_cache(maxsize=None)(kwargs["user_function"])
    maxsize, typed = _coconut_memoize_helper(*args, **kwargs)
    return _coconut.functools.lru_cache(maxsize, typed)
def _coconut_call_set_names(cls):
    if _coconut_sys.version_info < (3, 6):
        for k, v in _coconut.vars(cls).items():
            set_name = _coconut.getattr(v, "__set_name__", None)
            if set_name is not None:
                set_name(cls, k)
class override(_coconut_base_hashable):
    __slots__ = ("func",)
    def __init__(self, func):
        self.func = func
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self.func
        return _coconut.types.MethodType(self.func, obj)
    def __set_name__(self, obj, name):
        if not _coconut.hasattr(_coconut.super(obj, obj), name):
            raise _coconut.RuntimeError(obj.__name__ + "." + name + " marked with @override but not overriding anything")
    def __reduce__(self):
        return (self.__class__, (self.func,))
def reveal_type(obj):
    """Special function to get MyPy to print the type of the given expression.
    At runtime, reveal_type is the identity function."""
    return obj
def reveal_locals():
    """Special function to get MyPy to print the type of the current locals.
    At runtime, reveal_locals always returns None."""
    pass
def _coconut_handle_cls_kwargs(**kwargs):
    """Some code taken from six under the terms of its MIT license."""
    metaclass = kwargs.pop("metaclass", None)
    if kwargs and metaclass is None:
        raise _coconut.TypeError("unexpected keyword argument(s) in class definition: %r" % (kwargs,))
    def coconut_handle_cls_kwargs_wrapper(cls):
        if metaclass is None:
            return cls
        orig_vars = cls.__dict__.copy()
        slots = orig_vars.get("__slots__")
        if slots is not None:
            if _coconut.isinstance(slots, _coconut.str):
                slots = [slots]
            for slots_var in slots:
                orig_vars.pop(slots_var)
        orig_vars.pop("__dict__", None)
        orig_vars.pop("__weakref__", None)
        if _coconut.hasattr(cls, "__qualname__"):
            orig_vars["__qualname__"] = cls.__qualname__
        return metaclass(cls.__name__, cls.__bases__, orig_vars, **kwargs)
    return coconut_handle_cls_kwargs_wrapper
def _coconut_handle_cls_stargs(*args):
    temp_names = ["_coconut_base_cls_%s" % (i,) for i in _coconut.range(_coconut.len(args))]
    ns = _coconut.dict(_coconut.zip(temp_names, args))
    _coconut_exec("class _coconut_cls_stargs_base(" + ", ".join(temp_names) + "): pass", ns)
    return ns["_coconut_cls_stargs_base"]
def _coconut_dict_merge(*dicts, **kwargs):
    for_func = kwargs.pop("for_func", False)
    assert not kwargs, "error with internal Coconut function _coconut_dict_merge (you should report this at https://github.com/evhub/coconut/issues/new)"
    newdict = {}
    prevlen = 0
    for d in dicts:
        newdict.update(d)
        if for_func:
            if _coconut.len(newdict) != prevlen + _coconut.len(d):
                raise _coconut.TypeError("multiple values for the same keyword argument")
            prevlen = _coconut.len(newdict)
    return newdict
def ident(x, **kwargs):
    """The identity function. Generally equivalent to x -> x. Useful in point-free programming.
    Accepts one keyword-only argument, side_effect, which specifies a function to call on the argument before it is returned."""
    side_effect = kwargs.pop("side_effect", None)
    if kwargs:
        raise _coconut.TypeError("ident() got unexpected keyword arguments " + _coconut.repr(kwargs))
    if side_effect is not None:
        side_effect(x)
    return x
def call(_coconut_f, *args, **kwargs):
    """Function application operator function.

    Equivalent to:
        def call(f, /, *args, **kwargs) = f(*args, **kwargs).
    """
    return _coconut_f(*args, **kwargs)
def of(*args, **kwargs):
    """Deprecated built-in 'of' disabled by --strict compilation; use 'call' instead."""
    raise _coconut.NameError("deprecated built-in 'of' disabled by --strict compilation; use 'call' instead")
def safe_call(_coconut_f, *args, **kwargs):
    """safe_call is a version of call that catches any Exceptions and
    returns an Expected containing either the result or the error.

    Equivalent to:
        def safe_call(f, /, *args, **kwargs):
            try:
                return Expected(f(*args, **kwargs))
            except Exception as err:
                return Expected(error=err)
    """
    try:
        return _coconut_Expected(_coconut_f(*args, **kwargs))
    except _coconut.Exception as err:
        return _coconut_Expected(error=err)
class Expected(_coconut.collections.namedtuple("Expected", ("result", "error"))):
    """TODO"""
    _coconut_is_data = True
    __slots__ = ()
    def __add__(self, other): return _coconut.NotImplemented
    def __mul__(self, other): return _coconut.NotImplemented
    def __rmul__(self, other): return _coconut.NotImplemented
    __ne__ = _coconut.object.__ne__
    def __eq__(self, other):
        return self.__class__ is other.__class__ and _coconut.tuple.__eq__(self, other)
    def __hash__(self):
        return _coconut.tuple.__hash__(self) ^ hash(self.__class__)
    __match_args__ = ('result', 'error')
    def __new__(cls, result=None, error=None):
        if result is not None and error is not None:
            raise _coconut.ValueError("Expected cannot have both a result and an error")
        return _coconut.tuple.__new__(cls, (result, error))
    def __fmap__(self, func):
        return self if self.error is not None else self.__class__(func(self.result))
    def __bool__(self):
        return self.error is None
class flip(_coconut_base_hashable):
    """Given a function, return a new function with inverse argument order.
    If nargs is passed, only the first nargs arguments are reversed."""
    __slots__ = ("func", "nargs")
    def __init__(self, func, nargs=None):
        self.func = func
        self.nargs = nargs
    def __reduce__(self):
        return (self.__class__, (self.func, self.nargs))
    def __call__(self, *args, **kwargs):
        return self.func(*args[::-1], **kwargs) if self.nargs is None else self.func(*(args[self.nargs-1::-1] + args[self.nargs:]), **kwargs)
    def __repr__(self):
        return "flip(%r%s)" % (self.func, "" if self.nargs is None else ", " + _coconut.repr(self.nargs))
class const(_coconut_base_hashable):
    """Create a function that, whatever its arguments, just returns the given value."""
    __slots__ = ("value",)
    def __init__(self, value):
        self.value = value
    def __reduce__(self):
        return (self.__class__, (self.value,))
    def __call__(self, *args, **kwargs):
        return self.value
    def __repr__(self):
        return "const(%s)" % (_coconut.repr(self.value),)
class _coconut_lifted(_coconut_base_hashable):
    __slots__ = ("func", "func_args", "func_kwargs")
    def __init__(self, _coconut_func, *func_args, **func_kwargs):
        self.func = _coconut_func
        self.func_args = func_args
        self.func_kwargs = func_kwargs
    def __reduce__(self):
        return (self.__class__, (self.func,) + self.func_args, {"func_kwargs": self.func_kwargs})
    def __call__(self, *args, **kwargs):
        return self.func(*(g(*args, **kwargs) for g in self.func_args), **_coconut.dict((k, h(*args, **kwargs)) for k, h in self.func_kwargs.items()))
    def __repr__(self):
        return "lift(%r)(%s%s)" % (self.func, ", ".join(_coconut.repr(g) for g in self.func_args), ", ".join(k + "=" + _coconut.repr(h) for k, h in self.func_kwargs.items()))
class lift(_coconut_base_hashable):
    """Lifts a function up so that all of its arguments are functions.

    For a binary function f(x, y) and two unary functions g(z) and h(z), lift works as the S' combinator:
        lift(f)(g, h)(z) == f(g(z), h(z))

    In general, lift is requivalent to:
        def lift(f) = ((*func_args, **func_kwargs) -> (*args, **kwargs) ->
            f(*(g(*args, **kwargs) for g in func_args), **{k: h(*args, **kwargs) for k, h in func_kwargs.items()}))

    lift also supports a shortcut form such that lift(f, *func_args, **func_kwargs) is equivalent to lift(f)(*func_args, **func_kwargs).
    """
    __slots__ = ("func",)
    def __new__(cls, func, *func_args, **func_kwargs):
        self = _coconut.object.__new__(cls)
        self.func = func
        if func_args or func_kwargs:
            self = self(*func_args, **func_kwargs)
        return self
    def __reduce__(self):
        return (self.__class__, (self.func,))
    def __call__(self, *func_args, **func_kwargs):
        return _coconut_lifted(self.func, *func_args, **func_kwargs)
    def __repr__(self):
        return "lift(%r)" % (self.func,)
def all_equal(iterable):
    """For a given iterable, check whether all elements in that iterable are equal to each other.

    Supports numpy arrays. Assumes transitivity and 'x != y' being equivalent to 'not (x == y)'.
    """
    if iterable.__class__.__module__ in _coconut.numpy_modules:
        return not _coconut.len(iterable) or (iterable == iterable[0]).all()
    first_item = _coconut_sentinel
    for item in iterable:
        if first_item is _coconut_sentinel:
            first_item = item
        elif first_item != item:
            return False
    return True
def collectby(key_func, iterable, value_func=None, reduce_func=None):
    """Collect the items in iterable into a dictionary of lists keyed by key_func(item).

    if value_func is passed, collect value_func(item) into each list instead of item.

    If reduce_func is passed, instead of collecting the items into lists, reduce over
    the items of each key with reduce_func, effectively implementing a MapReduce operation.
    """
    collection = _coconut.collections.defaultdict(_coconut.list) if reduce_func is None else {}
    for item in iterable:
        key = key_func(item)
        if value_func is not None:
            item = value_func(item)
        if reduce_func is None:
            collection[key].append(item)
        else:
            old_item = collection.get(key, _coconut_sentinel)
            if old_item is not _coconut_sentinel:
                item = reduce_func(old_item, item)
            collection[key] = item
    return collection
def _namedtuple_of(**kwargs):
    """Construct an anonymous namedtuple of the given keyword arguments."""
    if _coconut_sys.version_info < (3, 6):
        raise _coconut.RuntimeError("_namedtuple_of is not available on Python < 3.6 (use anonymous namedtuple literals instead)")
    else:
        return _coconut_mk_anon_namedtuple(kwargs.keys(), of_kwargs=kwargs)
def _coconut_mk_anon_namedtuple(fields, types=None, of_kwargs=None):
    if types is None:
        NT = _coconut.collections.namedtuple("_namedtuple_of", fields)
    else:
        NT = _coconut.typing.NamedTuple("_namedtuple_of", [(f, t) for f, t in _coconut.zip(fields, types)])
    _coconut.copyreg.pickle(NT, lambda nt: (_coconut_mk_anon_namedtuple, (nt._fields, types, nt._asdict())))
    if of_kwargs is None:
        return NT
    return NT(**of_kwargs)
def _coconut_ndim(arr):
    if (arr.__class__.__module__ in _coconut.numpy_modules or _coconut.hasattr(arr.__class__, "__matconcat__")) and _coconut.hasattr(arr, "ndim"):
        return arr.ndim
    if not _coconut.isinstance(arr, _coconut.abc.Sequence):
        return 0
    if _coconut.len(arr) == 0:
        return 1
    arr_dim = 1
    inner_arr = arr[0]
    while _coconut.isinstance(inner_arr, _coconut.abc.Sequence):
        arr_dim += 1
        if _coconut.len(inner_arr) < 1:
            break
        inner_arr = inner_arr[0]
    return arr_dim
def _coconut_expand_arr(arr, new_dims):
    if (arr.__class__.__module__ in _coconut.numpy_modules or _coconut.hasattr(arr.__class__, "__matconcat__")) and _coconut.hasattr(arr, "reshape"):
        return arr.reshape((1,) * new_dims + arr.shape)
    for _ in _coconut.range(new_dims):
        arr = [arr]
    return arr
def _coconut_concatenate(arrs, axis):
    matconcat = None
    for a in arrs:
        if a.__class__.__module__ in _coconut.jax_numpy_modules:
            from jax.numpy import concatenate as matconcat
            break
        if a.__class__.__module__ in _coconut.numpy_modules:
            matconcat = _coconut.numpy.concatenate
            break
        if _coconut.hasattr(a.__class__, "__matconcat__"):
            matconcat = a.__class__.__matconcat__
            break
    if matconcat is not None:
        return matconcat(arrs, axis)
    if not axis:
        return _coconut.list(_coconut.itertools.chain.from_iterable(arrs))
    return [_coconut_concatenate(rows, axis - 1) for rows in _coconut.zip(*arrs)]
def _coconut_multi_dim_arr(arrs, dim):
    arr_dims = [_coconut_ndim(a) for a in arrs]
    arrs = [_coconut_expand_arr(a, dim - d) if d < dim else a for a, d in _coconut.zip(arrs, arr_dims)]
    arr_dims.append(dim)
    max_arr_dim = _coconut.max(arr_dims)
    return _coconut_concatenate(arrs, max_arr_dim - dim)
_coconut_self_match_types = (bool, bytearray, bytes, dict, float, frozenset, int, py_int, list, set, str, py_str, tuple)
_coconut_Expected, _coconut_MatchError, _coconut_count, _coconut_enumerate, _coconut_flatten, _coconut_filter, _coconut_ident, _coconut_map, _coconut_multiset, _coconut_range, _coconut_reiterable, _coconut_reversed, _coconut_starmap, _coconut_tee, _coconut_zip, TYPE_CHECKING, reduce, takewhile, dropwhile = Expected, MatchError, count, enumerate, flatten, filter, ident, map, multiset, range, reiterable, reversed, starmap, tee, zip, False, _coconut.functools.reduce, _coconut.itertools.takewhile, _coconut.itertools.dropwhile

# Compiled Coconut: -----------------------------------------------------------

import setuptools  # type: ignore

VERSION = "0.2.5"

setuptools.setup(name="coconut-prelude", version=VERSION, description="An implementation of Haskell's Prelude in Python using Coconut.", long_description="An implementation of Haskell's Prelude in Python using Coconut.", url="https://github.com/evhub/coconut-prelude", author="Evan Hubinger", author_email="evanjhub@gmail.com", packages=setuptools.find_packages(), install_requires=["coconut[mypy]",], extras_require={":python_version<'3.5'": ["typing",], "dev": ["pytest",]})
