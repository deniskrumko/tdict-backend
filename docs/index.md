# API documentation

Authorization:
- [POST /api/token/](#post-apitoken)

Dictionary:
- [GET /api/words/](#get-apiwords)
- [POST /api/words/](#post-apiwords)
- [GET /api/words/\<word_id\>/](#get-apiwordsword_id)
- [PATCH /api/words/\<word_id\>/](#patch-apiwordsword_id)
- [DELETE /api/words/\<word_id\>/](#delete-apiwordsword_id)

## POST /api/token/

Get auth token for using private API. Redeemed token used for `Authorization` header with value like
`Token d210ef6e0dea94adff006808f3e5b8e4b689b28e`.

**Request**
```
{
    "username": "deniskrumko",
    "password": "my cool password"
}
```

**Response (HTTP 200)** - token for auth
```
{
    "token": "d210ef6e0dea94adff006808f3e5b8e4b689b28e"
}
```

**Response (HTTP 400)**
```
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

## GET /api/words/

Get paginated response with own created words.

Requires `Authorization` header.

**Query params**:
- `?page=` — for pagination. By default is page 1.
- `?language=` — filter by language ("RU", "EN"). By default API returns all languages.

**Response (HTTP 200)**
```
{
    "count": 10,
    "next": "http://127.0.0.1:8000/api/words/?page=2",
    "previous": null,
    "results": [
        {
            "id": 228,
            "word": "lizard",
            "language": "EN",
            "description": "Description for lizard",
            "translations": [
                {
                    "id": 227,
                    "word": "ящерица",
                    "language": "RU"
                }
            ]
        }
    ]
}
```

**Response (HTTP 401)** - no token provided
```
{
    "detail": "Authentication credentials were not provided."
}
```

## POST /api/words/

Create new word translation.

Requires `Authorization` header.

**Request**:
```
{
    "word": "aboba",
    "language": "EN",
    "description": "Description for aboba",
    "translations": [228]  # id of another word
}
```

**Response (HTTP 201)**
```
{
    "id": 229,
    "word": "aboba",
    "language": "EN",
    "description": "Description for aboba",
    "translations": [228]
}
```

**Response (HTTP 400)**
```
{
    "non_field_errors": [
        "The fields word, description must make a unique set."
    ]
}
```


## GET /api/words/\<word_id\>/

Get single word by ID.

Requires `Authorization` header.

**Response (HTTP 200)**
```
{
    "id": 228,
    "word": "lizard",
    "language": "EN",
    "description": "Description for lizard",
    "translations": [
        {
            "id": 227,
            "word": "ящерица",
            "language": "RU"
        }
    ]
}
```

**Response (HTTP 404)**
```
{
    "detail": "Not found."
}
```

## PATCH /api/words/\<word_id\>/

Update single word by ID.

Requires `Authorization` header.

**Request**
```
{
    "word": "aboba",
    "language": "EN",
    "description": "Description for aboba",
    "translations": [228]
}
```

Request can contain all fields or only those fields that needed to be updated. Like this:
```
{
    "description": "New description",
}
```

**Response (HTTP 200)**
```
{
    "id": 229,
    "word": "aboba",
    "language": "EN",
    "description": "New description",
    "translations": [
        228
    ]
}
```

**Response (HTTP 404)**
```
{
    "detail": "Not found."
}
```

## DELETE /api/words/\<word_id\>/

Delete single word by ID.

Requires `Authorization` header.

**Response (HTTP 204)** with empty body
