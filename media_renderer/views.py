from django.template import RequestContext
from django.template.loader import get_template
from django.http import HttpResponse


def get_script(template):
    if template.endswith(".js"):
        template_type = "application/javascript"
    elif template.endswith(".css"):
        template_type = "text/css"
    else:
        raise Exception("the media_renderer only handles js or css, sorry")

    def render(request):
        t = get_template(template)
        r = t.render(RequestContext(request))
        return HttpResponse(r, mimetype=template_type)

    return render
