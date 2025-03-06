
SHELL=/bin/bash
CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

.PHONY: test
test:
	pytest --cov=sparrow_patterns sparrow_patterns/

.PHONY: branchify
branchify:
	if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then \
		if [ "$(shell git rev-parse --abbrev-ref HEAD)" != "main" ]; then \
			# Create a portable sed command that works on both Linux and macOS \
			if [ "$(shell uname)" = "Darwin" ]; then \
				sed -i '' 's/version = "\([0-9]*\.[0-9]*\.[0-9]*\)"/version = "\1.dev$(shell date +%s)"/g' pyproject.toml; \
			else \
				sed -i 's/version = "\([0-9]*\.[0-9]*\.[0-9]*\)"/version = "\1.dev$(shell date +%s)"/g' pyproject.toml; \
			fi \
		fi \
	fi

.PHONY: publish
publish: branchify
	pip install twine build
	rm -rf dist
	python -m build
	twine upload dist/* --username $(PYPI_USERNAME) --password $(PYPI_PASSWORD)
	git checkout -- pyproject.toml
	rm -rf dist

.PHONY: freeze
freeze:
	uv pip compile -q -o requirements.txt pyproject.toml
	echo "-e ." >> requirements.txt
	uv pip compile -q --extra dev -o requirements-dev.txt pyproject.toml
	echo "-e ." >> requirements-dev.txt

.PHONY: init
init:
	conda create -y -n sparrow-patterns python=3.12 pip
	conda init
	$(CONDA_ACTIVATE) sparrow-patterns ; pip install -U pip uv ; make freeze ; pip install -r requirements-dev.txt
	git init
	git add .
	git commit -m "first commit :rocket:"