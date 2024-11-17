from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form_control', 'placeholder':'Name of the product'}),
            'price' : forms.NumberInput(attrs={'class':'form_control', 'placeholder':'price'}),
            'desc' : forms.Textarea(attrs={'class':'form_control', 'placeholder':'description'}),
            'category' : forms.Select(attrs={'class':'form_control'}),
            'image' : forms.ClearableFileInput(attrs={'class':'form_control'}),
            'stock' : forms.NumberInput(attrs={'class':'form_control', 'placeholder':'Number of stocks available'})


        }