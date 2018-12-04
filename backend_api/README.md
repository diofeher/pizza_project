Pizza API
----------
To install the dependencies:

```
    pip3 install -r pip_requirements.txt
```

To setup the project:
```
    POSTGRES_USER=<your_postgres_username>
    POSTGRES_PWD=<your_postgres_password>
    python manage.py migrate
    python manage.py createsuperuser
```

Create with admin/admin123 so it will be easier to run the tests on the API. There are a lot of endpoint interactions on `tests.sh` file.
