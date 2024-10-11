var request = require('request');
var options = {
  'method': 'POST',
  'url': 'https://valvir-opus.tracelink.com/api/graphql',
  'headers': {
    'Authorization': 'Basic YOUR_TOKEN',
    'Content-Type': 'application/json',
    'Dataspace': 'default',
    'companyId': 'YOUR_COMPANY_ID',
    'processNetworkId': 'YOUR_PROCESS_NETWORK_ID'
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
