from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
scraped_data = []
START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome()
browser.get(START_URL)


def scrape():
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    bright_star_table = soup.find('table', attrs={'class', 'wikitable'})

    table_body = bright_star_table.find('tbody')

    table_rows = table_body.find_all('tr')

    for row in table_rows:
        table_cols = row.find_all('td')
        print(table_cols)


scrape()
