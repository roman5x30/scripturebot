from src.hadithapi import HadithAPI
from src.utils import Utils


class Hadith:
    @staticmethod
    def _parse_query(parts: list) -> list:
        required = []

        for part in parts:
            pair = part.split('-')

            if len(pair) == 1:
                required.append(part)
            else:
                verse = int(pair[0])
                to_verse = int(pair[1]) + 1

                if to_verse < verse:
                    to_verse = verse

                for hadith_no in range(verse, to_verse):
                    required.append(hadith_no)

        return required

    @staticmethod
    def _response_to_text(metadata: dict, hadiths: list) -> str:
        text = f'\n**{metadata["name"]}**\n\n'

        for hadith in hadiths:
            text += f'**{hadith["hadithnumber"]}** {Utils.escape_markdown(hadith["text"])}\n'

        return text

    @staticmethod
    def get(hadith_no: int, edition: str) -> str:
        hadith = HadithAPI.hadith(hadith_no, edition)
        metadata = hadith['metadata']
        hadiths = hadith['hadiths']

        return Hadith._response_to_text(metadata, hadiths)

    @staticmethod
    def query(query: str, edition: str):
        translation = HadithAPI.editions(edition)
        metadata = translation['metadata']
        hadiths = translation['hadiths']
        parts = Utils.split_query(query)
        required = Hadith._parse_query(parts)
        response_hadiths = []

        for hadith in hadiths:
            for item in required:
                try:
                    item = int(item)
                except ValueError:
                    continue

                if item == hadith['hadithnumber']:
                    response_hadiths.append(hadith)

        return Hadith._response_to_text(metadata, response_hadiths) if len(response_hadiths) else ''
