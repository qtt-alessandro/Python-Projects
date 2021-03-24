import os
from bs4 import BeautifulSoup
import re
import datetime
import csv
from langdetect import detect
import io

month_to_number = {'January': 1,
                   'February': 2,
                   'March': 3,
                   'April': 4,
                   'May': 5,
                   'June': 6,
                   'July': 7,
                   'August': 8,
                   'September': 9,
                   'October': 10,
                   'November': 11,
                   'December': 12}

def write_tsv_file(filename, content):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "wt", newline='', encoding='utf-8' ) as out_file:
        tsv_writer = csv.writer(out_file, delimiter='\t')
        tsv_writer.writerow(content)

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def parse_html_in_folder(path, destiny='final_tsv_files'):
    for html_file in os.listdir(path):
        with open(path + '/' + html_file, encoding='utf8') as infile:
            soup = BeautifulSoup(infile, features="lxml")
            # Plot can be hidden (if it is hidden we have to take the complete plot)
            try:
                Plot = ' '.join(
                    [remove_html_tags(str(c)) for c in soup.find_all('div', id="description")[0].contents[3].contents])
            except Exception:
                if not soup.find_all('div', id="description"):
                    Plot = ''
                else:
                    Plot = ' '.join([remove_html_tags(str(c)) for c in
                                     soup.find_all('div', id="description")[0].contents[1].contents])
            if Plot:
                if detect(Plot) != 'en':
                    print('Article removed:', html_file)
                    continue
            bookTitle = soup.find_all('h1')[0].contents[0].replace('\n', '').strip()
            bookSeries = soup.find_all('h2', id='bookSeries')[0].text.replace('\n', '').strip()
            bookAuthors = ', '.join([soup.find_all('span', itemprop='name')[i].contents[0] for i in range(
                len(soup.find_all('span', itemprop='name')))])
            ratingValue = soup.find_all('span', itemprop='ratingValue')[0].contents[0].replace('\n', '').strip()
            ratingCount = soup.find_all('meta', itemprop="ratingCount")[0]['content']
            reviewCount = soup.find_all('meta', itemprop="reviewCount")[0]['content']
            try:
                NumberofPages = re.findall(r'\d+', soup.find_all('span', itemprop="numberOfPages")[0].contents[0])[0]
            except:
                if not soup.find_all('span', itemprop="bookFormat"):
                    NumberofPages = ''
                else:
                    NumberofPages = soup.find_all('span', itemprop="bookFormat")[0].contents[0]
            try:
                temp_date = soup.find_all('div', id='details')[0].find_all('div', {"class": "row"})[1].text.split('\n')[
                    2].split()
            except:
                try:
                    temp_date = \
                    soup.find_all('div', id='details')[0].find_all('div', {"class": "row"})[0].contents[0].split('\n')[
                        2].split()
                except:
                    try:
                        temp_date = \
                        soup.find_all('div', id='details')[0].find_all('nobr', {"class": "greyText"})[0].contents[
                            0].split('\n')[1].split()[-3:]
                    except:
                        temp_date = ''
            PublishingDate = ' '.join(temp_date)
            characters = []
            settings = []
            for i in range(1, len(soup.find_all('div', id="bookDataBox")[0].find_all('a'))):
                if re.match(r'/characters/', soup.find_all('div', id="bookDataBox")[0].find_all('a')[i].attrs['href']):
                    characters.append(soup.find_all('div', id="bookDataBox")[0].find_all('a')[i].text)
                elif re.match(r'/places/', soup.find_all('div', id="bookDataBox")[0].find_all('a')[i].attrs['href']):
                    settings.append(soup.find_all('div', id="bookDataBox")[0].find_all('a')[i].text)
            characters = ', '.join(characters)
            settings = ', '.join(settings)
            url = soup.find_all('link', rel='canonical')[0].attrs['href']

            final_list = [bookTitle, bookSeries, bookAuthors, ratingValue, ratingCount, reviewCount,
                          Plot, NumberofPages, PublishingDate, characters, settings, url]

            filename = 'data/' + destiny + '/' + re.findall(r'\d+', html_file)[0] + '.tsv'

            write_tsv_file(filename, final_list)


def remove_stop_words(plot):
    # This allow us to identify stop word in english
    stopwords = nltk.corpus.stopwords.words('english')
    # stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(plot)
    filtered_sentence = [w.lower() for w in word_tokens if w.lower() not in stopwords and len(w) > 1]

    text = ' '.join(filtered_sentence)
    return text


