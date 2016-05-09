from api.models.product import Product
from api.models.images import Image
from api.models.seo_block import SeoBlock
from api.models.category import Category
import random

images = Image.objects.all()

categories = Category.objects.get(url='sub_cat_1'), Category.objects.get(url='sub_cat_2')
seo_block = SeoBlock.objects.get(pk=1)

for i in range(0, 500):
    product = Product()
    product.title = 'Test Product Title {}'.format(i)
    product.url = 'test_product_title {}'.format(i)
    product.price = 100 + i
    product.title_image = images[random.randrange(len(images) - 1)]
    product.category = categories[random.randrange(2)]
    product.seo_block = seo_block
    product.is_sale = random.randrange(2) == 1
    product.is_preorder = random.randrange(2) == 1
    product.is_new = random.randrange(2) == 1
    product.enabled = True
    product.save()
    print('create product {}'.format(i))
