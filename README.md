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
except utils.exceptions.APIException as e:
    return e.respond()
```

#### Custom Exceptions
Create a custom exception by extending the class from `APIException`<br>
Set following attributes for the exception (either as an attribute or by using `__init__` method)<br>
Example:
```
class ValidationException(APIException):
    http_status_code = 422
    message = _('Validation Error')

    def __init__(self, errors):
        self.errors = errors
```

#### API Documentation
* Create API Documentation using [apidocjs](//apidocjs.com)
* Checkout API Doc Doctype

#### Data Validation
* Use `utils.validator.validate(data, rules)` to validate data sent to the API
* For rules, checkout [validator](https://pypi.org/project/validator/) python package
* New rule: <kbd>utils.validator.rules.ExistsRule(doctype='User', fields='email', message='Email already taken')</kbd>
* New rule: <kbd>utils.validator.rules.LengthRule(length=10, message='Should be atleast {arg} in length.')</kbd>
* New rule: To validate HTTP method
<kbd>utils.validator.validate_http_method('post', 'patch')</kbd>

#### API Testing
* Can do API Testing only for the APIs written using the format given in [APIException Class](#apiexception-class)
* Go through `api.py` for knowing how to write APIs
* Go through `tests/test_api.py` to know how to write tests for those APIs.

#### License

MIT