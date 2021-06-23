from django.shortcuts import render
from products.models import Product, ProductCategory
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page=1):
    context = {'title': 'GeekShop-Каталог', 'categories': ProductCategory.objects.all()}
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, 3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context['products'] = products_paginator
    return render(request, 'products/products.html', context)


# class ProductsListView(ListView):
#     model = Product
#     template_name = 'products/products.html'
#     paginate_by = 3
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super(ProductsListView, self).get_context_data(**kwargs)
#         context['title'] = 'GeekShop - Административная панель'
#         context['categories'] = ProductCategory.objects.all()
#         return context
#
#     def get_queryset(self):
#         if 'category_id' in self.kwargs:
#             self.category_id = get_object_or_404(ProductCategory, id=self.kwargs['category_id'])
#             return Product.objects.filter(category_id=self.category_id)
#         else:
#             return Product.objects.all()
