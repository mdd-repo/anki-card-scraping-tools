import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape and format data
def scrape_and_format_data(base_url):
    # Initialize lists to store data
    all_front_column = []
    all_back_column = []
    
    # Iterate through each letter of the alphabet
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        page_number = 1  # Start with the first page
        
        while True:
            # Construct the URL for the current page
            page_url = base_url.format(letter, page_number)
            
            # Send a GET request to the page URL
            page_response = requests.get(page_url)
            
            # Check if the request was successful
            if page_response.status_code == 200:
                # Parse the HTML content
                page_soup = BeautifulSoup(page_response.text, 'html.parser')
                
                # Find all posts (dictionary entries)
                posts = page_soup.find_all('div', class_='post')
                
                # Check if there are no posts on the current page
                if not posts:
                    print(f"No more entries for letter '{letter}' on page {page_number}")
                    break
                
                # Initialize lists to store data for the current page
                front_column = []
                back_column = []
                
                # Iterate over each post on the current page
                for post in posts:
                    # Check for essential information in the post
                    mvskoke_word_tag = post.find('span', lang='mus')
                    pronunciation_tag = post.find('span', class_='pronunciations')
                    part_of_speech_tag = post.find('span', class_='sharedgrammaticalinfo')
                    
                    if mvskoke_word_tag and pronunciation_tag and part_of_speech_tag:
                        # Extract Mvskoke word
                        mvskoke_word = mvskoke_word_tag.text.strip()
                        
                        # Extract pronunciation
                        pronunciation = pronunciation_tag.text.strip()
                        
                        # Extract part of speech
                        part_of_speech = part_of_speech_tag.text.strip()
                        
                        # Extract sense numbers
                        sense_numbers_tags = post.find_all('span', class_='sensenumber')
                        sense_numbers = [tag.text.strip() for tag in sense_numbers_tags]
                        
                        # Extract English definitions
                        definitions = post.find_all(['span', 'div'], class_=['definitionorgloss', 'definition'])
                        english_definitions = []
                        for definition in definitions:
                            definition_text = definition.text.strip()
                            # Remove symbols and emojis
                            definition_text = definition_text.replace('🔊', '').replace('\n', ' ')
                            english_definitions.append(definition_text)
                        
                        # Format sense numbers with definitions
                        formatted_definitions = []
                        if sense_numbers:
                            for sense_number, definition in zip(sense_numbers, english_definitions):
                                formatted_definitions.append(f"{sense_number}. {definition}")
                        else:
                            formatted_definitions = english_definitions
                        
                        # Format data into columns
                        front_column.append(f"{mvskoke_word} [{pronunciation}]")
                        back_column.append(f"{part_of_speech}\n{'\n'.join(formatted_definitions)}")
                    else:
                        print("Skipping post with missing information")
                
                # Add the data for the current page to the overall data lists
                all_front_column.extend(front_column)
                all_back_column.extend(back_column)
                
                print(f"Scraped {len(posts)} entries for letter '{letter}' page {page_number}")
                
                # Move to the next page
                page_number += 1
            else:
                print(f"Failed to retrieve data for letter '{letter}' page {page_number}")
                break
    
    # Create a DataFrame from the lists
    data = {'Front': all_front_column, 'Back': all_back_column}
    df = pd.DataFrame(data)
    
    # Save the DataFrame to an Excel file
    df.to_excel('jbm_mmm_mvskoke_english_dictionary_entries.xlsx', index=False)
    
    print("Data saved to 'jbm_mmm_mvskoke_english_dictionary_entries.xlsx' successfully.")

# Base URL of the website
base_url = "https://www.webonary.org/muscogee/browse/browse-muscogee/?letter={}&key=mus&pagenr={}"

# Call the function with the base URL
scrape_and_format_data(base_url)
