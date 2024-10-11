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
    "eventName": "agile-process-teams:add-external-manufacturing-incident:v3",
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
    "partnerLocationId": "LOCATION_ID",
    "aptBusinessObjectSummary": "Missing Shipment",
    "aptBusinessObjectDescription": "Shipment XYZ missing at Location ABC",
    "deviationType": "PLANNED",
    "responsiblePartyAtCompany": "COMPANY_USER_ID",
    "responsibleDepartmentAtCompany": "CUSTOMER_SERVICE",
    "responsiblePartyAtPartner": "PARTNER_USER_ID",
    "responsibleDepartmentAtPartner": "SUPPLY_CHAIN",
    "currentlyAssignedCompanyUsers": [
      "COMPANY_USER_ID"
    ],
    "currentlyAssignedPartnerUsers": [
      "PARTNER_USER_ID",
      "PARTNER_USER_ID"
    ],
    "materialType": "FINISHED_GOOD",
    "materialSubtype": "CHEMICAL_API",
    "materialProblem": "MATERIAL_SHORTAGE",
    "originatingLocation": [{
      "originatingLocationId": "LOCATION_ID",
      "toIdType": "partnerLocationMasterData"
    }],
    "resolutionDueDate": 1651133945000,
    "createdByPartner": false,
    "isSubmittedToPartner": true,
    "referenceIdentifiers": [{
      "referenceTransactionType": "BILL_OF_LADING",
      "value": "GTIN-1161187176294956"
    }],
    "externalManufacturingMaterialInformation": {
      "companyInternalMaterialInformation": "pim161187176294672",
      "partnerInternalMaterialInformation": "pim161187176294672",
      "materialName": "Material Name",
      "materialDescription": "Material Description",
      "companyLotNumber": "cln161187176294679",
      "partnerLotNumber": "pln161187176294652",
      "defectiveQuantity": "1",
      "defectiveUnitOfMeasure": "CENTILITER",
      "defectiveItemInformation": "Defective Item Information",
      "samplesAvailable": false
    },
    "externalManufacturingResponse": {
      "initialResponseDueDate": 1641133945000,
      "initialResponseInformation": "Initial Response Information",
      "finalResponseDueDate": 1641133945000,
      "finalResponseInformation": "Final Response Information",
      "dateSamplesSentToCompany": 1641133945000,
      "dateSamplesReceivedByCompany": 1641133945000,
      "dateSamplesSentToPartner": 1641133945000,
      "dateSamplesReceivedByPartner": 1641133945000,
      "inventoryImpact": "Inventory Impact",
      "inventoryAnalysisMethod": "Inventory Analysis Method",
      "initialContainmentActions": "Final Containment Actions",
      "recommendationFromOriginatingCompany": "Recommendation From Originating Company",
      "immediateCorrectiveActions": "Immediate Corrective Actions",
      "potentialRootCauses": "DOCUMENTATION",
      "potentialRootCauseNotes": "Potential Root Cause Notes",
      "finalPreventativeActions": "Final Preventative Actions",
      "methodsToProvePreventativeActionsTaken": "Methods To Prove Preventative Actions Taken",
      "replacementMaterials": [
        {
          "availabilityDateForReplacements": 1641133945000,
          "transactionIDsForReplacements": {
            "referenceTransactionType": "INVOICE_NUMBER",
            "value": "100"
          }
        }
      ],
      "externalManufacturingImpact": {
        "businessImpact": "Business Impact",
        "businessPriority": "HIGH",
        "impactedDepartments": [
          "CUSTOMER_SERVICE"
        ],
        "highPriorityReasons": [
          "Reason1"
        ],
        "financialImpact": 164113394500,
        "dateSupplyImpacted": 1641133945000,
        "originatingLocationInvestigationDueDate": 1641133945000,
        "dateResourcesDeployed": 1641133945000,
        "dateEscalationReportRequested": 1641133945000
      },
      "impactedProducts": [
        "PRODUCT_ID"
      ],
      "potentiallyImpactedProducts": [
        "PRODUCT_ID",
        "PRODUCT_ID"
      ],
      "impactedLocations": {
        "locationId": "LOCATION_ID",
        "toIdType": "companyLocationMasterData",
        "locationType": "INTERNAL",
        "locationContact": "edavis"
      },
      "potentiallyImpactedLocations": [
        {
          "locationId": "LOCATION_ID",
          "toIdType": "companyLocationMasterData",
          "locationType": "INTERNAL",
          "locationContact": "edavis"
        }
      ],
      "isEscalated": true,
      "aptEscalationReportBox": {
        "addAttachment": [
          {
            "fileSize": "5mb",
            "fileName": "aptEscalationReportBox1",
            "requestIdentifier": "REQUEST_IDENTIFIER_ID",
            "visibilityType": "Public"
          },
          {
            "fileSize": "5mb",
            "fileName": "aptEscalationReportBox2",
            "requestIdentifier": "REQUEST_IDENTIFIER_ID",
            "visibilityType": "Public"
          }
        ]
      },
      "relatedProcesses": [
        {
          "processId": "PROCESS_ID",
          "processType": "incident"
        }
      ],
      "aptCommentBox": [
        {
          "aptComment": {
            "commentText": "add DSI.",
            "visibilityType": "Public"
          },
          "addAttachment": [
            {
              "fileSize": "5mb",
              "fileName": "File1",
              "requestIdentifier": "REQUEST_IDENTIFIER_ID",
              "visibilityType": "Public"
            }
          ]
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
        "eventName": "agile-process-teams:add-external-manufacturing-incident:v3",
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
### Edit Base State  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "newBaseState": "UnderInvestigation"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
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
### Edit Partner and Impact Information  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
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
    "partnerLocationId": "LOCATION_ID",
    "responsiblePartyAtPartner": "COMMENT_ID",
    "currentlyAssignedPartnerUsers": [
      "PARTNER_USER_ID"
    ],
    "directSupplierImpact": {
      "businessImpact": "Business Impact",
      "businessPriority": "HIGH",
      "impactedDepartments": [
        "CUSTOMER_SERVICE"
      ],
      "highPriorityReasons": [
        "Reason1"
      ],
      "financialImpact": 164113394500,
      "dateSupplyImpacted": 1641133945000,
      "originatingLocationInvestigationDueDate": 1641133945000,
      "dateResourcesDeployed": 1641133945000,
      "dateEscalationReportRequested": 1641133945000
    },
    "impactedProducts": "PRODUCT_ID",
    "potentiallyImpactedProducts": [
      "PRODUCT_ID",
      "PRODUCT_ID"
    ],
    "impactedLocations": [{
      "locationId": "LOCATION_ID",
      "toIdType": "companyLocationMasterData",
      "locationType": "Internal",
      "locationContact": "edavis"
    }],
    "potentiallyImpactedLocations": [
      {
        "locationId": "LOCATION_ID",
        "toIdType": "companyLocationMasterData",
        "locationType": "Internal",
        "locationContact": "edavis"
      }
    ],
    "referenceIdentifiers": [
      {
        "referenceTransactionType": "BILL OF LADING",
        "value": "FZ-1896155146"
      }
    ],
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Re-assigning to Jen",
        "visibilityType": "Internal"
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
        "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
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
### Edit with Initial Response  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "externalManufacturingResponse": {
      "initialResponseInformation": "Initial response from supplier."
    },
    "submitInitialResponse": true
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
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
### Edit with Final Response  
Python  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"

request_header = "{'Authorization': 'Basic YOUR_TOKEN', 'Content-Type': 'application/json'}"

request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "externalManufacturingResponse": {
      "finalResponseInformation": "Final response comment from manufacturer."
    },
    "submitFinalResponse": true
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:edit-external-manufacturing-incident:v3",
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
    "eventName": "agile-process-teams:copy-external-manufacturing-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "createdByPartner": false,
    "aptBusinessObjectSummary": "Tracking replacement order",
    "copyGeneralInfo": true,
    "copyPartnerInfo": true,
    "copyMaterialInfo": true,
    "copyImpactInfo": false,
    "copyReferenceIds": true,
    "copyRelatedProcesses": false
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:copy-external-manufacturing-incident:v1",
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
    "eventName": "agile-process-teams:close-external-manufacturing-incident:v2",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "resolutionType": "RESOLVED",
    "originatingLocation": [
      {
        "originatingLocationId": "LOCATION_ID",
        "toIdType": "companyLocationMasterData"
      }
    ],
    "aptCommentBox": {
      "aptComment": {
        "commentText": "Order received. Signed off by Receiving Manager on 23 Aug 2021",
        "visibilityType": "public"
      },
      "addAttachment": [
        {
          "fileName": "ORDER_1896155146_approved_RECEIVED 23-AUG",
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
        "eventName": "agile-process-teams:close-external-manufacturing-incident:v2",
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
    "eventName": "agile-process-teams:reopen-external-manufacturing-incident:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID",
    "aptCommentBox": {
      "aptComment": {
        "commentText": "INC-4098 closed prematurely - reopening to finalize record.",
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
        "eventName": "agile-process-teams:reopen-external-manufacturing-incident:v1",
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
    "eventName": "agile-process-teams:submit-external-manufacturing-incident-to-partner:v1",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
  },
  "payload": {
    "id": "ITEM_ID"
  }
}

result = requests.request("POST", url, headers=request_header, data=request_body)
```
The response from SCWM
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:submit-external-manufacturing-incident-to-partner:v1",
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
    "eventName": "agile-process-teams:read-externalManufacturingIncident:v4",
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
