from src.enums import Titles
from src.quranapi import QuranAPI
from src.utils import Utils


class Quran:
    @staticmethod
    def _parse_query(parts: list) -> list:
        current_chapter = -1
        required = []

        for part in parts:
            pair = part.split(':')

            if len(pair) == 1:
                if current_chapter == -1:
                    chapters = pair[0].split('-')

                    if len(chapters) == 1:
                        required.append([pair[0], '0', '0'])
                    else:
                        for chapter in range(int(chapters[0]), int(chapters[1]) + 1):
                            required.append([str(chapter), '0', '0'])
                else:
                    verses = pair[0].split('-')

                    if len(verses) == 1:
                        required.append([current_chapter, verses[0], verses[0]])
                    else:
                        required.append([current_chapter, verses[0], verses[1]])
            else:
                current_chapter = pair[0]
                verses = pair[1].split('-')

                if len(verses) == 1:
                    required.append([current_chapter, verses[0], verses[0]])
                else:
                    if int(verses[1]) < int(verses[0]):
                        verses[1] = verses[0]

                    required.append([current_chapter, verses[0], verses[1]])

        return required

    @staticmethod
    def _response_to_text(chapter: int, response: list) -> str:
        text = f'\n**{Titles.SURAH[chapter]}**\n'

        for verse in response:
            text += f'**{verse["verse"]}** {verse["text"]}\n'

        return text

    @staticmethod
    def get(chapter: int, verse: int, to_verse: int, edition: str) -> str:
        if verse == to_verse:
            verses = [QuranAPI.surah(chapter, edition=edition, verse=verse)]

            return Quran._response_to_text(chapter, verses)

        surah = QuranAPI.surah(chapter, edition=edition)
        verses = surah['chapter'][verse - 1:to_verse]

        return Quran._response_to_text(chapter, verses) if len(verses) else ''

    @staticmethod
    def query(query: str, edition: str):
        quran = QuranAPI.editions(edition)['quran']
        parts = Utils.split_query(query)

        try:
            required = Quran._parse_query(parts)
        except ValueError:
            return ''

        rukus = {}

        for ruku in quran:
            for item in required:
                try:
                    chapter = int(item[0])
                    verse = int(item[1])
                    to_verse = int(item[2])
                except ValueError:
                    continue

                if chapter == ruku['chapter'] and (verse <= ruku['verse'] <= to_verse or
                                                   verse == 0 and to_verse == 0):
                    if rukus.get(chapter):
                        rukus[chapter].append(ruku)
                    else:
                        rukus[chapter] = [ruku]

        response = ''

        for chapter in rukus:
            response += Quran._response_to_text(chapter, rukus[chapter])

        return response
