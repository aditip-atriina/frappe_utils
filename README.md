## Utils

Frappe & Bench utilities
```
import utils
```

#### Responder
Use following utility methods to return responses with keys like `data`, `message` and `errors`
```
return utils.responder.respondWithSuccess(self, status=200, message='Success', data={})
```
```
return utils.responder.respondWithFailure(self, status=500, message='Something went wrong', data={}, errors={})
```
```
return utils.responder.respondUnauthorized(self, status=401, message='Unauthorized')
```
```
return utils.responder.respondForbidden(self, status=403, message='Forbidden')
```

#### License

MIT