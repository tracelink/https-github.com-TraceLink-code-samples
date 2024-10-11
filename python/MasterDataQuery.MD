# Querying Master Data  
The full master data records for a company and its internal locations include the company's headquarters information, identifiers, and location master data on TraceLink. IT system administrators and app developers use these APIs to read the full master data record for their company and internal locations by submitting either regulatory identifier information for the company or location or a query that finds the company or location based on the contents of one or more fields. Additionally, IT system administrators use these APIs to edit the full master data record for their company and internal locations.  

Query master data using the same methods as the incident requests.  

Refer to the [Quickstart](Quickstart.md) walkthrough to prepare your scripting environment and variables.  

## Partner Master Data  
**Type or copy the following into your Python terminal, replacing necessary values**  
```
request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "masterdata-manager:get-partner-by-regulatory-identifier:v1",
    "ownerId": "YOUR_OWNER_ID",
    "dataspace": "default",
    "appName": "masterdata-manager"
  },
  "payload": {
    "regulatoryCompanyIdentifier": "YOUR_PARTNER_ID",
    "regulatoryCompanyIdentifierType": "SGLN"
  }
}
```

## Product Master Data  
**Type or copy the following into your Python terminal, replacing necessary values**  
```
request_body = {
  "header": {
    "headerVersion": 1,
    "eventName": "masterdata-manager:get-partner-by-regulatory-identifier:v1",
    "ownerId": "YOUR_OWNER_ID",
    "dataspace": "default",
    "appName": "masterdata-manager"
  },
  "payload": {
    "regulatoryCompanyIdentifier": "YOUR_PRODUCT_ID",
    "regulatoryCompanyIdentifierType": "SGLN"
  }
}
```

## Company Master Data  
**Type or copy the following into your Python terminal, replacing necessary values**  
```
request_body = {
  "header": {
    "appName": "masterdata-manager",
    "dataspace": "default",
    "eventName": "masterdata-manager:get-company-by-regulatory-identifier:v1",
    "headerVersion": 1,
    "ownerId": "YOUR_OWNER_ID"

  },
  "payload": {
    "regulatoryCompanyIdentifier": "YOUR_COMPANY_ID",
    "regulatoryCompanyIdentifierType": "GLN"
  }
}
```
