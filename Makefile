.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: local-setup
local-setup: ## Sets up the local environment (e.g. install git hooks)
	scripts/local-setup.sh
	make install

.PHONY: install
install: ## Install the app packages
	 rm -rf poetry.lock
	 poetry install --no-root

.PHONY: check-typing
check-typing:  ## Run a static analyzer over the code to find issues
	poetry run mypy .

.PHONY: check-lint
check-lint: ## Checks the code style
	poetry run ruff check

.PHONY: lint
lint: ## Lints the code format
	poetry run ruff check --fix

.PHONY: check-format
check-format:  ## Check format python code
	poetry run ruff format --check

.PHONY: format
format:  ## Format python code
	poetry run ruff format

.PHONY: test-year
test-year: ## Run all the tests for a given year
	 PYTHONPATH=. poetry run pytest -n auto tests/$(year) -ra

.PHONY: test
test: ## Run all the tests
	 PYTHONPATH=. poetry run pytest -n auto tests -ra

.PHONY: watch
watch: ## Run all the tests in watch mode
	 PYTHONPATH=. poetry run ptw --runner "pytest -n auto tests -ra"

.PHONY: generate-inputs
generate-inputs: ## Scaffold new exercise, ex: make generate-inputs day=02
		scripts/generate_inputs.sh $(day)

.PHONY: generate-code
generate-code: ## Scaffold new exercise, ex: make generate-code day=02
		scripts/generate_code.sh $(day)

.PHONY: pre-commit
pre-commit: check-format check-typing test
