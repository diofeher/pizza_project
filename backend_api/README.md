Pizza API
----------
1) Install the dependencies:

```
    pip3 install -r pip_requirements.txt
```

2) Create a database called `pizza_api` in your Postgres instance.

3) Setup the project:
```
    POSTGRES_USER=<your_postgres_username>
    POSTGRES_PWD=<your_postgres_password>
    python manage.py migrate
```

You can see a lot of endpoint interactions on `tests.sh` file.
