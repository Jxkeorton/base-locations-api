release: python manage.py makemigrations && python manage.py migrate
web: gunicorn base_locations_api.wsgi