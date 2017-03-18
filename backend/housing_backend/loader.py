import pandas as pd
from .models import *
from django.conf import settings
import requests
import io
import os


def loadAffordability(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create(year=row['Year'])
        n, _ = Neighborhood.objects.get_or_create(name=row['Neighborhood'],report_year=ry)
        d, _ = Demographic.objects.get_or_create(name=row['Demographic'])
        h, _ = HousingSize.objects.get_or_create(household_type=row['Unit_Size'])
        ry.save()
        d.save()
        h.save()
        n.save()
        if row['Affordable_ind'] == 'Y':
            aff = True
        elif row['Affordable_ind'] == 'N':
            aff = False

        a = Affordable(
            affordable=aff,
            demographic=d,
            housing_size=h,
            neighborhood=n,
        )
        a.save()


def loadDemographics(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        demo, _ = Demographic.objects.get_or_create(
                name=row['DP_TITLE'],
                income_median=row['DP_INCOME_MEDIAN'],
                housing_budget=row['DP_HOUSINGBUDGET'],
                per_with_children=row['DP_PERCENT_WITH_CHILDREN'],
                household_comp=row['DP_HOUSEHOLD_COMP']
        )
        demo.save()


def loadNeighborhoodRent(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        print(row)
        ry, _ = ReportYear.objects.get_or_create(year=row['NHM_ReportYear'])
        n, _ = Neighborhood.objects.get_or_create(id__exact=row['NP_ID'])
        h, _ = HousingSize.objects.get_or_create(household_type=row['NHM_UnitSize'])
        ry.save()
        n.save()
        h.save()
        rent, _ = NeighborhoodRent.objects.get_or_create(
                nh_id=n,
                housing_size=h,
                rent_amt=row['NHM_Rent_Amt']
        )
        rent.save()



# """ Neighborhoods are currently loaded in the loadAffordability function
#
#     When uncommenting this, also uncomment the function call at the bottom of the file
#
# """
#
#
# # def loadNeighborhoodProfiles(file):
# #     dframe = pd.read_csv(file)
# #
# #     for index, row in dframe.iterrows():
# #         ry, _ = ReportYear.objects.get_or_create()
# #         profile, _ = Neighborhood.objects.get_or_create(
# #                 name=row['NP_Title'],
# #                 report_year=ry
# #         )
# #         profile.save()



"""
    Note: Uncomment loadHousingSUpplyandPermits and its call at the bottom of the file once report_year is removed
    from the Neighborhood model
"""

# def loadHousingSupplyandPermits(file):
#     """Load housing supply and permit data into respective models"""
#
#     dframe = pd.read_csv(file)
#
#     for index, row in dframe.iterrows():
#         ry, _ = ReportYear.objects.get_or_create(year=row['ReportYear'])
#         n, _ = Neighborhood.objects.get_or_create(name=row['Neighborhood'].strip())
#         hs = HousingSupply(
#                             neighborhood= n,
#                             report_year= ry,
#                             single_units= row['SingleFamilyUnits'],
#                             multi_units= row['MultiFamilyUnits']
#         )
#         hs.save()
#
#         hp = HousingPermits(
#                             neighborhood=n,
#                             report_year=ry,
#                             single_permits=row['SingleFamilyPermits'],
#                             multi_permits=row['MultiFamilyPermits']
#         )
#         hp.save()
#



### MAIN ###
fileDemo = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/DemographicProfiles.csv"
fileNeighborhoods = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/NeighborhoodProfiles.csv"
fileAfford = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv"
fileRent = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/NeighborhoodHousingMarket.csv"
fileSupply = "https://raw.githubusercontent.com/hackoregon/housing-backend/datasources/HousingSupplyAndPermits.csv"

loadDemographics(fileDemo)

#loadNeighborhoodProfiles(fileNeighborhoods)

loadAffordability(fileAfford)
loadNeighborhoodRent(fileRent)
#loadHousingSupplyandPermits(fileSupply)

