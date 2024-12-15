from django.core.management.base import BaseCommand

from Task3app.models import User


class Command(BaseCommand):
    help = "Удаление пользователя по его ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='ID пользователя')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.delete()
            self.stdout.write(f'Пользователь с ID {pk} удалён!')
        else:
            self.stdout.write(f'Пользователь с ID {pk} не найден!')