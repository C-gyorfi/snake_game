setup:
	pipenv install --dev

shell:
	pipenv shell  

tests:
	pipenv run pytest --cov=src 

lint: lint-test lint-prod

lint-prod:
	pipenv run pylint ./src

lint-test:
	pipenv run pylint ./test

auto-lint:
	pipenv run autopep8 --in-place --recursive .

auto-lint-aggressive:
	pipenv run autopep8 --in-place --aggressive --aggressive --recursive .

run:
	pipenv run python ./game.py
