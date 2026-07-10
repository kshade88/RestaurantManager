from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from products.models import Product
from products.forms import ProductForm
from .forms import BeerForm, SpiritForm, WineForm, LiqueurForm, MixerForm, IngredientForm, GarnishForm
from .models import Beer, Spirit, Wine, Liqueur, Mixer, Ingredient, Garnish

class DashboardView(View):
    template_name = 'bar/dashboard.html'

    def get(self, request):
        return render(request, self.template_name)


class SpiritListView(ListView):
    model = Spirit
    template_name = 'bar/spirit_list.html'
    context_object_name = 'spirits'

class SpiritDetailView(DetailView):
    model = Spirit
    template_name = 'bar/spirit_detail.html'
    context_object_name = 'spirit'

class SpiritCreateView(View):

    template_name = 'bar/spirit_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'spirit_form': SpiritForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        spirit_form = SpiritForm(request.POST)

        if product_form.is_valid() and spirit_form.is_valid():

            product = product_form.save()

            detail = spirit_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('spirit-list')
        
        context = {
            'product_form': product_form,
            'spirit_form': spirit_form,
         }
        return render(request, self.template_name, context)

class SpiritUpdateView(View):

    template_name = 'bar/spirit_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        spirit_detail = Spirit.objects.get(product=product)

        product_form = ProductForm(instance=product)
        spirit_form = SpiritForm(instance=spirit_detail)

        context = {
            'product_form': product_form,
            'spirit_form': spirit_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        spirit_detail = Spirit.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        spirit_form = SpiritForm(request.POST, instance=spirit_detail)

        if product_form.is_valid() and spirit_form.is_valid():
            product_form.save()
            spirit_form.save()
            return redirect('spirit-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'spirit_form': spirit_form,
        }
        return render(request, self.template_name, context)

class SpiritDeleteView(DeleteView):
    template_name = 'bar/spirit_confirm_delete.html'
    model = Spirit
    success_url = reverse_lazy('spirit-list')

class BeerListView(ListView):
    model = Beer
    template_name = 'bar/beer_list.html'
    context_object_name = 'beers'

class BeerDetailView(DetailView):
    model = Beer
    template_name = 'bar/beer_detail.html'
    context_object_name = 'beer'

class BeerCreateView(View):
    template_name = 'bar/beer_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'beer_form': BeerForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        beer_form = BeerForm(request.POST)

        if product_form.is_valid() and beer_form.is_valid():

            product = product_form.save()

            detail = beer_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('beer-list')
        
        context = {
            'product_form': product_form,
            'beer_form': beer_form,
         }
        return render(request, self.template_name, context)

class BeerUpdateView(View):

    template_name = 'bar/beer_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        beer_detail = Beer.objects.get(product=product)

        product_form = ProductForm(instance=product)
        beer_form = BeerForm(instance=beer_detail)

        context = {
            'product_form': product_form,
            'beer_form': beer_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        beer_detail = Beer.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        beer_form = BeerForm(request.POST, instance=beer_detail)

        if product_form.is_valid() and beer_form.is_valid():
            product_form.save()
            beer_form.save()
            return redirect('beer-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'beer_form': beer_form,
        }
        return render(request, self.template_name, context)
    
class BeerDeleteView(DeleteView):
    template_name = 'bar/beer_confirm_delete.html'
    model = Beer
    success_url = reverse_lazy('beer-list')  

class WineListView(ListView):
    model = Wine
    template_name = 'bar/wine_list.html'
    context_object_name = 'wines'

class WineDetailView(DetailView):
    model = Wine
    template_name = 'bar/wine_detail.html'
    context_object_name = 'wine'

class WineCreateView(View):
    template_name = 'bar/wine_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'wine_form': WineForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        wine_form = WineForm(request.POST)

        if product_form.is_valid() and wine_form.is_valid():

            product = product_form.save()

            detail = wine_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('wine-list')
        
        context = {
            'product_form': product_form,
            'wine_form': wine_form,
         }
        return render(request, self.template_name, context)

class WineUpdateView(View):

    template_name = 'bar/wine_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        wine_detail = Wine.objects.get(product=product)

        product_form = ProductForm(instance=product)
        wine_form = WineForm(instance=wine_detail)

        context = {
            'product_form': product_form,
            'wine_form': wine_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        wine_detail = Wine.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        wine_form = WineForm(request.POST, instance=wine_detail)

        if product_form.is_valid() and wine_form.is_valid():
            product_form.save()
            wine_form.save()
            return redirect('wine-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'wine_form': wine_form,
        }
        return render(request, self.template_name, context)

class WineDeleteView(DeleteView):

    template_name = 'bar/wine_confirm_delete.html'
    model = Wine
    success_url = reverse_lazy('wine-list')

class LiqueurListView(ListView):
    model = Liqueur
    template_name = 'bar/liqueur_list.html'
    context_object_name = 'liqueurs'

class LiqueurDetailView(DetailView):
    model = Liqueur
    template_name = 'bar/liqueur_detail.html'
    context_object_name = 'liqueur'

class LiqueurCreateView(View):
    template_name = 'bar/liqueur_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'liqueur_form': LiqueurForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        liqueur_form = LiqueurForm(request.POST)

        if product_form.is_valid() and liqueur_form.is_valid():

            product = product_form.save()

            detail = liqueur_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('liqueur-list')
        
        context = {
            'product_form': product_form,
            'liqueur_form': liqueur_form,
         }
        return render(request, self.template_name, context)

class LiqueurUpdateView(View):

    template_name = 'bar/liqueur_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        liqueur_detail = Liqueur.objects.get(product=product)

        product_form = ProductForm(instance=product)
        liqueur_form = LiqueurForm(instance=liqueur_detail)

        context = {
            'product_form': product_form,
            'liqueur_form': liqueur_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        liqueur_detail = Liqueur.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        liqueur_form = LiqueurForm(request.POST, instance=liqueur_detail)

        if product_form.is_valid() and liqueur_form.is_valid():
            product_form.save()
            liqueur_form.save()
            return redirect('liqueur-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'liqueur_form': liqueur_form,
        }
        return render(request, self.template_name, context)

class LiqueurDeleteView(DeleteView):

    template_name = 'bar/liqueur_confirm_delete.html'
    model = Liqueur
    success_url = reverse_lazy('liqueur-list')

class MixerListView(ListView):
    model = Mixer
    template_name = 'bar/mixer_list.html'
    context_object_name = 'mixers'

class MixerDetailView(DetailView):
    model = Mixer
    template_name = 'bar/mixer_detail.html'
    context_object_name = 'mixer'

class MixerCreateView(View):
    template_name = 'bar/mixer_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'mixer_form': MixerForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        mixer_form = MixerForm(request.POST)

        if product_form.is_valid() and mixer_form.is_valid():

            product = product_form.save()

            detail = mixer_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('mixer-list')
        
        context = {
            'product_form': product_form,
            'mixer_form': mixer_form,
         }
        return render(request, self.template_name, context)

class MixerUpdateView(View):

    template_name = 'bar/mixer_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        mixer_detail = Mixer.objects.get(product=product)

        product_form = ProductForm(instance=product)
        mixer_form = MixerForm(instance=mixer_detail)

        context = {
            'product_form': product_form,
            'mixer_form': mixer_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        mixer_detail = Mixer.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        mixer_form = MixerForm(request.POST, instance=mixer_detail)

        if product_form.is_valid() and mixer_form.is_valid():
            product_form.save()
            mixer_form.save()
            return redirect('mixer-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'mixer_form': mixer_form,
        }
        return render(request, self.template_name, context)

class MixerDeleteView(DeleteView):

    template_name = 'bar/mixer_confirm_delete.html'
    model = Mixer
    success_url = reverse_lazy('mixer-list')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'bar/ingredient_list.html'
    context_object_name = 'ingredients'

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'bar/ingredient_detail.html'
    context_object_name = 'ingredient'

class IngredientCreateView(View):
    template_name = 'bar/ingredient_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'ingredient_form': IngredientForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        ingredient_form = IngredientForm(request.POST)

        if product_form.is_valid() and ingredient_form.is_valid():

            product = product_form.save()

            detail = ingredient_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('ingredient-list')
        
        context = {
            'product_form': product_form,
            'ingredient_form': ingredient_form,
         }
        return render(request, self.template_name, context)

class IngredientUpdateView(View):

    template_name = 'bar/ingredient_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        ingredient_detail = Ingredient.objects.get(product=product)

        product_form = ProductForm(instance=product)
        ingredient_form = IngredientForm(instance=ingredient_detail)

        context = {
            'product_form': product_form,
            'ingredient_form': ingredient_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        ingredient_detail = Ingredient.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        ingredient_form = IngredientForm(request.POST, instance=ingredient_detail)

        if product_form.is_valid() and ingredient_form.is_valid():
            product_form.save()
            ingredient_form.save()
            return redirect('ingredient-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'ingredient_form': ingredient_form,
        }
        return render(request, self.template_name, context)

class IngredientDeleteView(DeleteView):

    template_name = 'bar/ingredient_confirm_delete.html'
    model = Ingredient
    success_url = reverse_lazy('ingredient-list')

class GarnishListView(ListView):
    model = Garnish
    template_name = 'bar/garnish_list.html'
    context_object_name = 'garnishes'

class GarnishDetailView(DetailView):
    model = Garnish
    template_name = 'bar/garnish_detail.html'
    context_object_name = 'garnish'

class GarnishCreateView(View):
    template_name = 'bar/garnish_form.html'

    def get(self, request):

        context = {
            'product_form': ProductForm(),
            'garnish_form': GarnishForm(),
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        product_form = ProductForm(request.POST)
        garnish_form = GarnishForm(request.POST)

        if product_form.is_valid() and garnish_form.is_valid():

            product = product_form.save()

            detail = garnish_form.save(commit=False)
            detail.product = product
            detail.save()

            return redirect('garnish-list')
        
        context = {
            'product_form': product_form,
            'garnish_form': garnish_form,
         }
        return render(request, self.template_name, context) 

class GarnishUpdateView(View):

    template_name = 'bar/garnish_form.html'

    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        garnish_detail = Garnish.objects.get(product=product)

        product_form = ProductForm(instance=product)
        garnish_form = GarnishForm(instance=garnish_detail)

        context = {
            'product_form': product_form,
            'garnish_form': garnish_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        product = Product.objects.get(pk=pk)
        garnish_detail = Garnish.objects.get(product=product)

        product_form = ProductForm(request.POST, instance=product)
        garnish_form = GarnishForm(request.POST, instance=garnish_detail)

        if product_form.is_valid() and garnish_form.is_valid():
            product_form.save()
            garnish_form.save()
            return redirect('garnish-detail', pk=product.pk)

        context = {
            'product_form': product_form,
            'garnish_form': garnish_form,
        }
        return render(request, self.template_name, context)

class GarnishDeleteView(DeleteView):

    template_name = 'bar/garnish_confirm_delete.html'
    model = Garnish
    success_url = reverse_lazy('garnish-list')
    
    
