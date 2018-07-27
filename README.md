# Instagram Clone

This is a clone of the famous instagram app.Users can sign up login, view and post photos and folllow other users.

## User Stories

1. Register and Sign in to the application.
2. Upload my pictures to the application.
3. See my profile with all my pictures.
4. Follow other users and see their pictures on my timeline.
5. Like a picture and leave a comment on it.

## Features 

+ [x] User authentication with email confirmation.
+ [x] Public user profiles.
+ [x] Uploading photos to the site
+ [x] following and follow feature features.
+ [x] Photo feed displaying photos of users that the signed in user follows.
+ [x] Commenting on images.
+ [x] Search functionality for users.
+ [x] User profile where the user views only his/her photos.
+ [x] Django admin dashboard for adding & managing posts and user accounts

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Requirements 

* Python3
* Pip

### Installing

```
git clone https://github.com/mzazakeith/instagram-clone.git && cd instagram-clone
```

Create a virtual environment and activate it

```
python3 -m virtualenv virtual

source virtual/bin/activate
```
Install all requirements

```
pip install -r requirements.txt

```
Create a .env file 

set all environment variables to development 

set the allowed hosts to localhost

add your database infromation i.e
* DB_NAME= #database name
* DB_USER= #database user
* DB_PASSWORD=#database password
* DB_HOST="127.0.0.1"

Run migrations
```
python manage.py migrate

```

Start the server
```
python manage.py runserver

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```

## Deployment

Deployment was done using heroku.


## Author

* **Billie Thompson** - [Github](https://github.com/mzazakeith)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
