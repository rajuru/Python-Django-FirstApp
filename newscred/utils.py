import json, urllib
class Fetch:
  base_url = 'http://api.newscred.com'
  access_key = 'c4bcc3f7c9bf9ec159f51da0a86ca658'

  def get_topics(self, query):
    data = self.execute('/topics', urllib.urlencode({'query': query}))
    return data['topic_set']


  def get_topic(self, guid):
    data = self.execute('/topic/%s' % guid)
    return data['topic']

  def get_related_topic(self, guid):
    data = self.execute('/topic/%s/topics' % guid)
    return data['topic_set']

  def get_images(self, guid):
    data = self.execute('/topic/%s/images' % guid)
    return data['image_set']

  def execute(self, path, query_strings=''):

    if query_strings:
      url = "%s%s?%s&access_key=%s&format=json" % (self.base_url, path, query_strings, self.access_key)
    else:
      url = "%s%s?access_key=%s&format=json" % (self.base_url, path, self.access_key)
    response = urllib.urlopen(url)
    return json.loads(response.read())


