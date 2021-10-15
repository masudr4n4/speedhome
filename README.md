# SPEED HOME

### Pre-requisite:
Create a separate env for running this project.
activate the env in the terminal then 
run :```pip install -r requirements.txt```
make sure you have setup for java and allure in your system.
### Run test
run ```behave```<br>
This will run all the testcases we have in our features folder
if you want to see the result with reports run this command.<br>
```behave -f allure_behave.formatter:AllureFormatter -o reports```<br>
After running that it will generate a new reports folder.
run ```allure serve reports```
to see test reports