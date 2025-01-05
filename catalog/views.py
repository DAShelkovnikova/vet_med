from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView

from appointment.models import Appointment
from catalog.models import Category, Product, Company, Account


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Product.objects.all()[:5]
        return context


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class SearchView(TemplateView):
    model = Product
    template_name = "catalog/search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        return Product.objects.filter(name__icontains=query)


class CompanyListView(ListView):
    model = Company


class AccountListView(ListView):
    model = Appointment
    template_name = "catalog/account_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["appointments"] = Appointment.objects.all()  # Передаем все записи
        return context
