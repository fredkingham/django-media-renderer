from django.conf.urls import patterns, url
import views
import prefix
from django.conf import settings

urlpatterns = patterns('')

if settings.DEBUG:
    #turn this into a list comprehension
    urls = []
    for template in settings.STATIC_TEMPLATES:
        urls.append(url(r'^%s%s' % (prefix, template), views.get_script(template)))
    urlpatterns += patterns('', *urls)
