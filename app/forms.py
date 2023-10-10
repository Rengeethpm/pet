
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Register, Pet


class BuyerRegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = ('username','password', 'address', 'email', 'contact_no')


class PetRegisterForm(ModelForm):
    class Meta:
        model = Pet
        fields = ('breed', 'age', 'medical_certificate')


class BuyerEditForm(ModelForm):

    class Meta:
        model = Register
        fields = ('username', 'contact_no', 'address', 'email')

















