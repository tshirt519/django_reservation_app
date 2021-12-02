from django import forms

class ProfileForm(forms.Form):
  first_name = forms.CharField(max_length=30, label='姓')
  last_name = forms.CharField(max_length=30, label='名')