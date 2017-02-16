import pandas as pd
from .models import *
from django.conf import settings
import requests
import io

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
        ry, _ = ReportYear.objects.get_or_create(year=row['NHM_ReportYear'])
        n, _ = Neighborhood.objects.get_or_create(name=row['NP_ID'],report_year=ry)
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

def loadNeighborhoodProfiles(file):
    dframe = pd.read_csv(file)

    for index, row in dframe.iterrows():
        ry, _ = ReportYear.objects.get_or_create()
        profile, _ = Neighborhood.objects.get_or_create(
                name=row['NP_Title'],
                report_year=ry
        )
        profile.save()

     
### MAIN ###
fileDemo = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/DemographicProfiles.csv"
fileNeighborhoods = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/NeighborhoodProfiles.csv"
fileAfford = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/SoHAffordabilityDatabyNeighborhoodUpload.csv"
fileRent = "https://raw.githubusercontent.com/hackoregon/housing-17/datasources/NeighborhoodHousingMarket.csv"
loadDemographics(fileDemo)
loadNeighborhoodProfiles(fileNeighborhoods)
loadAffordability(fileAfford)
loadNeighborhoodRent(fileRent)
