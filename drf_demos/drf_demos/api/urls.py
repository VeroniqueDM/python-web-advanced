from django.urls import path

from drf_demos.api.views import ProductsListView

urlpatterns = (
    path('products/', ProductsListView.as_view(), name='products list'),
)