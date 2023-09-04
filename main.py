"""
    This is the entery point of the framework.
    It's purpose is to 
        1) trigger intial configuration
        2) execute the pytest
        3) generate reports
"""

import os
from logging import INFO, config
from os.path import dirname as up
import subprocess
from utilities.configuration_manager import ConfigurationManager
from utilities.logger import Logger

VERSION = "1.0.0"

logger = Logger(os.path.basename(__file__))

ConfigurationManager.init("DEFAULT")

def setup_configurations():
    """
    This function sets the configuration set
    """
    ConfigurationManager.init("DEFAULT")
    global ALLURE_REPORT_DIR 
    global ALLURE_RESULT_DIR
    ALLURE_REPORT_DIR = ConfigurationManager.get_config_value("allure_final_report_path")
    ALLURE_RESULT_DIR = ConfigurationManager.get_config_value("allure_result_path")
    
def run_tests():
    """
    This fundtion triggres the pytest
    """
    try:
        # Define the pytest command with allure reporting
        pytest_cmd = [
            "python",
            "-m",
            "pytest",
            "--alluredir=" + ALLURE_RESULT_DIR
            # Add other pytest options and test paths as needed
        ]
        subprocess.run(pytest_cmd)
    except Exception as ex:
        logger.debug(f"Exception whilst trying to run tests. {ex}")

def generate_allure_report():
    """
    For generating allure reports from allure results
    """
    try:
        allure_cmd = ['.\\.allure\\allure-2.21.0\\bin\\allure.bat', "generate" ,ALLURE_RESULT_DIR,"--clean", "-o", ALLURE_REPORT_DIR]
        subprocess.run(allure_cmd,check=True)
    except Exception as ex:
        logger.debug(f"Exception whilst trying to generate allure reports from allure results. {ex}")


def print_graphic_version():
    print('')
    print(r'        <<<<===================================================================>>>>        ')
    print(f'              Test Automation Framework Execution Started  (version {VERSION})')
    print(r'        <<<<===================================================================>>>>        ')
    print('')
    
# results\allure-reports
def main():
    setup_configurations()
    print_graphic_version()
    run_tests()
    generate_allure_report()
    
    
if __name__ == "__main__":
    main()
