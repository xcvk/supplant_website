from django import forms

class TestInput(forms.Form):
  test_input = forms.CharField(label="", max_length=2000, required=False)

class to_supplant(forms.Form):
  input_text = forms.CharField(label="", max_length=2000, required=False)