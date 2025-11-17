from selene import browser
from Part_1.utils.resourses import get_resource_path


class RegistrationPage:

    def open(self):
        browser.open("https://demoqa.com/automation-practice-form")

    def fill_first_name(self, f_name):
        browser.element('#firstName').type(f_name)

    def fill_last_name(self, l_name):
        browser.element('#lastName').type(l_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self):
        browser.element('label[for="gender-radio-2"]').click()

    def fill_mobile_number(self, number):
        browser.element('#userNumber').type(number)

    def fill_date(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').all('option')[1].click()
        browser.element('.react-datepicker__year-select').element('option[value="1990"]').click()
        browser.element('.react-datepicker__day--020').click()

    def select_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def select_hobbies(self):
        browser.element('label[for="hobbies-checkbox-1"]').click()

    def load_picture(self):
        file_path = get_resource_path('file_1.txt')
        browser.element('#uploadPicture').set_value(file_path)

    def fill_adress(self, adress):
        browser.element('[placeholder="Current Address"]').type(adress)

    def choice_state(self):
        browser.element('[class=" css-1hwfws3"]').click()
        browser.element('//div[contains(text(), "Uttar Pradesh")]').hover().click()

    def choice_city(self):
        browser.element('[class=" css-yk16xz-control"]').click()
        browser.element('//div[contains(text(), "Merrut")]').hover().click()

    def click_submit(self):
        browser.element('#submit').click()

    @property
    def modal_window(self):
        return browser.element('#example-modal-sizes-title-lg')

    @property
    def info_about_the_registered_user(self):
        return browser.all('.table-responsive tbody tr td')
