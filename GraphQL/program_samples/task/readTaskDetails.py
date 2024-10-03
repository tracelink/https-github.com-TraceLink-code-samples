import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"query ReadTaskDetails($id: String!, $type: String!)\\n{\\n    genericGetObject(type:$type, id: $id)\\n    {\\n        ... on ALL_RETURNS{\\n            ... on Task{\\n                id\\n                data{\\n                    templateName\\n                    aptBusinessObjectDescription\\n                    isAddRemoveSubtaskAllowed\\n                    businessPriority\\n                    responsibleDepartmentAtCompany\\n                }\\n                taskContainsSubTask{\\n                    to{\\n                        subType\\n                        objectType\\n                    }\\n                }\\n                __typename\\n            }\\n            __typename\\n        }\\n        __typename\\n    }    \\n}\",\"variables\":{\"type\":\"Task\",\"id\":\"YOUR_ID\"}}"
headers = {
  'Authorization': 'Basic YOUR_TOKEN',
  'Content-Type': 'application/json',
  'Dataspace': 'default',
  'companyId': 'YOUR_COMPANY_ID',
  'processNetworkId': 'YOUR_PROCESS_NETWORK_ID'
}

response = requests.request("POST", url, headers=headers, data=payload)

raw_json = json.loads(response.text)  # load the text result to into json

# schema_json = raw_json.get('data').get('genericActionCall')  # drill into object
schema_json = raw_json.get('data').get('genericGetObject') # use this for getObjectCalls
# api_json = json.loads(schema_json.get('result'))  # load the result object to json

# for genericGetObject, use schema_json. for genericActionCall, use api_json.
print(json.dumps(schema_json, indent=4, sort_keys=False))  # 'pretty print' the result
