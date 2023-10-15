from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, contact, ProductView, ProductCreateView, ProductListView, ProductUpdateView, \
    ProductDeleteView, VersionDeleteView, VersionCreateView, VersionUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('products/<int:pk>/', ProductView.as_view(), name='product'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('list/', ProductListView.as_view(), name='product_list'),
    path('update/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/create_version/', VersionCreateView.as_view(), name='version_create'),
    path('update_version/', VersionUpdateView.as_view(), name='version_update'),
    path('delete_version/', VersionDeleteView.as_view(), name='version_delete'),

]
