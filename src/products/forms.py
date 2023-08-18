from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    # overwrite fields
    title = forms.CharField(label='')

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    #add additional validation clean_<form_field_name>
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "COOL" in title:
            raise forms.ValidationError("Error, product is not COOL")
        return title
