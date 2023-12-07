from django import forms
from .models import Clue
from django.core.exceptions import ValidationError


class ClueForm(forms.ModelForm):
    class Meta:
        model = Clue
        fields = ('description', 'longitude', 'latitude', 'hints', 'bundle',)

    def clean_latitude(self):
        latitude = self.cleaned_data.get('latitude')

        if latitude is not None and (latitude < -90 or latitude > 90):
            raise ValidationError('Latitude must be between -90 and +90.')

        return latitude

    def clean_longitude(self):
        longitude = self.cleaned_data.get('longitude')

        if longitude is not None and (longitude < -180 or longitude > 180):
            raise ValidationError('Longitude must be between -180 and +180.')

        return longitude
