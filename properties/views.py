from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q, Subquery, OuterRef
from .models import Location, Property, PropertyImage

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
    q = request.GET.get("location", "").strip()
    location_name = (q.split(",")[0] if "," in q else q).strip()

    # Sub query for first image
    image_subquery = PropertyImage.objects.filter(property=OuterRef("pk")).values("image")[:1]

    if location_name:
        # Filter properties by related location (name, city, country)
        properties = Property.objects.filter(
            Q(location__name__icontains=location_name) |
            Q(location__city__icontains=location_name) |
            Q(location__country__icontains=location_name)
        ).annotate(
            image = Subquery(image_subquery)
        ).values(
            "id", "title", "location__name", "location__city", "location__country", "price_per_night", "likes_count", "reviews_count", "facilities", "image"
        )
    else:
        # If no location provided, return all properties
        properties = Property.objects.all().annotate(
            image = Subquery(image_subquery)
        ).values(
            "id", "title", "location__name", "location__city", "location__country", "price_per_night", "likes_count", "reviews_count", "facilities", "image"
        )

    return render(request, "properties.html", {"location": location_name.upper(), "properties": list(properties)})


# Property Details
def property_details(request, id):
    try:
        property = Property.objects.get(id=id)
        images = property.images.all().values()
        return render(request, "property_details.html", { "property": property,"images": images })
    except Property.DoesNotExist:
        message = f"Property with ID: {id} not found!"
        return render(request, "property_details.html", { "message": message})
