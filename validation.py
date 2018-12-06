class CurrencyValidation():

    def currency_length(self,currency_input):
        if len(currency_input) == 3:
            return True
        else:
            return False
    
class AmountValidation():

        def amount_type(self,amount_input):
            try:
                float_amount = float(amount_input)
                return True
            except(ValueError):
                return False

        def amount_positive(self,amount_input):
            if float(amount_input) < 0:
                return False
            elif float(amount_input) > 0:
                return True

        def validate_amount(self,amount_input):
            if self.amount_type(amount_input) and self.amount_positive(amount_input):
                return True


