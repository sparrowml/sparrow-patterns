#* Variables
SHELL := /usr/bin/env bash
PYTHON := python
PYTHONPATH := `pwd`

#* Docker variables
IMAGE := {{ project_name }}
VERSION := latest

.PHONY: test
test:
	PYTHONPATH=$(PYTHONPATH) poetry run pytest -c pyproject.toml --cov={{ source_directory }} {{ source_directory }}/

#* Formatters/Linters
.PHONY: codestyle
codestyle:
	poetry run pyupgrade --exit-zero-even-if-changed --py39-plus **/*.py
	poetry run isort --settings-path pyproject.toml ./
	poetry run black --config pyproject.toml ./

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only ./
	poetry run black --diff --check ./
	poetry run pylint {{ source_directory }}

.PHONY: mypy
mypy:
	poetry run mypy --config-file pyproject.toml {{ source_directory }}

.PHONY: check-safety
check-safety:
	poetry check
	poetry run safety check --full-report
	poetry run bandit -ll --recursive {{ source_directory }}

#* Docker
# Example: make docker-build VERSION=latest
# Example: make docker-build IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile --no-cache

# Example: make docker-remove VERSION=latest
# Example: make docker-remove IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

.PHONY: branchify
branchify:
ifneq ($(shell git rev-parse --abbrev-ref HEAD),main)
	poetry version $(shell poetry version -s).dev$(shell date +%s)
endif

.PHONY: publish
publish: branchify
	poetry publish --build --repository sparrow
