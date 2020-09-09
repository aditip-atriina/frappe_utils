## Utils

Frappe & Bench utilities <br>
To use just <br>
<kbd>import utils</kbd>


#### Responder
Use following utility methods to return responses with keys like `data`, `message` and `errors`
* <kbd>return utils.responder.respondWithSuccess(self, status=200, message='Success', data={})</kbd>
* <kbd>return utils.responder.respondWithFailure(self, status=500, message='Something went wrong', data={}, errors={})</kbd>
* <kbd>return utils.responder.respondUnauthorized(self, status=401, message='Unauthorized')</kbd>
* <kbd>return utils.responder.respondForbidden(self, status=403, message='Forbidden')</kbd>

#### APIException Class
Base Exception for API Requests

Example:
```
try:
    ...
except APIException as e:
    return e.respond()
```

#### Custom Exceptions
Create a custom exception by extending the class from `APIException`<br>
Set following attributes for the exception (either as an attribute or by using `__init__` method)<br>
Example:
```
class ValidationException(APIException):
    http_status_code = 422
    message = frappe._('Validation Error')

    def __init__(self, errors):
        self.errors = errors
```

#### License

MIT