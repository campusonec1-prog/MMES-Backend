from django.db import models

class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'location_country'

    def __str__(self):
        return self.country_name

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states', db_column='country_id')

    class Meta:
        db_table = 'location_state'

    def __str__(self):
        return self.state_name

class District(models.Model):
    district_id = models.AutoField(primary_key=True)
    district_name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='districts', db_column='state_id')

    class Meta:
        db_table = 'location_district'

    def __str__(self):
        return self.district_name

class Taluk(models.Model):
    taluk_id = models.AutoField(primary_key=True)
    taluk_name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='taluks', db_column='district_id')

    class Meta:
        db_table = 'location_taluk'

    def __str__(self):
        return self.taluk_name
