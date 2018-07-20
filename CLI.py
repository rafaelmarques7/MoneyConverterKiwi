import argparse
from convertlib import Money
from convertlib.utils import valid_currency

if __name__ == "__main__":
    # init argument parser
    parser = argparse.ArgumentParser()
    # add required and optional arguments
    parser.add_argument("-a", "--amount", required=True,
                        help="The amount to be converted", type=float)
    parser.add_argument("-i", "--input_currency", required=True,
                        help="The input currency (name/symbol)", type=valid_currency)
    parser.add_argument("-o", "--output_currency", required=False,
                        help="The output currency (name/symbol)", type=valid_currency)
    # get the arguments
    args = parser.parse_args()

    money = Money.Exchange(args.amount, args.input_currency, args.output_currency)

