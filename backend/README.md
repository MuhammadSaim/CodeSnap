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
![Uv](https://img.shields.io/badge/Uv-261230?style=for-the-badge&logo=uv&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-21D789?style=for-the-badge&logo=pycharm&logoColor=white)
![PyCharm](https://img.shields.io/badge/WebStorm-00CFFF?style=for-the-badge&logo=webstorm&logoColor=white)


# 🚀 Backend Setup Guide (Using `uv`)

### 🧩 Configuration Steps

1. **Step into the backend folder**
```bash
  cd backend
```

2. **Create and activate a virtual environment (Python 3.12 via uv)**
```bash
  uv venv --python 3.12
  source .venv/bin/activate
```

3. **Install all dependencies**
```bash
  uv sync
```

4. **Copy the environment file**
```bash
  cp .env.example .env
```

5. **Configure your database in <kbd>.env</kbd>**
```dotenv
SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://DB_USERNAME:DB_PASSWORD@127.0.0.1:3306/DB_DATABASE"
```

6. **Run database migrations**
```bash
  flask db upgrade
```

7. **Run the seeders**
```bash
  flask seeders all
```

8. **Start the Flask development server**
```bash
  flask run
```