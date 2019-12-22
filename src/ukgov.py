import webloader
from bs4 import BeautifulSoup as soup

def get_company_credentials(url):

    html = webloader.load(url)
    return html_to_list(html)

def html_to_list(html):
    page_soup = soup(html, "html.parser")
    table = page_soup.find("div", {"class": "govspeak"}).table.findAll("tr")

    table_list = []

    for row in table:
        cells = row.findAll("td")
        table_row = []

        for cell in cells:
            table_row.append(cell.contents[0])

        table_list.append(table_row)

    return table_list[1:-1]
