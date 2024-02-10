
run:
	poetry run python main.py

test:
	poetry run pytest .

format:
	poetry run pre-commit run --all-files
