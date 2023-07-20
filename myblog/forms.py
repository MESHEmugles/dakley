from django import forms

from blogstory.models import TutorialComment



class TutorialCommentForm(forms.ModelForm):
    name = forms.CharField(widget =forms.TextInput(attrs={'class':'user', 'placeholder':'Name'}))
    email = forms.EmailField(widget=forms.EmailInput( attrs={'class':'user', 'placeholder':'Email'}))
    comment = forms.CharField(widget = forms.Textarea( attrs={'class':'px-2 w-100', 'placeholder':'write something...'}))

    class Meta:
        model = TutorialComment
        fields = ['name','email','comment',]





