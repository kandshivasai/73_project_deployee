python manage.py collectstatic --noinput 
python manage.py migrate --noinput 
gunicorn student_form.wsgi:application --bind 0.0.0.0:$PORT