# Change Request API  

## Add Change  
### Minimum Required Fields
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "aptBusinessObjectSummary": "Scanner Upgrade",
    "isVisible": false,
    "businessPriority": "MEDIUM"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-change-response:v3",
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
### All Required Fields  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "partnerCompany": {
      "partnerId": "PARTNER_COMPANY_ID",
      "toIdType": "companyMasterData"
    },
    "isVisible": true,
    "aptBusinessObjectSummary": "Scanner Upgrade",
    "aptBusinessObjectDescription": "Replace existing scanners at Warehouse B with upgraded model",
    "responsiblePartyAtCompany": "COMPANY_USER_ID",
    "responsibleDepartmentAtCompany": "BUSINESS_DEVELOPMENT",
    "responsiblePartyAtPartner": "PARTNER_USER_ID",
    "responsibleDepartmentAtPartner": "BUSINESS_DEVELOPMENT",
    "currentlyAssignedPartnerUsers": [
      "PARTNER_USER_ID"
    ],
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID"
    ],
    "businessPriority": "MEDIUM",
    "changeType": "SUPPLIER",
    "implementationDueDate": 1611981070772,
    "implementationTeam": "implementationTeam",
    "initiatingCompany": {
      "partnerId": "PARTNER_USER_ID",
      "toIdType": "companyMasterData"
    },
    "subjectMatterExpert": [
      {
        "subjectMatterExpertEmail": "JDoe@example.com",
        "subjectMatterExpertName": "John Doe"
      }
    ],
    "changeImpact": {
      "changeReferenceIdentifiers": [
        {
          "referenceTransactionType": "INVOICE_NUMBER",
          "value": "55512345"
        }
      ],
      "riskType": "NONTECHNICAL_LOW_RISK",
      "implementationNeededByDate": 1611981070772,
      "businessScopeImpact": "OTHER",
      "otherBusinessScopeImpact": "User-Defined Business Scope",
      "reasonForChange": "STREAMLINE_OPERATIONS",
      "reasonForChangeNotes": "Reason why a change is required.",
      "potentialRisks": "potential Risks",
      "evaluationsOfChange": "Evaluations Of Change"
    },
    "createdByPartner": false,
    "productId": [
      "PRODUCT_ID",
      "PRODUCT_ID"
    ],
    "impactedLocation":
      {
        "locationId": "LOCATION_ID",
        "locationType": "Internal",
        "locationContact": "Elias Davis",
        "toIdType": "companyLocationMasterData"
      },
    "relatedProcesses":
      {
        "processId": "PROCESS_ID",
        "processType": "Incident"
      },
    "aptCommentBox":
      {
        "aptComment": {
          "commentText": "Comment to explain why this is necessary.",
          "visibilityType": "ownerOnly"
        },
        "addAttachment": [
          {
            "fileName": "changeScope_Approved.doc",
            "fileSize": "82kb",
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
        "eventName": "agile-process-teams:add-change-response:v3",
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
## Edit Change  
### Change Request Base State
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "isVisible": false,
    "newBaseState": "InImplementation"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-change-response:v3",
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
### Partner Impact  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "partnerCompany": {
      "partnerId": "PARTNER_COMPANY_ID",
      "toIdType": "companyMasterData"
    },
    "isVisible": true,
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID1",
      "COMPANY_USER_ID2"
    ],
    "initiatingCompany": {
      "toId": "COMPANY_ID",
      "toIdType": "companyMasterData"
    },
    "subjectMatterExpert": [
      {
        "subjectMatterExpertEmail": "JDoe@example.com",
        "subjectMatterExpertName": "John Doe"
      }
    ],
    "changeImpact": {
      "changeReferenceIdentifiers": [
        {
          "referenceTransactionType": "INVOICE_NUMBER",
          "value": "55512345"
        }
      ],
      "riskType": "NONTECHNICAL_LOW_RISK",
      "implementationNeededByDate": 1611981070772,
      "businessScopeImpact": "OTHER",
      "otherBusinessScopeImpact": "User-Defined Business Scope",
      "reasonForChange": "STREAMLINE_OPERATIONS",
      "reasonForChangeNotes": "Reason why a change is required.",
      "potentialRisks": "potential Risks",
      "evaluationsOfChange": "Evaluations Of Change"
    },
    "impactedLocation":
      {
        "locationId": "COMPANY_LOCATION_ID",
        "locationType": "Internal",
        "locationContact": "Elias Davis",
        "toIdType": "companyLocationMasterData"
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
        "eventName": "agile-process-teams:edit-change-response:v3",
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
## Copy Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:copy-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "YOUR_PROCESS_NETWORK_ID",
    "isVisible": true,
    "aptBusinessObjectSummary": "Make a copy of a change",
    "copyPartnerInfo": false,
    "copyGeneralInfo": true,
    "copyImpactInfo": true,
    "copyReferenceIds": false,
    "copyRelatedProcesses": true
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:copy-change-response:v3",
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
## Close Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:close-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "resolutionType": "ACCEPTED",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Closing Request 001. Requested changes approved and complete.",
        "visibilityType": "public"
      }
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
        "eventName": "agile-process-teams:close-change-response:v3",
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
## Reopen Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:reopen-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Reopening Change Request 001",
        "visibilityType": "ownerOnly"
      }
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
        "eventName": "agile-process-teams:reopen-change-response:v3",
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
## Change Comments  
### Add Comment for Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-comment-for-change:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "ITEM_ID",
    "processType": "change",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Attaching updated scanner PO per Jens request",
        "visibilityType": "public"
      },
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
        "eventName": "agile-process-teams:add-comment-for-change:v1",
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
### Edit Comment Text for Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-comment-for-change:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "COMMENT_ID",
    "processType": "change",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Removing incorrect PO document",
        "visibilityType": "public"
      }
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
        "eventName": "agile-process-teams:edit-change-response:v3",
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
### List Comments for Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:list-comments-for-change:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "ITEM_ID",
    "processType": "change"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:list-comments-for-change:v1",
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

## Toggle User Follows Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:toggle-user-follows-change:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "ITEM_ID",
    "processType": "change",
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
        "eventName": "agile-process-teams:toggle-user-follows-change:v1",
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
## Get Activity History for Change  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:get-activity-history-for-change:v1",
    "ownerId": "tracelink",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "processId": "ITEM_ID",
    "processType": "change"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:get-activity-history-for-change:v1",
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

## Read Change Data  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:read-change:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "CHANGE_ID"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
