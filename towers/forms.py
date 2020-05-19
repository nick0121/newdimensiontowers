from django import forms

from pages.choices import *




class SearchForm(forms.Form):

    # tower_id = forms.CharField(label='', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'e.g. mastercraft'}))
    tower_id = forms.ChoiceField(choices=MANUFACTURERS, label="", initial='', widget=forms.Select(attrs={'class': 'custom-select', 'style': 'width:200px', 'name': 'selection'}), required=True)

        
        