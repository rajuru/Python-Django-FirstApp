from django import template
import urllib, datetime
register = template.Library()

def topic_info(topic, arg):
  """ Returns topic related formatted string """
  return "Will come soon..."

@register.filter
def shorten(url):
  try:
    response = urllib.urlopen("http://to.ly/api.php?longurl=%s" % url)
    short_url = response.read()
  except:
    short_url = url
  return short_url

class TopicNode(template.Node):
  def __init__(self, topic):
    self.topic = template.Variable(topic)

  def render(self, context):
    topic = self.topic.resolve(context)
    return ("<div class='info'><br /><hr />Class: %s, Subclass: %s, Group: %s</div>" % (topic['topic_classification'], topic['topic_subclassification'], topic['topic_group'] ) )


@register.tag
def topic_info(parser, token):
  try:
    # split_contents() knows not to split quoted strings.
    tag_name, topic = token.split_contents()
  except ValueError:
    raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
  return TopicNode(topic)