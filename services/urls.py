from django.conf.urls import url, include
from tastypie.api import Api
from services.api import ProductResource, OrderResource

v1_api = Api(api_name='v1')
v1_api.register(ProductResource())
v1_api.register(OrderResource())

urlpatterns = [url(r'^api/', include(v1_api.urls))]
