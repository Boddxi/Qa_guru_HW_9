import dataclasses


@dataclasses.dataclass
class SimpleUsers:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


student = SimpleUsers(full_name='Juliya Smykova', email='julieta-petrova@yandex.ru',
                      current_address='Address1', permanent_address='Address2')
