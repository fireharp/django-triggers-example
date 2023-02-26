
## Initial Setup
```shell
poetry run python manage.py migrate

poetry run python manage.py createsuperuser
```

## Development
```shell
poetry run python manage.py runserver
```

## Test
```shell
poetry run pytest --cov tests/
```
