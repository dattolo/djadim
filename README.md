# Djadim  
Django Admin Improved gained by Navigation, Advanced search and db log.

Based on:
* django 3
* django-admin-tools
* django-admin-search-builder
* django-application-settings
* django-db-logger
* ipdb

## Quick start

### Create Virtual Environment

Create a Virtual Environment

```
python3 -m venv /path/to/new/virtual/environment
```

Activate venv

```commandline
source /path/to/new/virtual/environment/bin/activate
```

### Installation
*Copy and paste* in the teminal
````
git clone https://github.com/dattolo/djadim.git
cd djadim
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py loaddata data.json
python manage.py runserver
````

#### During installation

Insert *username* and *password* at prompt request. 

#### After installation

Login in [admin](http://127.0.0.1:8000/admin/) with previous *username* and *password*.

##### Generate dummy log

In Menu Naigation go in 

'Application' -> 'Identity' -> 'Digital Identity' 

Open and Save an identity.

A sample log will writed. 

Logs are in 

'Application' -> 'Log' -> 'Logging'

## Reference

### Pip freeze

```commandline
asgiref==3.5.0
asttokens==2.0.5
backcall==0.2.0
decorator==5.1.1
Django==3.2.13
django-admin-search-builder==0.2.2
django-admin-tools==0.9.2
django-application-settings==0.2
django-db-logger==0.1.12
executing==0.8.3
ipdb==0.13.9
ipython==8.3.0
jedi==0.18.1
matplotlib-inline==0.1.3
parso==0.8.3
pexpect==4.8.0
pickleshare==0.7.5
prompt-toolkit==3.0.29
ptyprocess==0.7.0
pure-eval==0.2.2
Pygments==2.12.0
pytz==2022.1
six==1.16.0
sqlparse==0.4.2
stack-data==0.2.0
toml==0.10.2
traitlets==5.1.1
wcwidth==0.2.5
```

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
