flashcard-french 🇫🇷
A French-English flashcard app built with Python and Tkinter. Cards auto-flip after 3 seconds to reveal the translation, and the app tracks which words you already know so you only study what you need.
Features

Displays a random French word on each flashcard
Automatically flips the card after 3 seconds to show the English translation
✅ Mark a word as known — it gets removed from future sessions
❌ Skip a word — it stays in the rotation
Progress is saved between sessions in words_to_learn.csv
On first run, loads all words from french_words.csv

Project Structure
flashcard-french/
│
├── main.py
├── data/
│   ├── french_words.csv       # Full word list
│   └── words_to_learn.csv     # Auto-generated — words still to learn
└── images/
    ├── card_front.png
    ├── card_back.png
    ├── right.png
    └── wrong.png
Requirements

Python 3.x
pandas

Install dependencies:
bashpip install pandas
How to Run
bashpython main.py
How It Works

On launch, the app checks if words_to_learn.csv exists. If it does, it loads that. Otherwise it loads french_words.csv.
A random word is shown on the front of the card in French.
After 3 seconds, the card flips to show the English translation.
Press ✅ if you knew the word — it's removed from the list and saved.
Press ❌ to move on without removing the word.
Repeat until you've learned them all!
