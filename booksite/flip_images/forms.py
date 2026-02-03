from django import forms
from .models import FlipbookImage


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class FlipbookImageForm(forms.Form):
    image = forms.FileField(
        widget=MultipleFileInput(),
        required=True
    )

    class Meta:
        model = FlipbookImage
        fields = ['image', 'is_front', 'title', 'date', 'caption']
