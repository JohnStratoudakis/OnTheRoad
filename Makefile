#PYTHON?=python.exe
PYTHON?=python3.7

.PHONY: help
help:
	echo "make test-filter filter=John"

.PHONY: clean
clean:
	find . -name "__pycache__" | xargs rm -rf

.PHONY: freeze
freeze:
	${PYTHON} -m pip freeze > requirements.txt

.PHONY: install-deps
install-deps:
	${PYTHON} -m pip install -r requirements.txt

.PHONY: test
test:
	@echo "Running tests"
	${PYTHON} -m pytest  -v ./tests/*
	#${PYTHON} -m pytest --show-capture all -v ./test/*

.PHONY: test-filter
test-filter:
	echo "Running tests with filter ${filter}"
	${PYTHON} -m pytest -v ./tests/* -k ${filter}

.PHONY: package
package:
	${PYTHON} setup.py sdist bdist_wheel

.PHONY: publish
publish:
	 ${PYTHON} -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

