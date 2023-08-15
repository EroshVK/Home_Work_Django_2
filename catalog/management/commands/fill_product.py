import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")
        with open("catalog_data.json", "r", encoding="windows-1251") as file:
            data = json.load(file)
            for item in data:
                if item["model"] == "catalog.category":
                    Product.objects.create(
                        name=item["fields"]["name"],
                        description=item["fields"]["description"],
                        image="",
                        category=Category.objects.get(pk=item["fields"]["category"]),
                        price=item["fields"]["price"],
                        creation_date=item["fields"]["creation_date"],
                        last_change_date=item["fields"]["last_change_date"]
                    )
