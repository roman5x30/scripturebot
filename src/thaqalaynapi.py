import requests


class ThaqalaynAPI:
    base_url = 'https://www.thaqalayn-api.net/api/v2'

    @staticmethod
    def url(endpoint):
        return ThaqalaynAPI.base_url + endpoint

    @staticmethod
    def books(book_id: str):
        return requests.get(ThaqalaynAPI.url('/' + book_id) if book_id else
                            ThaqalaynAPI.url('/allbooks')).json()

    @staticmethod
    def hadith(hadith_no: int, book_id: str):
        return requests.get(ThaqalaynAPI.url(f'/{book_id}/{hadith_no}')).json()
