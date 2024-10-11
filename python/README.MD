# Python

This repository provides developers with python code samples for interacting with TraceLink's Agile Process Teams (APT) app.

## Installation

NEEDS UPDATING

## Usage

This code was tested using python 3.10.0.

**The *requests* and *json* modules are required for use.**
Use the **utils.py** file for the following actions:  

- Add your token to the HTTP request header  
- Process the request payload from a JSON object or file  
- Create the payload body  
- Display the completed payload for accuracy prior to submitting  
- Submit your request to APT  


## Requests

All requests have three main components:

- **Request URL**
	- {{protocol}}://{{server}}/api/events  
- **Request header**
	- Authenticates to APT using a token and content type
- **Payload header**
	- Properly routes the request
- **Payload**
	- Provides the details of the request

# Next  

1. Review information on [authentication](../authentication.md).
2. Review [basic request formatting](FormatRequests.md).
3. Follow the [quickstart](Quickstart.md) for an example using the APT-SCWM API.
