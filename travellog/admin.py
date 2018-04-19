from django.contrib import admin
import nested_admin
from . import models as tl_models
from . import forms as tl_forms

class PhotoInline(nested_admin.NestedTabularInline):
    model = tl_models.Photo
    extra = 0

class LocationInline(nested_admin.NestedStackedInline):
    model = tl_models.Location
    form = tl_forms.LocationForm
    fields = (
        ('title', 'date'),
        'text',
        ('latitude', 'longitude', 'zoom', 'bearing', 'pitch'),
    )
    extra = 0
    inlines = [PhotoInline]

class SectionInline(nested_admin.NestedStackedInline):
    model = tl_models.Section
    form = tl_forms.SectionForm
    fields = (('title', 'icon'),)
    extra = 0
    inlines = [LocationInline]

@admin.register(tl_models.TravelLog)
class TravelLogAdmin(nested_admin.NestedModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    form = tl_forms.TravelLogForm
    inlines = [SectionInline]


