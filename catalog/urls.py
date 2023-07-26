from django.urls import path
from catalog.views import home, contacts

app_name = "catalog"

urlpatterns = [
    path('', home),
    path('contacts', contacts)
]
