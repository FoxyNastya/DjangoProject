from django.core.management.base import BaseCommand
from .models import Client


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = Client(fullname='John Lennon', email='john@example.com',
                    phonenum='secret', address='address', regdate='2024-01-11')
        client.save()
        self.stdout.write(f'{client}')
