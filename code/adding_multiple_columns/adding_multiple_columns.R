#' @title Adding multiple columns
#' 
#' @description This script explores how to add multiple columns to ad data set.
#' It mainly uses the tidyverse concepts.
#' 
#' @author Patrick Thiel 

#--------------------------------------------------
# load configuration file (which stores my settings/ paths)

source("config_R.R")

#--------------------------------------------------
# paths
# Note: Paths are stored in a configuration file

data_path = config_R()

#--------------------------------------------------
# libraries

suppressPackageStartupMessages({
    library(dplyr)
    library(data.table)
    library(lubridate)
})

#--------------------------------------------------
# load data
# I use data of coffee prices for this example.
# Download here: https://www.kaggle.com/datasets/psycon/daily-coffee-price

coffee_data <- data.table::fread(
    file.path(
        data_path,
        "coffee_prices/coffee.csv"
    )
)

#--------------------------------------------------
# add columns
# Assume we want to add:
    # - the month
    # - the weekday
    # - range of prices per day (range of high and low)

coffee_data <- coffee_data |>
    dplyr::mutate(
        month = lubridate::month(Date),
        weekday = weekdays(Date),
        price_range = High - Low
    ) |>
    dplyr::relocate(
        c(month, weekday),
        .before = Open
    ) |>
    dplyr::relocate(
        price_range,
        .after = Low
    )

#--------------------------------------------------
# export

data.table::fwrite(
    coffee_data,
    file.path(
        data_path,
        "coffee_prices/coffee_prep.csv"
    )
)

