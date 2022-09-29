from bs4 import BeautifulSoup as bs
import requests
import csv


def get_html(url):
    headers = {"User-Agent": "Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11"}
    request = requests.get(url, headers=headers)
    return request.text


def get_total_pages(html):
    soup = bs(html, 'lxml')
    pages_a = soup.find('div', class_='b-navigation').find_all('a')
    total_page = pages_a[-2].get('href').split('/')[-2]
    return int(total_page)


def write_to_csv(data):
    with open('anime_list.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow((data['cover'],
                         data['title'],
                         data['description'],
                         data['link']))


def get_page_data(html):
    # cover, title, description(genre, country, year), link
    soup = bs(html, 'lxml')
    anime_list = soup.find_all('div', class_='b-content__inline_item')

    for anime in anime_list:
        cover = anime.find('div', class_='b-content__inline_item-cover').find('img').get('src')
        # print(cover)
        title = anime.find('div', class_='b-content__inline_item-link').find('a').text
        # print(title)
        description = anime.find('div', class_='b-content__inline_item-link').find('div').text
        # print(description)
        link = anime.find('div', class_='b-content__inline_item-cover').find('a').get('href')
        data = {'cover': cover, 'title': title, 'description': description, 'link': link}
        write_to_csv(data)


def main():
    anime_url = "https://hdrezka.co/animation/"
    pages = 'page/'

    total_pages = get_total_pages(get_html(anime_url))

    for page in range(1, total_pages+1): #67
        url_with_page = anime_url + pages + str(page) + '/'
        html = get_html(url_with_page)
        response = get_page_data(html)
        return response


main()