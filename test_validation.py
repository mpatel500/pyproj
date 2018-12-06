import unittest
from validation import CurrencyValidation
from validation import AmountValidation

class Test_CurrencyValidation(unittest.TestCase):

    validate_currency = CurrencyValidation()

    def test_error_if_currency_from_variable_length_is_not_3(self):
        currency_from = 'GBP2'
        self.assertFalse(self.validate_currency.currency_length(currency_from))

    def test_error_if_currency_from_variable_length_is_3(self):
        currency_from = 'GBP'
        self.assertTrue(self.validate_currency.currency_length(currency_from))


class Test_AmountValidation(unittest.TestCase):

    validate_amount = AmountValidation()

    def test_value_clean_fails_if_multiple_dots_entered(self):
        value = '100.405.602'
        self.assertFalse(self.validate_amount.amount_type(value))

    def test_value_after_value_clean_is_float(self):
        value = '1000000'
        self.assertTrue(self.validate_amount.amount_type(value))

    def test_valid_number_returns_false_for_negative_numbers(self):
        value = -500
        self.assertFalse(self.validate_amount.amount_positive(value))

    def test_valid_number_returns_true_for_valid_number(self):
        value = 70000
        self.assertTrue(self.validate_amount.amount_type(value))


    



    
