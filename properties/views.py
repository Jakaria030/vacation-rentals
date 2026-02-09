from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.template import loader
from .models import Location

def index(request):
    template = loader.get_template("index.html")
    locations = Location.objects.all().values()
    context = {"locations": locations}
    return HttpResponse(template.render(context, request))

# Location auto complete whene type
def location_autocomplete(request):
    q = request.GET.get('q', '')
    if len(q) < 3:
        return JsonResponse([], safe=False)
    
    # Filter by name OR city OR country (case-insensitive)
    locations = Location.objects.filter(
        Q(name__icontains=q) | Q(city__icontains=q) | Q(country__icontains=q)
    )[:5].values("id", "name", "city", "country")
    
    
    return JsonResponse(list(locations), safe=False)