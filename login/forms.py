from django import forms
from .models import Region, Comuna

class RegistroForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label='Región')
    comuna = forms.ModelChoiceField(queryset=Comuna.objects.none(), label='Comuna')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'region' in self.data:
            try:
                region_id = int(self.data.get('region'))
                self.fields['comuna'].queryset = Comuna.objects.filter(region_id=region_id).order_by('nombre')
            except (ValueError, TypeError):
                pass
