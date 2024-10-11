from django.db import models

class Province(models.Model):
    name = models.CharField(max_length=100, primary_key=True,unique=True)  # Using name as primary key
    headquarters = models.CharField(max_length=100)
    area = models.FloatField()
    population = models.PositiveIntegerField()
    number_of_districts = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class District(models.Model):
    province = models.ForeignKey(Province, related_name='districts', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)  # Using name as primary key
    headquarters = models.CharField(max_length=100)
    area = models.FloatField()
    population = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class City(models.Model):
    district = models.ForeignKey(District, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, primary_key=True)  # Using name as primary key
    city_type = models.CharField(max_length=20, choices=[
        ('metropolitan', 'Metropolitan'),
        ('sub_metropolitan', 'Sub-Metropolitan'),
        ('municipality', 'Municipality'),
        ('rural_municipality', 'Rural Municipality')
    ])

    def __str__(self):
        return self.name

class Ward(models.Model):
    city = models.ForeignKey(City, related_name='wards', on_delete=models.CASCADE)
    ward_no = models.PositiveIntegerField()  # Ward number
    name = models.CharField(max_length=100,primary_key=True)  # Using name as primary key

    class Meta:
            unique_together = ('city', 'ward_no')  # Ensures that within a city, ward_no is unique

    def __str__(self):
            return f'Ward {self.ward_no}, {self.city.name}'

class Place(models.Model):
    city = models.ForeignKey(City, related_name='places', on_delete=models.CASCADE,default="Pokhara")
    ward = models.ForeignKey(Ward, related_name='places', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,primary_key=True)  
    description = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('city', 'ward', 'name')
    def __str__(self):
        return f'{self.name}, {self.ward.name}, {self.city.name}'
