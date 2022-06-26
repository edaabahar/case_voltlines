# case_voltlines 2022

## Requirements

Run these commands to start the api:

- For Windows:

```git
git clone git@github.com:edaabahar/case_voltlines.git
cd case_voltlines
py -m venv env
cd env
Scripts\activate
pip install django
pip install djangorestframework
cd ..
python manage.py runserver
```

- For Linux:
```git
git clone git@github.com:edaabahar/case_voltlines.git
cd case_voltlines
python3 -m venv env
source env/bin/activate
pip3 install django
pip3 install djangorestframework
python3 manage.py runserver
```

This project developed in Windows 10 OS using python version 3.8.5 and latest version of Django. This is my very first Django project that contains some functions which are not working. When you run the project open ```http://127.0.0.1:8000/voltlines_app/```. You will see a small api doc from django rest framework.