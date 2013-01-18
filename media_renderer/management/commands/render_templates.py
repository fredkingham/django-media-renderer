from django.core.management.base import BaseCommand, CommandError
from django.template.loader import get_template
from django.template import RequestContext
from django.http import HttpRequest
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'compiles templates to static files'

    def handle(self, *args, **options):

        for i in ["STATIC_TEMPLATE_DIR", "STATIC_TEMPLATES"]:
            if not hasattr(settings, i):
                raise CommandError("%s not set in settings" % i)
        static = settings.STATIC_TEMPLATE_DIR
        templates = settings.STATIC_TEMPLATES
        request = HttpRequest()
        context = RequestContext(request)

        for template in templates:
            t = get_template(template)
            name = os.path.join(static, template)
            self.stdout.write("writing %s \n" % name)
            template_file = open(name, 'w+')
            template_file.write(t.render(context))
            self.stdout.write("written \n")



