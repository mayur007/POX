from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class pocketdata (models.Model):
  item = models.CharField(max_length = 255)
  price = models.IntegerField()
  category = models.CharField(max_length = 255)
  comment = models.TextField()
  date = models.DateTimeField(auto_now_add = True)

  class Meta:
    ordering = ['-date']

  def __unicode__(self):
    return u'%s' % self.item

  def get_absolute_url(self):
    return reverse('pockettracker.views.pocketdatas', args=[self.category])
