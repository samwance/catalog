from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import IndexView, contact, ProductView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contact, name='contact'),
    path('products/<int:pk>/', ProductView.as_view())
]