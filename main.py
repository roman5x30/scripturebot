import disnake
from disnake.ext import commands

from src.bible import Bible
from src.config import TOKEN
from src.enums import Error, Translation, Titles, IslamBranch
from src.hadith import Hadith
from src.quran import Quran
from src.shia_hadith import ShiaHadith
from src.tafsir import Tafsir
from src.utils import Utils

intents = disnake.Intents.all()
bot = commands.Bot(case_insensitive=True, command_prefix='!', intents=intents)


async def handle_response(interaction, response, title: str = '', deferred=False):
    if deferred:
        if len(response) > 2000:
            return await interaction.followup.send(
                delete_after=10,
                embed=disnake.Embed(
                    title='🛑 Error!',
                    description=Error.TOO_LARGE_RESPONSE,
                    color=disnake.Color.from_rgb(221, 46, 68)
                )
            )
        elif not response:
            return await interaction.followup.send(
                delete_after=10,
                embed=disnake.Embed(
                    title='🛑 Error!',
                    description=Error.NO_RESPONSE,
                    color=disnake.Color.from_rgb(221, 46, 68)
                )
            )
        else:
            return await interaction.followup.send(
                embed=disnake.Embed(
                    color=disnake.Color.from_rgb(218, 157, 82),
                    description=response,
                    title=title
                )
            )

    if len(response) > 2000:
        return await interaction.response.send_message(
            ephemeral=True,
            embed=disnake.Embed(
                title='🛑 Error!',
                description=Error.TOO_LARGE_RESPONSE,
                color=disnake.Color.from_rgb(221, 46, 68)
            )
        )
    elif not response:
        return await interaction.response.send_message(
            ephemeral=True,
            embed=disnake.Embed(
                title='🛑 Error!',
                description=Error.NO_RESPONSE,
                color=disnake.Color.from_rgb(221, 46, 68)
            )
        )
    else:
        return await interaction.response.send_message(embed=disnake.Embed(
            color=disnake.Color.from_rgb(218, 157, 82),
            description=response,
            title=title
        ))


async def autocomplete_bible_book(_, user_input: str) -> list:
    if not user_input:
        return [
            'Matthew',
            'Mark',
            'Luke',
            'John',
            'Acts',
            'Romans',
            '1 Corinthians',
            '2 Corinthians',
            'Galatians',
            '1 Timothy',
            '2 Timothy',
            'Hebrews',
            'James',
            'Revelation',

            'Genesis',
            'Exodus',
            'Leviticus',
            'Numbers',
            'Deuteronomy',
            'Psalm',
            'Ecclesiastes',
            'Isaiah',
            'Ezekiel',
            'Daniel',
            'Malachi'
        ]

    return Utils.search_in_obj(user_input, Titles.BIBLE)[:25]


async def autocomplete_bible_translations(_, user_input: str) -> list:
    if not user_input:
        return [
            'King James Version (KJV)',
            'New King James Version (NKJV)',
            'Authorized (King James) (AKJV)',
            'New International Version (NIV)',
            'Legacy Standard Bible (LSB)',
            'New American Standard Bible (NASB)',
            'New American Standard Bible 1995 (NASB1995)',
            'New Living Translation (NLT)',
            'English Standard Version (ESV)',
            'Easy-to-Read Version (ERV)',

            'Ketab El Hayat (NAV)',
            'Arabic Bible: Easy-to-Read Version',

            'Hoffnung für Alle (HOF)',

            'Nueva Traducción Viviente (NTV)',
            'Nueva Versión Internacional (NVI)',

            'Hungarian Károli (KAR)',
            'Hungarian Bible: Easy-to-Read Version (ERV-HU)',

            'Ukrainian Bible (UKR)',
            'Ukrainian New Testament: Easy-to-Read Version (ERV-UK)',

            'New Russian Translation (NRT)',
            'Russian New Testament: Easy-to-Read Version (ERV-RU)',

            'Korean Living Bible (KLB)',

            'Japanese Living Bible (JLB)',

            'Chinese Standard Bible (Simplified) (CSBS)',
            'Chinese Standard Bible (Traditional) (CSBT)',
        ]

    return Utils.search_in_obj(user_input, Translation.BIBLE)[:25]


async def autocomplete_quran_chapter(_, user_input: str) -> list:
    if not user_input:
        return [
            '1. Al-Fatiha (The Opening)',
            '2. Al-Baqarah (The Cow)',
            '3. Al-Imran (The Family Of Imran)',
            '4. An-Nisa (The Women)',
            '5. Al-Maidah (The Table Spread)',
            '6. Al-An\'am (The Cattle)',
            '7. Al-A\'raf (The Heights)',
            '8. Al-Anfal (The Spoils of War)',
            '9. At-Taubah (The Repentance)',
            '10. Yunus (Prophet Jonah)',
            '11. Hud (Prophet Hud)',
            '12. Yusuf (Prophet Joseph)',
            '13. Ar-Rad (The Thunder)',
            '14. Ibrahim (Prophet Abraham)',
            '15. Al-Hijr (The Rocky Tract)',
            '16. An-Nahl (The Bee)',
            '17. Al-Isra (The Night Journey)',
            '18. Al-Kahf (The Cave)',
            '19. Maryam (Mary)',
            '20. Ta-Ha (Ta-Ha)',
            '21. Al-Anbiya (The Prophets)',
            '22. Al-Hajj (The Pilgrimage)',
            '23. Al-Mu\'minun (The Believers)',
            '24. Al-Noor (The Light)',
            '25. Al-Furqan (The Criterion)',
        ]

    return Utils.search_in_obj(user_input, Titles.SURAH, True)[:25]


async def autocomplete_quran_translations(_, user_input: str) -> list:
    if not user_input:
        return [
            '(English) Abdel Haleem',
            '(English) Abul Ala Maududi',
            '(English) Aisha Bewley',
            '(English) Farook Malik',
            '(English) Muhammad Taqi Ud Din Al Hilali And Muhammad Muhsin Khan',
            '(English) Syed Vickar Ahamed',
            '(English) Talal Itani',
            '(English) The Study Quran',
            '(English) Umm Muhammad',
            '(English) Muhammad Sarwar',

            '(Arabic) King Fahad Quran Complex',
            '(Arabic) Quran Warsh',
            '(Arabic) Quran Qumbul',
            '(Arabic) Quran Transliteration (Latin roman script version)',
            '(Arabic) Quran Simple',

            '(Spanish) Islamic Foundation (Latin roman script version)',
            '(Spanish) Islamic Foundation',

            '(Ukrainian) Hadi Abdollahian',
            '(Ukrainian) Dr. Mikhailo Yaqubovic',

            '(Russian) Elmir Kuliev',
            '(Russian) Ignaty Yulianovich Krachkovsky',

            '(Korean) Hamid Choi',

            '(Japanese) Ryoichi Mita',

            '(Chinese-traditional) Ma Jian'
            '(Chinese-simplified) Ma Zhong Gang'
        ]

    return Utils.search_in_obj(user_input, Translation.QURAN)[:25]


async def autocomplete_hadiths(_, user_input: str) -> list:
    if not user_input:
        return [
            '[Sunni] [Salafi] (English) Sahih al Bukhari',
            '[Sunni] [Salafi] (English) Sahih Muslim',
            '[Sunni] [Salafi] (English) Sunan an Nasai',
            '[Sunni] [Salafi] (English) Sunan Abu Dawud',
            '[Sunni] [Salafi] (English) Jami At Tirmidhi',
            '[Sunni] [Salafi] (English) Sunan Ibn Majah',
            '[Sunni] [Salafi] (English) Muwatta Malik',
            '[Sunni] [Salafi] (English) Forty Hadith of Shah Waliullah Dehlawi',
            '[Sunni] [Salafi] (English) Forty Hadith of an-Nawawi',
            '[Sunni] [Salafi] (English) Forty Hadith Qudsi',

            '[Shia] (English) Al-Amālī (Muḥammad al-Mufīd)',
            '[Shia] (English) Al-Amālī (ʿAlī al-Ṣaduq)',
            '[Shia] (English) Al-Kāfi - Volume 1',
            '[Shia] (English) Al-Kāfi - Volume 2',
            '[Shia] (English) Al-Kāfi - Volume 3',
            '[Shia] (English) Al-Kāfi - Volume 4',
            '[Shia] (English) Al-Kāfi - Volume 5',
            '[Shia] (English) Al-Kāfi - Volume 6',
            '[Shia] (English) Al-Kāfi - Volume 7',
            '[Shia] (English) Al-Kāfi - Volume 8',
            '[Shia] (English) Al-Khiṣāl',
            '[Shia] (English) Al-Tawḥīd',
            '[Shia] (English) Faḍaʾil al-Shīʿa',
            '[Shia] (English) Kāmil al-Ziyārāt',
            '[Shia] (English) Kitāb al-Ḍuʿafāʾ',
        ]

    return Utils.search_in_obj(user_input, Translation.HADITH)[:25]


async def autocomplete_tafsirs(_, user_input: str) -> list:
    return Utils.search_in_obj(user_input, Translation.TAFSIR)[:25]


@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}')


@bot.slash_command(name='ping', description='Ping bot')
async def ping(interaction):
    await interaction.response.send_message(content=f'Pong! *{int(bot.latency * 1000)}ms*', ephemeral=True)


@bot.slash_command(name='scripturebot', description='Getting started with ScriptureBot')
async def getting_started(interaction):
    await interaction.response.send_message(
        embed=disnake.Embed(
            color=disnake.Color.from_rgb(218, 157, 82),
            description=
            '**ScriptureBot** is a bot designed for quick access to the scripture or the texts related to it.'
            '\n## Bible'
            '\n### Books\n'
            'Due to Discord\'s limitations, only 25 books of the Bible are displayed in the options menu. However, you '
            'can search for any book, including the deuterocanonical ones, by typing its name. For instance, entering '
            '"lam" will display "Lamentations".'
            '\n### Translation\n'
            'Instead of typing full name of translation or manually choosing it from options menu, you can simply type '
            'the abbreviation of translation enclosed in braces (for example: `KJV`, `NIV` etc.)\n\nAlso, if you try '
            'to get deuterocanonical (aka apocryphal) book and your translation does not contain that book, then it '
            'will be automatically switched to the translation that does. This feature applies only to /bible command'
            '\n## Quran'
            '\n### Surahs\n'
            'Similarly to the Bible, Quran\'s options menu is limited to displaying 25 surahs. You can either select a '
            'surah from the menu or search for one by typing its number or name. For example, entering "7" will '
            'display all surahs that contain number 7. However, you can just leave the number "7" as it is and '
            'continue, by typing the verse and you will get the desired verse in the 7th chapter.',
        ),
        ephemeral=True
    )


@bot.slash_command(name='bible', description='Get Bible verses')
async def bible(
        interaction,
        book: str = commands.Param(
            description = 'Book of the Bible. Example: "John" or "Revelation" (shorthand "Rev.")',
            autocomplete = autocomplete_bible_book
        ),
        chapter: int = commands.Param(gt = 0, lt = 150),
        verse: int = commands.Param(gt = 0, lt = 176),
        to_verse: int = commands.Param(gt = 0, lt = 176, default = -1),
        translation: str = commands.Param(
            default = 'NKJV',
            autocomplete = autocomplete_bible_translations
        )
):
    if to_verse < 0:
        to_verse = verse

    if Translation.BIBLE.get(translation):
        translation = Translation.BIBLE[translation]

    if book.lower() in ['prayer of azariah'] and translation.upper() not in ['CEB', 'NRSVA', 'NRSVUE']:
        translation = 'CEB'

    if book.lower() in [
        'greek esther',
        'psalm 151', 'psalms 151', 'ps. 151', 'ps 151'
    ] and translation.upper() not in ['CEB', 'NRSVA', 'NRSVUE', 'RSV']:
        translation = 'CEB'

    if book.lower() in [
        'letter of jeremiah',
        'susanna', 'sus', 'sus.',
        'bel and the dragon'
        '1 esdras', '1 esd', '1 esd.',
        '2 esdras', '2 esd', '2 esd.',
        '3 maccabees', '3 mac', '3 mac.', '3 macc', '3 macc.',
        '4 maccabees', '4 mac', '4 mac.', '4 macc', '4 macc.',
        'prayer of manasseh'
    ] and translation.upper() not in ['CEB', 'NRSVA', 'NRSVUE', 'RSV', 'WYC']:
        translation = 'CEB'

    if book.lower() in [
        'tobit', 'tob', 'tob.',
        'judith', 'judi', 'judi.',
        'wisdom', 'wis', 'wis.', 'wisdom of solomon',
        'sirach', 'sir', 'sir.', 'wisdom of ben sira', 'ecclesiasticus',
        'baruch', 'bar', 'bar.',
        '1 maccabees', '1 mac', '1 mac.', '1 macc', '1 macc.',
        '2 maccabees', '2 mac', '2 mac.', '2 macc', '2 macc.'
    ] and translation.upper() not in\
            ['CEB', 'DRA', 'GNT', 'NABRE', 'NCB', 'NRSVA', 'NRSVACE', 'NRSVCE', 'NRSVUE', 'RSV', 'RSVCE', 'WYC']:
        translation = 'CEB'

    response = Bible.get(book, chapter, verse, to_verse, translation)

    await handle_response(interaction, response, title=Utils.get_corresponding_key(Translation.BIBLE, translation))


@bot.slash_command(name='query_bible', description='Query Bible verses')
async def query_bible(
        interaction,
        query: str = commands.Param(
            description = 'Query example: `Luke 24:46-47; Psalm 40:5, 18:6; Revelation 1:8, 17-18, 22:13`'
        ),
        translation: str = commands.Param(
            default = 'NKJV',
            autocomplete = autocomplete_bible_translations
        )
):
    if Translation.BIBLE.get(translation):
        translation = Translation.BIBLE[translation]

    response = Bible.query(query, translation)

    await handle_response(interaction, response, title=Utils.get_corresponding_key(Translation.BIBLE, translation))


@bot.slash_command(name='quran', description='Get Quran verses')
async def quran(
        interaction,
        chapter: str = commands.Param(
            description = 'aka surah',
            autocomplete = autocomplete_quran_chapter
        ),
        verse: int = commands.Param(gt = 0, lt = 286, description = 'aka ayat'),
        to_verse: int = commands.Param(gt = 0, lt = 286, default = -1),
        translation: str = commands.Param(
            default = 'eng-farookmalik',
            autocomplete = autocomplete_quran_translations
        )
):
    if to_verse < 0:
        to_verse = verse

    if Translation.QURAN.get(translation):
        translation = Translation.QURAN[translation]

    if chapter.isdecimal() and Titles.SURAH.get(int(chapter)):
        chapter = int(chapter)
    else:
        chapter = Utils.get_corresponding_key(Titles.SURAH, chapter)

    if chapter and 0 < chapter <= 114 and 0 < verse <= 286:
        response = Quran.get(chapter, verse, to_verse, translation)
    else:
        response = ''

    await handle_response(interaction, response, title=Utils.get_corresponding_key(Translation.QURAN, translation))


@bot.slash_command(name='query_quran', description='Query Quran verses')
async def query_quran(
        interaction,
        query: str = commands.Param(
            description = 'Query example: `11:3, 16:18, 53, 57:3`'
        ),
        translation: str = commands.Param(
            default = 'eng-farookmalik',
            autocomplete = autocomplete_quran_translations
        )
):
    if Translation.QURAN.get(translation):
        translation = Translation.QURAN[translation]

    response = Quran.query(query, translation)

    await handle_response(interaction, response, title=Utils.get_corresponding_key(Translation.QURAN, translation))


@bot.slash_command(name='hadith', description='Get hadith')
async def hadith(
        interaction,
        hadith_book: str = commands.Param(
            name = 'hadith',
            autocomplete = autocomplete_hadiths
        ),
        hadith_no: int = commands.Param(
            gt = 0
        ),
):
    branch = IslamBranch.SUNNI if hadith_book.startswith('[Sunni]') else IslamBranch.SHIA

    if Translation.HADITH.get(hadith_book):
        hadith_book = Translation.HADITH[hadith_book]

    response = ''

    if branch == IslamBranch.SUNNI:
        response = Hadith.get(hadith_no, hadith_book)
    elif branch == IslamBranch.SHIA:
        response = ShiaHadith.get(hadith_no, hadith_book)

    await handle_response(interaction, response)


@bot.slash_command(name='query_hadith', description='Query hadiths')
async def query_hadith(
        interaction,
        hadith_book: str = commands.Param(
            name = 'hadith',
            autocomplete = autocomplete_hadiths
        ),
        query: str = commands.Param(
            description = 'Query example: `2682, 3286, 3318-3319`'
        ),
):
    branch = IslamBranch.SUNNI if hadith_book.startswith('[Sunni]') else IslamBranch.SHIA

    if Translation.HADITH.get(hadith_book):
        hadith_book = Translation.HADITH[hadith_book]

    if branch == IslamBranch.SUNNI:
        response = Hadith.query(query, hadith_book)

        await handle_response(interaction, response)
    elif branch == IslamBranch.SHIA:
        await interaction.response.defer()

        response = ShiaHadith.query(query, hadith_book)

        await handle_response(interaction, response, deferred=True)


@bot.slash_command(name='tafsir', description='Get Tafsir')
async def tafsir(
        interaction,
        chapter: str = commands.Param(
            description = 'aka surah',
            autocomplete = autocomplete_quran_chapter
        ),
        verse: int = commands.Param(gt = 0, lt = 286, description = 'aka ayat'),
        to_verse: int = commands.Param(gt = 0, lt = 286, default = -1),
        translation: str = commands.Param(
            default = 'en-tafisr-ibn-kathir',
            autocomplete = autocomplete_tafsirs
        )
):
    if to_verse < 0:
        to_verse = verse

    if Translation.TAFSIR.get(translation):
        translation = Translation.TAFSIR[translation]

    if chapter.isdecimal() and Titles.SURAH.get(int(chapter)):
        chapter = int(chapter)
    else:
        chapter = Utils.get_corresponding_key(Titles.SURAH, chapter)

    if chapter and 0 < chapter <= 114 and 0 < verse <= 286:
        response = Tafsir.get(chapter, verse, to_verse, translation)
    else:
        response = ''

    await handle_response(interaction, response, title=Utils.get_corresponding_key(Translation.TAFSIR, translation))

bot.run(token=TOKEN)
