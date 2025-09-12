
from selene import browser, be, have
from selenium.webdriver.chrome.options import Options
import os



def test_submitting_the_form(windows_size):
    options = Options()
    # Запуск браузера без графического интерфейса:
    # options.add_argument('--headless')

    browser.config.driver_options = options
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element('#firstName').type('Juliya')
    browser.element('#lastName').type('Smykova')
    browser.element('#userEmail').type('julieta-petrova@yandex.ru')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').type('9111177777')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').all('option')[1].click()
    browser.element('.react-datepicker__year-select').element('option[value="1990"]').click()
    browser.element('.react-datepicker__day--020').click()
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').type(os.path.abspath('file_1.txt'))
    browser.element('[placeholder="Current Address"]').type('Adress')
    browser.element('[class=" css-1hwfws3"]').click()
    browser.element('//div[contains(text(), "Uttar Pradesh")]').hover().click()
    browser.element('[class=" css-yk16xz-control"]').click()
    browser.element('//div[contains(text(), "Merrut")]').hover().click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-title').should(have.text('Thanks for submitting the form'))
    browser.all('.table-responsive tbody tr td').should(have.texts(
        'Student Name', 'Juliya Smykova', 'Student Email', 'julieta-petrova@yandex.ru', 'Gender', 'Female',
        'Mobile', '9111177777', 'Date of Birth', '20 February,1990', 'Subjects', 'Maths', 'Hobbies', 'Sports',
        'Picture', 'file_1.txt', 'Address', 'Adress', 'State and City', 'Uttar Pradesh Merrut'))
    browser.element('#closeLargeModal').click()


