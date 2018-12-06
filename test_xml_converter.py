import unittest
from xml_converter import XmlConverter

class Test_XmlConverter(unittest.TestCase):

    def setUp(self):
        self.converter = XmlConverter()

    def test_if_dict_exists_and_length_is_empty(self):
        self.converter.get_dictionary_size()
        self.assertEqual(self.converter.get_dictionary_size(),0)

    def test_if_number_of_items_obtained_from_xml_stored_as_items_is_the_same_number_as_in_the_xml_file(self):
        self.converter.get_xml_item_number()
        self.assertEqual(self.converter.get_xml_item_number(),32)

    def test_if_dict_has_entries_and_they_equal_length_of_items_from_xml(self):
        self.converter.make_dict_from_xml()
        self.assertEqual(self.converter.get_dictionary_size(),(self.converter.get_xml_item_number()))

    def test_if_dict_key_gives_correct_corresponding_value(self):
        self.converter.make_dict_from_xml()
        self.converter.get_value_using_key_from_dict
        self.assertEqual(self.converter.get_value_using_key_from_dict("USD"),1.1261)

