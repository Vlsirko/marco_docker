from api.models.product import Product
from api.models.seo_block import SeoBlock
from api.models.category import Category
import random


categories = Category.objects.get(url='1_2'), Category.objects.get(url='3-4')
seo_block = SeoBlock.objects.get(pk=1)

for i in range(0, 500):
    product = Product()
    product.title = 'Test Product Title {}'.format(i)
    product.url = 'test_product_title {}'.format(i)
    product.price = 100 + i
    product.category = categories[random.randrange(2)]
    product.is_sale = random.randrange(2) == 1
    product.is_preorder = random.randrange(2) == 1
    product.is_new = random.randrange(2) == 1
    product.enabled = True
    product.save()
    print('create product {}'.format(i))
