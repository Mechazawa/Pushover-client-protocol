PushOver client api
=====

## Notes
* The API will return the default 404 page if a request was invalid and the api function is hidden. 
* The base url for all API requests is https://api.PushOver.net/1/
* If the returned status != 1 then something went wrong
* All API calls must be made over https
* You can only send one api call every two seconds. If you send too many you'll get banned for a couple of seconds

## Login - /login.json

This API call is used for creating a session token. Also known as "secret"

| Variable | Description       | Method |
|----------|-------------------|--------|
| Email    | Email of the user | POST   |
| Password | User password     | POST   |

The the request meets the specified parameters then the server will return the following

```js
{
    'status': 1, // If the status != 1 then something went wrong
    'secret': '9W8B3AFFCwzHf8ldaYYBHuMusDyebF8vGcgcVIdafuTstVAoQ7cg6uk5P3y9', // The session token
    'request': '35177dafc7f7179c6a045cb9817503b5', // The request identifier
    'id': 'cvw5lFwrUBHi99Y8iebcOxYGm36Jjx' // User ID (not 100% sure)
}
```

## Messages - /messages.json

This API cal is used for obtaining the queued messages from the server.

| Variable  | Description       | Method |
|-----------|-------------------|--------|
| secret    | The session token | GET    |
| device_id | The device uuid   | GET    |

```js
{
    "messages": [{ // An array containing all the messages
        "id": 1, // Notification ID 
        "message": "This message confirms that you are now able to receive messages on this device (curltest).\n\nVisit https://pushover.net/apps to view apps, plugins, and services to use with your account, or https://pushover.net/api to get started with our API.", // The message
        "app": "Pushover", // Application name
        "aid": 1, // Application id
        "icon": null, // an optional string indicating the icon id
        "date": 1395414736, // The timestamp for when it has been sent
        "priority": 0, // The priority
        "acked": 0, // If the push has been acknowledged
        "umid": 267,
        "title": "Welcome to Pushover" // an optional title
    }],
    "status": 1, // The request status
    "request": "4cd1a5c617b2ae9c1e31df4ddfed6faf" // The request id
}
```
