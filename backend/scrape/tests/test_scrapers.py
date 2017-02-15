from unittest import TestCase

from httmock import urlmatch, HTTMock

from scrape.scrapers import PDXCraigslistHousing


class TestPDXCraigslistHousing(TestCase):
    """ Test web scraper class """

    def test_custom_result_parse_valid_html(self):
        """ Test that scraper is correctly parsing html """

        # Create mock craigslist site
        @urlmatch(netloc=r'(.*\.)?craigslist\.org$')
        def craigslist_mock(url, request):
            return '<p class="attrgroup"><span><b>3BR</b> / <b>2Ba</b></span><span><b>1200</b>ft<sup>2</sup></span>' \
                   '<span class="housing_movein_now property_date" data-date="2017-03-05" data-today_msg="available now">' \
                   'available mar 5</span></p>'

        # open context to patch
        with HTTMock(craigslist_mock):
            test_scraper = PDXCraigslistHousing()
            test_scraper.custom_result_fields = True

            result_fixture = {
                            'price': '$2000',
                            'id': '6003436469',
                            'has_map': True,
                            'datetime': '2017-02-14 10:10',
                            'has_image': True,
                            'name': 'Woodstock & Reed Neighborhood-- steps from shopping & conveniences',
                            'url': 'http://portland.craigslist.org/mlt/apa/6003436469.html',
                            'geotag': None,
                            'where': 'SE 48th/ SE Woodstock'
            }

            custom_result = test_scraper.customize_result(result=result_fixture, html_row="")


        # custom_result should have empty fields for bedrooms, bathrooms, and sq_ft
        self.assertEquals(int(custom_result['bedrooms']), 3, "Bedrooms should be 3")
        self.assertEquals(int(custom_result['bathrooms']), 2, "Bathrooms should be 2")
        self.assertEquals(int(custom_result['sq_ft']), 1200, "sq_ft should be 1200")

    def test_custom_result_raise_value_error_if_missing_attrgroup_class(self):
        """ Test that scraper ignores missing values and assigns None """

        # Create mock craigslist site
        @urlmatch(netloc=r'(.*\.)?craigslist\.org$')
        def craigslist_mock(url, request):
            return '<html></html>'

        # open context to patch
        with HTTMock(craigslist_mock):
            test_scraper = PDXCraigslistHousing()
            test_scraper.custom_result_fields = True

            result_fixture = {
                'price': '$2000',
                'id': '6003436469',
                'has_map': True,
                'datetime': '2017-02-14 10:10',
                'has_image': True,
                'name': 'Woodstock & Reed Neighborhood-- steps from shopping & conveniences',
                'url': 'http://portland.craigslist.org/mlt/apa/6003436469.html',
                'geotag': None,
                'where': 'SE 48th/ SE Woodstock'
            }
            with self.assertRaises(AttributeError) as context:
                test_scraper.customize_result(result=result_fixture, html_row="")

                self.assertTrue('Unable to find correct html elements in page (p tag with class "attrgroup")' in context.exception)




    def test_custom_result_handle_empty_attrgroup_values(self):
        """ Test that scraper is correctly parsing html """

        # Create mock craigslist site
        @urlmatch(netloc=r'(.*\.)?craigslist\.org$')
        def craigslist_mock(url, request):
            return '<p class="attrgroup"><span><b></b> / <b></b></span><span><b></b>ft<sup>2</sup></span>' \
                   '<span class="housing_movein_now property_date" data-date="2017-03-05" data-today_msg="available now">' \
                   'available mar 5</span></p>'

        # open context to patch
        with HTTMock(craigslist_mock):
            test_scraper = PDXCraigslistHousing()
            test_scraper.custom_result_fields = True

            result_fixture = {
                            'price': '$2000',
                            'id': '6003436469',
                            'has_map': True,
                            'datetime': '2017-02-14 10:10',
                            'has_image': True,
                            'name': 'Woodstock & Reed Neighborhood-- steps from shopping & conveniences',
                            'url': 'http://portland.craigslist.org/mlt/apa/6003436469.html',
                            'geotag': None,
                            'where': 'SE 48th/ SE Woodstock'
            }

            custom_result = test_scraper.customize_result(result=result_fixture, html_row="")


        # custom_result should have empty fields for bedrooms, bathrooms, and sq_ft
        self.assertIsNone(custom_result['bedrooms'], "Bedrooms should be None")
        self.assertIsNone(custom_result['bathrooms'], "Bathrooms should be None")
        self.assertIsNone(custom_result['sq_ft'], "sq_ft should be None")






