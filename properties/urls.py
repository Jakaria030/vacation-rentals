from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "properties"
urlpatterns = [
    path("", views.index, name="index"),
    path("locations/", views.location_autocomplete, name="location_autocomplete"),
    path("properties/", views.properties_result, name="properties_result"),
    path("property_details/<int:id>/", views.property_details, name="property_details")
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
