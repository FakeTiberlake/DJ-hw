from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'avocado-tost': {
        'хлеб, ломтик': 1,
        'авокадо, шт': 1,
        'масло сливочное, г': 5,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'cappuccino': {
        'кофе в зернах, г': 30,
        'молоко 2,5%, мл': 50,
        'корица молотая, г': 2,
    }

}


def home_page(request):
    pages = {
        'Омлет': 'omlet/',
        'Паста': 'pasta/',
        'Тост с авокадо': 'tost/',
        'Бутерброд': 'buter/',
        'Капучино': 'coffee/',
    }

    context = {
        'pages': pages,
    }
    return render(request, home_page.html, context)


def pagi(request):
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator.get_page(CONTENT, 3)
    page = paginator.get_page(page_number)
    context = {
        'page': page,
    }
    return render (request, 'pagi.html', context)


def calculator(request):
    servings = int(request.GET.get('servings', 1))
    recipe = DATA.copy()
    if recipe and servings > 1:
        for key, value in recipe.items():
            recipe[key] = value * servings

    context = {
      'recipe': recipe,

    }

    return render(request, 'calculator/index.html', context)