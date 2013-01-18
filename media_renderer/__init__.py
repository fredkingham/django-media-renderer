version = (0, 0, 1)
__version__ = '.'.join(map(str, version))


from django.conf import settings

if hasattr(settings, "MEDIA_RENDER_PREFIX"):
    prefix = settings.MEDIA_RENDER_PREFIX
else:
    prefix = "__media_render/"
