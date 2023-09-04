import time
from pytest_bdd import scenarios, given, when, then, parsers
# from web_framework.kiosk.common.Constants.UI.commands import CommandsConstants
from utilities.logger import Logger
# from utilities.type_converter import TypeConverter
# from web_framework.kiosk.pages.Locators.commands_screen_locators import CommandsScreenPageLocators
# from web_framework.kiosk.pages.Locators.dash_board_screen_locators import DashBoardsScreenPageLocators
# from web_framework.kiosk.pages.Locators.top_level_dash_board_screen import TopLevelDashBoardScreenLocators
# from web_framework.kiosk.pages.page_type import PageType

import pytest

scenarios('../features/playground.feature')
logger = Logger("test_commands_screen")

    
@given('User navigates to web ui playground url')
def navigate_to_page(session_playground_page):
    pass
    
@when(parsers.cfparse('Fills up the personal details as {first_name} {last_name} {email} {phone_number} and {gender}'))
def add_personal_details(session_playground_page,first_name, last_name, email, phone_number, gender):
    session_playground_page.set_user_names_and_email( first_name = first_name
                                                     , last_name = last_name
                                                     , email=email
                                                     , phone_number = phone_number
                                                     , gender = gender )
    
    
@when(parsers.cfparse('Provides job application details as {vacancy_type} and {cv_path}'))
def add_job_details(session_playground_page, vacancy_type, cv_path):
    session_playground_page.set_vacancy_and_cv( vacancy_type = vacancy_type
                                               , cv_path = cv_path )   
    
@when('Agrees with the terms of personal data processing')
def accept_personal_data_agreement(session_playground_page):
    session_playground_page.check_data_process_agreement()

    
@then('Cliks on submit button')
def hit_submit_button(session_playground_page):
    session_playground_page.click_submit_button()
    session_playground_page.click_to_alert_box()


    