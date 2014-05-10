from django import forms

from market.models import Treet


class TreetCreationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TreetCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Treet
        fields = ['title', 'description', 'video']
