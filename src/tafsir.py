from src.tafsirapi import TafsirAPI
from src.utils import Utils
from src.enums import Titles


class Tafsir:
    @staticmethod
    def _parse_query(parts: list) -> list:
        required = []

        for part in parts:
            pair = part.split('-')

            if len(pair) == 1:
                required.append(int(part))
            else:
                verse = int(pair[0])
                to_verse = int(pair[1]) + 1

                if to_verse < verse:
                    to_verse = verse

                for ayah in range(verse, to_verse):
                    required.append(ayah)

        return required

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
            required = Tafsir._parse_query(parts)
        except ValueError:
            return ''

        for ayah in verses:
            if ayah['ayah'] in required:
                ayahs.append(ayah)

        return Tafsir._response_to_text(chapter, ayahs)
