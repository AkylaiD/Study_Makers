import requests
from bs4 import BeautifulSoup as BS
import csv

def get_html(url):
    response = requests.get(url)
    return response.text

def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='search-results-table')
    cars = catalog.find_all('div', class_='list-item list-label')
    for car in cars:
        try:
            title = car.find('h2', class_='name').text.strip()
        except:
            title = ''
        try:
            price = car.find('p', class_='price').find('strong').text.strip()
        except:
            price = ''
        try:
            img = car.find('div', class_='thumb-item-carousel').find('img').get('data-src')
        except:
            img = ''
        try:
            descr1 = car.find('p', class_='year-miles').text.strip()
            descr2 = car.find('p', class_='body-type').text.strip()
            descr3 = car.find('p', class_='volume').text.strip()
        except:
            descr1 = ''
            descr2 = ''
            descr3 = ''

        data = {
            'title': title,
            'price': price,
            'img': img,
            'description1': descr1,
            'description2': descr2,
            'description3': descr3
        }

        write_csv(data)

def write_csv(data):
    with open('special_cars.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='\n')
        writer.writerow((data['title'],data['img'], data['price'], data['description1'], data['description2'], data['description3']))


def main():
    for page in range(1, 18):
        url = f'https://www.mashina.kg/specsearch/all/?page={page}'
        html = get_html(url)
        data = get_data(html)

main()
       