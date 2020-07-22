PYTHON=python3.8

# Backup MySql Databases gist
# https://gist.github.com/spalladino/6d981f7b33f6e0afe6bb

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


.PHONY: clean
clean:
	find . -name "__pycache__" | xargs rm -rf
	rm -rf ./OnTheRoad/venv

#.PHONY: install-deps
#install-deps:
#	${PYTHON} -m pip install --user -r requirements.txt
#
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

OnTheRoad/venv: OnTheRoad/venv/bin/activate

#.PHONY: OnTheRoad/venv/bin/activate
OnTheRoad/venv/bin/activate: requirements.txt
	test -d OnTheRoad/venv || ${PYTHON} -m venv OnTheRoad/venv
	. ./OnTheRoad/venv/bin/activate; pip install -Ur requirements.txt
	touch OnTheRoad/venv/bin/activate

.PHONY: start_flask
start_flask: OnTheRoad/venv
	. ./OnTheRoad/venv/bin/activate; FLASK_ENV=development ${PYTHON} OnTheRoad/main.py

.PHONY: unit_tests
unit_tests: OnTheRoad/venv
	@echo "Running unit tests"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings --color=yes -r ap  ./tests/unit/

.PHONY: integration_tests
integration_tests: OnTheRoad/venv
	@echo "Running Integration Tests"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings --color=yes -r ap ./tests/integration/

# make test-info-TravelCostsTests
# make test-info-"TravelCostsTests and test_smoke"
.PHONY: test-info-%
test-info-%: OnTheRoad/venv
	@echo "Running tests with filter $* and info verbosity"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings -s -r p -k "$*" tests

# make test-TravelCostsTests
# make test-"TravelCostsTests and test_smoke"
.PHONY: test-%
test-%: OnTheRoad/venv
	@echo "Running tests with filter $*"
	#${PYTHON} -m pytest --color=yes -r ap -k TravelCosts -k "$*" tests
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m pytest --disable-pytest-warnings -r p -k "$*" tests

###############################################################################
export CITIES_FILE:=tests/unit/cities_list.txt
.PHONY: update_distance_matrix
update_distance_matrix: export OUTPUT_FILE:=tests/unit/MockDistance.py
update_distance_matrix: OnTheRoad/venv
	@echo "Dump Distance Matrix ${CITIES_FILE}"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE} --output ${OUTPUT_FILE}

.PHONY: dump_distance_matrix
dump_distance_matrix: OnTheRoad/venv
	@echo "Dump Distance Matrix Verbose"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE}

.PHONY: dump_distance_matrix-info
dump_distance_matrix-info: OnTheRoad/venv
	@echo "Dump Distance Matrix Verbose"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m OnTheRoad --dump-matrix --cities-file ${CITIES_FILE} --verbose

.PHONY: dump_path-%
dump_path-%: OnTheRoad/venv
	@echo "Dump path details for: $*"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m OnTheRoad --dump-path $*

.PHONY: simple_query
simple_query: OnTheRoad/venv
	@echo "Executing a simple query defined in ./tests/unit/small_tests.txt"
	. ./OnTheRoad/venv/bin/activate; ${PYTHON} -m OnTheRoad --calc-path ./tests/uname/small_tests.txt
###############################################################################
#
#.PHONY: package
#package:
#	${PYTHON} setup.py sdist bdist_wheel
#
#.PHONY: publish-test
#publish-test:
#	 ${PYTHON} -m twine upload --verbose --config-file .pypirc-bot -r testpypi dist/*
#
#.PHONY: publish-prod
#publish-prod:
#	 ${PYTHON} -m twine upload --verbose --config-file .pypirc-bot -r pypi dist/*
#
###############################################################################
# Running in WSL with Ubuntu 18

.PHONY: start_client
start_client:
	cd ontheroad_ui && yarn start

.PHONY: test-api
test-api:
	curl https://app.johnstratoudakis.com/OnTheRoad/version
