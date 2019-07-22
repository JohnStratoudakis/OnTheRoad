PYTHON?=python3.7

.PHONY: freeze
freeze:
	${PYTHON} -m pip freeze > requirements.txt

.PHONY: install-deps
install-deps:
	${PYTHON} -m pip install -r requirements.txt

.PHONY: test
test:
	echo "Running tests"
	${PYTHON} -m pytest -v ./test/*

