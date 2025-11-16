from Part_3.pages.application import app
from Part_3.data.users import student


def test_simple_registration_form(windows_size):
    app.simple_registration.open()
    app.simple_registration.register(student)
    app.simple_registration.should_have_registered(student)
