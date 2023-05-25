import csv
import re

# Specify the path of the input CSV file
input_csv_file = 'idrw_article_data.csv'

# Specify the path of the output CSV file
output_csv_file = 'cleaned.csv'

# Function to clean the article text
def clean_article_text(article_text):
    # Remove unwanted text
    cleaned_text = re.sub(r'NOTE\s*:\s*Article\s*cannot\s*be\s*reproduced\s*without\s*written\s*permission\s*of\s*idrw\.org\s*in\s*any\s*form\s*even\s*for\s*YouTube\s*Videos\s*to\s*avoid\s*Copy\s*right\s*strikes', '', article_text)
    cleaned_text = re.sub(r'Copyright\s*©\s*idrw\.org\s*\d{4}-\d{4}\.\s*All\s*Rights\s*Reserved\.Fair\s*Use\s*idrw\.org', '', cleaned_text)

    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text)

    return cleaned_text.strip()

# Read the input CSV file
with open(input_csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    header = next(reader)  # Read the header row

    # Get the index of the "Article Text" column
    article_text_index = header.index('Article Text')

    # Read and clean each row
    rows = []
    for row in reader:
        article_text = row[article_text_index]
        cleaned_text = clean_article_text(article_text)
        row[article_text_index] = cleaned_text
        rows.append(row)

# Write the cleaned data to the output CSV file
with open(output_csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Cleaned article data saved to {output_csv_file}.")
