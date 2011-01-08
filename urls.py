from collective.feeds import RssArticlesFeed, AtomArticlesFeed
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  # Uncomment the admin/doc line below to enable admin documentation:
  # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

  # Uncomment the next line to enable the admin:
  (r'^admin/', include(admin.site.urls)),

  # Uncomment for development
  #(r'^static/(?P<path>.*)$', 'django.views.static.serve',
  #    {'document_root': '/path/to/collective/themes/minimalbw-yourname/static'}),

  (r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>.*)$', 'articles.views.single'),
  (r'^archives/?$', 'articles.views.archives', {}, 'archives'),
  (r'^articles.atom$', AtomArticlesFeed(), {}, 'atom'),
  (r'^articles.rss$', RssArticlesFeed(), {}, 'rss'),
  (r'^(?P<page>\d{1,3})/?$', 'articles.views.index', {}, 'index'),
  (r'^/?$', 'articles.views.index', {}, 'index'),
)
