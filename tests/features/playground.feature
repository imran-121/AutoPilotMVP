Feature: Playground user interface

        @ui
        Scenario Outline: To verify submit button works with valid fields
        Given User navigates to web ui playground url
        When Fills up the personal details as <first_name> <last_name> <email> <phone_number> and <gender>
        And Provides job application details as <vacancy_type> and <cv_path>
        And Agrees with the terms of personal data processing
        Then Cliks on submit button

            Examples:
            |  first_name  | last_name | email               | phone_number | gender | vacancy_type     | cv_path   |
            |  Imran       |    Satti  | ximran786@gmail.com |     1234567  | m      | Business Analyst | \\tests\\test_data\\ui\\imran_test_cv.pdf |


           