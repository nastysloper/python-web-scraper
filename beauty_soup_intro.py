from bs4 import BeautifulSoup


def read_file():
    file = open('intro_to_soup_html.html')
    data = file.read()
    file.close()
    return data


# make soup
html = read_file()

soup = BeautifulSoup(html, 'lxml')  # lxml is the parser

print(soup.prettify())
