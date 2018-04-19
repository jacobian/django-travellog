import json
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import TravelLog

def travellog(request, slug):
    qs = TravelLog.objects.prefetch_related('sections', 'sections__locations', 'sections__locations__photos')
    tl = get_object_or_404(qs, slug=slug)

    chapters = {}
    for section in tl.sections.all():
        for location in section.locations.all():
            chapters[f'location-{location.id}'] = {
                "center": [location.latitude, location.longitude],
                "zoom": location.zoom,
                "bearing": location.bearing,
                "pitch": location.pitch,
                "duration": 8000,
            }

    return render(request, 'travellog.html', {
        'travellog': tl,
        'chapters_json': json.dumps(chapters),
        'MAPBOX_TOKEN': settings.MAPBOX_TOKEN,
    })
