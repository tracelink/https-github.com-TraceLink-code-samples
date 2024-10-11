# Incident API  

## Add Comment for Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-comment-for-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "ITEM_ID",
    "processType": "indirectSupplierIncident",
    "aptCommentBox": {
      "aptComment": [{
        "commentText": "Attaching latest order documentation per Jens request",
        "visibilityType": "public"
      }],
      "addAttachment": [
        {
          "fileName": "INC-4098_shipping-order.pdf",
          "fileSize": "3mb",
          "visibilityType": "public",
          "requestIdentifier": "REQUEST_IDENTIFIER_ID"
        }
      ]
    }
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-comment-for-incident:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```

## Edit Comment for Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-comment-for-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "commentId": "COMMENT_ID",
    "processType": "directSupplierIncident",
    "id": "ITEM_ID",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Incorrect order uploaded",
        "visibilityType": "public"
      },
      "removeAttachment": [
        "ATTACHMENT_ID"
      ]
    }
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-comment-for-incident:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```

## List Comments for Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:list-comments-for-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "processType": "incident"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:list-comments-for-incident:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```

## Toggle User Follows Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:toggle-user-follows-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "processType": "incident",
    "follow": true
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:toggle-user-follows-incident:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```

## Get Activity History for Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:get-activity-history-for-incident:v1",
    "ownerId": "tracelink",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "processType": "incident"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:get-activity-history-for-incident:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "ITEM_ID"
    }
}
```
