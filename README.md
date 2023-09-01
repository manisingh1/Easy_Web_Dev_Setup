This repo describes a base repo for a flask app. 

It has the following features:
- Flask for the backend.
- Utilizes docker containers, docker compose, and makefile for easy and consistent environment.
- Utilizes a Redis Cache, to improve performance of API requests.
- Utilizes Swagger / OpenAPI for documentation and clickable interface for visualizing the api.
- A single makefile command starts the flask app, redis container, and allows connecting a VSCode debugger (when in debug mode).

To Setup:

Install Docker:
[Docker Desktop Link](https://docs.docker.com/desktop/install/mac-install/)

Install the python environment
```sh
  pip install virtualenv
  python3 -m venv env
  source env/bin/activate
  ```

To Run:
There are four different environments available:
- Production:
```
make prod
```

- Debug (for connecting VSCode Debugger):
```
make debug
```
Once the containers start, press F5 in VSCode to connect the debugger

- Test (Runs pytest tests):
```
make test
```

- Debug Test (for connecting VSCode Debugger with tests):
```
make debug-test
```
Once the containers start, press F5 in VSCode to connect debugger


See the app running at:
[http://127.0.0.1:8001/](http://127.0.0.1:8001/)


To stop the app:
ctrl+c 

and, to bring everything down and remove containers:
```
make down
```

Helpful link for setting up the docker environment:
- https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/


