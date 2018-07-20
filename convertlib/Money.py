import json
from convertlib import utils


class Exchange(object):
    """ Class object for the conversion of money quantities. Output is available at self.output """

    def __init__(self, amount, input_currency, output_currency=None):
        """ Argument validation is done apriori."""
        self.configs = utils.load_json("configs.json")
        self.rates = utils.load_rates(int(self.configs["update_rate"])) # loads the exchange rates
        self.amount_in = amount                                         # amount to be converted
        self.input_currency = input_currency                            # type of input currency
        self.out_currencies = [output_currency] \
            if output_currency else list(self.rates.keys())             # desired output currency(ies)
        self.output = self.exchange()                                   # execute the exchange calculations
        print(self.output)

    def exchange(self):
        """ Converts an amount (defined at init) from one currency, to another (or to all available ones)."""
        outputs = [self.exchange_to(out_curr) for out_curr in self.out_currencies]
        return self.make_output(outputs)

    def exchange_to(self, out_curr):
        """ Exchanges self.amount_in to a specific currency """
        eur = self.to_eur(self.amount_in, self.input_currency)
        out_val = self.eur_to_curr(eur, out_curr)
        out_tuple = (out_curr, out_val)
        return out_tuple

    def to_eur(self, amount, input_currency):
        """ Converts given amount of input_currency to EURO"""
        if input_currency == "EUR":
            return amount
        return amount * (1/self.rates[input_currency])

    def eur_to_curr(self, amount, curr):
        """ Converts amount in euro to any given currency """
        return amount * self.rates[curr]

    def make_output(self, outputs):
        """ Creates output dictionary. Input: list of tuples (value, currency_type) """
        out = {
            "output": {},
            "input": {
                "amount": round(self.amount_in, 2),
                "currency": self.input_currency,
            }
        }
        for (out_curr, out_val) in outputs:
            out["output"][out_curr] = round(out_val, 2)
        return out

    def __str__(self):
        return json.dumps(self.output)

    def __repr__(self):
        return self.__str__()






