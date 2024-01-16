from django.shortcuts import render
from .models import Article


def articles_list(request):
    ordering = '-published_at'
    object_list = Article.objects.order_by(ordering)

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by

    return render(request, 'articles/news.html', {'object_list': object_list})