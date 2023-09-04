import os
import time

from utilities.logger import Logger
from core.ui.pages.base_page import BasePage
from core.ui.pages.locators.playground import PlaygroundLocators
from core.ui.pages.page_urls import PageUrlCollection


class PlayGroundScreen(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver=driver, base_url=base_url)
        self.URL = base_url + PageUrlCollection.PLAYGROUND_PAGE
        self.logger = Logger(self.__class__.__name__)
        
        
    def set_user_names_and_email(self,first_name, last_name, email, phone_number, gender):
        self.set_text(locator=PlaygroundLocators.FIRST_NAME, value=first_name)
        self.set_text(locator=PlaygroundLocators.LAST_NAME, value=last_name)
        self.set_text(locator=PlaygroundLocators.EMAIL, value=email)
        self.set_text(locator=PlaygroundLocators.PHONE_NUMBER, value=phone_number)
        self.set_gender_radio_button(gender=gender)
        
        
    def set_gender_radio_button(self,gender):
        if gender == 'm':
           self.find_element_and_click(locator=PlaygroundLocators.RADIO_BUTTON_MALE)
        elif(gender == 'f'):
            self.find_element_and_click(locator=PlaygroundLocators.RADIO_BUTTON_FEMALE)
        else:
            message = "Please provide a valid value for gender radio button"
            self.logger(message)
            raise Exception(message)
            
            
    def set_vacancy_and_cv(self,vacancy_type, cv_path):
        self.select_option_from_dropdown(locator=PlaygroundLocators.VACANCY_DROPDOWN
                                         , option_value= vacancy_type)
    
        self.upload_file(locator=PlaygroundLocators.FILE_UPLOAD
                         , file_path= os.getcwd() + cv_path )
        
        
    def check_data_process_agreement(self):
        self.find_element_and_click(locator=PlaygroundLocators.DATA_AGREEMENT)
        
        
    def click_submit_button(self):
        self.find_element_and_click(locator=PlaygroundLocators.SUBMIT_BUTTON)
        
        
    def click_to_alert_box(self):
        alert = self.get_driver().switch_to.alert
        alert.accept()

        
        
        
    