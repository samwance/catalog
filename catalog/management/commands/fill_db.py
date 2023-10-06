from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone

class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        # Очистка таблицы Category и Product
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создание объектов категорий
        category1 = Category.objects.create(name='Category 1', description='Description 1')
        category2 = Category.objects.create(name='Category 2', description='Description 2')

        # Создание объектов продуктов
        Product.objects.create(name='Product 1', description='Description 1', category=category1, purchase_price=10, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 2', description='Description 2', category=category2, purchase_price=20, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 3', description='Description 3', category=category1, purchase_price=30, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 4', description='Description 4', category=category2, purchase_price=40, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 5', description='Description 5', category=category1, purchase_price=50, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 6', description='Description 6', category=category2, purchase_price=60, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 7', description='Description 7', category=category1, purchase_price=70, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 8', description='Description 8', category=category2, purchase_price=80, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 9', description='Description 9', category=category1, purchase_price=90, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 10', description='Description 10', category=category2, purchase_price=100, created_at=timezone.now(), updated_at=timezone.now())
