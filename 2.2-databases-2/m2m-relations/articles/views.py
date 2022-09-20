from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.object.all().prefetch_related('scopes').order_by('-published_at')
    context = {
        'article': object_list,
               }

    return render(request, template, context)
