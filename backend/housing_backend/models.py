from django.db import models


class Affordable(models.Model):
    affordable = models.BooleanField()
    demographic = models.ForeignKey('Demographic', on_delete=models.CASCADE)
    housing_size = models.ForeignKey('HousingSize', on_delete=models.CASCADE)
    neighborhood = models.ForeignKey('Neighborhood', on_delete=models.CASCADE)

    def __str__(self):
        return self.group_typ + self.group_type + self.housing_size


class Demographic(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class HousingSize(models.Model):
    household_type = models.CharField(max_length=50)

    def __str__(self):
        return self.household_type


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    report_year = models.ForeignKey('ReportYear', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ReportYear(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)
