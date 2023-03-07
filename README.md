# TwitterAPI

This repository contains a template for building a RESTful API using FastAPI and MongoDB atlas and running it with Docker.


## Prerequisites
Before starting, you need to have Docker and Docker Compose installed in your system.

## Getting Started

To get started, clone the repository and navigate to the project directory.

```bash
git clone https://github.com/Mirestrepot/twitter-api-fastapi.git


```
Next, create a .env file in the root directory and add the following environment variables:
These environment variables will be used by Docker Compose to set up the MongoDB database. Change the values according to your requirements.

## Connect Datebase(MongoDB Alas)
```
MongoDB Shell: mongosh "mongodb+srv://twitterapi.tixzlnu.mongodb.net/myFirstDatabase" --apiVersion 1 --username mirestrepot
MongoDB VS code: mongodb+srv://mirestrepot:JCaCLq8ENMyCRIZJ@twitterapi.tixzlnu.mongodb.net/test
Username: mirestrepot
Password: JCaCLq8ENMyCRIZJ

```
## Installation
Use Python environment (venv) first.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt 

```
## Running the Application
To run the application, use the following command:

```bash
Run main.py
```
Now you can access the API at http://localhost/docs. This will open the FastAPI Swagger UI, where you can explore and test the endpoints.
## Running the Application with Docker
You need to download the docker documentation and use it to fetch the docker repository. "https://docs.docker.com/engine/reference/commandline/pull/"
```bash
docker pull mirestrepot/twitter-api-fastapi
```
## Project Structure
```bash
twitter-api-fastapi
├── backend
│   ├── backend
│   │   ├── dependencies
│   │   ├── endpoints
│   │   ├── __init__.py
│   │   └── router.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── schemas
│   │        ├──tweet.py
│   │        └──user.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── tweet.py
│   │   └── user.py
│   │    
│   ├── routers
│   │   ├── __init__.py
│   │   ├── tweet.py
│   │   ├── auth_users.py
│   │   ├── login.py
│   │   └── user.py
│   │
│   ├── utils
│   │   ├── __init__.py
│   │   └── fuction.py 
│   │
│   ├──main.py
│   ├──app.py
│   └──requirements.txt
├── docker-compose.yml
├── Dockerfile
├── .dockerignore
├── README.md
└── .gitignore

```
twitter-api-fastapi - Project
bakend- This directory contains the main application code.
backend/routers- This directory contains the API endpoints and their dependencies.
bakend/db - This directory contains the MongoDB database connection code.
backend/models - This directory contains the data models for the application.
docker-compose.yml - This file defines the Docker services and their configuration.
Dockerfile - This file defines the Docker image for the application.
requirements.txt - This file contains the Python dependencies for the application.
README.md - This file contains the project documentation.
.env - This file contains the environment variables for the application.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)