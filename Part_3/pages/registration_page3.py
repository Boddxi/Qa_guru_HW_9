from selene import browser, have
from Part_3.locators.locators import SimpleRegistrationLocators
from Part_3.data.users import SimpleUsers


class SimpleRegistrationPage3:

    def open(self):
        browser.open("https://demoqa.com/text-box")

    def register(self, user: SimpleUsers):
        browser.element(SimpleRegistrationLocators.FIELD_FULL_NAME).type(user.full_name)
        browser.element(SimpleRegistrationLocators.FIELD_USER_EMAIL).type(user.email)
        browser.element(SimpleRegistrationLocators.FIELD_CURRENT_ADDRESS).type(user.current_address)
        browser.element(SimpleRegistrationLocators.FIELD_PERMANENT_ADDRESS).type(user.permanent_address)
        browser.element(SimpleRegistrationLocators.BUTTON_SUBMIT).click()

    def should_have_registered(self, user: SimpleUsers):
        browser.all(SimpleRegistrationLocators.FIELD_RESULT).should(have.texts(
            f'Name:{user.full_name}\n'
            f'Email:{user.email}\n'
            f'Current Address :{user.current_address}\n'
            f'Permananet Address :{user.permanent_address}'))
