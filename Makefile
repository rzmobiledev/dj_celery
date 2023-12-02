.DEFAULT_GOAL=help

.PHONY: help
help: # Show help for each of the Makefile recipes.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: export-all
export-all: remove-warning export-dev export-test # export all depedency requirements

remove-warning:
	poetry config warnings.export false

export-dev:
	poetry export --without-hashes --format=requirements.txt > installer/requirements.txt --without test

export-test:
	poetry export --without-hashes --format=requirements.txt > installer/test_requirements.txt --only test

run-local: #Run python manage.py runserver
	python manage.py runserver