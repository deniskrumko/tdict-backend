# POST /api/token/

Get auth token for using private API. Redeemed token used for "Authorization" header like this:
`Authorization: Token d210ef6e0dea94adff006808f3e5b8e4b689b28e`

Request (POST, without headers):
```
{
    "username": "deniskrumko",
    "password": "my cool password"
}
```

Response (HTTP 200) - token for auth:
```
{
    "token": "d210ef6e0dea94adff006808f3e5b8e4b689b28e"
}
```

Response (HTTP 400):
```
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

# GET /words/

Get paginated response with own words. Requires `Authorization` header.

**Query params**:
- `?page=` - for pagination. By default is page 1.
- `?language=' - filter by language ("RU", "EN"). By default API returns all languages.

Response (HTTP 200):
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

Response (HTTP 401) - no token provided:
```
{
    "detail": "Authentication credentials were not provided."
}
```
