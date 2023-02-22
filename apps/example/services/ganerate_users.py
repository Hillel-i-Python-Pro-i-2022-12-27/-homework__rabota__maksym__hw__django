from typing import NamedTuple
from collections.abc import Iterator
from random import randint
from django.utils.crypto import get_random_string
from faker import Faker


class User(NamedTuple):
    login: str
    email: str
    password: str

    def __str__(self):
        return f"{self.login} {self.email} {self.password}"

    __repr__ = __str__


fake = Faker()


def generate_user() -> User:
    login = f"{fake.unique.first_name()}"
    password = get_random_string(randint(8, 16))
    domain = fake.domain_name()
    return User(login=login, email=f"{login}{randint(100, 999)}@{domain}", password=password)


def generate_users(amount: int = 10) -> Iterator[User]:
    for _ in range(amount):
        yield generate_user()
