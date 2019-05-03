

.PHONY: test
test:
	echo "Running tests"
	python3 -m unittest discover --pattern=*Tests.py

