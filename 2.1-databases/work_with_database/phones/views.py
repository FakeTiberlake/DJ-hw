from django.shortcuts import render, redirect, get_object_or_404

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort', False)

    if sort_param is not False:
        if sort_param == 'name':
            phones = Phone.objects.all().order_by('name')
        if sort_param == 'min_price':
            phones = Phone.objects.all().order_by('price')
        if sort_param == 'max_price':
            phones = Phone.objects.all().order_by('price').reverse()
    else:
        phones = Phone.objects.all()

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    # phone = Phone.objects.get(slug=slug)
    context = {
        'phone': phone,
    }
    return render(request, template, context)
