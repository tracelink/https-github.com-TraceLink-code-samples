import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"query getProductMasterData($action: String!, $regulatoryItemCodeValue: String!, $regulatoryItemCodeType: String!)\\n{\\n    genericActionCall(\\n        action: $action,\\n        payload:\\n        {\\n            regulatoryItemCodeValue: $regulatoryItemCodeValue,\\n            regulatoryItemCodeType: $regulatoryItemCodeType\\n            }\\n    )\\n    {\\n        result\\n        __typename\\n    }\\n}\",\"variables\":{\"action\":\"Getproductbyitemcode\",\"regulatoryItemCodeValue\":\"YOUR_PRODUCT_ID\",\"regulatoryItemCodeType\":\"ITEM_CODE_TYPE\"}}"
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
