from django.shortcuts import render
from .forms import MobileForm
from mobiles.models import Mobile

def create_mobile(request):
    
    mobile_form = MobileForm(request.POST or None)
    if mobile_form.is_valid():
        brand_name = mobile_form.cleaned_data.get('brand_name')
        brand_nationality = mobile_form.cleaned_data.get('brand_nationality')
        model = mobile_form.cleaned_data.get('model')
        price = mobile_form.cleaned_data.get('price')
        color = mobile_form.cleaned_data.get('color')
        resulation = mobile_form.cleaned_data.get('resulation')
        is_available = mobile_form.cleaned_data.get('is_available')
        manufacturer = mobile_form.cleaned_data.get('manufacturer')

        Mobile.objects.create(
            brand_name = brand_name, 
            brand_nationality = brand_nationality,
            model = model,
            price = price,
            color = color,
            resulation = resulation,
            is_available = is_available,
            manufacturer = manufacturer)

        mobile_form = MobileForm()    

    context= {
        'form' : mobile_form
    }
    return render(request, 'index.html', context)
