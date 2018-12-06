import unittest
from data_entry import DataEntry

class Test_DataEntry(unittest.TestCase):

    data_entry = DataEntry

    def test_when_standard_float_input__inputted_to_clean_value_return_same_value(self):
        value = '11211221212'
        self.assertEqual(self.data_entry.clean_input(value),'11211221212')
    
    
    def test_when_unclean_input_inputted_to_clean_value_return_same_value(self):
        value = '£1,000,000'
        self.assertEqual(self.data_entry.clean_input(value),'£1000000')
    
