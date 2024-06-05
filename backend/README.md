# CodeSnap Backend

This repository contains the backend code for the CodeSnap project. The backend is built using [Flask](https://flask.palletsprojects.com/), a lightweight WSGI web application framework in Python.

## Requirements
- Python
- Flask
- Flask SQLAlchemy
- Flask Marshmallow
- Flask Restfull
- Flask CORS


### Technologies

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PyPi](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)


### Configuration

1. Step into folder
```shell
cd backend
```
2. Create virtual environment
```shell
virtualenv venv 
```
3. Activate the venv
```shell
source venv/bin/activate
```
4. Install the dependencies
```shell
pip install -r requirements.txt
```

5. Copy the <kbd>.env.example</kbd> to <kbd>.env</kbd> and setup your DB on <kbd>.env</kbd>

6. Setup the DB
```.dotenv
SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://DB_USERNAME:DB_PASSWORD@127.0.0.1:3306/DB_DATABASE"
```
7. Run the migrations
```shell
flask db upgrade
```
8. Run the seeders
```shell
flask seeders all
```

7. Run the flask app
```shell
flask run
```
