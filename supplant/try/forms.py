from django import forms

class GetInput(forms.Form):
  to_fix = forms.CharField(label="", max_length=2000, required=False, widget=forms.Textarea)