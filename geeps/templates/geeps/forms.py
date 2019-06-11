from django import forms

from geeps.models import PrintingRequest


class PrintingRequestForm(forms.ModelForm):
    class Meta:
        model = PrintingRequest
        # fields = ('lastName', 'firstName', 'mail', 'phone')
        fields = ('lastName', 'firstName', 'mail', 'phone', 'office', 'date', 'widthFormat', 'heightFormat', 'comments')


