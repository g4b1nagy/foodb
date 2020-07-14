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


### Requirements

* Register new product batches for the warehouse
    - http://localhost:8000/api/v1/products/
    - http://localhost:8000/api/v1/batches/

* Update or modify stock of any batch
    - http://localhost:8000/api/v1/batches/1/ [PATCH]

* Retrieve the current inventory per product, for the whole warehouse, broken down by batches
    - http://localhost:8000/api/v1/products/1/batches/

* Retrieve the current inventory per product, for each batch individually
    - http://localhost:8000/api/v1/batches/1/

* Retrieve an overview of the freshness of food we have in the warehouse (3 states: fresh, expiring today, expired)
    - http://localhost:8000/api/v1/products/1/inventory/

* Retrieve the history of a given batch (we should be able to trace what came in, what went out)
    - ???
