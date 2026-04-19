import requests

class SeventeenLandsClient:

    BASE_URL = "https://www.17lands.com"
    DEFAULT_EXPANSION = "FIN"
    DEFAULT_FORMAT = "PremierDraft"

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json",
        })

    def get_card_ratings(self, expansion: str = DEFAULT_EXPANSION, format: str = DEFAULT_FORMAT) -> dict:
        """
        Fetch card ratings for a given set and format
        """

        url = f"{self.BASE_URL}/card_ratings/data"
        params = {
            "expansion": expansion,
            "format": format,
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_color_ratings(self, expansion: str = DEFAULT_EXPANSION,
                          format: str = DEFAULT_FORMAT,
                          event_type: str = DEFAULT_FORMAT,
                          start_date: str = "2025-01-01",
                          end_date: str = "2026-03-31") -> dict:
        """
        Fetch color pair ratings for a given set and format
        """

        url = f"{self.BASE_URL}/color_ratings/data"
        params = {
            "expansion": expansion,
            "format": format,
            "event_type": event_type,
            "start_date": start_date,
            "end_date": end_date,

        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
