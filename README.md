media_renderer
==============

allows you to use template tags in your .js/.css, then for production adds a management command to write them to your static files.

Can be used as the user wants, I've written this for single page applications so that I can use INCLUDE and URL tags in my .js files

installation
pip install https://github.com/fredkingham/django-media-renderer/master


the following settings are required in your settings file

media_renderer need to be added to your installed apps

STATIC_TEMPLATES -> a list of the templates that exist in your template dirs that you want to use tags in. 

e.g.
STATIC_TEMPLATES = ["js_template.js"]

STATIC_TEMPLATE_DIR -> The name of a directory that is in your STATICFILES_DIRS where the render template command will out put the rendered file

optional MEDIA_RENDER_PREFIX, this is the subdomain that the media will be rendered from, by default this is __media_render

useage
 add to your urls url(r'', include('js_render.urls')),

before collect static in your build scripts add the admin comman render_templates

