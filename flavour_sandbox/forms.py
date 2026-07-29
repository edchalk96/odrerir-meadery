from django import forms
from django_select2 import forms as s2forms
from .models import FlavourSandboxIdea, Comment


class IdeaForm(forms.ModelForm):
    class Meta:
        model = FlavourSandboxIdea
        fields = ['title', 'ingredients', 'mead_type', 'content',]
        widgets = {'mead_type': s2forms.Select2MultipleWidget(attrs={'data-placeholder': 'Leave blank or select mead type...', 'data-allow-clear': 'true', 'style': 'width: 100%'})}

    def __init__(self, *args, **kwargs):
        super(IdeaForm, self).__init__(*args, **kwargs)
        self.fields['mead_type'].required = False


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)