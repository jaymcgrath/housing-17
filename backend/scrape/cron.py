"""
Cron classes for scheduling craigslist scraper
"""
import logging
import random
import re
from time import sleep

from django.db import IntegrityError

from django_cron import CronJobBase, Schedule

from .models import CraigslistPosting
from .scrapers import todays_listings

import datetime
from django.utils import timezone




class DailyScraperCronJob(CronJobBase):
    """ Scrape craigslist housing posts and add them to database

    This cron will create an instance of the PDXCraigslistHousing scraper class.
    This class exposes a generator of the relevant listings, calls will be slept randomly for 'compassionate scraping.'

    """

    RUN_EVERY_MINS = ['360']  # Run four times daily
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
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

                # create TZ aware datetime - set TZ to UTC
                try:
                    listed_on = datetime.datetime.strptime(listing['datetime'], "%Y-%m-%d %H:%M")
                    listed_on.replace(tzinfo=timezone.utc)
                except (TypeError, ValueError):
                    # Set the listing time to when it was scraped in the case of missing or bad data
                    listed_on = datetime.datetime.now(tz=timezone.utc)

                # Build kwargs dict
                listing_attrs = {
                    'listed_on': listed_on,
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
                try:
                    this_posting.save()
                    print("saved", this_posting)
                except IntegrityError:
                    # Record already in database or malformed. Ignore and move to next one
                    pass
            except:
                logging.exception('')

            #  Sleep randomly betwen 0 and 2 seconds
            sleep_seconds = random.random() * 2
            sleep(sleep_seconds)  # Zzzz
