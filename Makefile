dev:
	python manage.py runserver
.PHONY: app
app:
	django-admin startapp $(name)