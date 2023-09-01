from django import forms

class userForm(forms.Form):
    n1 = forms.CharField(label='email')
    n2 = forms.ChoiceField(label='passwd' , widget= forms.TextInput)