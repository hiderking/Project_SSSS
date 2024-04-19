from django import forms
from schoolap.models import ViewerContacts
class ViewerContactsForm(forms.Form):
    class Meta:
        model=ViewerContacts
        fields=['id','fullname','subject','message','submitDate']
