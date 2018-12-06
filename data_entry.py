from validation import AmountValidation
from validation import CurrencyValidation
from calculations import Calculations
from xml_converter import XmlConverter


class DataEntry():

    calculation = Calculations()
    amount_validation = AmountValidation()
    currency_validation = CurrencyValidation()
    converter = XmlConverter()
    converter.make_dict_from_xml()

    def clean_input(self,input_string):
        return input_string.replace(',','')

    validated = False
    while(True):

        while(validated == False):
            print('Avaiable currencies:',end=' ')
            for key in converter.get_dictionary():
                print(key,end=', ')
                
            currency_in_lower_case = input('Enter the currency code that you want to convert from: ')
            currency_in = currency_in_lower_case.upper()
            validated = currency_validation.currency_length(currency_in)
            if validated == False:
                print('Error: Currency codes are 3 characters long')

            try:
                calculation.get_float_from_dict_for_currency_in(currency_in)
            except(KeyError):
                validated = False
                print('That key does not exist, please ensure you have typed it properly')
                continue

        validated = False
        while(validated == False):
            currency_out_lower_case = input('Enter the currency code that you want to convert to: ')
            currency_out = currency_out_lower_case.upper()
            validated = currency_validation.currency_length(currency_out)
            if validated == False:
                print('Error: Currency codes are 3 characters long')

            try:
                calculation.get_float_from_dict_for_currency_out(currency_out)
            except(KeyError):
                validated = False
                print('That key does not exist, please ensure you have typed it properly')
                continue

        while(True):
            input_value = input('Enter an amount to convert: ')
            if amount_validation.validate_amount(input_value):
                cleaned_input = float(clean_input(1,input_value))
                break
            else:
                print('You have entered an incorrect value! Please try again')
                continue   
        break

    calculation.calculate_the_rate_between_two_currencies(cleaned_input,currency_out)
