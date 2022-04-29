# Django Admin Improved
Djadim, Django Admin navigation, advanced search and db log.

Based on:
* django>3
* django-admin-tools
* django-admin-search-builder
* django-application-settings
* django-db-logger
* ipdb==0.13.9

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

### Clone repository in local

#### Quick start
````
git clone git@github.com:dattolo/djadim.git
cd djadim
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata identity_dumps.json
python manage.py runserver
````

#### Authors

Francesco Dattolo
