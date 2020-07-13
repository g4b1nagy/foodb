# foodb

Inventory management system

![foodb screenshot](https://raw.github.com/g4b1nagy/foodb/master/foodb.png)

* git clone git@github.com:g4b1nagy/foodb.git
* cd foodb/
* virtualenv -p python3 venv
* source venv/bin/activate
* pip install -r requirements.txt
* ./manage.py migrate
* ./manage.py loaddata fixtures.json
* ./manage.py createsuperuser
* ./manage.py runserver
* http://localhost:8000/admin/products/batch/
