# Django implementation of DMS backend

Setup
-----

- Create virtual environment with:

`virtualenv -p python3.6 --no-site-packages --prompt="(dms.backend)" venv`

- Install requirements:

`pip install -r requirements/base.txt`

- Create user for local database:

`createuser -U postgres -d dms.backend`

- Using psql change user password:

`ALTER ROLE "dms.backend" PASSWORD 'top_secret';`

- Create local database:

`createdb -U dms.backend -E UTF-8 -T template0 dms.backend`

- Add `settings.json` file in project root dir with such contents:

```
{
  "APP_URL": "http://localhost:8000",
  "PORT": 8000,
  "DEBUG": true,
  "PRODUCTION": false,
  "DATABASE": {
    "NAME": "dms.backend",
    "PASSWORD": "top_secret",
    "USER": "dms.backend"
  },
  "SECRET_KEY": "any_random_value"
}
```

- Activate virtualenv:

`source venv/bin/activate`

- Add `DJANGO_SETTINGS_MODULE` environment variable (for Windows users - add it to PATH):

`export DJANGO_SETTINGS_MODULE='conf.settings'`

- Run migrations:

`python manage.py migrate`

- Run server:

`python manage.py runserver`

- Try to open `http://localhost:8000` URL in your browser
