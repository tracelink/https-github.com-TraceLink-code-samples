import requests
import json

url = "https://valvir-opus.tracelink.com/api/graphql"

payload = "{\"query\":\"query readDocumentReview($id: String!, $type: String!)\\n{\\n    genericGetObject(type: $type, id: $id)\\n    {\\n        ... on ALL_RETURNS{\\n            ... on DocumentReview {\\n                id\\n                currentBaseState\\n                currentSubState\\n                data {\\n                    aptBusinessObjectId\\n                    aptBusinessObjectSummary\\n                    aptBusinessObjectDescription\\n                    responsibleDepartmentAtCompany\\n                    responsibleDepartmentAtPartner\\n                    businessPriority\\n                    createdByPartner\\n                    productId\\n                    aptBusinessObjectImpactsLocationMasterData{\\n                        locationType\\n                        locationContact\\n                        partnerLocationId\\n                    }\\n                    __typename\\n                }\\n                aptBusinessObjectContainsComment{\\n                    to {\\n                        ... on AptComment{\\n                            id\\n                            data{\\n                                commentText\\n                                visibilityType\\n                            }\\n                        }\\n                    }\\n                }\\n                aptBusinessObjectContainsAttachment{\\n                    to {\\n                        ... on AptAttachment{\\n                            data{\\n                                fileName\\n                                fileSize\\n                                visibilityType\\n                                fileS3Location\\n                            }\\n                        }\\n                    }\\n                }\\n                __typename\\n            }\\n            __typename\\n        }\\n    }    \\n}\",\"variables\":{\"type\":\"DocumentReview\",\"id\":\"YOUR_ID\"}}"
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

# schema_json = raw_json.get('data').get('genericActionCall')  # drill into object
schema_json = raw_json.get('data').get('genericGetObject') # use this for getObjectCalls
# api_json = json.loads(schema_json.get('result'))  # load the result object to json

# for genericGetObject, use schema_json. for genericActionCall, use api_json.
print(json.dumps(schema_json, indent=4, sort_keys=False))  # 'pretty print' the result
