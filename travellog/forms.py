from django import forms
from . import models as tl_models

class TravelLogForm(forms.ModelForm):
    class Meta:
        model = tl_models.TravelLog
        fields = '__all__'

    title = forms.CharField()

class SectionForm(forms.ModelForm):
    class Meta:
        model = tl_models.Section
        fields = '__all__'

    title = forms.CharField()

class LocationForm(forms.ModelForm):
    class Meta:
        model = tl_models.Location
        fields = '__all__'

    title = forms.CharField()
    date = forms.CharField()

    # FIXME can I build a map selector widget thing?

    # FIXME validate these
    bearing = forms.IntegerField(min_value=0, max_value=360)
    pitch = forms.IntegerField(min_value=0, max_value=100)

