"""
Cron classes for scheduling craigslist scraper
"""
from django_cron import CronJobBase, Schedule
from .scrapers import todays_listings
from .models import CraigslistPosting
from time import sleep
import random
import re
import logging


class DailyScraperCronJob(CronJobBase):
    """ Scrape craigslist housing posts and add them to database

    This cron will create an instance of the PDXCraigslistHousing scraper class.
    This class exposes a generator of the relevant listings, calls will be slept randomly for 'compassionate scraping.'

    """

    RUN_AT_TIMES = ['11:30']  # Run once daily at 11:30 AM
    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'scrape.daily_scrape_cron_job'  # a unique code

    @staticmethod
    def clean_price(price):
        """ Remove non-digit characters from price. """
        match = re.search(r'^\$?(?P<digits>[0-9]+)', price)
        return match.group('digits')

    def do(self, listing_source=todays_listings):
        """ Create a scraper for only today's results and save each result as CraigslistPosting model instance

        :param: listing_source: generator function of listings to iterate over

        """

        # Iterate over listings, save each one to django Model

        for listing in listing_source():
            """Save each listing to database and sleep before processing the next one"""

            # TODO - Look up relevant portland neighborhood using GIS and census housing track shapefiles

            # Web data is messy - just log errors and move on to the next listing
            try:
                # Strip dollar sign and possible trailing cents from the rent amount:
                cleaned_price = self.clean_price(listing['price'])

                # Get lat, lon if available, otherwise set to null
                try:
                    lat, lon = listing['geotag']
                except TypeError:
                    lat, lon = None, None

                # Build kwargs dict
                listing_attrs = {
                    'listed_on': listing['datetime'],
                    'rent': cleaned_price,
                    'cl_id': listing['id'],
                    'bedrooms': listing['bedrooms'],
                    'bathrooms': listing['bathrooms'],
                    'sq_ft': listing['sq_ft'],
                    'url': listing['url'],
                    'title': listing['name'],
                    'lat': lat,
                    'lon': lon,
                }

                this_posting = CraigslistPosting(**listing_attrs)
                this_posting.save()
            except:
                logging.exception('')


            print("saved", this_posting)

            # Sleep randomly betwen 0 and 2 seconds
            sleep_seconds = random.random() * 2
            sleep(sleep_seconds) # Zzzz







