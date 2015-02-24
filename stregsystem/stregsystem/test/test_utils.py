from django.test import TestCase
from stregsystem import utils


class TestGrouper(TestCase):
    pass


class TestPhoneLetterConverter(TestCase):
    def test_phone_letter_converter_lower(self):
        self.assertEqual(utils.phone_letter_converter('5052treo'), '50527625')

    def test_phone_letter_converter_upper(self):
        self.assertEqual(utils.phone_letter_converter('5052TREO'), '50527625')
