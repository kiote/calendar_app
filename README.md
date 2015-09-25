![](https://api.travis-ci.org/kiote/calendar_app.svg)

Django version of calendar app

#### Requirements

This project had been tested under Python 2.7 and Django 1.8.4.

#### To run tests locally:

- ```export LOCAL_DEV=1```
- ```export PYTHONPATH=.```
- ```python manage.py test```

#### How to embed this app to external Django application

As it's not more than a standard Django app under the hood, you probably need to copy all models to your Django app: ```added_event```, ```event_template```, ```google_auth```, ```guser```.

After that you need to activate that models in your ```settings.py```:

```python
INSTALLED_APPS = (
    ...
    'google_auth',
    'event_template',
    'guser',
    'added_event',
)
```

Finally, you need to run migrations to have all tables in place:

```python manage.py migrate```

Also you'd probably need some libraries installed from ```requirements.txt```. You can simply copy all that file to your own ```requirements.txt``` and manually handle comflicts (if any). Then run ```pip install -r requirements.txt```

Now you are ready to go with GCalendar app functionality included to your application!
