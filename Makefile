.PHONY: env-create run

env-create:
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.py

run:
	fastapi run app/main.py --host 0.0.0.0 --port 8500 --workers 1