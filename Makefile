help:
	@echo "clean-pyc - remove Python file artifacts"
	@echo "isort-check - check code by iSort"
	@echo "isort - iSorting all code"
	@echo "deploy - deploy on production host"
	@echo "lint - run flake8 linter"
	@echo "install_requirements - install project requirements"

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

isort-check:
	isort -rc -c app
	isort -rc -c tests

isort:
	isort -rc app
	isort -rc tests

deploy:
	fab -n 5 deploy

lint:
	flake8 app tests

install_requirements:
	pip install -U pip
	pip install --no-cache-dir -r requirements/base.txt