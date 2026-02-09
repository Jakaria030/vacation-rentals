from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from .models import Location

# Home page render
def index(request):
    return render(request, "index.html")


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


# Properties result
def properties_result(request):
    q = request.GET.get("location", "")

    return render(request, "properties.html", {"q": q})