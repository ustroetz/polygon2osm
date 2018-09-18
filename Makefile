setup-env:
	virtualenv -p python3 venv
	source venv/bin/activate

bootstrap:
	@pip install -r requirements.txt
