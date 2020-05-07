
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

.PHONY: help
help:
	@echo "clean"
	@echo "install-deps "
	@echo "unit_tests"
	@echo "integration_tests"
	@echo "Testing"
	@echo 
	@echo "test-info-<test_filter>"
	@echo "test-<test_filter>"
	@echo "dump_distance_matrix"
	@echo 
	@echo "dump_path-%"
	@echo "simple_query"
	@echo "package"
	@echo "publish-test"
	@echo "publish-prod"
	@echo "start_server"
	@echo "start_uwsgi"
	@echo "start_client"


.PHONY: universal-win
universal-win:
	@echo Windows version of Universal Rule

.PHONY: universal
universal:
	@echo UNIVERSAL RULE
	@echo Detected Architecture: ${ARCH}

.PHONY: clean
clean:
	find . -name "__pycache__" | xargs rm -rf

.PHONY: install-deps
install-deps:
	${PYTHON} -m pip install --user -r requirements.txt

# Log Levels and what they print
# DEBUG: INFO, ERROR, DEBUG
# INFO: INFO, ERROR
# ERROR: ERROR
###############################################################################
# Testing Section

# -v, --verbose         increase verbosity.
# -q, --quiet           decrease verbosity.
#   --show-capture={no,stdout,stderr,log,all}
#                       Controls how captured stdout/stderr/log is shown on
#                       failed tests. Default is 'all'.
#  -k EXPRESSION         only run tests which match the given substring
#                        expression. An expression is a python evaluatable
#                        expression where all names are substring-matched
#                        against test names and their parent classes. Example:
#                        -k 'test_method or test_other' matches all test
#                        functions and classes whose name contains
#                        'test_method' or 'test_other', while -k 'not
#                        test_method' matches those that don't contain
#                        'test_method' in their names. -k 'not test_method and
#                        not test_other' will eliminate the matches.
#                        Additionally keywords are matched to classes and
#                        functions containing extra names in their
#                        'extra_keyword_matches' set, as well as functions

# --capture=method      per-test capturing method: one of fd|sys|no.
# -s                    shortcut for --capture=no.
# -r chars              show extra test summary info as specified by chars
#                       (f)ailed, (E)error, (s)skipped, (x)failed, (X)passed,
#                       (p)passed, (P)passed with output, (a)all except pP.
#                       Warnings are displayed at all times except when
#                       --disable-warnings is set

.PHONY: unit_tests
unit_tests:
	@echo "Running unit tests"
	${PYTHON} -m pytest --disable-pytest-warnings --color=yes -r ap  ./tests/unit/

.PHONY: integration_tests
integration_tests:
	@echo "Running Integration Tests"
	${PYTHON} -m pytest --disable-pytest-warnings --color=yes -r ap ./tests/integration/

# make test-info-TravelCostsTests
# make test-info-"TravelCostsTests and test_smoke"
.PHONY: test-info-%
test-info-%:
	@echo "Running tests with filter $* and info verbosity"
	${PYTHON} -m pytest --disable-pytest-warnings -s -r p -k "$*" tests

# make test-TravelCostsTests
# make test-"TravelCostsTests and test_smoke"
.PHONY: test-%
test-%:
	@echo "Running tests with filter $*"
	#${PYTHON} -m pytest --color=yes -r ap -k TravelCosts -k "$*" tests
	${PYTHON} -m pytest --disable-pytest-warnings -r p -k "$*" tests

###############################################################################
export CITIES_FILE:=tests/unit/cities_list.txt
.PHONY: update_distance_matrix
update_distance_matrix: export OUTPUT_FILE:=tests/unit/MockDistance.py
update_distance_matrix:
	@echo "Dump Distance Matrix ${CITIES_FILE}"
	${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE} --output ${OUTPUT_FILE}

.PHONY: dump_distance_matrix
dump_distance_matrix:
	@echo "Dump Distance Matrix Verbose"
	${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE} --verbose

.PHONY: dump_distance_matrix-info
dump_distance_matrix-info:
	@echo "Dump Distance Matrix Verbose"
	${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE}

.PHONY: dump_path-%
dump_path-%:
	@echo "Dump path details for: $*"
	${PYTHON} -m OnTheRoad --dump-path $*

.PHONY: simple_query
simple_query:
	@echo "Executing a simple query defined in ./tests/unit/small_tests.txt"
	${PYTHON} -m OnTheRoad --calc-path ./tests/uname/small_tests.txt
###############################################################################

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


###############################################################################
# Running in WSL with Ubuntu 18
# Create Virtualenv
# $ python3.8 -m venv myenv
# $ source myenv/bin/activate
# $ pip install -r requirements.txt
# $ pip list
	
# Run
# uwsgi --http-socket :5000 --plugin python3 --module wsgi:app
# uwsgi --http-socket :5000 --plugin python38 --module wsgi:app 
# uwsgi --http-socket :5000 --py-autoreload --plugin python38 --module wsgi:app 

# Quick test
# curl http://127.0.0.1:5000/version

# Stop
# pkill -9 uwsgi
#
# PRODUCTION USE
#
