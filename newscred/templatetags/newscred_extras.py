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
@register.tag(name='current_time', do_current_time)
def do_current_time(parser, token):
  try:
    # split_contents() knows not to split quoted strings.
    tag_name, format_string = token.split_contents()
  except ValueError:
    raise template.TemplateSyntaxError("%r tag requires a single argument" % token.contents.split()[0])
  if not (format_string[0] == format_string[-1] and format_string[0] in ('"', "'")):
    raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
  return CurrentTimeNode(format_string[1:-1])

class CurrentTimeNode(template.Node):
  def __init__(self, format_string):
    self.format_string = format_string
  def render(self, context):
    return datetime.datetime.now().strftime(self.format_string)