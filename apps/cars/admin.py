from django.contrib import admin

from .models import Car
from apps.core.admin.mixin import ThumbnailMixin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin, ThumbnailMixin):
    list_display = [field.name for field in Car._meta.fields]
    list_display += ["thumbnail"]
    list_filter = ("year", "model")
    list_per_page = 5
    list_display_links = ("id", "car_title", "state")
    list_editable = ("is_features", "fuel_type")
    search_fields = (
        "year",
        "car_title",
        "model",
        "fuel_type",
        "state",
        "mileages",
        "transmission",
        "engine",
        "body_style",
    )

    def thumbnail(self, obj, *args):
        return super(CarAdmin, self).thumbnail(obj)
