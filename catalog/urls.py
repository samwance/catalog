from django.urls import path
from django.views.decorators.cache import cache_page, never_cache

from catalog.apps import CatalogConfig
from catalog.views import IndexView, contact, ProductDetailView, ProductCreateView, ProductListView, ProductUpdateView, \
    ProductDeleteView, VersionDeleteView, VersionCreateView, VersionUpdateView, categories

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('products/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/update/', never_cache(ProductUpdateView.as_view()), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/create_version/', VersionCreateView.as_view(), name='version_create'),
    path('update_version/', VersionUpdateView.as_view(), name='version_update'),
    path('delete_version/', VersionDeleteView.as_view(), name='version_delete'),
    path('categories/', categories, name='categories'),

]
