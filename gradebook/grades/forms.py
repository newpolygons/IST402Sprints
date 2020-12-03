from django import forms


class GradeForm(forms.Form):
    post = forms.CharField()