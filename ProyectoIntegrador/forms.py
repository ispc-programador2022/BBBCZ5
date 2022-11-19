from django import forms 
from ProyectoIntegrador.models import *

class FormPoblacion(forms.Form):
    pais = forms.CharField(max_length=50,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
    poblacion = forms.CharField(max_length=50,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))
    superficie = forms.CharField(max_length=50,required=False,widget=forms.Textarea(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        pais = cleaned_data.get("pais")
        poblacion = cleaned_data.get("poblacion")
        superficie = cleaned_data.get("superficie")

        if not pais and not poblacion and not superficie:
            raise forms.ValidationError("Debe ingresar al menos un dato")

        return cleaned_data

    def save(self):
        pais = self.cleaned_data.get("pais")
        poblacion = self.cleaned_data.get("poblacion")
        superficie = self.cleaned_data.get("superficie")
        WorldPopulationByCountryName.objects.create(name=pais, population=poblacion, area=superficie)

    def search(self):
        pais = self.cleaned_data.get("pais")
        poblacion = self.cleaned_data.get("poblacion")
        superficie = self.cleaned_data.get("superficie")
        if pais:
            return WorldPopulationByCountryName.objects.filter(name=pais)
        elif poblacion:
            return WorldPopulationByCountryName.objects.filter(population=poblacion)
        elif superficie:
            return WorldPopulationByCountryName.objects.filter(area=superficie)
    