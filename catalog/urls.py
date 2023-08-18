from django.urls import path
from catalog.views import home, contacts, product

app_name = "catalog"

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contact'),
    path('product/<int:id>/', product, name='product')
]
