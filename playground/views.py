from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product, Collection
from tags.models import TaggedItem


def say_hello(request):
    collection = Collection()
    collection.title = "Video Games"
    collection.featured_product = Product(pk=1)

    return render(request, 'hello.html', {'name': 'Ibrahim', "tags": list(queryset)})
