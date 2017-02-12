from django.test import TestCase
from scrape.cron import DailyScraperCronJob
from datetime import datetime, timezone

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
