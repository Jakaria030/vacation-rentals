from django.db import models

# Location Model
class Location(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}, {self.city}, {self.country}"


# Property Model
class Property(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="properties")
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.PositiveIntegerField()
    likes_count = models.IntegerField(default=0)
    reviews_count = models.IntegerField(default=0)
    facilities = models.CharField(max_length=255)  # comma-separated
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# Property Image Model
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="media/images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name if self.image else "No image"
