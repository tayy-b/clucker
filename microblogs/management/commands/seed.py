from django.core.management.base import BaseCommand, CommandError
from faker import Faker
import random
from microblogs.models import User


class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.faker =  Faker('en_GB')

    def handle(self,*args,**options):
        for i in range(100):
            self.user = User.objects.create_user(
                first_name =self.faker.first_name(),
                last_name=self.faker.last_name(),
                username = '@' + self.faker.first_name() + self.faker.last_name() + str(random.randint(1000,9999)),
                email=self.faker.email(),
                password=self.faker.password(),
                bio=self.faker.sentence(nb_words=10,variable_nb_words=True)
            )
