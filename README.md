# OctopusAgilePrices

## Author: AlloysRS

### Date: January 3, 2024

### Description:
This script retrieves Agile pricing data using the OctopusAgile library and saves it to a CSV file. The user can customize the date range selection, choose whether to save the data to a file, and print the results. The script is designed to extract date-time and rate information for Agile pricing within the specified date range.

### Usage:
- Set the `date_range_selection_method` variable to either of the below to choose the desired date range.
    - 'Range' (A specified Date Range in YYYY_MM_DD format, note this cannot fetch more than a year worth of data)
    - 'Current' (Data from Midnight today until the latest data point [After 4 pm, the following day's prices are published])
    - 'Now' (Half-hourly time slots from the current time rounded down for 'num_periods' amount of slots)
- Set the `should_save_file` variable to 'True' if you want to save the data to a CSV file as specified, or 'False' otherwise.
- Set the `should_print_results` variable to 'True' if you want to print the extracted data, or 'False' otherwise.
- Set the `region_code` variable to the region you are in for localized prices without '_' (See [Distribution Network Operator Codes](https://en.wikipedia.org/wiki/Distribution_network_operator))
- Set the `tariff_code` variable to the tariff you want to get the unit rates for. Refer to [TARIFF_LIST](TARIFF_LIST.md) for a list of available tariff codes.

### Dependencies:
- OctopusAgile library (ensure it is installed via pip: 'pip install OctopusAgile')
- Python 3
