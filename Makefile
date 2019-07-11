.PHONY: test
test: install
	pytest --strict -s ./prelude

.PHONY: clean-install
clean-install: clean install

.PHONY: install
install: build
	pip install -e .

.PHONY: build
build:
	coconut setup.coco --strict --target 3.6
	coconut "prelude-source" prelude --strict --target 3.6 --jobs sys --mypy

.PHONY: build-univ
build-univ:
	coconut setup.coco --strict
	coconut "prelude-source" prelude --strict --jobs sys

.PHONY: setup
setup:
	pip install -U setuptools pip pytest
	pip install -U "coconut-develop[watch,cPyparsing,jobs,mypy]"

.PHONY: upload
upload: clean build-univ
	python3 setup.py sdist bdist_wheel
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
