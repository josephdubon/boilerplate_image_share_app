from urllib import request
from django import forms
from django.core.files.base import ContentFile
from django.utils.text import slugify

from .models import Image


# Submit image form
class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            'title',
            'url',
            'description',
        )
        # Users will not enter the image URL directly in the form.
        # - Instead user will be provided with a JavaScript tool to choose an image from an external site.
        # -- The form will then receive the URL as a parameter.
        widgets = {
            'url': forms.HiddenInput,
        }

    # Check that filename ends with jpg or jpeg to ONLY allow these file types
    def clean_url(self):
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not ' \
                                        'match valid image extensions.')
        return url

    # Override the save() method of ModelForm
    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.rsplit('.', 1)[1].lower()
        image_name = f'{name}.{extension}'
        # download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image
