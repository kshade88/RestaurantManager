from django.shortcuts import render
from .models import Product, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
 
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['product_name', 'category', 'tags']
    success_url = '/products/'

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_form.html'
    fields = ['product_name', 'category', 'tags']
    success_url = '/products/'

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    success_url = '/products/'