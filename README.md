# practice_2
Test app for the second lab
***
### Quickstart
#### Pre-Installation requirements
##### Host-based web service (Linux only)
- git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- python 3.9 (https://www.python.org/downloads/)
- pip (comes with python)
##### Container-based web service
- Docker desktop (Windows OS)
- docker, docker-compose (Linux OS)
#### Install
##### Host-based web service (Linux)
1. Project setup
    - clone project from github
        ```
        $ git clone git@github.com:kiforchuk/practice_2.git
        ```
    - go to the directory with the cloned project and install required packages
        ```
        $ cd practice_2
        $ pip install -r requirements.txt
        ```
1. Web service run
    - go to the directory with project
    - run web service
        ```
        $ honcho start
        ```
    - you should see similar output:
        ```
        18:49:11 web.1  | [2021-03-21 18:49:11 +0200] [17813] [INFO] Starting gunicorn 20.0.4
        18:49:11 web.1  | [2021-03-21 18:49:11 +0200] [17813] [INFO] Listening at: http://0.0.0.0:8001 (17813)
        18:49:11 web.1  | [2021-03-21 18:49:11 +0200] [17813] [INFO] Using worker: aiohttp.GunicornWebWorker
        18:49:11 web.1  | [2021-03-21 18:49:11 +0200] [17815] [INFO] Booting worker with pid: 17815
        ```
    - go to http://0.0.0.0:8001
    - you should see Swagger app with the `/ping` and `/free_text` endpoints
##### Docker container
1. Project setup
    - clone project from github
        ```
        $ git clone git@github.com:kiforchuk/practice_2.git
        ```
2. Web service build and run
    - Windows:
        ```
        > cd practice_2
        > docker build -t lab2 .  
        ```
        Go to docker desktop and build container from image (you must specify port)
   - Linux:
        ```
        $ cd practice_2
        $ docker-compose up      
        ```
