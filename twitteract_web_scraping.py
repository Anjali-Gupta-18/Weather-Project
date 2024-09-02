import requests
import csv
from bs4 import BeautifulSoup

# Fetch the website content
website = requests.get('https://en.wikipedia.org/wiki/List_of_most-followed_Twitter_accounts').text

# Parse the content using BeautifulSoup
soup = BeautifulSoup(website, 'lxml')

# Find the table
table = soup.find('table', class_='wikitable')

# Extract table headers (column names)
headers = [header.text.strip() for header in table.findAll('th')]
headers = headers[1:5]

# Extract table rows
table_rows = table.findAll('tr')

# Initialize an empty list to store the data
data = []

# Iterate through table rows and extract the data
for tr in table_rows:
    td = tr.findAll('td')
    rows = [i.text.strip() for i in td]
    if rows:  # Only append rows that contain data
        data.append(rows)

# Export the data to a CSV file
with open('twitter_accounts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)

    # Write the headers
    writer.writerow(headers)

    # Write the data rows
    writer.writerows(data)

print("Data has been saved to CSV file successfully!")
