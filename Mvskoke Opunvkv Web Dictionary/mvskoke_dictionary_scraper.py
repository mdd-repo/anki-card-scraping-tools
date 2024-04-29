import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_and_format_data(base_url):
    all_front_column = []
    all_back_column = []
    
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        page_number = 1
        
        while True:
            page_url = base_url.format(letter, page_number)
            page_response = requests.get(page_url)
            
            if page_response.status_code == 200:
                page_soup = BeautifulSoup(page_response.text, 'html.parser')
                
                posts = page_soup.find_all('div', class_='post')
                
                if not posts:
                    print(f"No more entries for letter '{letter}' on page {page_number}")
                    break
                
                front_column = []
                back_column = []
                
                for post in posts:
                    mvskoke_word_tag = post.find('span', lang='mus')
                    pronunciation_tag = post.find('span', class_='pronunciations')
                    part_of_speech_tag = post.find('span', class_='sharedgrammaticalinfo')
                    
                    if mvskoke_word_tag and pronunciation_tag and part_of_speech_tag:
                        mvskoke_word = mvskoke_word_tag.text.strip()
                        
                        pronunciation = pronunciation_tag.text.strip()
                        
                        part_of_speech = part_of_speech_tag.text.strip()
                        
                        sense_numbers_tags = post.find_all('span', class_='sensenumber')
                        sense_numbers = [tag.text.strip() for tag in sense_numbers_tags]
                        
                        definitions = post.find_all(['span', 'div'], class_=['definitionorgloss', 'definition'])
                        english_definitions = []
                        for definition in definitions:
                            definition_text = definition.text.strip()
                            # Remove symbols and emojis
                            definition_text = definition_text.replace('🔊', '').replace('\n', ' ')
                            english_definitions.append(definition_text)
                        
                        formatted_definitions = []
                        if sense_numbers:
                            for sense_number, definition in zip(sense_numbers, english_definitions):
                                formatted_definitions.append(f"{sense_number}. {definition}")
                        else:
                            formatted_definitions = english_definitions
                        
                        front_column.append(f"{mvskoke_word} [{pronunciation}]")
                        back_column.append(f"{part_of_speech}\n{'\n'.join(formatted_definitions)}")
                    else:
                        print("Skipping post with missing information")
                
                all_front_column.extend(front_column)
                all_back_column.extend(back_column)
                
                print(f"Scraped {len(posts)} entries for letter '{letter}' page {page_number}")
                
                page_number += 1
            else:
                print(f"Failed to retrieve data for letter '{letter}' page {page_number}")
                break
    
    data = {'Front': all_front_column, 'Back': all_back_column}
    df = pd.DataFrame(data)
    
    df.to_excel('jbm_mmm_mvskoke_english_dictionary_entries.xlsx', index=False)
    
    print("Data saved to 'jbm_mmm_mvskoke_english_dictionary_entries.xlsx' successfully.")

base_url = "https://www.webonary.org/muscogee/browse/browse-muscogee/?letter={}&key=mus&pagenr={}"

scrape_and_format_data(base_url)
