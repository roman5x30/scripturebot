from src.biblegateway import BibleGateway, Title, Verse, BreakLine, Headline


class Bible:
    @staticmethod
    def _response_to_text(response) -> str:
        text = ''

        for item in response:
            if isinstance(item, Title):
                text += f'### {item.text}\n\n'
            elif isinstance(item, Verse):
                if item.verse == '-1':
                    text += '\n' + item.text
                    continue

                text += f' **{item.verse}** {item.text}'
            elif isinstance(item, BreakLine):
                text += '\n\n'
            elif isinstance(item, Headline):
                text += f'**{item.text}**\n\n'

        return text

    @staticmethod
    def query(query: str, translation: str) -> str:
        return Bible._response_to_text(BibleGateway.query(query, translation))

    @staticmethod
    def get(book: str, chapter: int, verse: int, to_verse: int, translation: str) -> str:
        return Bible.query(f'{book} {chapter}:{verse}-{to_verse}', translation)
