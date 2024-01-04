# Octopus Energy Tariffs

Octopus Energy provides a variety of tariffs catering to different energy consumption needs. These tariffs, identified by unique codes, play a crucial role in determining the unit rates for energy consumption. The script fetches data from the API based on the specified tariff code, allowing users to access accurate and up-to-date information.

## Important Information
- If you are not using an Agile rate, the API will still function, but adjustments may be necessary. Specifically, the `start_date` and `end_date` or `num_periods` should be modified, as the API pulls data only when rates change for non-Agile tariffs.

## Tariff Codes and Descriptions
Here is a table outlining some of the Octopus Energy tariffs, their respective codes, and brief descriptions:

| **Code** | **Tariff Name** | **Description** |
|----------|------------------|------------------|
| AGILE-23-12-06 | Agile Octopus December 2023 v1 | Access half-hourly energy prices tied to wholesale prices, updated daily. Unit rate capped at 100p/kWh. |
| AGILE-OUTGOING-19-05-13 | Agile Outgoing Octopus May 2019 | Pays for exported energy based on the day-ahead wholesale rate. |
| COOP-LOYAL-FIX-12M-23-12-30 | Co-op Loyal 12M Fixed December 2023 v2 | Fixed prices save around £70/year compared to Ofgem Price Cap, with a £75 early exit fee. |
| COOP-PP-VAR-20-04-01 | Co-op Key and Card | Non-smart prepayment tariff. |
| COOP-SEG-FIX-12M-20-11-11 | Co-op Smart Export Guarantee November 2020 v1 | Smart Export Guarantee compliant export tariff. |
| COOP-VAR-23-04-01 | Co-op Flexible | Offers great value and 100% renewable electricity. Variable tariff with notice of price changes. |
| COSY-22-12-08 | Cosy Octopus | Heat pump tariff with six hours of super cheap electricity daily for home heating. |
| EB-PP-VAR-21-10-08 | Ebico Prepayment | Great value and 100% renewable electricity. Variable tariff with notice of price changes for prepayment. |
| EP-LOYAL-FIX-12M-23-12-30 | Ebico Loyal Prime 12 Saver December 2023 v2 | Fixed prices save around £70/year compared to Ofgem Price Cap, with a £75 early exit fee. |
| ES-VAR-23-04-01 | Ebico Standard | Great value and 100% renewable electricity. Variable tariff with notice of price changes. |
| FLUX-EXPORT-23-02-14 | Octopus Flux Export February 2023 v1 | Variable tariff for exporting energy. |
| FLUX-IMPORT-23-02-14 | Octopus Flux Import | 100% renewable energy for homes with solar and battery systems. |
| GO-GREEN-VAR-22-10-14 | Octopus Go Green October 2022 v1 | EV tariff for Volkswagen Group EV drivers, offering green energy. |
| GO-VAR-22-10-14 | Octopus Go October 2022 v1 | Smart EV tariff with super cheap electricity between 00:30 - 04:30 every night. |
| GO-FASTER-VAR-22-10-14 | Octopus Go Faster October 2022 v1 | Faster charging for electric vehicles, with a higher daytime rate. |
| GO-ESSENTIAL-23-07-31 | Octopus Go Essential | Simple tariff with a low flat rate 24/7. |
| INTELLI-GO-22-10-14 | Octopus Intelligent Octopus Go October 2022 v1 | Same as Intelligent Octopus Go October 2022 v1, offered by Octopus Energy. |
