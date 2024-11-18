# APT-SCWM API Quickstart

This quickstart covers:

1. Creating a direct supplier incident using the APT-SCWM API
2. Using the response data to add a comment to the created incident   

*This example uses Python version 3.10 or later entering commands in a Python terminal.*  

**To follow along with the example, open your preferred Python terminal and use a single session through the entire process.**  

## Create Your Request  


### Request Body  

For this example, create the request body first.  In its simplest form, the request body contains a header and a payload and conforms to this format:
```
{
  "header":{},
  "payload":{}
}
```
**Type or copy the following into your Python terminal, replacing necessary values**  
```
request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
    "appName": "agile-process-teams",
    "dataspace": "default"
    },
  "payload": {
    "aptBusinessObjectSummary": "Incomplete shipment received.",
    "aptBusinessObjectDescription": "Several packages missing or damaged.",
    "deviationType": "UNPLANNED",
    "materialType": "FINISHED_GOOD",
    "materialSubtype": "SHIPPED",
    "materialProblem": "SHORT_SHIPMENT_RECEIVED",
    "isEscalated": False,
    "createdByPartner": False,
    "isSubmittedToPartner": False,
    "directSupplierImpact": {
      "businessImpact": "Business Impact",
      "businessPriority": "HIGH"
    }
  }
}
```
This creates a dictionary object containing the `header` and `payload` elements discussed earlier.  Make any necessary changes before submitting the request.  

For example, change the priority of this incident from `HIGH` to `MEDIUM`.  To change this value, reference the `businessPriority` item.  To reach this value, reference the `directSupplierImpact` element of the `payload`.  

**Type or copy the following into your Python terminal, replacing necessary values**
```
request_body.get('payload').get('directSupplierImpact').update({'businessPriority': 'MEDIUM'})
```
Use the `.get()` method for each element in our tree that we wish to access.  The `.update()` method allows changing a value by referencing its key.
Use care to include the braces `{}` when updating an item.  

Take a moment to add your `ownerId` and `processNetworkId` values using the method outlined above.  
Some sample code is below as a hint:  
```
# establish a couple of variables for convenience later
ownerId = "YOUR_OWNER_ID"
network_id = "YOUR_PROCESS_NETWORK_ID"

request_body.get('header').update({'ownerId': owner_id})
request_body.get('header').update({'processNetworkId': network_id})
```

### Request Header
APT-SCWM uses tokens for authentication. For single interactive requests, use a short-lived bearer token, which lasts for an hour, or a longer-lived token for automated processes.  The token is a string that contains 'user:password' in Base64 encoding.

**Type or copy the following into your Python terminal, replacing necessary values**  
```
method = 'Basic'
token = 'YOUR_TOKEN_HERE'
request_headers = {"Authorization": "{0} {1}".format(method, token), "Content-Type": "application/json"}
```
The resulting `headers` variable will look similar to:  
`{'Authorization': 'Basic YOUR_TOKEN_HERE', 'Content-Type': 'application/json'}`  

You are free to use any method you wish to create the request header.  APT-SCWM requires at a minimum an `Authorization` item containing a method and a token along with a `Content-Type` of `application/json`.

## Package Your Request  
At this point you should have a request body, request header, and made all required modifications using Python dictionary methods.  APT-SCWM requires requests formatted as JSON (JavaScript Object Notation).  

Until now, we have been using a Python terminal without any additional packages.  It's time to add the JSON library so we can translate our dictionary into a format accepted by APT-SCWM.  The JSON library is included in the Python installation by default, so no extra installations are required.  

If you wish to verify your request prior to submission, use the json.dumps() method of the json library against your existing request_body dictionary.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
import json
print(json.dumps(request_body, indent=4, sort_keys=False))
```
The response is similar to:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident:v3",
        "ownerId": "YOUR_OWNER_ID",
        "processNetworkId": "YOUR_PROCESS_NETWORK_ID",
        "appName": "agile-process-teams",
        "dataspace": "default"
    },
    "payload": {
        "aptBusinessObjectSummary": "Incomplete shipment received.",
        "aptBusinessObjectDescription": "Several packages missing or damaged.",
        "deviationType": "UNPLANNED",
        "materialType": "FINISHED_GOOD",
        "materialSubtype": "SHIPPED",
        "materialProblem": "SHORT_SHIPMENT_RECEIVED",
        "isEscalated": false,
        "createdByPartner": false,
        "isSubmittedToPartner": false,
        "directSupplierImpact": {
            "businessImpact": "Business Impact",
            "businessPriority": "MEDIUM"
        }
    }
}
```  
Note that your `False` values have been converted to `false` according to the JSON specification.  Convert the dictionary to a JSON string for submission.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
request_body_json = json.dumps(request_body)
```
Note that we have omitted the `indent=4, sort_keys=False` options from the `json.dumps()` command that we included in the print statement.  We used these for clarity when printing, but are not necessary when creating our JSON string.

## Send Request
Once the request header and request body are complete the request is ready to submit.  
This requires a URL for the APT-SCWM environment. Contact your administrator for this information.  
APT-SCWM uses an event driven API that communicates using the POST verb for all API calls.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
import requests
url = "URL_FROM_YOUR_ADMINISTRATOR"
result = requests.request("POST", url, headers=request_header, data=request_body_json)
```
An example successful response:
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-direct-supplier-incident-response:v3",
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

## Response Handling

The `id` in a successful response payload is the identifier of the created incident. Notice that the response is a JSON object that is converted to a string for transmission. To work with this data, convert it to a Python dictionary.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
response_json = json.loads(result.text)
incident_id = response_json.get('payload').get('id')
```

## Add Incident Comment

The APT-SCWM shared API contains processes for adding, editing, or listing comments for incidents along with other utility functions.  The header of this request body is slightly different (in this case only the `eventName` changes) and uses the same authorization configuration as the previous request.  
If you are building or modifying your requests programmatically, use the `ITEM_ID` created in the previous step.  The JSON library allows using `json.loads(string)` to create a dictionary from an existing JSON object and then use the `json.dumps(dictionary)` to convert the modified dictionary back to a JSON object.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
comment_request = {
  "header": {
    "appName": "agile-process-teams",
    "dataspace": "default",
    "eventName": "agile-process-teams:add-comment-for-incident:v1",
    "headerVersion": 1,
    "ownerId": "YOUR_OWNER_ID",
    "processNetworkId": "YOUR_PROCESS_NETWORK_ID"
    },
  "payload": {
    "processId": "my_incident_id",
    "processType": "directSupplierIncident",
    "aptCommentBox":{
      "aptComment":{
        "commentText": "Please provide a list of missing items and we will replace them.",
        "visibilityType": "Public"
      }
    }
  }
}
```
Use the `.update()` method to update the `ITEM_ID`.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
comment_request.get('header').update({'ownerId': owner_id})
comment_request.get('header').update({'processNetworkId': network_id})

comment_request.get('payload').update({'processId': incident_id})
```
After making the desired modifications, convert the dictionary to a JSON string and send the request.  

**Type or copy the following into your Python terminal, replacing necessary values**  
```
comment_request_json = json.dumps(comment_request)  
comment_result = requests.request("POST", url, headers=request_header, data=comment_request_json)
```
The response:  
```
{
    "header": {
        "headerVersion": 1,
        "eventName": "agile-process-teams:add-comment-for-incident-response:v1",
        "ownerId": "YOUR_OWNER_ID",
        "isErr": false,
        "errCode": "200_OK",
        "licensePlate": "LICENSE_PLATE_ID"
    },
    "payload": {
        "id": "COMMENT_ID"
    }
}
```
## Read the details of your newly created incident


Use the previously stored incident id to retrieve details about the incident.
Use the same methods outlined above to generate a request similar to the following:
```
read_request = {
   "header": {
       "headerVersion": 1,
       "eventName": "agile-process-teams:read-directSupplierIncident:v3",
       "ownerId": "YOUR_OWNER_ID",
       "appName": "agile-process-teams",
       "dataspace": "default",
       "processNetworkId": "YOUR_PROCESS_NETWORK_ID"
   },
   "payload": {
       "id": "COMMENT_ID"
   }
}
```
Prepare and send your request.  
```
read_request.get('header').update({'ownerId': owner_id})
read_request.get('header').update({'processNetworkId': network_id})
read_request.get('payload').update({'id': incident_id})

...

read_request_json = json.dumps(read_request)  
read_result = requests.request("POST", url, headers=request_header, data=read_request_json)
```
The response provides the complete record for the incident:
```
{
"header": {
	"headerVersion": 1,
	"eventName": "agile-process-teams:read-directSupplierIncident-response:v3",
	"ownerId": "YOUR_OWNER_ID",
	"isErr": false,
	"errCode": "200_OK",
	"licensePlate": "LICENSE_PLATE_ID"
},
"payload": {
	"createdByUserId": "YOUR_OWNER_ID",
	"schemaVersion": 3,
	"data": {
		"aptBusinessObjectSummary": "Kinaxis - Late: PO, Exception ID: MY_EXCEPTION_ID",
		"aptBusinessObjectDescription": "Order: MY_ORDER_ID",
		"responsibleDepartmentAtPartner": "CONTRACT_MANAGEMENT",
		"responsibleDepartmentAtCompany": "SUPPLY_CHAIN",
		"businessPriority": "HIGH",
		"incidentType": "MATERIAL_SHORTAGE",
		"otherIncidentType": "Purchase Order Discrepancy",
		"aptBusinessObjectImpactsLocationMasterData": [],
		"currentlyAssignedPartnerUsersId": [
			"YOUR_OWNER_ID"
		],
		"resolutionDueDate": 1661817600000,
		"referenceIdentifiers": [
			{
				"referenceTransactionType": "PO_NUMBER",
				"value": " Order: MY_ORDER_ID"
			}
		],
		"response": {},
		"responsiblePartyAtPartnerUserId": "MY_PARTNER_ID",
		"responsiblePartyAtCompanyUserId": "MY_USER_ID",
		"currentlyAssignedCompanyUsersId": [
			"MY_USER_ID"
		],
		"primaryPartnerLocationId": "MY_LOCATION_ID",
		"fkProcessNetworkId": "YOUR_PROCESS_NETWORK_ID",
		"aptBusinessObjectId": "USPT-10101",
		"aptBusinessObjectIntegerIdentifier": 10101,
		"createdByPartner": false,
		"aptBusinessObjectAssignedToCompanyPartnerMasterData": {
			"partnerId": "MY_PARTNER_ID",
			"toIdType": "partnerMasterData"
		},
		"followerId": [
			"MY_USER_ID"
		],
		"aptBusinessObjectNumericIdentifierDerivedField": "10101",
		"businessPriorityDerivedField": "c",
		"incidentConclusion": {
			"resolutionType": "NOT_AN_ISSUE",
			"isReoccuring": true,
			"dateClosed": 1661528887906,
			"finalRootCause": "OTHER"
		},
		"advanceMetrics": {
			"timeToClose": 3,
			"closedOnTime": true
		}
	},
	"dataVersion": 2,
	"ownerId": "YOUR_OWNER_ID",
	"objectType": "agile-process-teams:directSupplierIncident",
	"currentBaseState": "Closed",
	"schemaId": "agile-process-teams:directSupplierIncident",
	"lastUpdatedByUserId": "YOUR_OWNER_ID",
	"contextualOwnerId": "YOUR_OWNER_ID",
	"id": "ITEM_ID",
	"lastUpdatedDateTime": 1661528888803,
	"creationDateTime": 1661276934457
}
}
```

## Next steps
You will need a mechanism to create or update your payload data whether it is stored in a file or submitted at runtime and discarded.  
You will also need a method to retain the `id` number for each incident you wish to reference.  

## Troubleshooting
Review the [troubleshooting primer](Troubleshooting.md).
