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