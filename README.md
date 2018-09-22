
[![Build Status](https://travis-ci.org/Wabuluka/api.svg?branch=master)](https://travis-ci.org/Wabuluka/api) 
[![Coverage Status](https://coveralls.io/repos/github/Wabuluka/api/badge.svg?branch=master)](https://coveralls.io/github/Wabuluka/api?branch=master)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)
# CRUD API - Andela

In this API, I have put together a simple way in which you can create, retrieve, update and delete data from a list
## Getting Started
To get start with this API, you will need to set up a few prerequists as I am going to guide below.
### Prerequisites

What things you need to install the software and how to install them

```
Windows Mac or Linux
```

### Installing


create a virtual environment with (virtualenv yourEnv).

Activate the virtual environment. (source yourEnv/bin/activate)

```
install python (pip install python)
```

```
Install Flask (pip install flask)
```

```
Install requirements (pip freeze > requirements.txt)
```

## Endpoints in the API
|REQUEST TYPE| URL | DESCRIPTION |
|------------|-----|-------------|
|POST| /api/v1/orders/|Place a new order|
|GET| /api/v1/orders |Get all orders|
|GET| /api/v1/orders/<int:orderId> |Get specific order by orderId|
|DELETE| /api/v1/orders/<int:orderId> |Delete order|

## Running the tests

It only needs one code statement to run the test for this simple application

Run the following command in your terminal or cmd
Although at the moment my tests are not fully functional, am still learning how to make them better

```
python -m unittest
```

## Deployment

You can find a demo view of how this application works from heroku
* [Heroku](https://flask-api-wabuluka.herokuapp.com/) - Simple CRUD application in Flask

If you want to test the api from your localhost, clone the source code and install the requirements
```
https://github.com/Wabuluka/api.git
```

## Authors

* **Davies Wabuluka**  - [Github](https://github.com/Wabuluka)

