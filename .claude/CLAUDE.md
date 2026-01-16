# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

coconut-prelude is an implementation of Haskell's Prelude standard library in Python using the Coconut functional programming language. It provides Haskell-style types (`Maybe`, `Either`, `Ordering`), operators, and functional programming utilities with full MyPy type-checking support.

**Important**: All source code is written in Coconut (`.coco` files) in the `prelude-source/` directory. The `prelude/` directory contains generated Python files - never edit these directly.

## Coconut

You should always try your best to use the most idiomatic Coconut rather than just writing Python. Refer regularly to [Coconut's documentation](https://raw.githubusercontent.com/evhub/coconut/refs/heads/master/DOCS.md) to understand all Coconut-specific features and actively look for useful ways to make use of them.

## Common Commands

```bash
make setup         # Install dev dependencies (coconut-develop, pytest)
make build         # Compile .coco files to Python with MyPy checking
make test          # Build, install, and run pytest
make watch         # Auto-recompile on source changes
make clean         # Remove all generated files
make docs          # Generate HTML documentation with pydoc
```

### Running Tests

```bash
make test          # Full test suite (builds first)
```

Tests are in `prelude-source/main_test.coco` and `prelude-source/util_test.coco`. They use `assert` statements and run via pytest on the compiled Python.

### Compilation

The build process compiles Coconut to Python 3.5+ compatible code:
```bash
coconut "prelude-source" prelude --strict --pure --target 3.5 --jobs sys --mypy
```

Flags:
- `--strict` - Enables strict mode
- `--pure` - Disallows all variable reassignments
- `--mypy` - Generates MyPy stub files for type checking

## Architecture

### Source Structure

```
prelude-source/          # Source code (Coconut .coco files)
├── __init__.coco        # Re-exports main module
├── main.coco            # Core implementation: Maybe, Either, Ordering, operators
├── main_test.coco       # Tests for main
├── typevars.coco        # TypeVar definitions (Ta, Tb, Tc, Td, Tco, Tcontra)
├── util.coco            # Utility functions
└── util_test.coco       # Tests for util

prelude/                 # Generated Python (do not edit)
```

### Core Components

**`main.coco`** - Primary implementation containing:
- Data types: `Bool`, `Maybe` (Nothing/Just), `Either` (Left/Right), `Ordering` (LT/EQ/GT)
- Haskell operators mapped to Python names (e.g., `apply` for `$`, `bind` for `>>=`)
- Type class operations: Functor, Applicative, Monad
- List operations: head, tail, take, drop, map, filter, etc.
- Decorators: `derivingOrd`, `derivingBoundedEnum`, `definesBind`, `definesReturn`

**`typevars.coco`** - Generic type parameters for type-safe functions

### Haskell to Python Name Mappings

Key operator translations (since Python reserves some names):
- `apply` = `($)`, `bind` = `(>>=)`, `dot` = `(.)`
- `not_`, `and_`, `or_`, `return_`, `break_` - underscore suffix for reserved words
- `at` = `(!!)`, `cons` = `(:)`, `chain` = `(++)`

## Development Workflow

1. Edit `.coco` files in `prelude-source/`
2. Run `make build` or `make watch` to compile
3. Run `make test` to validate
4. Generated `.py` files in `prelude/` are automatically updated
