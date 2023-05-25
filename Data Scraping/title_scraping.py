import requests
import csv
from bs4 import BeautifulSoup

# Specify the base URL and number of pages to scrape
base_url = 'https://idrw.org/page/'
num_pages = 103

# Create a list to store all the extracted data
data = []

# Iterate over the page numbers
for page in range(1, num_pages + 1):
    # Construct the URL for the current page
    url = base_url + str(page) + '/'

    # Send an HTTP GET request to the website
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()

        # Parse the HTML content using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all header elements and extract titles, links, and published dates
        headers = soup.find_all('a', {'rel': 'bookmark'})
        dates = soup.find_all('span', {'class': 'entry-date'})

        # Extract the title, link, and published date for each header and append to the data list
        for header, date in zip(headers, dates):
            title = header.text.strip()
            link = header['href']
            published_date = date.text.strip()
            data.append([title, link, published_date])

    except (requests.exceptions.RequestException, requests.exceptions.Timeout) as e:
        print(f"An error occurred while requesting page {page}: {str(e)}")
        continue

# Save the data to a CSV file
csv_filename = 'idrw_webdata.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link', 'Published Date'])
    writer.writerows(data)

print(f"Scraped data saved to {csv_filename}.")