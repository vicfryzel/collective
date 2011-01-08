from articles.models import Article
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import Http404
from django.shortcuts import render_to_response

def index(request, page=1):
  articles = Article.objects.all().order_by('-pub_date')
  paginator = Paginator(articles, 5)
  try:
    articles = paginator.page(page)
  except (EmptyPage, InvalidPage):
    articles = paginator.page(paginator.num_pages)

  return render_to_response('articles/index.html', {'articles': articles})

def single(request, year, month, day, slug):
  try:
    article = Article.objects.get(pub_date__year=year, pub_date__month=month,
                                  pub_date__day=day, slug=slug)
  except Article.DoesNotExist:
    raise Http404
  except ValueError:
    raise Http404
  return render_to_response('articles/single.html', {'article': article})

def archives(request):
  articles = Article.objects.all().order_by('-pub_date')
  return render_to_response('articles/archives.html', {'articles': articles})
