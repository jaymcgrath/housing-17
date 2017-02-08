"""
Scraper classes for regular fetching of portland housing data
"""

import re
from bs4 import BeautifulSoup
from craigslist import requests_get
from craigslist import CraigslistHousing


class PDXCraigslistHousing(CraigslistHousing):
    """Scrape Portland, OR craigslist housing listings.

    Subclasses generic CL Housing scraper, customized to point at PDX metro
    This casts a wide-ish net, and will need some location filtering

    This scraper should be run daily since it uses
    CL's 'posted today' feature to filter results on the server side.

    """

    def customize_result(self, result, html_row):
        """
        Add custom/delete/alter fields to result.
        Here, we get # bedrooms, baths, and sqft
        """

        response = requests_get(result['url'], logger=self.logger)
        self.logger.info('GET %s', response.url)
        self.logger.info('Response code: %s', response.status_code)

        if response.ok:
            soup = BeautifulSoup(response.content, 'html.parser')

            # Get the bedrooms baths sqft badges
            badges = soup.find('p', {'class': 'attrgroup'}).get_text()

            if badges:
                try:
                    num_br = re.search(r'(?P<num_br>\d+)BR', badges).group('num_br')
                except:
                    num_br = None

                try:
                    num_ba = re.search(r'(?P<num_ba>\d+)Ba', badges).group('num_ba')
                except:
                    num_ba = None

                try:
                    sq_ft = re.search(r'(?P<sqft>\d+)ft2', badges).group('sqft')
                except:
                    sq_ft = None

                custom_result = {
                                'bedrooms': num_br,
                                'bathrooms': num_ba,
                                'sq_ft': sq_ft
                            }

                result.update(custom_result)

        return result


def todays_listings():
    """
    Creates a craigslist housing scraper, setting the following search params:
    Specific vars for the local area:
        site = 'portland'
        area = 'mlt'
        category = 'apa'

        # Add custom filters
        filters.update({
                       'bundleDuplicates': 1,
                       'postedToday': 1
                       })

    :return: Generator of listings
    """

    scraper = PDXCraigslistHousing(site='portland', area='mlt', category='apa')

    # Tell the scraper to be on the lookout for our br/ba/sqft custom result fields
    scraper.custom_result_fields = True

    # Add a few custom filters to query
    custom_filters = dict(postedToday=1, collapseDuplicates=1)
    scraper.filters.update(custom_filters)

    return scraper.get_results(sort_by='newest', geotagged=True)






