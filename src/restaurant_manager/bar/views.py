from django.shortcuts import redirect, render
from django.views import View


from products.models import Product, Category
from products.forms import ProductForm
from .forms import SpiritDetailForm
from .models import SpiritDetail

# Create your views here.

def spirit_list(request):
    # Fetch all products from the database
    Category.objects.filter(category_name='Spirit')

    spirits = Product.objects.filter(category__category_name='Spirit')
    
    # Render the template with the products context
    return render(request, 'bar/spirit_list.html', {'spirits': spirits})

def spirit_detail(request, pk):
    # Fetch the specific product based on the primary key (pk)
    product = Product.objects.get(pk=pk)
    spirit = SpiritDetail.objects.get(name=product)
    
    # Render the template with the product context
    return render(request, 'bar/spirit_detail.html', {'spirit': spirit})

class SpiritDetailView(View):

    template_name = 'bar/spirit_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'detail_form': SpiritDetailForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        detail_form = SpiritDetailForm(request.POST)

        if product_form.is_valid() and detail_form.is_valid():

            product = product_form.save()

            detail = detail_form.save(commit=False)
            detail.name = product
            detail.save()

            return redirect('spirit-list')
        
        context = {
            'product_form': product_form,
            'detail_form': detail_form,
         }
        return render(request, self.template_name, context)