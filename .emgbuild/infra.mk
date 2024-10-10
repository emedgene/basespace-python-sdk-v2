# This file is a part of template-python. Manual changes will be overwritten.

EMGBUILD_VENV?=.venv
EMGBUILD_COV_DIR?=$(EMGBUILD_VENV)/coverage
EMGBUILD_POETRY_INSTALL?=default
EMGBUILD_RUFF_ENABLE?=1
EMGBUILD_FLAKE8_ENABLE?=0
EMGBUILD_TEST_VERBOSE?=0
EMGBUILD_PYTEST_ARGS?=
EMGBUILD_PYTHONPATH?=
EMGBUILD_EMG_ENV?=test
EMGBUILD_DOCKER_DEPS?=
EMGBUILD_DOCKER_DEPS_AMD64?=
EMGBUILD_HAS_DOCKER?=$(shell which docker >/dev/null 2>&1 && echo 1)
EMGBUILD_ECR_REGISTRY?=124607710305.dkr.ecr.us-east-1.amazonaws.com
# only for GHA
EMGBUILD_BUILD_RUNNER?=1
EMGBUILD_BUILD_PACKAGE?=0
EMGBUILD_DISABLE_COVERAGE?=1

unexport MAKEFLAGS += --no-builtin-rules --no-builtin-variables

# GNU make workaround.
# GNU make tries to avoid executing the shell [1], but forgets to pass the updated
# environment to the spawned process. To workaround this, force the "slow"
# codepath [2].
# [1]: https://git.savannah.gnu.org/cgit/make.git/tree/job.c?h=4.0&id=52191d9d613819a77a321ad6c3ab16e1bc73c381#n3456
# [2]: https://git.savannah.gnu.org/cgit/make.git/tree/job.c?h=4.0&id=52191d9d613819a77a321ad6c3ab16e1bc73c381#n2987
SHELL := env sh

.PHONY: help
help:
	@echo "Possible targets:"
	@$(MAKE) -npq .DEFAULT 2>/dev/null | sed -n '1,/^# * Files/d;/^# * Not a target/,/^$$/d; /^[#[:space:].]/d; /^[._]/d; s/^\(.*\):.*/  \1/p' |sort


.PHONY: init reinit init-precommit
init: init-precommit _venv_activate
	case "$(EMGBUILD_POETRY_INSTALL)" in \
		main)    poetry install --no-root --only=main ;; \
		noroot)  poetry install --no-root ;; \
		default) poetry install ;; \
		*) echo "Bad value for EMGBUILD_POETRY_INSTALL: $(EMGBUILD_POETRY_INSTALL)"; exit 1 ;; \
    esac
reinit:
	[ ! -d "$(EMGBUILD_VENV)" ] || rm -rf "$(EMGBUILD_VENV)"
	$(MAKE) init
init-precommit:
	if ! which pre-commit && which brew; then \
		echo "WARN pre-commit unavailable, installing using brew" >&2; \
		brew install pre-commit; \
	fi
	if which pre-commit; then \
		 pre-commit install && pre-commit run; \
	elif [ -f /.dockerenv ]; then \
		: "no pre-commit in docker"; \
	else \
		echo "WARN Please install pre-commit" >&2; \
	fi

.PHONY: format format-check lint lint-fix check fix
ifeq ($(EMGBUILD_RUFF_ENABLE),1)
format: _venv_activate
	ruff format
format-check: _venv_activate
	ruff format --check
lint: _venv_activate
	ruff check
lint-fix: _venv_activate
	ruff check --fix
check: format-check lint
fix: format lint-fix
else ifeq ($(EMGBUILD_FLAKE8_ENABLE),1)
lint: _venv_activate
	flake8 "--exclude=$(EMGBUILD_VENV)"
check: lint
else
format format-check lint lint-fix check fix:
	@echo "WARNING ruff is disabled by EMGBUILD_RUFF_ENABLE=$(EMGBUILD_RUFF_ENABLE)" >&2
endif

# pytest --basetemp is a workaround for too long tmpdir under macos
.PHONY: test
test: _venv_activate
	set -exu; \
	$(if $(and $(EMGBUILD_HAS_DOCKER),$(EMGBUILD_DOCKER_DEPS)$(EMGBUILD_DOCKER_DEPS_AMD64)),$(MAKE) docker-pull-deps;) \
	[ -n "$${EMG_ENV:-}" ] || export EMG_ENV="$(EMGBUILD_EMG_ENV)"; \
	[ -z "$(EMGBUILD_PYTHONPATH)" ] || export PYTHONPATH="$(EMGBUILD_PYTHONPATH)$${PYTHONPATH:+:}$${PYTHONPATH:-}"; \
	pytest \
		$(if $(filter $(EMGBUILD_TEST_VERBOSE),1),--capture=no) \
		--basetemp=/tmp/pytest \
		--cov \
		--cov-report=term-missing \
		--cov-report=xml:$(EMGBUILD_COV_DIR)/coverage-report.xml \
		--junitxml=$(EMGBUILD_COV_DIR)/pytest-junitxml.xml \
		$(EMGBUILD_PYTEST_ARGS)

.PHONY: _venv_activate
_venv_activate: $(EMGBUILD_VENV)
	$(eval export PATH=$(shell . $(EMGBUILD_VENV)/bin/activate && echo "$$PATH"))
	$(info using venv: $(EMGBUILD_VENV))
	which python

$(EMGBUILD_VENV):
	python -m venv "$@"

.PHONY: clean
clean:
	rm -rf "$(EMGBUILD_VENV)"
	rm -rf .pytest_cache
	rm -rf .ruff_cache

.PHONY: docker-login
docker-login:
	set -exu; \
	docker login "$(EMGBUILD_ECR_REGISTRY)" </dev/null && exit || true; \
	if ! aws ecr get-authorization-token | grep -Fwq "$(EMGBUILD_ECR_REGISTRY)"; then \
		echo ; \
		echo "WARN No access to ECR $(EMGBUILD_ECR_REGISTRY)" >&2; \
		echo "Login using aws cli and setup your environment" >&2; \
		exit 1; \
	fi; \
	region=$$(echo "$(EMGBUILD_ECR_REGISTRY)" | awk -F. '{print $$(NF-2)}'); \
	aws ecr get-login-password --region=$${region} | docker login --username AWS --password-stdin "$(EMGBUILD_ECR_REGISTRY)"

.PHONY: docker-pull-deps
docker-pull-deps:
	set -exu; \
	logged_in=""; \
	for image in $(EMGBUILD_DOCKER_DEPS); do \
		docker image inspect "$$image" >/dev/null 2>&1 && continue; \
		[ -n "$$logged_in" ] || { $(MAKE) docker-login; logged_in=1; }; \
		docker pull "$(EMGBUILD_ECR_REGISTRY)/$$image"; \
		docker tag "$(EMGBUILD_ECR_REGISTRY)/$$image" "$${image##*/}"; \
	done; \
	for image in $(EMGBUILD_DOCKER_DEPS_AMD64); do \
		docker image inspect "$$image" >/dev/null 2>&1 && continue; \
		[ -n "$$logged_in" ] || { $(MAKE) docker-login; logged_in=1; }; \
		docker pull --platform=linux/amd64 "$(EMGBUILD_ECR_REGISTRY)/$$image"; \
		docker tag "$(EMGBUILD_ECR_REGISTRY)/$$image" "$${image##*/}"; \
	done

.PHONY: .emgbuild-config
.emgbuild-config:
	echo "EMGBUILD_BUILD_RUNNER=$(EMGBUILD_BUILD_RUNNER)"
	echo "EMGBUILD_BUILD_PACKAGE=$(EMGBUILD_BUILD_PACKAGE)"
	echo "EMGBUILD_DISABLE_COVERAGE=$(EMGBUILD_DISABLE_COVERAGE)"
