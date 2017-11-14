#!/bin/bash
mkdir app migrations tests 
touch requirements.txt config.py manage.py
mkdir app/templates app/static app/main
cd app/main 
touch __init__.py errors.py forms.py views.py
cd -
cd app 
touch __init__.py email.py models.py
cd -
cd tests
touch __init__.py test.py
