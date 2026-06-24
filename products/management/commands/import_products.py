import pandas as pd

from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        df = pd.read_csv("products_data.csv")

        Product.objects.all().delete()

        for _, row in df.iterrows():

            Product.objects.create(
                product_name=row["product_name"],
                product_description=row["product_description"],
                category=row["category"],
                tags=row["tags"]
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Products imported successfully"
            )
        )