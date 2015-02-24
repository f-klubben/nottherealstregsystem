from django.test import TestCase
from stregsystem import models
from django.core.exceptions import ValidationError


class MemberPhoneNumberTestCase(TestCase):
    def test_phone_number_set_success_space(self):
        m = models.Member(phone_number='12 34')
        self.assertEqual(m.phone_number, '1234')

    def test_phone_number_set_success_dash(self):
        m = models.Member(phone_number='12-34')
        self.assertEqual(m.phone_number, '1234')

    def test_phone_number_set_success_underscore(self):
        m = models.Member(phone_number='12_34')
        self.assertEqual(m.phone_number, '1234')

    def test_phone_number_format_even(self):
        m = models.Member(phone_number='1234')
        self.assertEqual(m.phone_number_format(), '12 34')

    def test_phone_number_format_odd(self):
        m = models.Member(phone_number='123')
        self.assertEqual(m.phone_number_format(), '1 23')

    def test_phone_number_validator_fail_nothing(self):
        with self.assertRaises(ValidationError):
            models.validate_phone_number('')

    def test_phone_number_validator_fail_long(self):
        with self.assertRaises(ValidationError):
            models.validate_phone_number('12345678901234567')

    def test_phone_number_validator_fail_letters(self):
        # Recall that this is not a likely thing to happen.
        with self.assertRaises(ValidationError):
            models.validate_phone_number('1234567a')

    def test_phone_number_validator_success_short(self):
        self.assertEqual(models.validate_phone_number('1'), None)

    def test_phone_number_validator_success_middle(self):
        self.assertEqual(models.validate_phone_number('12345678'), None)

    def test_phone_number_validator_success_long(self):
        self.assertEqual(models.validate_phone_number('1234567890123456'),
                         None)


class MemberPinTestCase(TestCase):
    def setUp(self):
        self.member = models.Member(pin='1234')

    def test_check_pin_fail(self):
        self.assertFalse(self.member.check_pin('4321'))

    def test_check_pin_success(self):
        self.assertTrue(self.member.check_pin('1234'))

    def test_change_pin_fail(self):
        self.assertFalse(self.member.change_pin('2234', '4321'))
        self.assertFalse(self.member.check_pin('4321'))

    def test_change_pin_success(self):
        self.assertTrue(self.member.change_pin('1234', '4321'))
        self.assertTrue(self.member.check_pin('4321'))

    def test_pin_validator_fail_short(self):
        with self.assertRaises(ValidationError):
            models.validate_pin('123')

    def test_pin_validator_fail_long(self):
        with self.assertRaises(ValidationError):
            models.validate_pin('12345')

    def test_pin_validator_fail_letters(self):
        with self.assertRaises(ValidationError):
            models.validate_pin('abcd')

    def test_pin_validator_success(self):
        self.assertEqual(models.validate_pin('1234'), None)
