from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='admin@mail.ru',
            username='admin',
        )
        user.set_password('07052001')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        self.stdout.write(self.style.SUCCESS('User successfully created'))