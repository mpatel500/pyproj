from xml_converter import XmlConverter

class Calculations():
    __converter = XmlConverter()
    
    def __init__(self, out_currency_rate=0, in_currency_rate=0):
        self.__conversion_info = self.__converter.make_dict_from_xml()
        self.__out_currency_rate = out_currency_rate
        self.__in_currency_rate = in_currency_rate
        
    def get_float_from_dict_for_currency_in(self,currency_in):
        self.__in_currency_rate = self.__conversion_info[currency_in]
        return self.__in_currency_rate

    def get_float_from_dict_for_currency_out(self,currency_out):
        self.__out_currency_rate = self.__conversion_info[currency_out]
        return self.__out_currency_rate
    
    def calculate_the_rate_between_two_currencies(self,amount_in,currency_out):
        __rate = self.__out_currency_rate / self.__in_currency_rate
        __amount_out = __rate * amount_in
        print(str("{0:.2f}".format(round(__amount_out, 2)))+ " " + currency_out)          
        return float("{0:.2f}".format(round(__amount_out, 2)))