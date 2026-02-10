import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from properties.models import Location, Property


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        csv_file_path = os.path.join(settings.BASE_DIR, "properties", "data", "properties.csv")

        if not os.path.exists(csv_file_path):
            print("Error: CSV file not found")
            return
        
        with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for _, row in enumerate(reader, start=1):
                location, _ = Location.objects.get_or_create(
                    name=row["name"],
                    city=row["city"],
                    country=row["country"]
                )
                Property.objects.create(
                    location=location,
                    title=row["title"],
                    description=row["description"],
                    price_per_night=int(row["price_per_night"]),
                    likes_count=int(row.get("likes_count", 0)),
                    reviews_count=int(row.get("reviews_count", 0)),
                    facilities=row["facilities"]
                )

        print("\nCSV import completed successfully")
