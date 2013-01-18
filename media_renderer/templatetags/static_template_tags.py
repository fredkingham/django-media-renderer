from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag
def static_template_url():
    if settings.DEBUG and not getattr(settings, "STATIC_TEMPLATES_DISABLED"):
        from media_renderer import prefix
        return prefix
    else:
        return settings.STATIC_URL
