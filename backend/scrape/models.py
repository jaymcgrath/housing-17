from django.db import models

from decimal import Decimal

class CurrencyField(models.DecimalField):
    "Custom currency field, returns two decimal places"
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
    created_on = models.DateTimeField(auto_now_add=True, help_text='when the record was created')
    listed_on = models.DateTimeField(help_text='when the craigslist listing was posted')
    district = models.CharField(max_length=256, help_text='neighborhood according to craigslist')
    price = CurrencyField(help_text='monthly rent')
    bedrooms = DecimalField(null=True, help_text='number of bedrooms')
    bathrooms = DecimalField(null=True, help_text='number of bathrooms') # Decimal to handle 1.5 bath, etc
    sq_ft = IntegerField(null=True, help_text='square footage')
    url = TextField(help_text='url of original listing from which this info was scraped')
    title = TextField(help_text='original title of the listing')
    lat = models.FloatField(null=True, help_text='latitude')
    lon = models.FloatField(null=True, help_text='longitude')


