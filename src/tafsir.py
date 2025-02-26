from src.enums import Titles
from src.queryparser import QueryParser
from src.tafsirapi import TafsirAPI
from src.utils import Utils


class Tafsir:
    @staticmethod
    def _response_to_text(chapter: int, response: list) -> str:
        text = f'\n**{Titles.SURAH[chapter]}**\n'

        for verse in response:
            text += f'**{verse["ayah"]}** {verse["text"]}\n'

        return text

    @staticmethod
    def get(chapter: int, verse: int, to_verse: int, edition: str) -> str:
        if verse == to_verse:
            verses = [TafsirAPI.surah(chapter, verse, edition)]

            return Tafsir._response_to_text(chapter, verses)

        surah = TafsirAPI.surah(chapter, edition=edition)
        verses = surah['ayahs']

        ayahs = []

        for ayah in verses:
            if verse <= ayah['ayah'] <= to_verse:
                ayahs.append(ayah)

        return Tafsir._response_to_text(chapter, ayahs)

    @staticmethod
    def query(query: str, chapter: int, edition: str):
        surah = TafsirAPI.surah(chapter, edition=edition)
        parts = Utils.split_query(query)
        verses = surah['ayahs']
        ayahs = []

        try:
            required = QueryParser.parse_without_chapters(parts)
        except ValueError:
            return ''

        for ayah in verses:
            if ayah['ayah'] in required:
                ayahs.append(ayah)

        return Tafsir._response_to_text(chapter, ayahs)
