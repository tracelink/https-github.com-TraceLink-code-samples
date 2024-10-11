# Authentication

This process involves:

1. Obtaining a short-lived token
2. Exhanging the token for a long-lived API key and secret
3. Encoding the API key and secret
4. Formatting a basic authorization header

## Prerequisites

1. You must be able to login to the Opus Platform and access APT-SCWM.

2. Once logged into Opus on your browser, select the desired process. For example, **Direct Supplier Incident**.

![Opus in Browser](images/opus_apt.png)

3. Using the directions below for your designated browser, generate the following values:

- `_store_js_production_token`, a short lived token valid for one session
- `_store_js_production_processNetworkOwnerId`, passed in the [body header](python/FormatRequests.md#header)
- `_store_js_production_processNetworkId`, passed in the [body header](python/FormatRequests.md#header)

### Chrome

From the Chrome menu, navigate to **View** > **Developer** > **Developer Tools**.
Select the **Application** tab from the Developer Tools pane. From the left hand navigation menu, under the storage section, select
**Local Storage** from the dropdown. Then, click `https://opus.tracelink.com`. You should now see a list of key/value pairs. The
values in the screenshot below were redacted.

![Key Value Pairs](images/chrome_apt.png)

### Firefox

From the Firefox menu, navigate to **Tools** > **Web Developer Tools**.
Select the **Storage** tab from the Web Developer Tools pane. From the left hand navigation menu, click **Local Section** and then
`https://opus.tracelink.com`. You should now see a list of key/value pairs. The values in the screenshot below were redacted.

![Key Value Pairs](images/firefox_apt.png)

## Generate API Key and Secret

### Postman

1. Set up a call to `https://valvir-opus.tracelink.com/api/events` with `POST` as the HTTP method.
2. Under the **Authorization** tab select **Bearer Token** as the **Type** and insert `_store_js_production_token`, obtained
from your browser, as the **Token**.

![Postman Token](images/postman_token.png)

3. Click the **Body** tab and use the JSON below. Do not replace any values, including the ownerID. Ensure **raw** and JSON are selected.

```json
{
    "payload": {
        "description": "descJ100"
    },
    "header": {
        "dataspace": "default",
        "appName": "user-admin",
        "headerVersion": 1,
        "eventName": "authorization-manager:generate-apiKeyCredentials:v1",
        "ownerId": "00000000-0000-0000-0000-000000000000"
    }
}
```

![Postman Token](images/postman_body.png)

Here is an example response:

```json
{
  "header": {
    "headerVersion": 1,
    "eventName": "authorization-manager:generate-apiKeyCredentials-response:v1",
    "ownerId": "00000000-0000-0000-0000-000000000000",
    "isErr": false,
    "errCode": "200_OK",
    "licensePlate": "abCdef-0Ab1cD"
  },
  "payload": {
    "apiKey": "XXXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX",
    "apiSecret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  }
}
```

The API key and secret are long-lived, static values that do not expire.

## Encode API Key and Secret

1. Take the values of `apiKey` and `apiSecret` and convert them into a string with the format {{KEY}}:{{SECRET}}, with a colon seperating the two values.

   For example: `a12b3c45d-6e78-90f1-g234-h56i7j890k1l:mn2o3pq4RsTuVwXyZAbc5defghIjklMn`.

2. Use the following command in your terminal window to encode the string: `echo -n 'KEYSECRETSTRING' | base64`

   For example: `echo -n 'a12b3c45d-6e78-90f1-g234-h56i7j890k1l:mn2o3pq4RsTuVwXyZAbc5defghIjklMn' | base64`.
   An example response: `YTEyYjNjNDVkLTZlNzgtOTBmMS1nMjM0LWg1Nmk3ajg5MGsxbDptbjJvM3BxNFJzVHVWd1h5WkFiYzVkZWZnaElqa2xNbg==`.

   Alternatively, you can use an online resource such as https://www.base64encode.org/ to encode your string.

3. This encoded result can now be used in a basic authorization header.
   For example, `authorization: Basic YTEyYjNjNDVkLTZlNzgtOTBmMS1nMjM0LW...bDpjJvM3BxNFJzVHVWd1h5WkFiYzVkZWZnaElqa2xNbg==`.


### Python

```python
import base64

def create_token(api_key, api_secret):
    combine = api_key + ':' + api_secret
    step_two = combine.encode("UTF-8")
    encoded_token = base64.b64encode(step_two).decode("UTF-8")
    auth_header = {"Authorization" : "Basic %s" % encoded_token}
    print(auth_header)
```
