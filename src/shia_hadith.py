from src.thaqalaynapi import ThaqalaynAPI
from src.utils import Utils


class ShiaHadith:
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
    def _response_to_text(hadiths: list, english: bool) -> str:
        if len(hadiths) == 0:
            return ''

        text = f'\n**{hadiths[0]["book"]}**\n\n'

        if english:
            for hadith in hadiths:
                text += f'**{hadith["id"]}** {Utils.escape_markdown(Utils.remove_numeration(hadith["englishText"]))}\n'
        else:
            for hadith in hadiths:
                text += f'**{hadith["id"]}** {hadith["arabicText"]}\n'

        return text

    @staticmethod
    def get(hadith_no: int, book: str) -> str:
        english = book.startswith('en-')
        book = book[3:]

        hadiths = ThaqalaynAPI.hadith(hadith_no, book)

        return ShiaHadith._response_to_text(hadiths, english)

    @staticmethod
    def query(query: str, book: str):
        english = book.startswith('en-')
        book = book[3:]
        hadiths = ThaqalaynAPI.books(book)
        parts = Utils.split_query(query)
        required = ShiaHadith._parse_query(parts)
        response_hadiths = []

        for hadith in hadiths:
            for item in required:
                try:
                    item = int(item)
                except ValueError:
                    continue

                if item == hadith['id']:
                    response_hadiths.append(hadith)

        return ShiaHadith._response_to_text(response_hadiths, english) if len(response_hadiths) else ''
