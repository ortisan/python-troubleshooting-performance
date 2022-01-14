
Criacao do ambiente

```sh
python3 -m venv  ./.venv
pip install -r requirements.txt
docker-compose up --build
uvicorn main:app --reload
```
Run sql script

```sh
mysql --host=localhost --user=root --password=123456 mydb
CREATE TABLE `tick` (`id` INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY, `epoch_timestamp` BIGINT NOT NULL, `symbol` VARCHAR(50) NOT NULL, `value` BIGINT NOT NULL) []
INSERT INTO tick (`epoch_timestamp`, `symbol`, `value`) VALUES (123456, 'ETH', 1000000);
```

Run performance tests

```sql
k6 run k6-post-script.js
```

TODO documentar o django
```sh
django-admin startproject app
cd app
django-admin startapp ticker
```sh

Create models

python manage.py makemigrations
python manage.py migrate

GUNICORN_CMD_ARGS="--bind=0.0.0.0:8000 --workers=3 --reload --chdir=ticker/" gunicorn tiker.wsgi




