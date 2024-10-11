# Incorporating GraphQL into your automation solutions #  
The GraphQL code samples provided contain the payloads necessary to make requests to the Opus platform.  
Use your preferred programming language to construct the HTTP request for the desired action.  Your ```Headers``` section contains the relevant authorization data for your environment.  
Incorporate the payload into the body of your request.  The request text must be converted to a JSON string for inclusion.  
For example:  
### Original Query ###  
Query:  
```
mutation AddIncident($action: String!, $payload: JSON!) {
  genericActionCall(action: $action, payload: $payload) {
    result
    __typename
  }
}
```  
Variables  
```
{
"action": "Addincident",
"payload":{
    "aptBusinessObjectSummary": "Printing error",
    "aptBusinessObjectDescription":"Label printing offset",
    "businessPriority":"LOW",
    "incidentType":"LABEL_COMPLIANCE_ERROR",
    "resolutionDueDate":"1736613281000" // 11 Jan 2025
    }
}
```  
Add your converted strings to a payload.  Create a single object containing query and variables objects.  
### Python ###  
```
import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"mutation AddIncident($action: String!, $payload: JSON!)\\n{\\n    genericActionCall(action: $action, payload: $payload)\\n    {\\n    result\\n    __typename\\n    }    \\n}\",\"variables\":{\"action\": \"Addincident\",\"payload\": {\"aptBusinessObjectSummary\":\"Printing error\",\"aptBusinessObjectDescription\": \"Label printing offset on package\",\"businessPriority\": \"LOW\",\"incidentType\":\"LABEL_COMPLIANCE_ERROR\",\"resolutionDueDate\": \"1736613281000\"}}}"
headers = {
  'Authorization': 'Basic YOUR_AUTH_TOKEN',
  'Content-Type': 'application/json',
  'Dataspace': 'default',
  'companyId': 'YOUR_COMPANY_ID',
  'processNetworkId': 'YOUR_NETWORK_ID'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```
### Node.js ###  
```
var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://valvir-opus.tracelink.com/api/graphql',
  'headers': {
    'Authorization': 'Basic YOUR_AUTH_TOKEN',
    'Content-Type': 'application/json',
    'Dataspace': 'default',
    'companyId': 'YOUR_COMPANY_ID',
    'processNetworkId': 'YOUR_NETWORK_ID'
  },
  body: JSON.stringify({
    query: `mutation AddIncident($action: String!, $payload: JSON!)
{
    genericActionCall(action: $action, payload: $payload)
    {
    result
    __typename
    }    
}`,
    variables:
    {"action": "Addincident",
    "payload":
    {"aptBusinessObjectSummary":"Printing error",
    "aptBusinessObjectDescription": "Label printing offset on package",
    "businessPriority": "LOW",
    "incidentType":"LABEL_COMPLIANCE_ERROR",
    "resolutionDueDate": "1736613281000"}}
  })
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
```  
In this example, Opus automatically assigns Business Object and Id values.  The response will contain both values and be similar to the example below:  
```
{
  "data": {
      "genericActionCall": {
          "result": "{\"aptBusinessObjectId\":\"USPT-0000\",\"id\":\"aa0a00aa-0a00-0aaa-0a00-000000a000000\"}",
          "__typename": "ReadResult"
      }
  }
}
```  
The ```id``` item allows subsequent calls to update, copy, close, and reopen this new record.  
