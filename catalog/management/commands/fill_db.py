from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Fill the database with sample data'

    def handle(self, *args, **options):
        # Очистка таблицы Category и Product
        Category.objects.all().delete()
        Product.objects.all().delete()

        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1;")
            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1;")

        # Создание объектов категорий
        category1 = Category.objects.create(name='Category 1', description='Description 1')
        category2 = Category.objects.create(name='Category 2', description='Description 2')

        # Создание объектов продуктов
        Product.objects.create(name='Product 1', description='Description 1', image='products/product1.jpg', category=category1, purchase_price=10, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 2', description='Description 2', image='products/product2.jpg', category=category2, purchase_price=20, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 3', description='Description 3', image='products/product3.jpg', category=category1, purchase_price=30, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 4', description='Description 4', image='products/product4.jpg', category=category2, purchase_price=40, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 5', description='Description 5', image='products/product5.jpg', category=category1, purchase_price=50, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 6', description='Description 6', image='products/product6.jpg', category=category2, purchase_price=60, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 7', description='Description 7', image='products/product7.jpg', category=category1, purchase_price=70, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 8', description='Description 8', image='products/product8.jpg', category=category2, purchase_price=80, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 9', description='Description 9', image='products/product9.jpg', category=category1, purchase_price=90, created_at=timezone.now(), updated_at=timezone.now())
        Product.objects.create(name='Product 10', description='Description 10', image='products/product10.jpg', category=category2, purchase_price=100, created_at=timezone.now(), updated_at=timezone.now())

        self.stdout.write(self.style.SUCCESS('Successfully filled the database'))