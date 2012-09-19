from django.db import models
import json, urllib2, urllib
from newscred.utils import Fetch

class Topic(models.Model):
  name = models.CharField(max_length=255)
  topic_group = models.CharField('Topic Group', max_length=255)
  description = models.TextField()
  image_url = models.TextField(max_length=255)
  link = models.TextField(max_length=255)
  guid = models.TextField(max_length=255, unique=True)

  def __unicode__(self):
    return self.name

  def retrieve_image(self, topic):
    #image = fetcher.topics(self.name)
    try:
      return self.image.url
    except Image.DoesNotExist:
      #fetch image
      fetcher = Fetch()
      image_data = fetcher.image(self)

      img = Image(topic=self, url=image_data)
      return img.url

class Image(models.Model):
  topic = models.OneToOneField(Topic, primary_key=True)
  url = models.TextField(max_length=255)


