# This is mainly an Internship given by codingAtom
I mainly took the devops path option and the aim of this internship is the building of simple health-dashboard with endpoints to check if the app is been running properly.
**CodingAtom is a plateform that offers various internship opportunities to student to make them work on their skills and be ready for reel world work**
For this simple app i gonna mainly used FastApi to handle the backend since i gonna create a simple app i will do not alots of dependecies 
1. We need to create python Virtual environment for that  on linux i gonna used the **Command:** ` python3 -m venv .venv`
2. let activiate the python3 environment we creatd using the **Command:**`source .venv/bin/activate`.
3. Let i will install  the following dependecies using the pip package manager 
4. **Commands:** `pip install fastapi uvicorn httpx pytest pytandic-settings`
5. Then stored all our requirements into a file call **requirements.txt** using the command `pip freeze > requirements.txt`
6. Then create our app folder using the **Command**:`mkdir app && cd app`
7.  Inside our app let create our config.py the file that will used our pydantic-settings package modules using the simple command `touch config.py`
8.  Inside our config.py we gonna define the app name,version and actual dev environment. Also consider it will used the .env file in it base configs on deployement
9.  Let add a .gitignore file before we continue the  initial a Github public repo for our work. Create the gitignore file out of the app directory using the command  `touch .gitignore ~/Documents/health-dashboard/ ` on my machine path
10. Inside the gitignore let add our .venv folder so that those package should be push to the github repo 
11. With all set up can push our code into a github repository in peace starting from the path ~/Documents/health-dashboard/ using git vscode extension 
12. Now let us move to the main part of our application that is creating a file with name main.py using the command `touch  main.py ~/Documents/health-dashboard/app`
13. Let move on to the test part of our application  for that we simple gonna create a folder with name tests which outside of the app directory which means is path is created using the **Commands:** `mkdir tests ~/Documents/health-dashboard`  then move on to the test folder uses **cd tests**
14. Inside the test folder used the command touch and create a new file mainly `touch test_main.py` the let start adding our test inide the file and this file mainly used the pytest dependency for it work 
15. After writing the test_main.py file we can then run our app just for testing the server in local using the **Command:** `uvicorn app.main:app --relaod` 
16. Then will the running server add the screenshot images 
17. Then we can move to the **MultiStage Dockerfile** which is mainly our second task while using a Multistage Dockerfile this mainly to build and light image for our server so that we can have a very-light  docker-image to deploy 
18. Let create our Dockerfile `touch Dockerfile ~/Documents/health-dashboards` 
19. Now we need to write the Dockerfile contain since i using FastApi for this app i will used the docker-images **python3.12-slim** as base image builder.
20. In writhing Dockerfile we mainly using the command **apt-get update && apt-get upgrade** which is the main standard here instend of using classic apt update 
21. Then after correcting the errors inside the Dockerfile we can launch the Docker build process using the **Command:** `docker build  -t health-dashboard .`
22. When the docker container is been build we then used the command **docker images** to list all our local docker images where we gonna find a container with name **health-dashboard:latest** and with a small size 
23. Now let run the command using the docker **Command :** `docker run -p 8000:8000 health-dashboard` 
24. Now let check our docker images size using the **Command:** `docker images | grep health-dashboard` i will add the screenshoy of it here
25. 
26. 