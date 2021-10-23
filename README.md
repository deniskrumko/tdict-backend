# tdict-django
Backend for TDict project on Django 3

# Works on
- Python 3.9.6
- Django 3.2.8
- Django REST Framework 3.12.4

# Project hosted by Heroku
https://tdict-django.herokuapp.com/

# URLs

Admin:
- GET `/admin` - Admin UI

Auth:
- POST `/api/token/` - get auth token

Words (PUBLIC):
- GET `/api/public/words/` - public API for get all words

Words (PRIVATE, requires auth token):
- GET `/api/words/` - get words of current user
- GET `/api/words/?language=EN` - get words by language (EN/RU)
- POST `/api/words/` - create new word
- GET `/api/words/<id>/` - get specific word of current user
- PATCH `/api/words/<id>/` - update specific word of current user
- DELETE `/api/words/<id>/` - delete specific word of current user
