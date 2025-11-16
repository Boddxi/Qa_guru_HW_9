import dataclasses
from datetime import date


@dataclasses.dataclass
class Users:
    first_name: str
    last_name: str
    email: str
    mobile_number: str
    date_of_birth: date
    subject: str
    current_address: str


student = Users(first_name='Juliya', last_name='Smykova', email='julieta-petrova@yandex.ru',
                mobile_number='9111177777', date_of_birth=date(1990, 2, 20), subject='Maths', current_address='Adress')
