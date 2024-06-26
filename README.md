# Anki Card Scraping Tools
A collection of Python scripts used for generating Anki cards through web scraping and file scraping.<br>
`ctrl + shift + s` downloads target files after clicking the link to them; key files linked below.

**I love language learning and using Anki.**<br>
Now, ideally, I would just type entire dictionaries[^1] into the card creator by hand. Unfortunately life is short and I do not have time to do that for everything. So I automate the process in Python whenever I run into a resource I need to scrape for vocabulary.

------

### Wiktionary: Persian lemmas (Persian / Farsi Anki Cards)
`This card deck was last scraped on April 30th, 2024.`<br>
I cannot fully explain what possessed me to do this, beyond "I will use it."<br> 
Will anyone else? Maybe. Maybe not. I still wanted to do it.<br>

This is a web scraped Anki deck pack that includes the [entire Wiktionary database for words and phrases in Farsi/Persian](https://en.wiktionary.org/wiki/Category:Persian_lemmas). Incredibly hefty at 13,383 cards. They are sorted by part of speech, just as the Persian lemmas page divides them, and from there the script picks out the word, pronunciation, definitions, and etymology; redundant entries are passed over in favor of those with definitions. Due to the sheer quantity, expect minor formatting errors. Due to the nature of Wikipedia/Wiktionary, be critical.<br>

Included: the [Python code](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Wiktionary%20Persian%20lemmas/wiktionary_persian_definition_scraper.py), the spreadsheets, and the [Anki deck pack](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Wiktionary%20Persian%20lemmas/Wiktionary%20Persian%20lemmas.apkg).<br>
Categories: adjectives, adverbs, conjunctions, determiners, interjections, morphemes, multi-word terms, nouns, numerals, particles, phrases, prepositions, pronouns, verbs.<br>

I have taken the liberty of removing any racial and ethnic slurs that I could find; this process may not have been perfect. Words that indicate sexual behavior and contact remain in the pack from a standpoint of linguistic knowledge. Please be aware of this when using the cards.

Available on [AnkiNet #1446159529](https://ankiweb.net/shared/info/1446159529)

------

### Muskogee / Mvskoke Language Web Dictionary (Mvskoke Anki Cards)
`This card deck was last scraped from the April 24th, 2024 update.`<br>
The wonderful teachers at [Mvskoke Opunvkv](https://www.mvskokeopunvkv.com/) have included an online edition of the 2000 "A Dictionary of Creek / Muskogee" reference book compiled by Jack B. Martin and Margaret McKane Mauldin, viewable [here](https://www.webonary.org/muscogee/overview/introduction/).[^2]<br>

Included: the [Python code](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/mvskoke_dictionary_scraper.py), the [spreadsheet](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/jbm_mmm_mvskoke_english_dictionary_entries.xlsx), and the [Anki deck](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/A%20Dictionary%20of%20Mvskoke%20Card%20Deck.apkg) made from the current release.<br>

Available on [AnkiNet #2044931447](https://ankiweb.net/shared/info/2044931447).<br>

 

 
[^1]:Recommendation for the whole-dictionary method: After importing into Anki, click on the deck, then Browse, then shift-click the first and last cards to select everything. Right click, and Toggle Suspend. Go section by section, or by words as you learn them individually, and un-Toggle Suspend, so as to not be overwhelmed. You can also use this to construct your own frequency lists, particularly for languages that do not have readily available lists to study.
[^2]: This web edition is still in its drafting stages. According to the roadmap, there will be several more rounds of community review before its final version is made public.
