
"""
    Adding multiple columns.
    
    This script explores how to add multiple columns to ad data set.
"""

import sys
sys.path.append("G:/Programming-Language-Exchange")

#--------------------------------------------------
# import modules

import os
from os.path import join
import pandas as pd
from config_Python import config

#--------------------------------------------------
# paths
# Note: Paths are stored in a configuration file

data_path = config().get("data_path")

#--------------------------------------------------
# load data
# I use data of coffee prices for this example.
# Download here: https://www.kaggle.com/datasets/psycon/daily-coffee-price

coffee_data = pd.read_csv(
    join(data_path, "coffee_prices/coffee.csv")
)

#--------------------------------------------------
# add columns
# Assume we want to add:
    # - the month
    # - the weekday
    # - range of prices per day (range of high and low)
# Nice thing about assign: I could chain other operations after assigning new
# columns

# set Date as datetime
coffee_data["Date"] = pd.to_datetime(coffee_data["Date"])

# add desired columns
coffee_data = (coffee_data
    .assign(
        month = coffee_data["Date"].dt.month,
        weekday = coffee_data["Date"].dt.day_name(),
        price_range = coffee_data["High"] - coffee_data["Low"]
    )
)

# reorder
coffee_data.insert(1, "month", coffee_data.pop("month"))
coffee_data.insert(2, "weekday", coffee_data.pop("weekday"))
coffee_data.insert(5, "price_range", coffee_data.pop("price_range"))

#--------------------------------------------------
# export

coffee_data.to_csv(
    join(data_path, "coffee_prices/coffee_prep.csv")
)