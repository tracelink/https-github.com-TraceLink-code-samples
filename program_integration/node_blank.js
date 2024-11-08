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
    query: `mutation takeAction}}($action: String!, $payload: JSON!)
{
    genericActionCall(action: $action, payload: $payload)
    {
    result
    __typename
    }
}`,
    variables:
    {}
  })
};
request(options, function (error, response) {
  if (error) throw new Error(error);
  console.log(response.body);
});
