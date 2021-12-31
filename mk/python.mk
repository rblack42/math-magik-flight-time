PYTHON_VERSION := $(wordlist 2,4,$(subst ., ,$(shell python3 --version 2>&1)))
PYMAJ := $(word 1,${PYTHON_VERSION})
PYMIN := $(word 2,${PYTHON_VERSION})
PYPAT := $(word 3,${PYTHON_VERSION})


.PHONY: run
run:    ## Run project application
	python3 -m $(PROJECT)

.PHONY: pyinit
pyinit:	## Create Python virtual environment
	test -d .direnv || \
	echo 'layout python3' > .envrc && \
		direnv allow
	pip install --upgrade pip

.PHONY: pyreqs
pyreqs: requirements.txt 	## Load Python requirements
	pip install -r requirements.txt

.PHONY: test
test: ## Run unit tests
	tox -v

.PHONY: changes
changes:	## create CHANGES file from git logs
	git log --oneline --pretty=format:"* %ad: %s" --date=short > CHANGES

.PHONY: deploy
deploy:	## deploy web pages to public server
	scripts/deploy.sh

.PHONY: type-check
type-check:	## Check types with mypy
	mypy sphinxcontrib

.PHONY: pyversion
pyversion:	## fetch current python3 version string
	@echo $(PYTHON_VERSION)

