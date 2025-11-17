from selene import have
from Part_1.pages.registration_page import RegistrationPage


def test_student_registration_form(windows_size):
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Juliya')
    registration_page.fill_last_name('Smykova')
    registration_page.fill_email('julieta-petrova@yandex.ru')
    registration_page.fill_gender()
    registration_page.fill_mobile_number('9111177777')
    registration_page.fill_date()
    registration_page.select_subjects('Maths')
    registration_page.select_hobbies()
    registration_page.load_picture()
    registration_page.fill_adress('Address')
    registration_page.choice_state()
    registration_page.choice_city()
    registration_page.click_submit()
    registration_page.modal_window.should(have.text('Thanks for submitting the form'))
    registration_page.info_about_the_registered_user.should(have.texts(
        'Student Name', 'Juliya Smykova', 'Student Email', 'julieta-petrova@yandex.ru', 'Gender', 'Female',
        'Mobile', '9111177777', 'Date of Birth', '20 February,1990', 'Subjects', 'Maths', 'Hobbies', 'Sports',
        'Picture', 'file_1.txt', 'Address', 'Address', 'State and City', 'Uttar Pradesh Merrut'))
