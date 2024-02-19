# Late Night Entry

## THINGS TO DO:

### By Jay
- [ ] Install Postman [Download Link](https://www.postman.com/downloads/)
- [ ] Learn the flask basics [Learn Here](https://flask.palletsprojects.com/en/3.0.x/quickstart/#)
- [ ] Learn about REST API and different HTTP methods. [Basic Intro Learn Here](https://testsigma.com/blog/different-types-of-apis-and-protocols-2022-updated/#2_REST_Representational_State_Transfer)
- [ ] Create a request with HTTP get method in flask and sent the response hello in the json format, [use quickstart and learn how to send data in json fomrat]
  - [ ] Path of request should be "/userId"
  - [ ] Return should be {"userId":1}
  - [ ] test:
    - [ ] Start Server [see how to run the project section]
    - [ ] Open Postman [check a tutorial if want to send the get request from postman]
    - [ ] Send a get request with "/userId"
    - [ ] check the output is correct or not
- [ ] Create a request with HTTP post method that includes {name:"xyz"} this name can be different for each request access the request object and send name in json object [Learn Here](https://flask.palletsprojects.com/en/3.0.x/quickstart/#the-request-object)
  - [ ] Object to sent in request is {"name":"xyz"}
  - [ ] Return should be {"name":"xyz"}
  - [ ] test:
    - [ ] Start Server [see how to run the project section]
    - [ ] Open Postman [check a tutorial if want to send the post request from postman, with body as json]
    - [ ] Send a post request with request body
    - [ ] check the output is correct or not
- [ ] Create a request with HTTP get method that includes "/:userId", learn how to access data from query params
  - [ ] Path will be ":/userId"
  - [ ] Return will be {"userId":[value in query parms]}
  - [ ] test-> same as first task
- [ ] Learn about sessions and how to create them between frontend and backend, how to send data in request headers

### By Jitendra
- [ ] Basic flask and Flask_SQLAlchemy Project setup with tests
- [ ] Create a wiki for the project setup
- [ ] Install and setup basic server, and server db connection.
- [ ] Process for storing the env variable in flask
- [ ] Setup logger and debugging


## How to run the project
1) Create virtual environment, and activate the virtual environment
2) Run "pip install -r requirements.txt" it will install all the dependency
3) Do your all code in server.py file
4) Run flask --app server run
5) Open http://127.0.0.0.1:5000, this is where server will host the application