from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from .models import Article, Comment
from django.urls import reverse


def index(request):
    latest_articles_list = Article.objects.order_by("-pub_date")[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def test(request):
    return render(request, 'articles/list.html')


def detail(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("статья не найденна")

    return render(request, 'articles/detail.html', {'article': a})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("статья не найденна")

    a.comment_set.create(author_name=request.POST["name"], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))
