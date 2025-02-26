import re

from disnake.utils import escape_markdown


class Utils:
    @staticmethod
    def split_query(request: str) -> list:
        return re.split('[,;]', re.sub(r'\s+', '', request))

    @staticmethod
    def apply_charmap(text: str, charmap: dict) -> str:
        result = ''

        for char in text:
            result += charmap.get(char) or charmap.get(char.lower()) or char

        return result

    @staticmethod
    def small_caps(text: str) -> str:
        return Utils.apply_charmap(text, {
            'q': 'ǫ',
            'w': 'ᴡ',
            'e': 'ᴇ',
            'r': 'ʀ',
            't': 'ᴛ',
            'y': 'ʏ',
            'u': 'ᴜ',
            'i': 'ɪ',
            'o': 'ᴏ',
            'p': 'ᴘ',
            'a': 'ᴀ',
            's': 'ꜱ',
            'd': 'ᴅ',
            'f': 'ꜰ',
            'g': 'ɢ',
            'h': 'ʜ',
            'j': 'ᴊ',
            'k': 'ᴋ',
            'l': 'ʟ',
            'z': 'ᴢ',
            'x': 'x',
            'c': 'ᴄ',
            'v': 'ᴠ',
            'b': 'ʙ',
            'n': 'ɴ',
            'm': 'ᴍ'
        })

    @staticmethod
    def fullwidth(text: str) -> str:
        return Utils.apply_charmap(text, {
            '0': '０',
            '1': '１',
            '2': '２',
            '3': '３',
            '4': '４',
            '5': '５',
            '6': '６',
            '7': '７',
            '8': '８',
            '9': '９',
        })

    @staticmethod
    def italic(text: str) -> str:
        return Utils.apply_charmap(text, {
            'a': '𝘢',
            'b': '𝘣',
            'c': '𝘤',
            'd': '𝘥',
            'e': '𝘦',
            'f': '𝘧',
            'g': '𝘨',
            'h': '𝘩',
            'i': '𝘪',
            'j': '𝘫',
            'k': '𝘬',
            'l': '𝘭',
            'm': '𝘮',
            'n': '𝘯',
            'o': '𝘰',
            'p': '𝘱',
            'q': '𝘲',
            'r': '𝘳',
            's': '𝘴',
            't': '𝘵',
            'u': '𝘶',
            'v': '𝘷',
            'w': '𝘸',
            'x': '𝘹',
            'y': '𝘺',
            'z': '𝘻',
            'A': '𝘈',
            'B': '𝘉',
            'C': '𝘊',
            'D': '𝘋',
            'E': '𝘌',
            'F': '𝘍',
            'G': '𝘎',
            'H': '𝘏',
            'I': '𝘐',
            'J': '𝘑',
            'K': '𝘒',
            'L': '𝘓',
            'M': '𝘔',
            'N': '𝘕',
            'O': '𝘖',
            'P': '𝘗',
            'Q': '𝘘',
            'R': '𝘙',
            'S': '𝘚',
            'T': '𝘛',
            'U': '𝘜',
            'V': '𝘝',
            'W': '𝘞',
            'X': '𝘟',
            'Y': '𝘠',
            'Z': '𝘡'
        })

    @staticmethod
    def get_corresponding_key(obj: dict, value: any):
        for key in obj:
            if obj[key] == value:
                return key

    @staticmethod
    def search_in_obj(request: str, obj: dict, display_value: bool = False) -> list:
        keywords = re.split(r'\s+', request.strip())

        if display_value:
            return [
                obj[item] for item in obj if
                len([keyword for keyword in keywords if keyword.lower() in str(item).lower()]) == len(keywords)
            ]

        return [
            item for item in obj if
            len([keyword for keyword in keywords if keyword.lower() in str(item).lower()]) == len(keywords)
        ]

    @staticmethod
    def escape_markdown(text: str) -> str:
        return escape_markdown(text)

    @staticmethod
    def remove_numeration(text: str) -> str:
        return re.sub(r'^\s*\d+\.\s*', '', text)
