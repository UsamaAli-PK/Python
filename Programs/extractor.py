import requests
from bs4 import BeautifulSoup
import csv

# URL of the AI News archive page
url = "https://buttondown.com/ainews/archive/ainews-lots-of-small-launches/"

# Fetch the webpage content
response = requests.get(url)
if response.status_code != 200:
    raise Exception(f"Failed to load page {url}")

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Extract the title (if available)
title_tag = soup.find('h1')
title = title_tag.get_text(strip=True) if title_tag else 'No title found'

# Extract the publication date (if available, e.g., within a <time> tag)
time_tag = soup.find('time')
pub_date = time_tag.get_text(strip=True) if time_tag else 'No date found'

# Extract bullet points.
# First try to find list items within any unordered list.
bullet_points = [li.get_text(strip=True) for li in soup.find_all('li') if li.get_text(strip=True)]

# Fallback: if no bullet points were found, look for lines that start with a dash.
if not bullet_points:
    bullet_points = []
    for line in soup.get_text().splitlines():
        line = line.strip()
        if line.startswith("-"):
            bullet_points.append(line)

# Check if we extracted any data
if not bullet_points:
    print("No bullet points were found. The page structure might have changed.")

# Write the extracted information to a CSV file.
csv_filename = "ai_news.csv"
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write a header row
    writer.writerow(['Title', 'Publication Date', 'Bullet Point'])
    # Write one row per bullet point
    for bullet in bullet_points:
        writer.writerow([bullet])

print(f"Data has been written to {csv_filename}")
