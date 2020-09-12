define({ "api": [
  {
    "type": "POST",
    "url": "/api/resource/User",
    "title": "Create User",
    "name": "Create_User",
    "group": "Miscellaneous",
    "version": "0.0.0",
    "filename": "/Users/neel/qct/frappe-bench/config/apidocs/apidoc.py",
    "groupTitle": "Miscellaneous",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Authorization token</p>"
          },
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Accept",
            "defaultValue": "application/json",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Mobile App Headers",
          "content": "{\"Authorization\":\"token lkasdjfaksdfjlka\",\"Accept\":\"application/json\"}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "defaultValue": "Success",
            "description": ""
          },
          {
            "group": "Success 200",
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Success 200",
          "content": "{\"message\":\"Success\",\"data\":{\"field_x\":\"value_x\"}}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 401": [
          {
            "group": "Error 401",
            "type": "String",
            "optional": false,
            "field": "message",
            "defaultValue": "Unauthorized",
            "description": ""
          }
        ],
        "Error 403": [
          {
            "group": "Error 403",
            "type": "String",
            "optional": false,
            "field": "message",
            "defaultValue": "Forbidden",
            "description": ""
          }
        ],
        "Error 422": [
          {
            "group": "Error 422",
            "type": "String",
            "optional": false,
            "field": "message",
            "defaultValue": "Validation Error",
            "description": ""
          },
          {
            "group": "Error 422",
            "type": "Object",
            "optional": false,
            "field": "errors",
            "description": ""
          }
        ]
      },
      "examples": [
        {
          "title": "Error 401",
          "content": "{\"message\":\"Unauthorized\"}",
          "type": "json"
        },
        {
          "title": "Error 403",
          "content": "{\"message\":\"Forbidden\"}",
          "type": "json"
        },
        {
          "title": "Error 422",
          "content": "{\"message\":\"Validation Error\",\"errors\":{\"field_x\":\"error_message_x\"}}",
          "type": "json"
        }
      ]
    }
  },
  {
    "type": "GET",
    "url": "/api/resource/User",
    "title": "Get User List",
    "name": "Get_User_List",
    "group": "Miscellaneous",
    "version": "0.0.0",
    "filename": "/Users/neel/qct/frappe-bench/config/apidocs/apidoc.py",
    "groupTitle": "Miscellaneous"
  }
] });
