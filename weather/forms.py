from .models import City
from django.forms import ModelForm, TextInput

class cityform(ModelForm):
    class Meta:
        model = City
        fields = ['Name']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'})}
