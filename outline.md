## Session Outline

### Introduction to REST APIs
`DevAsc blueprint associated with this portion of the session:`
> 2.1 Construct a REST API request to accomplish a task given API documentation
>
> 2.5 Troubleshoot a problem given the HTTP response code, request and API documentation
>
> 2.7 Utilize common API authentication mechanisms: basic, custom token, and API keys
> 
Lecture: 15 minutes
- Introduction to REST APIs
- What is REST?
- Authentication and Authorization
- Components of REST APIs
- Provide overview of Postman (Using Webex APIs as an example)

Hands-on Lab: 30 minutes **All Done in Postman**
- Provide an API documentation for a simple REST API https://api.chucknorris.io/
- Students will use Postman to make a GET request to the API
  - They will pull a list of categories 
  - They will pull a random joke from a specific category
  - They will pull a random joke using a query text search
- Bring in Authentication and Authorization
  - Using Webex APIs
  - Students will navigate to the API documentation and generate a token from their personal account
  - Students to create a new room using the APIs and add us 3 to the room
  - Student to POST a message in that room using the API
  - Students to navigate POSTMAN export option and get CURL command equivalent to posting a message in the same room


## Introduction to Python
`DevAsc blueprint associated with this portion of the session:`
> 2.9 Construct a Python script that calls a REST API using the requests library
> 
> 3.1 Construct a Python script that uses a Cisco SDK given SDK documentation
> 
> 3.9 Construct code to perform a specific operation based on a set of requirements and given API reference documentation such as these:
> - 3.9.a Obtain a list of network devices by using Meraki, Cisco DNA Center, ACI, Cisco SD-WAN, or NSO.
> - 3.9.b Manage spaces, participants, and messages in Webex.
> - 3.9.c Obtain a list of clients / hosts seen on a network using Meraki or Cisco DNA Center.

Lecture: 20 minutes
- Introduction to Python
- Why Python?
- Python Basics (variables, data types, loops, functions, etc.)
- focus on looping through dicts
- Python Libraries (requests, json, etc.)
- Python virtual environments
- Understand SDKs in relation to APIs

Hands-on Lab: 60 minutes
- Students will be handed a list of Meraki Devices in a JSON format
- Students will be given a python skeleton code, asked to complete the relevant parts to pratice the concepts we discussed above
- Students will be asked to use the requests library to make a GET request to the Meraki API to pull a list of devices-
  - Students will be asked to use the requests library to make a POST request to the Meraki API to 
  - Get organization ID
  - Create a new network
  - claim devices
  - add devices to network 
- **Use Case # 1:** we will give them a scenario, they are to leverage the Meraki SDK to build out a new site in their organization, 
  - we will only provide them with comments in the python file, no code will be provided
  - we will provide the documentation needed to complete the task
  - they need to create a virtual env 
  - they can pip install as part of the learning process to get the SDK
  - **optional** netbox devices and ask them to pull the devices from netbox and push them to Meraki

## Introduction to model-driven programmability
`DevAsc blueprint associated with this portion of the session:`
> 3.8 Apply concepts of model driven programmability (YANG, RESTCONF, and NETCONF) in a Cisco environment
> 
> 5.10 Interpret the results of a RESTCONF or NETCONF query
> 
> 5.11 Interpret basic YANG models

Lecture: 20 minutes
- Introduction to model-driven programmability
- What is YANG?
- explain the structure of YANG models
- exploring YANG models with pyang
- underestanding RESTCONF and NETCONF
- Introduction to yangsuite

Hands-on Lab: 60 minutes
- Students will be given a set of instruction to traverse yang models using yangsuite
- Students will connect to device using NETCONF and pull a set of data using the NCClient library
- Students will connect to device using RESTCONF and pull a set of data using the requests library or Postman

## Introduction to Docker
`DevAsc blueprint associated with this portion of the session:`
> 4.6 Interpret contents of a Dockerfile
>
> 4.7 Utilize Docker images in local developer environment
> 
> 4.11 Utilize Bash commands (file management, directory navigation, and environmental variables)


**Quinn/Palmer** build this out?
**Quinn/Palmer** What other topics should we cover? aligning to BP and cert
