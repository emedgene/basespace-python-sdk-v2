EMGBUILD_RUFF_ENABLE=0
EMGBUILD_BUILD_RUNNER=0
EMGBUILD_BUILD_PACKAGE=1
#EMGBUILD_DISABLE_COVERAGE=1

build:
	$(if $(PEP440_VERSION),poetry version "$(PEP440_VERSION)",)
	poetry build
