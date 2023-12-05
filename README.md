
# Raw Django with Nginx-Celery-Rabbitmq-Redis 

This is a  raw project with complete setup of django rest framework


## Run Locally

Clone the project

```bash
  git clone git@github.com:rzmobiledev/dj_celery.git
```

Go to the project directory

```bash
  cd dj_celery
```

Install dependencies

```bash
  pip install poetry 
```
```bash
  poetry install
```

Start the server

```bash
  docker compose build
```
```bash
  docker compose up -d
```

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`DEBUG=True`
`SECRET_KEY=`
`DB_HOST=`
`DB_USER=`
`DB_PASSWORD=`
`DB_NAME=`

# Superuser Variable
`USERNAME=`
`PASSWORD=`
`EMAIL=`
`FIRST_NAME=`
`LAST_NAME=`


## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Authors

- [@rizalsafril](https://www.github.com/rzmobiledev)


## 🚀 About Me
I'm a python developer with main focus on Backend Engineer

