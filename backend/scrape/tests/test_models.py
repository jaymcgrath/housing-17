from django.test import TestCase
from scrape.models import CraigslistPosting
from datetime import datetime, timezone

# models test
class CraigslistPostingTest(TestCase):
    """ Test creation of CraiglistPosting model"""

    def create_craigslist_posting(self, **kwargs):
        attrs = {
            'listed_on': datetime(2017, 1, 31, 12, 16, tzinfo=timezone.utc),
            'rent': '690',
            'cl_id': '5994893759',
            'bedrooms': '3.5',
            'bathrooms': '1.5',
            'sq_ft': '1920',
            'url': 'http://portland.craigslist.org/mlt/apa/5994893759.html',
            'title': 'stunning 3.5 br 1.5 ba charmer! OH YEAH!!',
            'lat': '45.487576',
            'lon': '-122.673211',
        }

        # Allow override of specific values via kwargs dict
        for k, v in kwargs.items():
            attrs[k] = v

        return CraigslistPosting.objects.create(**attrs)

    def test_craigslistposting_creation(self):
        p = self.create_craigslist_posting()
        self.assertTrue(isinstance(p, CraigslistPosting))

    def test_craisglist_posting_creation_no_bedrooms(self):
        # Verify bedroom field accepts null value.
        p = self.create_craigslist_posting(bedrooms=None)
        self.assertTrue(isinstance(p, CraigslistPosting))
        self.assertEqual(p.bedrooms, None)

    def test_craisglist_posting_creation_no_bathrooms(self):
        # Verify bathroom field accepts null value.
        p = self.create_craigslist_posting(bathrooms=None)
        self.assertTrue(isinstance(p, CraigslistPosting))
        self.assertEqual(p.bathrooms, None)

    def test_craisglist_posting_creation_no_cl_id(self):
        # Verify bathroom field accepts null value.
        p = self.create_craigslist_posting(cl_id=None)
        self.assertTrue(isinstance(p, CraigslistPosting))
        self.assertEqual(p.cl_id, None)

    def test_craisglist_posting_creation_no_lat(self):
        # Verify bathroom field accepts null value.
        p = self.create_craigslist_posting(lat=None)
        self.assertTrue(isinstance(p, CraigslistPosting))
        self.assertEqual(p.lat, None)

    def test_craisglist_posting_creation_no_lon(self):
        # Verify bathroom field accepts null value.
        p = self.create_craigslist_posting(lon=None)
        self.assertTrue(isinstance(p, CraigslistPosting))
        self.assertEqual(p.lon, None)


    def test_craigslist_posting_str_method(self):
        p = self.create_craigslist_posting()
        self.assertEqual(p.__str__(), "[2017-01-31 12:16:00+00:00]3.5 BR 1.5 BA, 1920 sqft: $690")

    def test_craigslist_posting_repr_method(self):
        p = self.create_craigslist_posting()
        self.assertEqual(p.__repr__(), "[2017-01-31 12:16:00+00:00]3.5 BR 1.5 BA, 1920 sqft: $690")


