
ifeq ($(OS),Windows_NT)
    ARCH=win
	PYTHON?=python.exe
else
	PYTHON?=python3.7
	UNAME_S := $(shell uname -s)
	UNAME_M := $(shell uname -m)
    ifeq ($(UNAME_S),Linux)
		ifeq ($(UNAME_M),armv7l)
			ARCH=rpi
		else
			ARCH=linux
		endif
    endif
    ifeq ($(UNAME_S),Darwin)
    	ARCH=osx
    endif
endif

.PHONY: universal-win
universal-win:
	@echo Windows version of Universal Rule

.PHONY: universal
universal:
	@echo UNIVERSAL RULE
	@echo Detected Architecture: ${ARCH}

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
	${PYTHON} -m pip install --user -r requirements.txt

.PHONY: utest
utest:
	@echo "Running tests"
	${PYTHON} -m pytest --show-capture all -s -r p -v ./tests/unit/

.PHONY: itest
itest:
	@echo "Running Integration Tests"
	${PYTHON} -m pytest --show-capture all -s -v ./tests/integration/

.PHONY: test-%
test-%:
	echo Running tests with filter $*
	${PYTHON} -m pytest -v --disable-pytest-warnings -s -r p -k $* tests

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
	${PYTHON} flaskapp.py

.PHONY: start_uwsgi
start_uwsgi:
	uwsgi --socket 0.0.0.0:5000 --protocol=http -w flaskapp:app

.PHONY: start_client
start_client:
	cd ontheroad_ui && yarn start

