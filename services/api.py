from tastypie.resources import ModelResource
from services.models import Product, Order
from services.authentication import CustomApiKeyAuthentication
import time

class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'product'
        excludes = ["product_type", "price"]
        allowed_methods = ['get']
        authentication = CustomApiKeyAuthentication()

    def dehydrate(self, bundle):
        bundle.data["name"] = bundle.data["name"].upper()
        return bundle


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        allowed_methods = ['get', 'post', 'put']
        authentication = CustomApiKeyAuthentication()
