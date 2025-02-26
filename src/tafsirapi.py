import requests

default_edition = 'en-tafisr-ibn-kathir'


class TafsirAPI:
    base_url = 'https://github.com/spa5k/tafsir_api/raw/refs/heads/main/tafsir'

    @staticmethod
    def url(endpoint):
        return TafsirAPI.base_url + endpoint + '.json'

    @staticmethod
    def editions():
        return requests.get(TafsirAPI.url('/editions')).json()

    @staticmethod
    def surah(chapter: int, verse: int = -1, edition: str = default_edition):
        return requests.get(TafsirAPI.url(f'/{edition}/{chapter}/{verse}' if verse > 0 else
                                          f'/{edition}/{chapter}')).json()
