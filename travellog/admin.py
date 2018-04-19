from django.contrib import admin
from . import models as tl_models
from . import forms as tl_forms

@admin.register(tl_models.TravelLog)
class TravelLogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ["title"]}
    form = tl_forms.TravelLogForm

@admin.register(tl_models.Section)
class SectionAdmin(admin.ModelAdmin):
    form = tl_forms.SectionForm

class PhotoInline(admin.TabularInline):
    model = tl_models.Photo
    extra = 1

@admin.register(tl_models.Location)
class LocationAdmin(admin.ModelAdmin):
    form = tl_forms.LocationForm
    inlines = [PhotoInline]


