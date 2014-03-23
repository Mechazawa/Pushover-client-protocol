PushOver client api
=====

## Notes
The API will return the default 404 page if a request was invalid and the api function is hidden. 

## Login
POST

This API call is used for creating a session token. Also known as "secret"

| Variable | Description       | Method |
|----------|-------------------|--------|
| Email    | Email of the user | POST   |
| Password | User password     | POST   |

*returns*
```json
{
    'status': 1, // If the status != 1 then something went wrong
    'secret': '9W8B3AFFCwzHf8ldaYYBHuMusDyebF8vGcgcVIdafuTstVAoQ7cg6uk5P3y9', // The session token
    'request': '35177dafc7f7179c6a045cb9817503b5', // The request identifier
    'id': 'cvw5lFwrUBHi99Y8iebcOxYGm36Jjx' // User ID (not 100% sure)
}
```
