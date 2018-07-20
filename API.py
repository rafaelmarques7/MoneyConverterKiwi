from flask import Flask, request, jsonify
from convertlib import Money
from convertlib.utils import valid_currency, load_currencies

app = Flask(__name__)


@app.route('/')
def index():
    main_msg = "Hello, this is the API for money exchange calculations<br/>routes:<br/>" \
               " - '/currency_converter' - the main application<br/>" \
               " - '/currencies' - displays the valid currencies"
    return main_msg


@app.route('/currencies')
def currencies():
    valid_currencies = load_currencies()
    return jsonify(valid_currencies)


@app.route('/currency_converter')
def converter():
    # handle input amount and validate
    amount = request.args.get("amount", type=float)
    if not amount:
        return make_error(400, "Bad input for amount parameter - requires float type value")
    # handle input input_currency and validate
    try:
        input_currency = request.args.get("input_currency", type=valid_currency)
    except:
        return make_error(400, "Bad input for input_currency - requires valid currency - check '/currencies' route")
    # handle input output_currency and validate
    try:
        output_currency = request.args.get("output_currency", type=valid_currency, default=None)
    except:
        return make_error(400, "Bad input for output_currency - requires valid currency - check '/currencies' route")
    # try to converter and handle server errors
    try:
        money = Money.Exchange(amount, input_currency, output_currency)
    except Exception as e:
        return make_error(500, "There was an internal error: {}".format(str(e)))
    # return successful response
    return jsonify(money.output)


def make_error(status_code, message):
    response = jsonify({
        'status': status_code,
        'message': message,
    })
    response.status_code = status_code
    return response
