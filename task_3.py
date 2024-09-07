from task_1 import logger

from faker import Faker

@logger
def get_fake_email() -> str:
    fake_email = Faker().email(domain='yandex.ru')
    return fake_email


get_fake_email()