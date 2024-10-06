from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)  # Capital City
    area = models.FloatField()  # Area in km²
    population = models.PositiveIntegerField()
    number_of_districts = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class District(models.Model):
    province = models.ForeignKey(Province, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)  # Capital of the district
    area = models.FloatField()  # Area in km²
    population = models.PositiveIntegerField()  # Population (2021)

    def __str__(self):
        return self.name

class Ward(models.Model):
    district = models.ForeignKey(District, related_name='wards', on_delete=models.CASCADE)
    ward_no = models.PositiveIntegerField()  # Ward number
    name = models.CharField(max_length=100)  # Name of the ward

    def __str__(self):
        return f"Ward {self.ward_no} - {self.name}"

class Place(models.Model):
    ward = models.ForeignKey(Ward, related_name='places', on_delete=models.CASCADE)  # Link to Ward
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)  # Optional description

    def __str__(self):
        return self.name
