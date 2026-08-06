from django import forms


class ContactDeveloperForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True)
