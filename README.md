# contact-management-api
Demo REST API for performing CRUD operations on Contacts(Similar to what exists in a phone book)


## Introduction

API Authenticates via JWT

API implements GET, POST, PUT, PATCH, DELETE endpoints

### Prerequisites

### Running the project locally

First clone the repository to your local machine

```
$ git clone https://github.com/Akohrr/contact-management contact_management
```

Change your directory

```
$ cd contact_management
```

create a virtual environment

```
$ mkvirtualenv contact-management
```

To activate the virtual environment

```
$ workon contact-management
```

Install the dependencies

```
$ pip install -r requirements.txt
```

Create database

```
$ python manage.py migrate
```

Create user

```
$ python manage.py createsuperuser --
```
Finally, run the development server

```
$ python manage.py runserver
```
