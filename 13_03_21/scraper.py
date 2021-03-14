# listing im-manufacturers-listing
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

ENDPOINT = 'https://buy.am/hy/food-court?p={}'
FILE_NAME = 'buyam_{}.html'


def save_data(endpoint):
    page = 1
    while page != 18:
        response = requests.get(endpoint.format(page))
        if response.status_code == 200:
            with open(FILE_NAME.format(page), 'w+b') as html_file:
                html_file.write(response.content)
            page += 1
        else:
            print(response.status_code, response.text)
            break

# save_data(ENDPOINT)

def get_parsed_data(pages):
    data_dict = []

    for page in range(1, pages+1):
        html_1 = open(FILE_NAME.format(page), 'r')
        data = html_1.read()
        html_1.close()
        strainer = SoupStrainer(name='div', attrs={'class': 'listing im-manufacturers-listing'})

        soup = BeautifulSoup(data, 'html.parser', parse_only=strainer)
        list_of_rest = soup.div.find_all('a')

        for a in list_of_rest:
            infos = a.find('div', attrs={'class': "manufacturer-info"}).stripped_strings


            data_dict.append({
                'name': next(infos),
                'open_hours': next(infos),
                'image_url': a.find('span', attrs={'class': "img-logo-media"}).img['src']
            })
    return data_dict

data_dict = get_parsed_data(1)
print(data_dict)
