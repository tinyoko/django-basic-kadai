from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Product
from django.urls import reverse_lazy


# Create your views here.
class TopView(TemplateView):
    template_name = "Top.html"


class ProductListView(ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3


class ProductCreateView(CreateView):
    model = Product
    fields = "__all__"
    template_name = "form.html"


class ProductUpdateView(UpdateView):
    model = Product
    fields = "__all__"
    # fields = ["price"]
    template_name = "update.html"


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("list")
    template_name = "confirm_delete.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "detail.html"
