import csv
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import Timeout, RequestException
from time import sleep

# Specify the CSV file path
csv_file = 'idrw_webdata.csv'

# Specify the number of links to test
num_links_to_test = 1516

# Create a list to store all the article data
article_data = []

# Function to scrape an article
def scrape_article(row, retry=False):
    title = row[0]
    link = row[1]
    published_date = row[2]

    try:
        # Send an HTTP GET request to the article page with a timeout
        response = requests.get(link, timeout=10)
        response.raise_for_status()

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the article content by locating the paragraphs
        paragraphs = soup.find_all('p')

        # Extract the text from the paragraphs and join them into a single string
        article_text = ' '.join([p.get_text() for p in paragraphs])

        # Append the article data to the list
        article_data.append([title, link, published_date, article_text])
    except Timeout:
        if retry:
            print(f"Timeout occurred again while scraping the article for {title}. Skipping.")
        else:
            print(f"Timeout occurred while scraping the article for {title}. Retrying...")
            # Retry scraping after a delay of 5 seconds
            sleep(5)
            scrape_article(row, retry=True)
    except RequestException as e:
        print(f"An error occurred while scraping the article for {title}: {str(e)}")

# Read the CSV file
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)

    # Create a thread pool executor
    with ThreadPoolExecutor() as executor:
        # Iterate over the rows in the CSV file
        for row in reader:
            if num_links_to_test == 0:
                break

            # Submit the scraping task to the executor
            future = executor.submit(scrape_article, row)

            num_links_to_test -= 1

# Save the article data to a new CSV file
article_csv_filename = 'idrw_article_data.csv'
with open(article_csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Published Date', 'Article Text'])
    writer.writerows(article_data)

print(f"Scraped article data saved to {article_csv_filename}.")
