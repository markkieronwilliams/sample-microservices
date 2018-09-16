cd /app
python3.6 manage.py makemigrations
python3.6 manage.py makemigrations attemptapp
python3.6 manage.py migrate
python3.6 manage.py runserver 0.0.0.0:8000