import pytest
from django.db import transaction, IntegrityError
from django.test import TestCase

from scrape.cron import DailyScraperCronJob
from scrape.models import CraigslistPosting

pytestmark = pytest.mark.django_db

class DailyScraperCronJobTest(TestCase):
    """ Test DailyScraperCronJob django_cron class"""

    def create_daily_scraper_cron(self, *args, **kwargs):
        return DailyScraperCronJob()

    def test_daily_scraper_cron_creation(self):
        c = self.create_daily_scraper_cron()
        self.assertTrue(isinstance(c, DailyScraperCronJob))

    def test_daily_scraper_clean_price_method(self):
        """ Test that clean_price returns only digits"""
        c = self.create_daily_scraper_cron()
        self.assertEqual(c.clean_price('$690'), '690')
        self.assertEqual(c.clean_price('$1200.00'), '1200')
        self.assertEqual(c.clean_price('$1300.00\n'), '1300')
        self.assertEqual(c.clean_price('$1300.00;lkjaf98343'), '1300')

    def test_daily_scraper_do_method_saves_to_model(self):
        c = self.create_daily_scraper_cron()

        test_listings = ({
                        'where': '1515 SE 31St Ave, Portland, OR 97214',
                        'datetime': '2017-02-07 18:04',
                        'price': '$1399',
                        'has_map': True,
                        'id': '5994219642',
                        'bathrooms': '1',
                        'name': '\u260e Schedule a Tour Starbucks Gift Card!*',
                        'bedrooms': '1',
                        'geotag': (45.511926, -122.633901),
                        'sq_ft': '511',
                        'has_image': True,
                        'url': 'http://portland.craigslist.org/mlt/apa/5994219642.html'
        },)

        # do method expects a generator as input, so pass in a lambda serving the test fixture
        c.do(listing_source=lambda: test_listings)

        # Retrieve CraisglistPosting instance created by cron.do()
        this_obj = CraigslistPosting.objects.get(pk=1)

        self.assertTrue(isinstance(this_obj, CraigslistPosting),
                        "do method should save CraisglistPosting model instance")
        self.assertEqual(this_obj.rent, int(c.clean_price(test_listings[0]['price'])),
                         "CraigslistPosting object rent should equal cleaned test fixture price")
        self.assertEqual(this_obj.bedrooms, float(test_listings[0]['bedrooms']),
                         "CraigslistPosting object bedrooms should equal test fixture bedrooms")
        self.assertEqual(this_obj.bathrooms, float(test_listings[0]['bathrooms']),
                         "CraigslistPosting object bathrooms should equal test fixture bathrooms")
        self.assertEqual(this_obj.sq_ft, int(test_listings[0]['sq_ft']),
                         "CraigslistPosting object sq_ft should equal test fixture sq_ft")
        self.assertEqual(this_obj.title, test_listings[0]['name'],
                         "CraigslistPosting object title should equal test fixture title")
        self.assertEqual((this_obj.lat, this_obj.lon), tuple(float(x) for x in test_listings[0]['geotag']),
                         "CraigslistPosting object lat should equal test fixture lat")


class DailyScraperCronJobTestBadData(TestCase):
    """ Test that scraper will continue after encountering a corrupted listing """
    def create_daily_scraper_cron(self, *args, **kwargs):
        return DailyScraperCronJob()

    def test_daily_scraper_do_method_handles_type_errors(self):
        c = self.create_daily_scraper_cron()

        test_listings = ({
                             'where': '1515 SE 31St Ave, Portland, OR 97214',
                             'datetime': '2017-02-07 18:04',
                             'price': '$1399',
                             'has_map': True,
                             'id': '',
                             'bathrooms': '1',
                             'name': '\u260e Schedule a Tour Starbucks Gift Card!*',
                             'bedrooms': '',
                             'geotag': (45.511926, -122.633901),
                             'sq_ft': '',
                             'has_image': True,
                             'url': ''
                         },)

        count_before = CraigslistPosting.objects.count()

        # do method expects a generator as input, so pass in a lambda serving the test fixture
        with transaction.atomic():
            c.do(listing_source=lambda: test_listings)

        count_after = CraigslistPosting.objects.count()

        self.assertEqual(count_before, count_after, "Fixture with Null id data should not be saved")

    def test_daily_scraper_do_method_handles_empty_lat_lon(self):
        c = self.create_daily_scraper_cron()

        test_listings = ({
                             'where': '1515 SE 31St Ave, Portland, OR 97214',
                             'datetime': '2017-02-07 18:04',
                             'price': '$1399',
                             'has_map': True,
                             'id': '5994219642',
                             'bathrooms': '1',
                             'name': '\u260e Schedule a Tour Starbucks Gift Card!*',
                             'bedrooms': '1',
                             'geotag': None,
                             'sq_ft': '511',
                             'has_image': True,
                             'url': 'http://portland.craigslist.org/mlt/apa/5994219642.html'
                         },)

        # do method expects a generator as input, so pass in a lambda serving the test fixture
        c.do(listing_source=lambda: test_listings)

        # Retrieve CraisglistPosting instance created by cron.do()
        this_obj = CraigslistPosting.objects.get(pk=1)

        self.assertTrue(isinstance(this_obj, CraigslistPosting),
                        "do method should save CraisglistPosting model instance")
        self.assertEqual(this_obj.rent, int(c.clean_price(test_listings[0]['price'])),
                         "CraigslistPosting object rent should equal cleaned test fixture price")
        self.assertEqual(this_obj.bedrooms, float(test_listings[0]['bedrooms']),
                         "CraigslistPosting object bedrooms should equal test fixture bedrooms")
        self.assertEqual(this_obj.bathrooms, float(test_listings[0]['bathrooms']),
                         "CraigslistPosting object bathrooms should equal test fixture bathrooms")
        self.assertEqual(this_obj.sq_ft, int(test_listings[0]['sq_ft']),
                         "CraigslistPosting object sq_ft should equal test fixture sq_ft")
        self.assertEqual(this_obj.title, test_listings[0]['name'],
                         "CraigslistPosting object title should equal test fixture title")
        self.assertEqual((this_obj.lat, this_obj.lon), (None, None),
                         "CraigslistPosting object lat lon should be null")

    def test_daily_scraper_do_method_handles_empty_date(self):
        c = self.create_daily_scraper_cron()

        test_listings = ({
                             'where': '1515 SE 31St Ave, Portland, OR 97214',
                             'datetime': None,
                             'price': '$1399',
                             'has_map': True,
                             'id': '5994219642',
                             'bathrooms': '1',
                             'name': '\u260e Schedule a Tour Starbucks Gift Card!*',
                             'bedrooms': '1',
                             'geotag': (45.511926, -122.633901),
                             'sq_ft': '511',
                             'has_image': True,
                             'url': 'http://portland.craigslist.org/mlt/apa/5994219642.html'
                         },)

        # do method expects a generator as input, so pass in a lambda serving the test fixture
        c.do(listing_source=lambda: test_listings)

        # Retrieve CraisglistPosting instance created by cron.do()
        this_obj = CraigslistPosting.objects.get(pk=1)

        self.assertTrue(isinstance(this_obj, CraigslistPosting),
                        "do method should save CraisglistPosting model instance")
        self.assertEqual(this_obj.rent, int(c.clean_price(test_listings[0]['price'])),
                         "CraigslistPosting object rent should equal cleaned test fixture price")
        self.assertEqual(this_obj.bedrooms, float(test_listings[0]['bedrooms']),
                         "CraigslistPosting object bedrooms should equal test fixture bedrooms")
        self.assertEqual(this_obj.bathrooms, float(test_listings[0]['bathrooms']),
                         "CraigslistPosting object bathrooms should equal test fixture bathrooms")
        self.assertEqual(this_obj.sq_ft, int(test_listings[0]['sq_ft']),
                         "CraigslistPosting object sq_ft should equal test fixture sq_ft")
        self.assertEqual(this_obj.title, test_listings[0]['name'],
                         "CraigslistPosting object title should equal test fixture title")
        self.assertEqual((this_obj.lat, this_obj.lon), tuple(float(x) for x in test_listings[0]['geotag']),
                         "CraigslistPosting object lat should equal test fixture lat")
        self.assertIsNotNone(this_obj.listed_on, "listed_on should be auto-set to now() if bad or missing value")

class TestDailyScraperDuplicateCLID(TestCase):
    """ Test that a duplicate listing insertion exception will be handle"""

    def create_daily_scraper_cron(self, *args, **kwargs):
        return DailyScraperCronJob()

    def test_duplicate_cl_id_exception_handled(self):
        """ Test that cron job handles duplicate insertions gracefully """
        c = self.create_daily_scraper_cron()

        test_listings = ({
                             'where': '1515 SE 31St Ave, Portland, OR 97214',
                             'datetime': '2017-02-07 18:04',
                             'price': '$1399',
                             'has_map': True,
                             'id': '5994219642',
                             'bathrooms': '1',
                             'name': '\u260e Schedule a Tour Starbucks Gift Card!*',
                             'bedrooms': '1',
                             'geotag': (45.511926, -122.633901),
                             'sq_ft': '511',
                             'has_image': True,
                             'url': 'http://portland.craigslist.org/mlt/apa/5994219642.html'
                         },)

        # do method expects a generator as input, so pass in a lambda serving the test fixture
        c.do(listing_source=lambda: test_listings)

        # try to insert the same record again, should raise an error
        self.assertRaises(IntegrityError, c.do(listing_source=lambda: test_listings),  "Should raise Attribute Error")











