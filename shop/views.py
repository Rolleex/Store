from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from cart.forms import CartAddForm
from store.permissions import IsAdminOrReadOnly
from .models import ProductItem, Category
from rest_framework import viewsets
from .serializers import ProductItemSerializer


# Create your views here.
###########################################################
# DRF Part
class IndexApi(viewsets.ModelViewSet):
    queryset = ProductItem.objects.all()
    serializer_class = ProductItemSerializer
    permission_classes = (IsAdminOrReadOnly,)

###########################################################


def index(request):
    items = ProductItem.objects.all()

    form = CartAddForm()
    return render(request, 'shop/index.html', context={'items': items, 'form': form, })


class CategoryView(View):
    def get(self, request, pk):
        items = ProductItem.objects.filter(category__pk=pk)

        context = {
            'items': items,

        }
        return render(request, 'shop/index.html', context)


class Search(View):
    def get(self, request, *args, **kwargs):
        q = self.request.GET.get('q')
        items = ProductItem.objects.filter(title__icontains=q)
        context = {
            'items': items,

        }
        return render(request, 'shop/index.html', context)


def product_item_detail(request, pk):
    item = ProductItem.objects.get(pk=pk)
    form = CartAddForm()
    itemcat = Category.objects.get(productitem__pk=pk)
    context = {
        'itemcat': itemcat,
        'item': item,
        'form': form,

    }
    return render(request, 'shop/product_item_detail.html', context)
