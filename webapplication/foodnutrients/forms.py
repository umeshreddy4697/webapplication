from django import forms
from foodnutrients.models import nutrients


class nutrientsForm(forms.ModelForm):
    class Meta:
        model = nutrients
        fields ="__all__"
