# Anki Card Scraping Tools
A collection of Python scripts used for generating Anki cards through web scraping and file scraping.

**I love language learning and using Anki.**
Now, ideally, I would just type entire dictionaries[^1] into the card creator by hand. Unfortunately life is short and I do not have time for that for everything. So I automate the process in Python whenever I run into a resource I need to scrape for vocabulary.

### Mvskoke Opunvkv Web Dictionary
The wonderful teachers at [Mvskoke Opunvkv](https://www.mvskokeopunvkv.com/) have included an online edition of the 2000 "A dictionary of Creek / Muskogee" reference book compiled by Jack B. Martin and Margaret McKane Mauldin, viewable [here](https://www.webonary.org/muscogee/overview/introduction/)[^2].
I have created a Python code that targets various HTML elements and extracts their contents, then formats them into two Anki-friendly columns. Included is the [Python code](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/mvskoke_dictionary_scraper.py), the [spreadsheet](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/jbm_mmm_mvskoke_english_dictionary_entries.xlsx), and the [Anki deck](https://github.com/mdd-repo/anki-card-scraping-tools/blob/main/Mvskoke%20Opunvkv%20Web%20Dictionary/A%20Dictionary%20of%20Mvskoke%20Card%20Deck.apkg) made from the current release.
`This card deck is from the site's April 24th, 2024 update.`

[^1]:Recommendation for the whole-dictionary method: After importing into Anki, click on the deck, then Browse, then shift-click the first and last cards to select everything. Right click, and Toggle Suspend. Go section by section, or by words as you learn them individually, and un-Toggle Suspend, so as to not be overwhelmed.
[^2]: This web edition is still in its drafting stages. According to the roadmap, there will be several more rounds of peer and scholarly review before its final version is made public.
