install:
	pip install -r requirements.txt

migrate:
	alembic upgrade head

run:
	python main.py

test:
	pytest -v

format:
	ruff format .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf .pytest_cache/ .mypy_cache/ .ruff_cache/