.PHONY: install
install: build
	pip install -e .

.PHONY: setup
setup:
	pip install -U setuptools pip pytest
	pip install -U "coconut-develop[watch,cPyparsing]"

.PHONY: build
build:
	coconut setup.coco --no-tco --strict
	coconut "prelude-source" prelude --no-tco --strict --jobs sys --mypy

.PHONY: upload
upload: clean install
	python3 setup.py sdist bdist_wheel
	pip3 install -U twine
	twine upload ./dist/*

.PHONY: test
test: install
	pytest --strict -s ./prelude/tests

.PHONY: clean
clean:
	rm -rf ./dist ./build
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete

.PHONY: wipe
wipe: clean
	rm -rf ./prelude
	find . -name '*.py' -delete

.PHONY: watch
watch: install
	coconut "prelude-source" prelude --watch --no-tco --strict
