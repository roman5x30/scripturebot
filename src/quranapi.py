import requests

default_edition = 'eng-farookmalik'


class QuranAPI:
    base_url = 'https://github.com/fawazahmed0/quran-api/raw/refs/heads/1'

    @staticmethod
    def url(endpoint):
        return QuranAPI.base_url + endpoint + '.min.json'

    @staticmethod
    def editions(edition: str = ''):
        return requests.get(QuranAPI.url('/editions/' + edition if edition else
                                         '/editions')).json()

    @staticmethod
    def surah(chapter: int, verse: int = -1, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/{chapter}/{verse}' if verse > 0 else
                                         f'/editions/{edition}/{chapter}')).json()

    @staticmethod
    def juzs(juz: int, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/juzs/{juz}')).json()

    @staticmethod
    def rukus(ruku: int, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/rukus/{ruku}')).json()

    @staticmethod
    def pages(page: int, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/pages/{page}')).json()

    @staticmethod
    def manzils(manzil: int, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/manzils/{manzil}')).json()

    @staticmethod
    def maqras(maqra: int, edition: str = default_edition):
        return requests.get(QuranAPI.url(f'/editions/{edition}/maqras/{maqra}')).json()
