from selene import browser, have
import os
from Part_2.locators.locators import StudentRegistrationFormLocators
from Part_2.data.users import Users


class RegistrationPage2:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")

    def register(self, user: Users):
        browser.element(StudentRegistrationFormLocators.FIELD_FIRST_NAME).type(user.first_name)
        browser.element(StudentRegistrationFormLocators.FIELD_LAST_NAME).type(user.last_name)
        browser.element(StudentRegistrationFormLocators.FIELD_USER_EMAIL).type(user.email)
        browser.element(StudentRegistrationFormLocators.GENDER_FEMALE).click()
        browser.element(StudentRegistrationFormLocators.FIELD_MOBILE_NUMBER).type(user.mobile_number)
        browser.element(StudentRegistrationFormLocators.FIELD_DATE_OF_BIRTH).click()
        browser.element(StudentRegistrationFormLocators.DATE_PICKER_MONTH).all(
            StudentRegistrationFormLocators.VALUE_MONTH)[1].click()
        browser.element(StudentRegistrationFormLocators.DATE_PICKER_YEAR).element(
            StudentRegistrationFormLocators.VALUE_YEAR).click()
        browser.element(StudentRegistrationFormLocators.DATE_PICKER_DAY).click()
        browser.element(StudentRegistrationFormLocators.FIELD_SUBJECTS).type(user.subject).press_enter()
        browser.element(StudentRegistrationFormLocators.CHECK_BOX_HOBBIES_SPORTS).click()
        browser.element(StudentRegistrationFormLocators.BUTTON_PICTURE_SELECTION).set_value(
            os.path.abspath('Part_2/resources/file_1.txt'))
        browser.element(StudentRegistrationFormLocators.FIELD_CURRENT_ADDRESS).type(user.current_address)
        browser.element(StudentRegistrationFormLocators.FIELD_STATE).click()
        browser.element(StudentRegistrationFormLocators.STATE_UTTAR_PRADESH).hover().click()
        browser.element(StudentRegistrationFormLocators.FIELD_CITY).click()
        browser.element(StudentRegistrationFormLocators.CITY_MERRUT).hover().click()
        browser.element(StudentRegistrationFormLocators.BUTTON_SUBMIT).click()

    def should_have_registered(self, user: Users):
        formatted_date = user.date_of_birth.strftime('%d %B,%Y')
        browser.all(StudentRegistrationFormLocators.VALUE_MODAL_WINDOW_RESULT).should(have.texts(
            'Student Name', f'{user.first_name} {user.last_name}',
            'Student Email', user.email,
            'Gender', 'Female',
            'Mobile', user.mobile_number,
            'Date of Birth', formatted_date,
            'Subjects', user.subject,
            'Hobbies', 'Sports',
            'Picture', 'file_1.txt',
            'Address', user.current_address,
            'State and City',
            'Uttar Pradesh Merrut'))
