# Task Template API  

## Add Task Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-task-template:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "templateName": "API Created Task Template",
    "aptBusinessObjectDescription": "Template to demonstrate creation via API",
    "isTemplateModifiableByMember": true,
    "isAddRemoveSubtaskAllowed": true,
    "completionRequiredWithinDays": 14,
    "businessPriority": "LOW",
    "responsibleDepartmentAtCompany": "CUSTOMER_SERVICE",
    "responsiblePartyAtCompany": "COMPANY_USER_ID",
    "currentlyAssignedCompanyUsers": ["ASSIGNED_COMPANY_USER_ID"]
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-task-template:v1",
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

## Edit Task Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-task-template:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "TEMPLATE_ID",
    "aptBusinessObjectDescription": "Updated template for customer service tasks",
    "completionRequiredWithinDays": 3,
    "businessPriority": "HIGH",
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID"
    ]
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-task-template:v3",
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

## Copy Task Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:copy-task-template:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "TASK_TEMPLATE_ID",
    "templateName": "Copy of Template for customer service tasks",
    "copyGeneralInfo": true,
    "copySubTasks": true
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:copy-task-template:v1",
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
## Add Sub-Task to Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-sub-task-to-template:v2",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "templateId": "TEMPLATE_ID",
    "subTaskName": "Sub-Task 01234",
    "subTaskType": "Sub-Task Type XYZ",
    "completionRequiredWithinDays": 7,
    "businessPriority": "LOW",
    "partnerCompany": {
      "partnerId": "PARTNER_COMPANY_ID",
      "toIdType": "companyMasterData"
    },
    "responsiblePartyAtPartner": "PARTNER_USER_ID",
    "responsibleDepartmentAtPartner": "SUPPLY_CHAIN",
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID1",
      "COMPANY_USER_ID2"
    ],
    "currentlyAssignedPartnerUsers": [
      "PARTNER_USER_ID"
    ],
    "referenceIdentifiers": [
      {
        "referenceTransactionType": "BILL_OF_LADING",
        "value": "GTIN-1161187176294956"
      }
    ],
    "relatedProcesses": [
      {
        "processId": "PROCESS_ID",
        "processType": "incident",
        "relationship": "Contains"
      }
    ]
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-sub-task-to-template:v2",
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
## Edit Sub-Task on Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-sub-task-on-template:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "TEMPLATE_ID",
    "subTaskName": "Sub-Task 56789",
    "subTaskType": "Sub-Task Type ABC",
    "subTaskDueDate": 1631133945000,
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID"
    ],
    "currentlyAssignedPartnerUsers": [
      "PARTNER_USER_ID1",
      "PARTNER_USER_ID2"
    ]
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-sub-task-on-template:v3",
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
## List Sub-Task for Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:list-sub-task-for-template:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "TEMPLATE_ID"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:list-sub-task-for-template:v1",
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
## Remove Sub-Task for Template  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:remove-sub-task-from-template:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "SUBTASK_ID"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:remove-sub-task-from-template:v1",
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
