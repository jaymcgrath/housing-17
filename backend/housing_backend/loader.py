import pandas as pd
from .models import *
from django.conf import settings
import requests
import io
"""
This script is meant to be used with this specific dataset
https://drive.google.com/file/d/0B0810KzsNR3mUDkzdERQNmc3U00/view?usp=sharing
"""
#TODO:
#   (1/31) - Update to take in new csv files: NeighborhoodProfiles, NeighborhoodHousingMarket and Demographic profiles

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

# Black demographic isnt loading in correctly - STILL NEEDS WORKS
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
        rent, _ = NeighborhoodRent.objects.get_or_create(
                nh_id=row['NP_ID'],
                housing_size=row['NHM_UnitSize'],
                rent_amt=row['NHM_Rent_Amt']
        )
        rent.save()

def loadNeighborhoodProfiles(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        profile, _ = NeighborhoodRent.objects.get_or_create(
                nh_id=row['NP_Title']
        )
        profile.save()

# TODO: Standardize place to load data csv from - maybe load it from AWS S3? Right now it's just set up for Eric's local environment
     
### MAIN ###
fileDemo = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/DemographicProfiles.csv"
fileNeighborhoods = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/NeighborhoodProfiles.csv"
fileAfford = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv"
fileRent = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/NeighborhoodHousingMarket.csv"
loadDemographics(fileDemo)
loadAffordability(fileAfford)
#loadNeighborhoodProfiles(fileNeighborhoods)
#loadNeighborhoodRent(fileRent)
