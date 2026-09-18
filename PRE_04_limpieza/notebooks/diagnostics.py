import os

import pandas as pd

def clean_supplier_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, SUPPLIER_REPLACEMENTS)
    return series

def clean_country_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, COUNTRY_REPLACEMENTS)
    return series

def clean_city_column(series):
    series = strip_whitespace(series)
    series = make_replacements(series, CITY_REPLACEMENTS)
    return series




def clean_purchase_date_column(series):
    series = strip_whitespace(series)
    series = series.str.replace(r".", "-", regex=False)
    series = series.str.replace(r"/", "-", regex=False)
    series = transform_dd_dd_dd_to_dd_dd_20dd(series)
    series = transform_dd_mm_yyyy_to_yyyy_mm_dd(series)
    series = transform_yyyy_dd_mm_to_yyyy_mm_dd(series)
    return series

def main():

    df = pd.read_csv(INPUT_FILE)

    df = clean_column_names(df)
    
    df["supplier"] = clean_supplier_column(df["supplier"])
    df["country"] = clean_country_column(df["country"])
    df["city"] = clean_city_column(df["city"])
    df["purchase_date"] = clean_purchase_date_column(df["purchase_date"])
    
    df.to_csv(OUTPUT_FILE, index=False)

    

if __name__ == "__main__":
    main()