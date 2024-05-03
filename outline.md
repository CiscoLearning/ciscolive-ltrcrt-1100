# Session Outline

## Introduction to REST APIs (Quinn/Kareem)

`DevAsc blueprint associated with this portion of the session:`
> 2.1 Construct a REST API request to accomplish a task given API documentation
> 2.5 Troubleshoot a problem given the HTTP response code, request and API documentation
> 2.7 Utilize common API authentication mechanisms: basic, custom token, and API keys

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

## Introduction to Git/Gitlab (Kareem: Slides, Lab: Palmer)

`DevASC blueprint associated with this portion of the session:`

> 1.8 Utilize common version control operations with Git
>  - 1.8.a Clone
>  - 1.8.b Add/remove
>  - 1.8.c Commit
>  - 1.8.d Push / pull
>  - 1.8.e Branch
>  - 1.8.f Merge and handling conflicts
>  - 1.8.g diff

Lecture: 10 minutes

- Introduction to Git
  - 

## Introduction to Python (Kareem)

`DevAsc blueprint associated with this portion of the session:`

> 2.9 Construct a Python script that calls a REST API using the requests library
> 3.1 Construct a Python script that uses a Cisco SDK given SDK documentation
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

## Introduction to Docker (Quinn)

`DevAsc blueprint associated with this portion of the session:`

> 4.6 Interpret contents of a Dockerfile
> 4.7 Utilize Docker images in local developer environment
> 4.11 Utilize Bash commands (file management, directory navigation, and environmental variables)

Lecture: 15 minutes

- What and what of containerization?
- Introduction to Docker
- Dockerfile syntax and commands
- Environment variables, packages, and layers
- Validation and testing
- Docker container management

Hands-on Lab: 60 minutes

- Students will be given a sample Dockerfile to build a vanilla Linux container
- Students will build and run the container, entering and exiting the shell of the running container
- Students will look at logs of the running container and manage its running state through the use of Docker commands, showing the separation of the container from the host
- Students will learn how to map volumes into a container to show file access between host and container
- **Use Case #1:** We will give them a scenario in which they have to take the API knowledge from the Postman section and create a container that will send Chuck Norris jokes to Webex
  - we will provide them with a skeleton code file with comments on where they need to add in a few components (URLs or parsers for the JSON)
  - we will provide a skeleton Dockerfile with missing pieces for either verbs or commands to be run
  - they will need to add in the appropriate ENV vars to allow communication to Webex messaging
  - they will need to validate and build the container
  - they will need to run the container and validate that a Chuck Norris joke is sent to the Webex room


## TODO

- :white_circle: Palmer to validate Gitlab instance per pod
- :white_circle: Palmer to validate HTTP proxy for web access into pod
- :white_check_mark: Quinn to validate Postman (Free) allows for requests and code extraction via lightweight HTTP client
- :white_circle: Kareem to send over presentation for Git to Palmer
- :white_circle: Quinn to append tree of folder structure to this outline
- :white_circle: Kareem to create recurring meeting