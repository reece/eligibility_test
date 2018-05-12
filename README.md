# eligibility_test

Response to a coding challenge

1. Prepare runtime environment
	Step 1: Move contents to ~/eligibility_test
        Step 2: Directory structure should look like ~/eligibility_test/src, ~/eligibility_test/test/ etc.
        Step 3: pip install jsonschema
        Step 4: pip install flask

2. Starting the service
	Step 1: export FLASK_APP=~/eligibility_test/src/eligibility_service.py
        Step 2: python3 -m flask run

3. Command line examples


EXAMPLE 1 : ping 

    pratik@ubuntu:~/test_code/eligibility$ curl -D- http://127.0.0.1:5000/v1/ping
    HTTP/1.0 200 OK
    Content-Type: text/html; charset=utf-8
    Content-Length: 0
    Server: Werkzeug/0.14.1 Python/3.5.2
    Date: Fri, 11 May 2018 03:50:28 GMT


EXAMPLE 2 : config

    pratik@ubuntu:~/test_code/eligibility$ curl -D- http://127.0.0.1:5000/v1/acme/config
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 137
    Server: Werkzeug/0.14.1 Python/3.5.2
    Date: Fri, 11 May 2018 04:01:59 GMT
    
    {"title": "Employee ids", "required": ["employee_id"], "properties": {"employee_id": {"minimum": 0, "type": "number"}}, "type": "object"}


EXAMPLE 3 : successful check 

    pratik@ubuntu: curl -XPOST "http://127.0.0.1:5000/v1/acme/check" -H 'Content-Type: application/json' -d '{"employee_id": 23}'
    {"message": "Success", "eligible": true}


EXAMPLE 4 : unsuccessful check. employee id not found

    pratik@ubuntu:~/test_code/eligibility$ curl -XPOST "http://127.0.0.1:5000/v1/acme/check" -H 'Content-Type: application/json'  -d '{"employee_id": 23345}'
    {"message": "employee_id = 23345 not found", "eligible": false}


EXAMPLE 5 : unsuccessful check. incorrect input format

    pratik@ubuntu:~/test_code/eligibility$ curl -XPOST "http://127.0.0.1:5000/v1/acme/check" -H 'Content-Type: application/json' -d '{"emp_id": 23345,}'
    {"message": "Invalid json input format", "eligible": false}


EXAMPLE 6 : unsuccessful check. required fields not passed

    curl -XPOST "http://127.0.0.1:5000/v1/acme/check" -H 'Content-Type: application/json' -d '{"employee_idadfasdf": 23}'
    {"message": "Input validation failed. Please validate against config", "config": {"properties": {"employee_id": {"minimum": 0, "type": "number"}}, "required": ["employee_id"], "type": "object", "title": "ACME json schema"}, "eligible": false}


EXAMPLE 7 : Unsupported URL on the server

    pratik@ubuntu:~$ curl -D- http://127.0.0.1:5000/v1/acme/asfsdfa
    HTTP/1.0 404 NOT FOUND
    Content-Type: text/html
    Content-Length: 233
    Server: Werkzeug/0.14.1 Python/3.5.2
    Date: Fri, 11 May 2018 05:17:04 GMT
    
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>404 Not Found</title>
    <h1>Not Found</h1>
    <p>The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.</p>


4. Next Steps
	1. Containerize the whole application so that all the dependencies would be in one place
	2. Add a database backend if needed
	3. Better error handling and checks
	4. More test cases
	5. Incorporate Swagger to generate server stubs
	6. Add a deploy script
