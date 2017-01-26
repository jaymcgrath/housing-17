from django.db import models

from decimal import Decimal

class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None


# Create your models here.

class CraigslistPosting(models.Model):
    """
    Model for an individual housing listing scraped from Craigslist
    """
    district = models.CharField(max_length=256, help_text='neighborhood according to craigslist')
    price = CurrencyField(help_text='monthly rent')
    bedrooms = DecimalField(null=True, help_text='Number of bedrooms')
    bathrooms = DecimalField(null=True, help_text='Number of bathrooms')
    url = TextField(null=True, help_text='URL from which this info was scraped')
    title = TextField(null=True, help_text='original title of the listing')
    lon = models.FloatField(help_text='longitude')
    lat = models.FloatField(help_text='latitude')