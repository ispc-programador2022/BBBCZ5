import json

from .models import WorldPopulationByCountryName

class importService():
    

    @classmethod
    def importWorldPopulationData(cls):
        filename = "C:/Users/Usuario/Desktop/Romina/Proyecto_ISPC_IA/db/poblacion.json"
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                WorldPopulationByCountryName.objects.create(name=item['Pais'], population=item['Poblacion'],
                                                            area=item['Superficie (Km2)'], density=item['Densidad (P/Km2)'])
        return "OK"


