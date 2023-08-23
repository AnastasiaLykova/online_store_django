from django.core.management import BaseCommand

from catalog.models import Product, Category

import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('catalog_data.json', 'r', encoding='utf-8') as file:
            catalog_data = json.load(file)

        category_for_create = []
        product_for_create = []
        id_category = 0
        for item in catalog_data:
            if item['model'] == 'catalog.category':
                id_category += 1
                category_for_create.append(Category(id=id_category, **item['fields']))
        Category.objects.bulk_create(category_for_create)

        id_product = 0
        for item in catalog_data:
            if item['model'] == 'catalog.product':
                id_product += 1
                product_for_create.append(Product(id=id_product, category=category_for_create[item['fields']['category']-1],
                                                  name=item['fields']['name'],
                                                  description=item['fields']['description'],
                                                  preview=item['fields']['preview'],
                                                  price=item['fields']['price']
                                                  ))
        Product.objects.bulk_create(product_for_create)
