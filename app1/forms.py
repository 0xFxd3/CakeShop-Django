from django import forms
from django.forms import ModelForm
from .models import customerPurchaseInfo

class myForm(ModelForm):
    class Meta:
        model = customerPurchaseInfo
        fields = {"customer_ref","name","address","email","date","membership"}
        label = {"Customer_Ref","Name","Address","Email","Date","Membership"}
        widgets = {
            "customer_ref":forms.NumberInput(attrs={"class":"form-control"}),
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "date":forms.DateInput(attrs={"class":"form-control"}),
            "membership":forms.NumberInput(attrs={"class":"form-control"}),
        }