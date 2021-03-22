# listing im-manufacturers-listing
import os
import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from helpers import send_email_for, engine, Restaurant
from sqlalchemy.orm import sessionmaker
abs_path = os.getcwd()

ENDPOINT = 'https://buy.am/hy/food-court?p={}'
FILE_NAME = f'{abs_path}/13_03_21/buyam_{{}}.html'


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
session = sessionmaker(engine)()

def get_parsed_data(pages):
    new_restaurants_ids = []
    for page in range(1, pages+1):
        html_1 = open(FILE_NAME.format(page), 'r')
        data = html_1.read()
        html_1.close()
        strainer = SoupStrainer(name='div', attrs={'class': 'listing im-manufacturers-listing'})

        soup = BeautifulSoup(data, 'html.parser', parse_only=strainer)
        list_of_rest = soup.div.find_all('a')

        for a in list_of_rest:
            infos = a.find('div', attrs={'class': "manufacturer-info"}).stripped_strings
            identifier = os.path.basename(a['href'])
            existing_restaurant = session.query(Restaurant).filter(Restaurant.identifier_id==identifier).one_or_none()
            img = a.find('span', attrs={'class': "img-logo-media"}).img['src']
            if not existing_restaurant:
                restaurant = Restaurant(**{
                    'name': next(infos),
                    'open_hours': next(infos),
                    'image_url': img,
                    'identifier_id': identifier
                })
                session.add(restaurant)
                new_restaurants_ids.append(identifier)
            else:
                existing_restaurant.name = next(infos)
                existing_restaurant.open_hours = next(infos)
                existing_restaurant.image_url = img
                session.add(existing_restaurant)
            session.commit()

    send_email_for(new_restaurants_ids, session)
get_parsed_data(5)
print(session.query(Restaurant.image_url).all())
