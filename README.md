# Crud_CI-CD_AWS_Backend


#List Items
```
{
  "httpMethod": "GET",
  "path": "/items",
  "headers": {
    "Content-Type": "application/json"
  }
}
```

#Create Items
```
{
  "httpMethod": "POST",
  "path": "/items",
  "headers": {
    "Content-Type": "application/json"
  },
  "body": "{\"name\": \"Item 1\", \"description\": \"This is item 1\"}"
}
```


#GetItems
```
{
  "httpMethod": "GET",
  "path": "/items/123",
  "headers": {
    "Content-Type": "application/json"
  },
  "pathParameters": {
    "id": "123"
  }
}
```

#Update Items
``
{
  "httpMethod": "PUT",
  "path": "/items/123",
  "headers": {
    "Content-Type": "application/json"
  },
  "pathParameters": {
    "id": "123"
  },
  "body": "{\"name\": \"Updated Item 1\", \"description\": \"This is the updated item 1\"}"
}
``



#Delete Items
```

{
  "httpMethod": "DELETE",
  "path": "/items/123",
  "headers": {
    "Content-Type": "application/json"
  },
  "pathParameters": {
    "id": "123"
  }
}
```
