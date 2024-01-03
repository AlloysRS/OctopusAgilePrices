"""
Agile Pricing Data Extractor

Author: Alloys
Date: January 3, 2024

Description:
This script retrieves Agile pricing data using the OctopusAgile library and saves it to a CSV file. The user can customize the date range selection, choose whether to save the data to a file, and print the results. The script is designed to extract date-time and rate information for Agile pricing within the specified date range.

Usage:
- Set the 'date_range_selection_method' variable to either of the below to choose the desired date range.
    - 'Range' (A specified Date Range in YYYY_MM_DD format, note this cannot fetch more than a year worth of data)
    - 'Current' (Data from Midnight today until latest data point [After 4pm the following day's prices are published])
    - 'Now' (Half hourly time slots from the current time rounded down for 'num_periods' amount of slots)
- Set the 'should_save_file' variable to 'True' if you want to save the data to a CSV file as specified, or 'False' otherwise.
- Set the 'should_print_results' variable to 'True' if you want to print the extracted data, or 'False' otherwise.
- Set the 'region_code' variable to the region you are in for localised prices (See https://en.wikipedia.org/wiki/Distribution_network_operator)

Dependencies:
- OctopusAgile library (ensure it is installed via pip: 'pip install OctopusAgile')
- Python 3

Note:
Make sure to customize the 'region_code' variable according to your geographical location ('M' for example).
"""

from OctopusAgile import Agile
from datetime import datetime, timedelta
import csv

date_range_selection_method = "Now"
should_save_file = False  
should_print_results = True 
region_code = 'M'
num_periods = 4

def set_start_end_dates(date_range_selection):
    if date_range_selection == "Range":
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 1, 2)
    elif date_range_selection == "Current":
        start_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=0)
        end_date = start_date + timedelta(days=2)
    elif date_range_selection == "Now":
        current_datetime = datetime.now()
        start_date = current_datetime - timedelta(minutes=current_datetime.minute % 30, seconds=current_datetime.second, microseconds=current_datetime.microsecond)
        end_date = start_date + timedelta(minutes=(30 * num_periods), seconds=-current_datetime.second, microseconds=-current_datetime.microsecond)
    else:
        raise ValueError("Choose a valid selection method")

    return start_date, end_date

def save_data_to_csv(csv_file_path, date_rate_dict):
    with open(csv_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Date/Time', 'Rate'])

        for date_time, rate in date_rate_dict.items():
            csv_writer.writerow([date_time, rate])

    print(f'Data has been saved to {csv_file_path}')

def main():

    agile = Agile(region_code)
    start_date, end_date = set_start_end_dates(date_range_selection_method)
    rates_data = agile.get_rates(start_date.strftime("%Y-%m-%dT%H:%M:%SZ"), end_date.strftime("%Y-%m-%dT%H:%M:%SZ"))

    if 'date_rates' in rates_data:
        date_rate_dict = rates_data['date_rates']

        if should_print_results:
            print("Your Agile Rates Are: ")
            for date_time, rate in date_rate_dict.items():
                print(f'{date_time}: {rate}')

        if should_save_file:
            csv_file_path = f'C:\\Users\\Lewis\\Documents\\Agile_Prices_{start_date.strftime("%Y-%m-%d")}_{end_date.strftime("%Y-%m-%d")}.csv'
            save_data_to_csv(csv_file_path, date_rate_dict)
    else:
        print("Error: 'date_rates' key not found in rates_data.")
        print("Rates data structure:", rates_data)

if __name__ == "__main__":
    main()