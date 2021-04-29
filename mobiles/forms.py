from django import forms
from .models import Mobile
from django.core import validators


mobiles_color = [
    ('white', 'سفید'),
    ('black', 'مشکی'),
    ('gold', 'طلایی'),
    ('silver', 'نقره ای'),
    ('blue', 'آبی'),
]

class MobileForm(forms.Form):

    brand_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'نام برند را وارد کنید'}),
                               label='نام برند')

    brand_nationality = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' ملیت برند را وارد کنید'}),
                               label='ملیت برند')
    model = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' مدل گوشی را وارد کنید'}),
                               label='مدل گوشی')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': ' قیمت را وارد کنید','min':'0','oninput':'validity.valid||(value="-");'}),
                               label='قیمت')
    color = forms.ChoiceField(widget=forms.Select(attrs={'placeholder': ' رنگ را وارد کنید'}),
                               label=' رنگ', choices=mobiles_color)
    resulation = forms.FloatField(widget=forms.NumberInput(attrs={'placeholder': 'سایز صفحه را وارد کنید','min':'0','oninput':'validity.valid||(value="-");'}),
                               label='سایز صفحه نمایش')     
    is_available = forms.BooleanField(required=False, 
                                label='وضعیت موجودی')
    manufacturer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': ' کشور سازنده وارد کنید'}),
                               label='کشور سازنده')    

    def clean_model(self):
        model = self.cleaned_data.get('model')
        is_exist_model = Mobile.objects.filter(model = model).exists()
        if is_exist_model:
            raise forms.ValidationError('مدل مورد نظر موجود می باشد.')
        return model

