import requests
from OctopusAgile import Agile

class CustomAgile(Agile):
    def __init__(self, area_code, tariff_code: str = "NEW-TARIFF-CODE", **kwargs):
        super().__init__(area_code, **kwargs)
        self.tariff_code = tariff_code

    def get_raw_rates(self, date_from: str, date_to: str = None) -> dict:
        date_from = f"?period_from={date_from}"
        if date_to is not None:
            date_to = f"&period_to={date_to}"
        else:
            date_to = ""
        
        base_url = f"https://api.octopus.energy/v1/products/{self.tariff_code}/electricity-tariffs"
        
        headers = {"content-type": "application/json"}
        r = requests.get(
            f"{base_url}/"
            f"E-1R-{self.tariff_code}-{self.area_code}/"
            f"standard-unit-rates/{ date_from }{ date_to }",
            headers=headers,
        )
        results = r.json()["results"]
        return results
