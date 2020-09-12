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
