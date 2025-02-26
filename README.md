# ScriptureBot

**ScriptureBot** is a bot that was created for quick access to the scripture or the texts related to it.

![](https://img.shields.io/badge/Python-3.8.9-blue.svg) ![](https://img.shields.io/badge/Disnake-2.9.3-blue.svg)

## What texts can I access through bot?

For now, you can access Bible (including deuterocanon), Quran, hadiths and tafsirs.

## Todo

- [ ] Add councils
- [x] Add ability to look for shia hadiths
- [x] Add tafsir slash command

## Getting started

(First two steps can be skipped, although, they are recommended)

Setup the virtual environment:

```sh
python -m venv venv
```

Then activate it:

```sh
%cd%/venv/Scripts/activate.bat
```

Install the required packages:

```sh
pip install -r requirements.txt
```

Then, create `.env` file with token of your discord bot:

```none
TOKEN=your_bot's_token_here
```

Done! Now you can start bot, by simply typing:

```sh
python main.py
```