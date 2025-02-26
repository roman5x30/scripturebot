import requests
from bs4 import BeautifulSoup as bs

from src.utils import Utils


class Title:
    def __init__(self, text):
        self.text = text


class Verse:
    def __init__(self, verse: str, text: str):
        self.verse = verse
        self.text = text


class BreakLine:
    def __init__(self):
        ...


class Headline:
    def __init__(self, text):
        self.text = text


class BibleGateway:
    base_url = 'https://www.biblegateway.com'

    @staticmethod
    def query(search: str, translation: str = 'NKJV'):
        response = requests.get(BibleGateway.base_url + f'/passage/?search={search}&version={translation}')
        soup = bs(response.content, 'html.parser')
        result = []

        passage_tables = soup.find_all(class_='passage-table')

        for passage_table in passage_tables:
            book = passage_table.find(class_='dropdown-display-text').text
            text = passage_table.find(class_='passage-text')
            paragraphs = text.find_all('p')

            result.append(Title(book))

            for paragraph in paragraphs:
                verses = paragraph.find_all('span', class_='text')

                if paragraph.previous_sibling and paragraph.previous_sibling.name in ['h2', 'h3', 'h4']:
                    result.append(Headline(paragraph.previous_sibling.text))
                elif paragraph.parent.previous_sibling and paragraph.parent.previous_sibling.name in ['h2', 'h3', 'h4']:
                    result.append(Headline(paragraph.parent.previous_sibling.text))

                for verse in verses:
                    verse_num = verse.find(class_='versenum')

                    # Getting number of the verse

                    if verse_num:
                        verse_num = verse_num.text
                    else:
                        chapter_num = verse.find(class_='chapternum')

                        # If it's a chapter number (the beginning), then obviously it's the 1st verse of the chapter.
                        # Alternatively, you can display the chapter number, but make it distinguishable via fullwidth.

                        if chapter_num:
                            verse_num = '1'
                            # verse_num = Utils.fullwidth(chapter_num.text)
                        else:
                            verse_num = '-1'

                    def do_nothing(x):
                        return x

                    def delete_elem(_):
                        return ''

                    to_unwrap = [
                        [lambda: verse.find_all(class_='versenum'), delete_elem],  # Appears in some translations
                        [lambda: verse.find_all(class_='crossreference'), delete_elem],  # Aren't required
                        [lambda: verse.find_all(class_='footnote'), delete_elem],  # Aren't required (2)
                        [lambda: verse.find_all('i'), Utils.italic],
                        [lambda: verse.find_all(class_='small-caps'), Utils.small_caps],
                        [lambda: verse.find_all(class_='woj'), do_nothing],
                        [lambda: verse.find_all(class_='persons'), do_nothing],
                    ]

                    for nodes_func, func in to_unwrap:
                        nodes = nodes_func()

                        for node in nodes:
                            node.string = func(node.text)
                            node.unwrap()

                    text = ''
                    text_nodes = verse.find_all(text=True, recursive=False)

                    for text_node in text_nodes:
                        text += text_node.text

                    result.append(Verse(verse_num, text))

                    if verse.parent.next_element.name == 'br':
                        result.append(BreakLine())

                result.append(BreakLine())

        return result
