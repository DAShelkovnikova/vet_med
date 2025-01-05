from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import (
    CategoryDetailView,
    CategoryListView,
    ContactsView,
    ProductDetailView,
    ProductListView,
    SearchView,
    CompanyListView,
    AccountListView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("", CategoryListView.as_view(), name="category_list"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
    path("category/product/", ProductListView.as_view(), name="product_list"),
    path(
        "category/product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"
    ),
    path("search/", SearchView.as_view(), name="search"),
    path("company/", CompanyListView.as_view(), name="company_list"),
    path("account/", AccountListView.as_view(), name="account_list"),

]
