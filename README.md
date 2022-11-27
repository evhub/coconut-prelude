# coconut-prelude

An implementation of [Haskell's Prelude](https://hackage.haskell.org/package/base-4.10.1.0/docs/Prelude.html) in Python 3.8+ using [Coconut](http://coconut-lang.org).

## Installation

```
pip install coconut-prelude
```

## Usage

To use `coconut-prelude`, just
```python
from prelude import *
```
which should make all the standard Haskell built-ins available to you. The only exceptions are Haskell operators and Haskell built-ins that use reserved names in Python, which have been given the following names:
```haskell
fmapConst = (<$)
ap = (<*>)
seqAr = (*>)
seqAl = (<*)
bind = (>>>=)
seqM = (>>>)
bindFrom = (=<<<)
dot = (.)
apply = ($)
cbv = ($!)
cons = (:)
chain = (++)
at = (!!)
not_ = not
return_ = return
and_ = and
or_ = or
break_ = break

import Data.Ratio
over = (%)
```

Furthermore, the following special functions are made available to mimic certain Haskell syntaxes, with information on each accessible via `help(func)`:
```python
of
do
asIO
unIO
derivingOrd
derivingBoundedEnum
definesBind
definesReturn
```

Additionally, it is highly recommended, though fully optional, that `coconut-prelude` be used with [MyPy](https://mypy.readthedocs.io/en/stable/) to enable static type-checking and [Coconut](http://coconut-lang.org) to enable easier usage of functional programming constructs, such as those used to define the prelude in the first place.

Even if not using Coconut, however, to get MyPy working with `coconut-prelude` will require you to follow the instructions [here](https://coconut.readthedocs.io/en/master/DOCS.html#mypy-integration) to generate the necessary stub files and add them to your `MYPYPATH`.

If you are using Coconut, you can also get access to actual custom Haskell operators with the code:
```python
from prelude import operator $$  # apply ($)
from prelude import operator %%  # over (%)
from prelude import operator <$  # fmapConst
from prelude import operator <*>  # ap
from prelude import operator *>  # seqAr
from prelude import operator <*  # seqAl
from prelude import operator >>>=  # bind (>>=)
from prelude import operator >>>  # seqM (>>)
from prelude import operator =<<<  # bindFrom (=<<)
from prelude import operator ++  # chain
from prelude import operator !!  # at
```

For additional documentation, either [read the source code](https://github.com/evhub/coconut-prelude/blob/master/prelude-source/main.coco) or view the [auto-generated documentation](https://refined-github-html-preview.kidonng.workers.dev/evhub/coconut-prelude/raw/master/prelude.html).
