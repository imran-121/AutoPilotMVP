# AutoPilotMVP
This is a test automated framework developed in python (3.8.0), the goal here is to design the architecture of the framework not test case coverage.
## Application Under test
We are considering this sample page under test (https://vladimirwork.github.io/web-ui-playground/) and I have named it as **PlayGroundScreen** and automated only one happy test case touching all of the fields

## Approach and Patterns Used
The basic approach is to develope a centralized framework to address all kinds of automation platforms(web/mobile) and layers(api/ui/db), following are the basic patterns that I have utilized so far
  * Page Factory Pattern
  * Behaviour Driven Developement (BDD)
  * Driver Approach (Combine diffrent pages to make drivers, here I had only one page but showed a room in the arcitecture)

## Tools and Technologies
Below are the major naming 
  * Python 3.8.0
  * Selenium 3.12.0
  * Pytest-Bdd 6.1.1
  * Bash Scripting
  * Allure Reporting 2.13.2
  * Logging Library
  * VS Code as IDE and plugins

## Architecture
The framework is divided into 5 components which work togeather
1. **config** component contains all of the configurational scripts and files like logger, package requirements and basic platform configurations
2. **core** contains the reuseable backend logic for test cases like page object model and is totally segreated for ui/api/db
3. **tests** contains the definitions of test cases in the form of features and steps files, following BDD approach
4. **utilities** are the common methods used across the framework
5. **results** component contains all of the framework outputs like reports, logs etc


## Flow of execution
Below is the folw of execution
1. To execute test cases you just need to run the **start.sh** file, which is in the root folder. This will install python packages and triggers the **main.py** file
2. **main.py** file is the entry point of framework, its purpose is to triggers configurations, execute the test cases and generate report. Arrage, Act and Assert
3. **pytest.ini** will be triggred by main.py to do the pytest configuration
4. **conftest.py**  will be triggred by pytest.ini and it will compile fixtures and pre-steps for test case execution





