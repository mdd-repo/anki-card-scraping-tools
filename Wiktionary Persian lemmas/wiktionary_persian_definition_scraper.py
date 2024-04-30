import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_word_page(word_url):
    try:
        print("Scraping word page:", word_url)
        response = requests.get(word_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate Persian word
        persian_word_element = soup.find('strong', class_='Arab')
        persian_word = persian_word_element.text.strip() if persian_word_element else "Not found"

        # Locate pronunciation
        pronunciation_element = soup.find('span', class_='headword-tr')
        pronunciation = pronunciation_element.text.strip() if pronunciation_element else "Not found"

        # Locate definitions excluding redundant redirects
        definitions = []
        # Find the section with the Persian language heading
        persian_heading = soup.find('span', class_='mw-headline', id='Persian')
        if persian_heading:
            # Navigate to the next <ol> element containing definitions
            headword_line_span = persian_heading.find_next('span', class_='headword-line')
            if headword_line_span:
                ol_list = headword_line_span.find_next('ol')
                if ol_list:
                    # Locate text from <li> elements
                    for li in ol_list.find_all('li'):
                        # Exclude <dl> and <ul> elements
                        for dl in li.find_all('dl'):
                            dl.decompose()
                        for ul in li.find_all('ul'):
                            ul.decompose()
                        definition_text = li.get_text(separator=' ').strip()  # Get text with space separators
                        # Check if the definition contains "Alternative form of"
                        if "Alternative form of" not in definition_text:
                            definitions.append(definition_text)
        else:
            definitions = ["Not found"]

        # Locate etymology
        etymology = ""
        etymology_heading = soup.find('span', class_='mw-headline', string='Etymology')
        if etymology_heading:
            etymology_paragraph = etymology_heading.find_next('p')
            etymology = etymology_paragraph.text.strip() if etymology_paragraph else "Not found"

        return persian_word, pronunciation, "\n".join(definitions), etymology
    except Exception as e:
        print(f"Error scraping word page: {word_url}")
        print(e)
        return "Not found", "Not found", "Not found", "Not found"

def scrape_category_words(category_url):
    data = []
    while category_url:
        print("Scraping category page:", category_url)
        try:
            response = requests.get(category_url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the list of words under headings containing the phrase "Pages in category _"
            word_list_headings = soup.find_all('h2', string=lambda text: 'Pages in category' in text)
            if word_list_headings:
                print("Found 'Pages in category' headings")
                for heading in word_list_headings:
                    word_list = heading.find_next('div', class_='mw-category')
                    if word_list:
                        print("Found word list")
                        # Locate word URLs
                        word_links = word_list.find_all('a')
                        for word_link in word_links:
                            # How to build the URL for each word page
                            word_url = "https://en.wiktionary.org" + word_link.get("href") + "#Persian"
                            # Scrape the word page for information
                            persian_word, pronunciation, definitions, etymology = scrape_word_page(word_url)
                            # Skip words with only "Alternative form of _" definitions
                            if definitions != "Not found" and not all("Alternative form of" in definition for definition in definitions):
                                print("Scraped word:", persian_word, "Pronunciation:", pronunciation, "Definitions:", definitions, "Etymology:", etymology)
                                data.append([f"{persian_word} ({pronunciation})", definitions, etymology])
                    # Stop scraping when another h2 element is encountered to prevent going into other language categories
                    next_h2 = heading.find_next_sibling('h2')
                    if next_h2:
                        if next_h2.find('span', class_='mw-headline', string='Persian'):
                            break
            else:
                print("Could not find 'Pages in category' headings")

            # Find the link to the next page
            next_page_link = soup.find('a', text='next page')
            if next_page_link:
                category_url = "https://en.wiktionary.org" + next_page_link.get("href")
            else:
                category_url = None
        except Exception as e:
            print(f"Error scraping category page: {category_url}")
            print(e)
            category_url = None  # Move to the next category URL if an error occurs

    return data

# Target category page in the Lemmas
category_url = "https://en.wiktionary.org/wiki/Category:Persian_nouns"
data = scrape_category_words(category_url)

# Convert data to the column format needed
df = pd.DataFrame(data, columns=["Front", "Back", "Footnotes"])

# Export to Excel
df.to_excel("wiktionary_persian_nouns.xlsx", index=False)
print("Data exported to 'wiktionary_persian_nouns.xlsx'")


# List of website / file name pairs. I purposefully chose not to automate this because of the length of the Nouns category. Long story. If you re-run this, run the Nouns last.
# https://en.wiktionary.org/wiki/Category:Persian_adjectives = wiktionary_persian_adjectives.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_adverbs = wiktionary_persian_adverbs.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_conjunctions = wiktionary_persian_conjunctions.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_determiners = wiktionary_persian_determiners.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_interjections = wiktionary_persian_interjections.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_prefixes = wiktionary_persian_morphemes_prefixes.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_suffixes = wiktionary_persian_morphemes_suffixes.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_multiword_terms = wiktionary_persian_multiword_terms.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_nouns = wiktionary_persian_nouns.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_numerals = wiktionary_persian_numerals.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_particles = wiktionary_persian_particles.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_phrases = wiktionary_persian_phrases.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_prepositions = wiktionary_persian_prepositions.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_pronouns = wiktionary_persian_pronouns.xlsx
# https://en.wiktionary.org/wiki/Category:Persian_verbs = wiktionary_persian_verbs.xlsx