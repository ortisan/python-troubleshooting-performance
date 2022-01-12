
pip install -r requirements.txt

django-admin startproject app
cd app
django-admin startapp ticker

Create models

python manage.py makemigrations
python manage.py migrate

GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000 --workers=3 --reload --chdir=ticker/" gunicorn tiker.wsgi


k6 run k6-post-script.js
