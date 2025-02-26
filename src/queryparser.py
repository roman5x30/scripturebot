class QueryParser:
    @staticmethod
    def parse_with_chapters(parts: list) -> list:
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
    def parse_without_chapters(parts: list) -> list:
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

                for num in range(verse, to_verse):
                    required.append(num)

        return required
