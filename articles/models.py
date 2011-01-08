from django.db import models

class Article(models.Model):
  slug = models.SlugField(max_length=200)
  title = models.CharField(max_length=200)
  body = models.TextField()
  pub_date = models.DateTimeField()

  @models.permalink
  def get_absolute_url(self):
    return ('articles.views.single', (),
            {'year': '%04d' % self.pub_date.year,
             'month': '%02d' % self.pub_date.month,
             'day': '%02d' % self.pub_date.day,
             'slug': str(self.slug)})

  def __unicode__(self):
    return u'%s' % self.title
