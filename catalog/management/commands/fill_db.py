from django.conf import settings
from catalog.models import Product, Category
from django.core.management import BaseCommand, call_command
from django.db import IntegrityError, ProgrammingError


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        Product.objects.all().delete()
        Category.objects.all().delete()

        fixtures_path = settings.BASE_DIR.joinpath('data.json')
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
