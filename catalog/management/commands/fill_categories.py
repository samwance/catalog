from django.conf import settings
from catalog.models import Category
from django.core.management import BaseCommand, call_command
from django.db import IntegrityError, ProgrammingError


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()

        fixtures_path = settings.BASE_DIR.joinpath('categories.json')
        try:
            call_command('loaddata', fixtures_path)
        except ProgrammingError:
            pass
        except IntegrityError as e:
            self.stdout.write(f'Invalid fixtures: {e}', self.style.NOTICE)
        else:
            self.stdout.write(
                f'Command have been completed successfully',
                self.style.SUCCESS
            )