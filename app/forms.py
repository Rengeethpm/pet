
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Register, Pet


class BuyerRegisterForm(UserCreationForm):
    class Meta:
        model = Register
        fields = ('username','password1', 'password2', 'address', 'email', 'contact_no')


class PetRegisterForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('breed', 'age', 'medical_certificate')
















