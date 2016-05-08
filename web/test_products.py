from api.models.product import Product
from api.models.images import Image
from api.models.seo_block import SeoBlock
from api.models.category import Category

image = Image.objects.all()[0]
category = Category.objects.get(url='1_2')
seo_block = SeoBlock.objects.get(pk=1)

for i in range(0, 10000):
    product = Product()
    product.title = 'Test Product Title {}'.format(i)
    product.url = 'test_product_title {}'.format(i)
    product.price = 100 + i
    product._title_image = image
    product.category = category
    product.seo_block = seo_block
    product.is_sale = False
    product.is_preorder = False
    product.is_new = False
    product.enabled = True
    product.save()
