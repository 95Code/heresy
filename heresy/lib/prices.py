# --- IMPORTS ---

import krakenex
from pykrakenapi import KrakenAPI
import pandas as pd


# --- GLOBALS ---

API = KrakenAPI(krakenex.API())

PAIR_NAME = {
    "XBT_EUR": "XXBTZEUR"
}


# --- FUNCTIONS ---

def get_ohlc_data(pair="XXBTZEUR", minutes=1):
    ohlc, last = API.get_ohlc_data(PAIR[pair])
    return ohlc, last



# --- MAIN SCRIPT ---

if __name__ == "__main__":
    ohlc = get_ohlc_data()
    ohlc.to_csv("test.csv")
