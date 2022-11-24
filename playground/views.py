from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from store.models import Product


def say_hello(request):
    queryset = Product.objects.filter(title__icontains='coffee')

    return render(request, 'hello.html', {'name': 'Ibrahim', 'products': list(queryset)})
