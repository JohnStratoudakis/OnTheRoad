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

.PHONY: utest
utest:
	@echo "Running tests"
	${PYTHON} -m pytest --show-capture all -s -v ./tests/unit/

.PHONY: itest
itest:
	@echo "Running Integration Tests"
	${PYTHON} -m pytest --show-capture all -s -v ./tests/integration/

.PHONY: test-filter
test-filter:
	echo "Running tests with filter ${filter}"
	${PYTHON} -m pytest -v ./tests/* -k ${filter}

.PHONY: package
package:
	${PYTHON} setup.py sdist bdist_wheel

.PHONY: publish-test
publish-test:
	 ${PYTHON} -m twine upload --verbose --config-file .pypirc-bot -r testpypi dist/*

.PHONY: publish-prod
publish-prod:
	 ${PYTHON} -m twine upload --verbose --config-file .pypirc-bot -r pypi dist/*

# Test via make itest
.PHONY: start_server
start_server:
	${PYTHON} app.py
