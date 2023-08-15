import json

from django.core.management import BaseCommand
from django.db import connection

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        with connection.cursor() as cursor:
            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")
        with open("catalog_data.json", "r", encoding="windows-1251") as file:
            data = json.load(file)
            for item in data:
                if item["model"] == "catalog.category":
                    Category.objects.create(
                        name=item["fields"]["name"],
                        description=item["fields"]["description"]
                    )
