from django import forms
from .models import BankModel, BranchModel
from django.contrib.auth.models import User

class BankForm(forms.ModelForm):
    class Meta:
        model = BankModel
        fields = ['owner', 'bankname', 'swift_code', 'inst_num', 'description']

class BranchForm(forms.ModelForm):
    class Meta:
        model = BranchModel
        fields = ['bank','name', 'transit_num', 'address', 'email', 'capacity']

        

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__' 