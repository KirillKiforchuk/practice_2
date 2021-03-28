# practice_2
Test app for the second lab
***
### Quickstart
##### Pre-Installation requirements
- git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- python 3.9 (https://www.python.org/downloads/)
- pip (comes with python)
##### Install

1. Project setup
    - clone project from github
    ```
    $ git clone https://github.com/KirillKiforchuk/practice_2.git
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
    - go to http://localhost:8001
    - you should see Swagger app with the `/ping` and `/free_text` endpoints
