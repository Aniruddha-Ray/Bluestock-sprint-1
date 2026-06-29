setup:
	pip install -r requirements.txt

run:
	python src/etl/loader.py

test:
	pytest tests/

format:
	black src tests

lint:
	flake8 src

clean:
	rm -rf __pycache__