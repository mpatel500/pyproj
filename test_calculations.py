import unittest
from calculations import Calculations

class Test_Calculations(unittest.TestCase):

    def setUp(self):
        self.algorithm = Calculations()
    
    def test_get_float_from_dict_for_currency_in_and_is_a_float(self):
       self.algorithm.get_float_from_dict_for_currency_in('GBP')
       self.assertTrue(isinstance(self.algorithm.get_float_from_dict_for_currency_in('GBP'), float))
    
    def test_get_float_from_dict_for_currency_out_and_is_a_float(self):
       self.algorithm.get_float_from_dict_for_currency_out('GBP')
       self.assertTrue(isinstance(self.algorithm.get_float_from_dict_for_currency_out('GBP'), float))
    
    def test_calculate_the_rate_between_two_currencies_returns_right_value_one_GBP_USD(self):
        self.algorithm.get_float_from_dict_for_currency_in('GBP')
        self.algorithm.get_float_from_dict_for_currency_out('GBP')
        self.algorithm.calculate_the_rate_between_two_currencies(1,'GBP')
        self.assertEqual(self.algorithm.calculate_the_rate_between_two_currencies(1.30,'GBP'),1.30)
    
    def test_calculate_the_rate_between_two_currencies_returns_right_value_one_AUD_HKD(self):
        self.algorithm.get_float_from_dict_for_currency_in('GBP')
        self.algorithm.get_float_from_dict_for_currency_out('GBP')
        self.algorithm.calculate_the_rate_between_two_currencies(5.64,'GBP')
        self.assertEqual(self.algorithm.calculate_the_rate_between_two_currencies(5.64,'GBP'),5.64)
