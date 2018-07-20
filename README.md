The goal of this project is to successfully complete the project request by Kiwi.

That is, create a currency converter, which works both as a CLI and API.

start time: 19/07/2018 16:48h

relevant files:
 
    1) CLI.py - client line interface that implements the desired functions
    2) API.py - Application Programming Interface (via Flask) that does the same
    3) convertlib/Money.py - OOP of the desired functions
    4) convertlib/utils.py - holds some important functions - json manipulation, HTTP request methods, etc.
 
finish time: 20/07/2018 17:30h
 

How does the application work?

Both CLI and API work by creating an "Exchange" class object, from the Money library, which takes "amount", "input_currency" and "output_currency" (opt)
as parameters, and outputs the exchanged currencies.

In order to do this, it is necessary to have the currencies exchange rate. This is done by making a request to
"fixer.io", which has the available information. The response is saved into a file (data/rates.json),
which is updated once per day - this update rate can be changed in the "configs.json" file, at the root directory.

After this, it is straightforward. Convert the amount first to EUR (because "fixer.io" rates have EUR base), and after this to 
the desired currencies.

Both CLI and API are error safe. They validate input, and throw personalized error message and information upon any error.

The CLI application PRINTS the output. 
The API returns a json response with the desired output.

The API views are displayed in the root directory, and are: 
1) "currency_converter" - implements the desired functions.
2) "currencies" - displays the available currencies - any other currency leads to an error message.


The only thing currently missing is the acceptance of currencies via SYMBOL instead of currency code.
This functionality is missing because there is ambiguity regarding this functionality. 
A currency symbol, like $, may stand for multiple currencies, as United State Dollars, or Bahamas Dollars, or Australian Dollars.
As the Python Zen says "in the face of ambiguity, refuse the temptation to guess".
Yesterday I sent an email regarding this question, and got no response yet.

However, If someone can tell me how to proceed regarding this symbols I will adapt the application accordingly.

I hope you like my work.

Thankfully, 

Rafael Marques