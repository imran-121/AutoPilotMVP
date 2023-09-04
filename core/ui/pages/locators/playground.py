from selenium.webdriver.common.by import By


class PlaygroundLocators:
    FIRST_NAME = (By.XPATH, "//div[@id='root']//input[@name='FirstName']")
    LAST_NAME = (By.XPATH, "//div[@id='root']//input[@name='LastName']")
    EMAIL = (By.XPATH, "//div[@id='root']//input[@name='Email']")
    PHONE_NUMBER = (By.XPATH, "//div[@id='root']//input[@name='PhoneNumber']")
    RADIO_BUTTON_MALE = (By.XPATH, "//input[@type='radio' and @name='Gender' and @value ='Male']")
    RADIO_BUTTON_FEMALE = (By.XPATH, "//input[@type='radio' and @name='Gender' and @value ='<Female>']")
   
    VACANCY_DROPDOWN = (By.XPATH, "//select[@name='Vacancy']")
    FILE_UPLOAD =  (By.XPATH, "//input[@name='myfile']")
    
    DATA_AGREEMENT = (By.XPATH, "//input[@name='Agreement']")
    
    SUBMIT_BUTTON = (By.XPATH, "//input[@name='submitbutton']")