from django.urls import path
from catalog.views import ProductListView, ContactsView, ProductDetailView
from catalog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = "catalog"

urlpatterns = [
    path('', ProductListView.as_view(), name='home'),
    path('contacts/', ContactsView.as_view(), name='contact'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_pk'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
