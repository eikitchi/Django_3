from django.core.management import BaseCommand

from main.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [
            {
                "name": "GoogleWatch",
                "description": "",
                "category": "Smartwatch",
                "price": 10000,
                "date_create": "2023-05-10 19:00",
                "date_change": "2023-05-10 19:30"
            },
            {
                "name": "AppleWatch",
                "description": "",
                "category": "Smartwatch",
                "price": 20000,
                "date_create": "2023-05-10 20:00",
                "date_change": "2023-05-10 21:10"
            },
        ]

        products_objects = []
        for item in product_list:
            products_objects.append(Product(**item))

        Product.objects.bulk_create(products_objects)