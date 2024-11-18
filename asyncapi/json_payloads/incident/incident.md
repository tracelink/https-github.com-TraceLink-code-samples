# Incident API  

## Add Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-incident:v5",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "aptBusinessObjectSummary": "Kendall Pharma | ACME Inc | INC-2023-01 | No EPCIS Data for 1 package",
        "aptBusinessObjectDescription": "Shipment quarantined due to T1 reflecting incomplete data|SO 3027209239|PO 5201019344|Transaminase enzyme, CDX-017 (ACS-4007466). EPCIS shows 48 pallets and receiving called out 50 received ",
        "businessPriority": "HIGH",
        "incidentCategory":"Aggregate Shipment Error",
        "referenceIdentifiers": [
            {
                "referenceTransactionType": "PO Number",
                "value": "PO-123"
            },
            {
                "referenceTransactionType": "PO Number",
                "value": "PO-345"
            }
        ],
        "impactedProducts": [
            {
                "productDetailId": "PRODUCT_ID",
                "impactedLots": "4"
            }
        ],
        "responsibleEntity": {
            "partnerId": "PARTNER_COMPANY_ID",
            "toIdType": "companyLocationMasterData"
        },
        "resolutionDueDate": 1681640075000,
        "responsiblePartyAtCompany": "COMPANY_USER_ID",
        "currentlyAssignedCompanyUsers": [
            "COMPANY_USER_ID1",
            "COMPANY_USER_ID2"
        ],
        "responsiblePartyAtPartner": "PARTNER_USER_ID",
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

## Edit Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-incident:v5",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "aptBusinessObjectSummary": "Kendall Pharma | ACME Inc | INC-2023-01 | No EPCIS Data for 1 package",
        "aptBusinessObjectDescription": "Shipment quarantined due to T1 reflecting incomplete data|SO 3027209239|PO 5201019344|Transaminase enzyme, CDX-017 (ACS-4007466). EPCIS shows 48 pallets and receiving called out 50 received",
        "businessPriority": "HIGH",
        "incidentCategory":"Aggregate Shipment Error",
        "referenceIdentifiers": [
            {
                "referenceTransactionType": "PO Number",
                "value": "PO-123"
            },
            {
                "referenceTransactionType": "PO Number",
                "value": "PO-345"
            }
        ],
        "impactedProducts": [
            {
                "productDetailId": "ea92a360-55ac-15eb-bb95-8bd76e7bd0015",
                "impactedLots": "4"
            }
        ],
        "responsibleEntity": {
            "partnerId": "c923a50c-3fbe-4cd2-bb6e-14b2be894189",
            "toIdType": "companyLocationMasterData"
        },
        "resolutionDueDate": 1681640075000,
        "responsiblePartyAtCompany": "9fc845af-3a50-43d7-83a4-4358108057c2",
        "currentlyAssignedCompanyUsers": [
            "d5b2b867-fdeb-4b1c-a0d4-8aabf853c169",
            "a4bc6e7f-6436-4499-b453-270cdd052271"
        ],
        "responsiblePartyAtPartner": "13fb0cc6-771c-447a-a1bb-02513a235b24",
        "currentlyAssignedPartnerUsers": [
            "13fb0cc6-771c-447a-a1bb-02513a235b24",
            "ee532337-89d2-4f5f-b024-bfa070139b73"
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

## Copy Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:copy-incident:v3",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "id": "INCIDENT_ID",
        "aptBusinessObjectSummary": "Copy Without generalInfo",
        "copyRelatedProcesses": true,
        "createdByPartner":true
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

## Close Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:close-incident:v1",
         "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "id": "INCIDENT_ID",
        "resolutionType": "NOT_AN_ISSUE",
        "isReoccuring": false,
        "finalRootCause": "AUDIT_ERROR",
        "closingStatement": "Closing this incident"
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

## Reopen Incident  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:reopen-incident:v1",
         "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "id": "INCIDENT_ID",
        "resolutionType": "NOT_AN_ISSUE",
        "isReoccuring": false,
        "finalRootCause": "AUDIT_ERROR",
        "closingStatement": "Closing this incident"
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
## Submit Incident to Partner  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:submit-incident-to-partner:v1",
         "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "id" : "INCIDENT_ID"
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

## Read Incident Data  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:read-incident:v4",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "INCIDENT_ID"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
