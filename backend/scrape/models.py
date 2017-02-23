from decimal import Decimal

from django.db import models

from datetime import date


#TODO: fix this for django 1.10, then assign to price (currently IntegerField)
# class CurrencyField(models.DecimalField):
#     """
#     Custom currency field, returns two decimal places
#     """
#
#     __metaclass__ = models.SubfieldBase
#
#     def to_python(self, value):
#         try:
#             return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
#         except AttributeError:
#             return None


class CraigslistPosting(models.Model):
    """ Model for an individual housing listing scraped from Craigslist """
    created_on = models.DateTimeField(auto_now_add=True, help_text='when the record was created')
    listed_on = models.DateTimeField(help_text='when the craigslist listing was posted')
    rent = models.IntegerField(help_text='monthly rent')
    cl_id = models.BigIntegerField(unique=True, help_text='craigslist ID of listing')
    # DecimalField to handle 1.5 bedroom or bathroom designations
    bedrooms = models.DecimalField(null=True, max_digits=3, decimal_places=1, help_text='number of bedrooms')
    bathrooms = models.DecimalField(null=True, max_digits=3, decimal_places=1, help_text='number of bathrooms')
    sq_ft = models.IntegerField(null=True, help_text='square footage')
    url = models.TextField(help_text='url of original listing from which this info was scraped')
    title = models.TextField(help_text='original title of the listing')
    lat = models.FloatField(null=True, help_text='latitude')
    lon = models.FloatField(null=True, help_text='longitude')

    def __str__(self):
        """ Return useful representation of a for-rent ad"""

        template = "[{tm}]{br} BR {bt} BA, {sq} sqft: ${rn}"
        return template.format(
            tm=self.listed_on,
            br=self.bedrooms,
            bt=self.bathrooms,
            sq=self.sq_ft,
            rn=self.rent
        )

    def __repr__(self):
        """ Return useful representation of a for-rent ad"""

        template = "[{tm}]{br} BR {bt} BA, {sq} sqft: ${rn}"
        return template.format(
            tm=self.listed_on,
            br=self.bedrooms,
            bt=self.bathrooms,
            sq=self.sq_ft,
            rn=self.rent
        )

