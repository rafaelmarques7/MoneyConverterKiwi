import os
import json
import xlrd
import time
import argparse
import requests


def valid_currency(curr):
    """ Validates the introduced currencies"""
    currencies = load_currencies()
    curr = curr.upper()
    if curr in currencies.keys():
        return curr
    else:
        error_msg = "The currency introduced - {curr} - is not valid".format(curr=curr)
        raise argparse.ArgumentTypeError(error_msg)


def get_path_from_rel(rel_path):
    """ makes an absolute path from a relative one, using the cwd"""
    cwd = os.getcwd()
    return os.path.join(cwd, rel_path)


def currencies_excel_to_json():
    curr_dict = {}

    excel_rel_path = "data/currencies.xlsx"
    excel_path = get_path_from_rel(excel_rel_path)
    json_rel_path = "data/currencies.json"
    json_path = get_path_from_rel(json_rel_path)

    df = xlrd.open_workbook(excel_path)
    table = df.sheets()[0]

    for num_row in range(table.nrows-1):
        row = table.row_values(num_row)
        code = row[0]
        name = row[1]
        curr_dict[code] = {
            "code": code,
            "name": name,
            "symbol": "",
        }
    write_json(json_path, curr_dict)


def write_json(fpath, data_dict):
    """ (Over)writes a json file with the given dict. Does not perform json validation """
    with open(fpath, 'w') as f:
        json.dump(data_dict, f)


def load_json(fpath):
    with open(fpath, 'r') as f:
        data = json.load(f)
    return data


def load_currencies():
    json_rel_path = "data/currencies.json"
    json_path = get_path_from_rel(json_rel_path)
    currencies = load_json(json_path)
    return currencies


def load_rates(update_rate=86400):
    """ Loads exchange rate from file. If file is outdated makes a new request, and updates it."""
    rates_path = get_path_from_rel("data/rates.json")
    data_rates = load_json(rates_path)
    if time.time() - int(data_rates["timestamp"]) > update_rate:
        data_rates = get_exchange_rates()
    write_json(rates_path, data_rates)
    return data_rates["rates"]


def get_exchange_rates():
    """ Makes HTTP GET to fixer.io to get current exchange rates """
    configs_path = get_path_from_rel("configs.json")
    configs = load_json(configs_path)
    fixer_key = configs["fixer_key"]
    url_exchange = "http://data.fixer.io/api/latest?access_key={key}".format(key=fixer_key)
    response = requests.get(url_exchange)
    assert response.status_code == 200
    result = response.json()
    return result


if __name__ == "__main__":
    currencies_excel_to_json()