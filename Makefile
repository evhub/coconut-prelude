.PHONY: test
test: docs
	python -m pytest --strict-markers -s ./prelude

.PHONY: clean-install
clean-install: clean install

.PHONY: base-install
base-install:
	pip install --upgrade pytest
	pip install --upgrade --no-deps -e .

.PHONY: install
install: build base-install

.PHONY: install-univ
install-univ: build-univ base-install

.PHONY: build
build:
	coconut setup.coco --strict --target 3.7
	coconut "prelude-source" prelude --strict --target 3.7 --jobs sys --mypy

.PHONY: build-univ
build-univ:
	coconut setup.coco --strict
	coconut "prelude-source" prelude --strict --jobs sys

.PHONY: docs
docs: install
	pydoc -w prelude
	pydoc -w prelude.main
	pydoc -w prelude.util

.PHONY: setup
setup:
	pip install -U setuptools wheel pip
	pip install -U coconut-develop[watch,jobs,mypy]

.PHONY: package
package:
	python setup.py sdist bdist_wheel

.PHONY: upload
upload: clean install-univ package
	pip3 install -U twine
	twine upload ./dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build ./prelude
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	find . -name "*.py" -delete

.PHONY: watch
watch: install
	coconut "prelude-source" prelude --watch --strict --target 3.7 --mypy
