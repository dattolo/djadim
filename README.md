# Django Admin Improved
Djadim, Django Admin navigation, advanced search and db log.

Based on:
* django 3
* django-admin-tools
* django-admin-search-builder
* django-application-settings
* django-db-logger
* ipdb

## Quick start

**Create your Virtual Environment**

Copy and paste in terminal
````
git clone git@github.com:dattolo/djadim.git
cd djadim
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata data.json
python manage.py runserver
````

## Reference

**Django version**

```commandline
python -c "import django; print(django.get_version())"
3.2.13
```

**Django Admin Tools**

**IPDB**


```commandline
python manage.py shell

In [1]: %load_ext autoreload
   ...: %autoreload 2
   ...: from django.contrib.auth import get_user_model
   ...: User = get_user_model()
In [2]: user = User.objects.get(pk=1)
```

**Log**
customized django-db-logger with advanced search

**Local settings**

### Authors

Francesco Dattolo
