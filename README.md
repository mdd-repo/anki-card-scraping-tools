# Anki Card Scraping Tools
A collection of Python scripts used for generating Anki cards through web scraping and file scraping.<br>
`ctrl + shift + s` downloads target files after clicking the link to them; key files linked below.

**I love language learning and using Anki.**<br>
Now, ideally, I would just type entire dictionaries[^1] into the card creator by hand. Unfortunately life is short and I do not have time to do that for everything. So I automate the process in Python whenever I run into a resource I need to scrape for vocabulary.

------

### 4/30/24 - Literally All Of Wiktionary: Persian lemmas (Persian / Farsi Anki Cards)
Note: This is still currently scraping. Description has been written in advance. It is over 8900 cards so will take a little while.<br>
`This card deck was last scraped on April 30th, 2024.`<br>
I cannot fully explain what possessed me to do this, beyond "I will use it."<br> 
Will anyone else? Maybe. Maybe not. I still wanted to do it.<br>

This is a web scraped Anki deck pack that includes the [entire Wiktionary database for words and phrases in Farsi/Persian](https://en.wiktionary.org/wiki/Category:Persian_lemmas). They are sorted by part of speech, just as the "Persian lemmas" page divides them, and from there the script picks out the word, pronunciation, definitions, and etymology; redundant entries are passed over in favor of those with definitions. Due to the sheer quantity, expect minor formatting errors. Due to the nature of Wikipedia/Wiktionary, be critical.<br>

Included: the [Python code](), the [spreadsheets](), and the [Anki deck pack]().<br>
Categories: adjectives, adverbs, conjunctions, determiners, interjections, multi-word terms, nouns, numerals, particles, phrases, prepositions, pronouns, verbs.

------

### 4/28/24 - Muskogee / Mvskoke Language Web Dictionary (Mvskoke Anki Cards)
`This card deck was last scraped from the April 24th, 2024 update.`<br>
The wonderful teachers at [Mvskoke Opunvkv](https://www.mvskokeopunvkv.com/) have included an online edition of the 2000 "A Dictionary of Creek / Muskogee" reference book compiled by Jack B. Martin and Margaret McKane Mauldin, viewable [here](https://www.webonary.org/muscogee/overview/introduction/).[^2]<br>

Included: the [Python code](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/mvskoke_dictionary_scraper.py), the [spreadsheet](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/jbm_mmm_mvskoke_english_dictionary_entries.xlsx), and the [Anki deck](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/A%20Dictionary%20of%20Mvskoke%20Card%20Deck.apkg) made from the current release.<br>

 

 
[^1]:Recommendation for the whole-dictionary method: After importing into Anki, click on the deck, then Browse, then shift-click the first and last cards to select everything. Right click, and Toggle Suspend. Go section by section, or by words as you learn them individually, and un-Toggle Suspend, so as to not be overwhelmed. You can also use this to construct your own frequency lists, particularly for languages that do not have readily available lists to study.
[^2]: This web edition is still in its drafting stages. According to the roadmap, there will be several more rounds of community review before its final version is made public.
