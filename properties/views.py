from django.http import HttpResponse
from django.template import loader
from .models import Location

def index(request):
    template = loader.get_template("index.html")
    locations = Location.objects.all().values()
    context = {"locations": locations}
    return HttpResponse(template.render(context, request))