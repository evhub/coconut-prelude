.PHONY: test
test: install
	python -m pytest --strict -s ./prelude

.PHONY: clean-install
clean-install: clean install

.PHONY: install
install: build
	pip install -Ue .[dev]

.PHONY: install-univ
install-univ: build-univ
	pip install -Ue .[dev]

.PHONY: build
build:
	coconut setup.coco --strict --target 3.6
	coconut "prelude-source" prelude --strict --target 3.6 --jobs sys --mypy

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
	pip install -U setuptools pip
	pip install -U coconut-develop[watch,jobs,mypy]

.PHONY: upload
upload: clean install-univ
	python setup.py sdist bdist_wheel
	pip3 install -U twine
	twine upload ./dist/*

.PHONY: clean
clean:
	rm -rf ./dist ./build ./prelude
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.py' -delete

.PHONY: watch
watch: install
	coconut "prelude-source" prelude --watch --strict --target 3.6 --mypy
