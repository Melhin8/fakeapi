from django.forms import ModelForm
from django import forms
from list.models import Elfs

class AddForm(ModelForm):
    class Meta:
      model = Elfs
      fields = ['name', 'old', 'genus']
form = AddForm()

class SearchForm(ModelForm):
    class Meta:
      model = Elfs
      fields = ['name']
form = SearchForm()

class Sort(forms.Form):
  CHOICES = (('null', 'Sort by',), ('name', 'Name',), ('old', 'Old',), ('genus', 'Genus',))
  
  sort = forms.ChoiceField(
                          widget=forms.Select(attrs={'onchange': 'this.form.submit();'}), 
                          choices=CHOICES, 
                          required=True, 
                          )
  