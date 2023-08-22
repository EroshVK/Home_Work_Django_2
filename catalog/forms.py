from django import forms
from catalog.models import Product

FORBIDDEN_PRODUCT_TYPES = [
    'казино',
    'криптовалюта',
    'крипта',
    'биржа',
    'дешево',
    'бесплатно',
    'обман',
    'полиция',
    'радар'
]


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        cleaned_name = self.cleaned_data.get('name')
        for product_type in FORBIDDEN_PRODUCT_TYPES:
            if product_type in cleaned_name.lower():
                raise forms.ValidationError('Такие продукты нельзя добавлять')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data.get('description')
        for product_type in FORBIDDEN_PRODUCT_TYPES:
            if product_type in cleaned_description.lower():
                raise forms.ValidationError('Такие продукты нельзя добавлять')
        return cleaned_description

    class Meta:
        model = Product
        exclude = ('creation_date', 'last_modified_date')
