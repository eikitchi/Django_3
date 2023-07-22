from django import forms
from main.models import Product, Version


class FormStyleMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormStyleMixin, forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'preview', 'category', 'price',)

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for word in self.forbidden_words:
            if word in cleaned_name.lower():
                raise forms.ValidationError(f'Название не может содержать слово "{word}"')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in cleaned_description.lower():
                raise forms.ValidationError(f'Описание не может содержать слово "{word}"')
        return cleaned_description


class VersionForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'