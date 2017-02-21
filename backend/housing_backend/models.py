from django.db import models


class Affordable(models.Model):
    affordable = models.BooleanField()
    demographic = models.ForeignKey('Demographic', on_delete=models.CASCADE)
    housing_size = models.ForeignKey('HousingSize', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.demographic) + str(self.housing_size) + str(self.neighborhood)


class NeighborhoodRent(models.Model):
    nh_id = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)
    housing_size = models.ForeignKey('HousingSize', on_delete=models.CASCADE)
    rent_amt = models.IntegerField(default=0)

class Demographic(models.Model):
    name = models.CharField(max_length=50)
    income_median = models.IntegerField(default=0)
    housing_budget = models.IntegerField(default=0)
    per_with_children = models.IntegerField(default=0)
    household_comp = models.DecimalField(default=0.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name


class HousingSize(models.Model):
    household_type = models.CharField(max_length=50)

    def __str__(self):
        return self.household_type


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    report_year = models.ForeignKey('ReportYear', on_delete=models.CASCADE)
    #shape_file = models.FieldFile() possibility if shape file data needs to be stored

    def __str__(self):
        return self.name


class ReportYear(models.Model):
    year = models.IntegerField(default=0)

    def __str__(self):
        return str(self.year)
