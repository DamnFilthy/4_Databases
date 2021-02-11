from django.shortcuts import render
from phones.models import Phone
import datetime


def show_catalog(request):
    sort = request.GET.get('sort', '')
    print(sort)
    if sort == 'price':
        phones = Phone.objects.order_by("price")
        return render(request, "catalog.html", {"phones": phones})
    elif sort == 'alf':
        phones = Phone.objects.order_by("name")
        return render(request, "catalog.html", {"phones": phones})
    phones = Phone.objects.all()
    return render(request, "catalog.html", {"phones": phones})


def show_product(request, name):
    this_phone = Phone.objects.get(slug=name)
    return render(request, 'product.html', {'phone': this_phone})
