install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

install-package:
	python3 -m pip install --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

test:
	poetry run pytest
