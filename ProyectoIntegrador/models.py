import uuid

from django.db import models


class WorldPopulationByCountryName(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(db_column='name', max_length=255, default="")
    population = models.CharField(db_column='population', max_length=255, default="")
    area = models.CharField(db_column='area', max_length=255, default="")
    density = models.CharField(db_column="Density", max_length=255, default="")

    class Meta:
        db_table = 'world_pop_by_country_name'


