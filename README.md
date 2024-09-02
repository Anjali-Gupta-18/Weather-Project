# Web Scraping Twitter Account Data from Wikipedia

## Project Overview
This project involves a Python script that scrapes data from the Wikipedia page listing the most-followed Twitter accounts. The script extracts information from an HTML table, including the rank, account name, number of followers, and other relevant details. The data is then saved to a CSV file with UTF-8 encoding, ensuring compatibility and proper handling of special characters.

## Features
- Scrapes the most-followed Twitter accounts from Wikipedia.
- Extracts key information such as rank, account name, and follower count.
- Saves the extracted data into a CSV file.
- Uses BeautifulSoup for parsing HTML and CSV module for data export.

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `lxml` parser (for BeautifulSoup)

## Installation
To get started, clone this repository and install the required Python packages:

```bash
git clone https://github.com/yourusername/twitter-scraper.git
cd twitter-scraper
pip install requests beautifulsoup4 lxml
