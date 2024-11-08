# Formatting API Requests  

## HTTP Request URL

Your administrator can provide the URL you will use for submitting requests.  
These requests will use the **POST** verb.

## Request Header  

To authenticate with the APT application, include the following in the header of your HTTP request:  
A **Token** that is your authorization to make requests.  
A **Content Type** that identifies the format of the data passed.  In this case it will be *application/json*.  

## Payload  

This is the data submitted to the application for processing, which contains a header and body.

### Header  

The request body header identifies how APT processes your request.  All items below are required:

| Name                 | Type    | Description                                                            | Value                                      |
| -------------------- | ------- | ---------------------------------------------------------------------- | ------------------------------------------ |
| `headerVersion`      | integer | The version identifier for the request                                 | `1`                                        |
| `eventName`          | string  | The fully qualified name of the request event.                         | See [event name mapping](../EventNames.md)    |
| `ownerID`            | string  | The Owner company associated with the request.                         | See [authentication](../authentication.md) |
| `processNetworkId`   | string  | The network within the Owner company containing the process.           | See [authentication](../authentication.md) |
| `appName`            | string  | The application that owns the event.                                   | `"agile-process-teams"`                    |
| `dataspace`          | string  | The dataspace inside within the environment where the request is made. | `"default"`                                |   

### Body
A properly constructed JSON object is required as the payload. You can dynamically create the JSON object at runtime or create a file with the appropriate values to import as needed.

The body parameters change depending on the `eventName` value passed in the body header. Please reference [API documentation](https://opus.tracelink.com/documentation/2021.1/en-US/apt/Content/topics/api/landing_incident_apis.htm?tocpath=Set%20up%20APIs%7CIncident%20process%20APIs%7C_____0) for more information on each event type. The [samples folder](../payload_samples) contains example payload bodies for each event type.  

An example of a complete payload body for adding a direct supplier incident:
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
        "aptBusinessObjectSummary": "Product from manufacturer does not meet specifications.",
        "directSupplierImpact": {
        "businessPriority": "HIGH"
        }
    }
}
```

# Next
Review [event name mapping](eventNames.json) for each event type.  
Follow [the quickstart](Quickstart.md) for an example using the APT-SCWM API.
