<!-- This file is a part of template-python. Manual changes will be overwritten. -->

# How to develop

For easier local development you can use the provided makefile. To get a list of
available make commands just run `make` or `make help`.

## Start local development

```bash
git clone git@git.illumina.com:Emedgene/$PROJECT
cd $PROJECT
make init
make test
```

The project-local virtual env is created at `$PROJECT/.venv/`.

## Before commit & push

It's recommended to run formatter, linter and unit tests before pushing.

```bash
make format
make lint
make test
# can combine
make format lint test
```
