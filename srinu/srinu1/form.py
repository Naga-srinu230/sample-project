from django import forms
from srinu1.models import Srinu

class SrinuForm(forms.ModelForm):
    class Meta:
        model = Srinu
        fields ="__all__"

class EmpForm(forms.Form):
    firstname = forms.CharField(label="Enter First Name",max_length=50)
    lastname =forms.CharField(label = "Enter last name",max_length=50)
    email = forms.EmailField(label = "Enter Email")
    file = forms.FileField()
    