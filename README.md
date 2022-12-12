# STORICARD.COM - API

## Introduction

+ It is recommended to have installed on your computer [Python 3.10.1](https://www.python.org/downloads/release/python-3101/)
+ The API was created with the framework [Flask](https://flask.palletsprojects.com/en/2.0.x/)
+ The connection to the database is achieved with the ORM [SQLAlchemy](https://www.sqlalchemy.org/blog/2022/06/24/sqlalchemy-1.4.39-released/)
+ For unit tests, the library was used [Unitest](https://pypi.org/project/unittest2/)

## Prerequisitos

+ It is recommended to have installed on your computer [Python 3.10.1](https://www.python.org/downloads/release/python-3101/)
Create a `.env` file in the root directory of the project, you can refer `.env.example` for this.

## Project configuration with python virtual env

+ Enable python virtual environment and then install project dependencies.
```commandline
python -m venv ./venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app/manage.py runserver
```

## Project configuration with Docker

+ In order to complete the next steps you must need to have installed docker in your local machine.
Once docker is installed you can run the following command:
```commandline
docker-compose up -d
```

## Unit Testing with Unittest

```commandline
python -m unittest app/test.py
```

# Endpoint

+ The endpoint to consume the service is:
```commandline
GET http://127.0.0.1:5000/api/v1/transactions
```

![alt text](https://github.com/jmelo77/Challenge-Stori/blob/main/doc/endpoint_stori.png)

![alt text](https://github.com/jmelo77/Challenge-Stori/blob/main/doc/email_stori.png)
