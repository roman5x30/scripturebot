import requests


class HadithAPI:
    base_url = 'https://github.com/fawazahmed0/hadith-api/raw/refs/heads/1'

    @staticmethod
    def url(endpoint):
        return HadithAPI.base_url + endpoint + '.min.json'

    @staticmethod
    def editions(edition: str = ''):
        return requests.get(HadithAPI.url('/editions/' + edition if edition else
                                          '/editions')).json()

    @staticmethod
    def hadith(hadith_no: int, edition: str):
        return requests.get(HadithAPI.url(f'/editions/{edition}/{hadith_no}')).json()
