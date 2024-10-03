import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"mutation AddDocumentReview($action: String!, $payload: JSON!)\\n{\\n    genericActionCall(action: $action, payload: $payload)\\n    {\\n    result\\n    __typename\\n    }    \\n}\",\"variables\":{\"action\": \"Adddocumentreview\",\"payload\":{\"aptBusinessObjectSummary\":\"New Document Review using graphQL and postman\",\"aptBusinessObjectDescription\":\"Adding a document review using Python and graphQL\",\"businessPriority\":\"LOW\",\"approvalDueDate\": \"1736613281000\"}}}"
headers = {
  'Authorization': 'Basic YOUR_TOKEN',
  'Content-Type': 'application/json',
  'Dataspace': 'default',
  'companyId': 'YOUR_COMPANY_ID',
  'processNetworkId': 'YOUR_PROCESS_NETWORK_ID'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
raw_json = json.loads(response.text)  # load the text result to into json

schema_json = raw_json.get('data').get('genericActionCall')  # drill into object
# schema_json = raw_json.get('data').get('genericGetObject') # use this for getObjectCalls
api_json = json.loads(schema_json.get('result'))  # load the result object to json

# for genericGetObject, use schema_json. for genericActionCall, use api_json.
print(json.dumps(api_json, indent=4, sort_keys=False))  # 'pretty print' the result
