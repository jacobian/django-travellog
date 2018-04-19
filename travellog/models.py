from django.db import models

class TravelLog(models.Model):
    """
    The top-level object - a single travel log, with many locations and photos.
    Might be used to group by year, or around a single epic trip, etc.
    """
    title = models.TextField()
    slug = models.SlugField(db_index=True)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Section(models.Model):
    """
    A section of a travel log, which can contain a bunch of locations.

    Sections don't have semantic meaning - might be a state, or a stretch
    of days, or whatever you like.
    """
    travellog = models.ForeignKey(TravelLog, related_name='sections', on_delete=models.CASCADE)
    title = models.TextField()

    ICONS = ['map-us-ca', 'map-us-or', 'map-us-wa']
    ICON_CHOICES = zip(ICONS, ICONS)

    icon = models.TextField(default='map-us-ca', choices=ICON_CHOICES) # FIXME: chocies from Mapglyphs


    class Meta:
        order_with_respect_to = 'travellog'

    def __str__(self):
        return f'{self.title} ({self.travellog.title})'

class Location(models.Model):
    """
    A single location, which can have some text and a bunch of photos.
    """
    section = models.ForeignKey(Section, related_name='locations', on_delete=models.CASCADE)
    title = models.TextField()
    text = models.TextField(blank=True)
    date = models.TextField(blank=True) # FIXME: should this be a datefield?

    # FIXME: validate min/maxes, default choices for the map display fields
    # ideally the admin would let you do this graphically??
    latitude = models.FloatField()
    longitude = models.FloatField()
    zoom = models.FloatField(default=12.5)
    bearing = models.PositiveSmallIntegerField(default=0)
    pitch = models.PositiveSmallIntegerField(default=0)

    class Meta:
        order_with_respect_to = 'section'

    def __str__(self):
        return self.title

class Photo(models.Model):
    """
    A photo of a place, contained in a Location.
    """
    location = models.ForeignKey(Location, related_name='photos', on_delete=models.CASCADE)

    def _photo_upload_path_callback(instance, filename):
        return f'photos/{instance.location.section.slug}/{filename}'

    # FIXME: imagefield when I'm back online
    photo = models.FileField(max_length=1000, upload_to=_photo_upload_path_callback)

    SIZES = ["1x1", "1x2", "2x1", "2x2", "3x1", "3x2", "3x3"]
    SIZE_CHOICES = zip(SIZES, SIZES)
    size = models.CharField(max_length=3, choices=SIZE_CHOICES, default='1x1')

    class Meta:
        order_with_respect_to = 'location'

    def __str__(self):
        return f"{self.photo} ({self.location})"
