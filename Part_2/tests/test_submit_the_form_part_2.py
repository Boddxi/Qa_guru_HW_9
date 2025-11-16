from Part_2.pages.registration_page2 import RegistrationPage2

from Part_2.data.users import student


def test_student_registration_form(windows_size):
    registration_page = RegistrationPage2()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
