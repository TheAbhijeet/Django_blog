install:
	pip install -r requirements.txt

test:
	python manage.py test

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run:
	python manage.py runserver
