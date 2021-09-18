import os
import requests
from bs4 import BeautifulSoup

ROOT_URL = 'https://archive.ics.uci.edu/ml/'

def fix_url(url):
  return url if ROOT_URL in url else ROOT_URL + url


def get_dataset_list():
  # fetch html file
  response = requests.get(ROOT_URL + 'datasets.html')

  # initialize our parser
  html_doc = response.text
  soup = BeautifulSoup(html_doc, 'html.parser')

  # uncomment to print prettified html
  # comment befores submitting
  # print(soup.prettify())

  rows = soup.findAll('table')[5].findAll('tr')

  datasets = []

  for row in rows[1::2]:
    title_elem = row.findAll('a', href=True)[1]
    title = title_elem.get_text()
    url = fix_url(title_elem['href'])
    datasets.append({'title': title, 'url': url})

  return datasets

def get_dataset(url):
  # set destination URL where files are stored
  prefix = 'https://archive.ics.uci.edu/ml/machine-learning-databases/'
  response = requests.get(url)
  html_doc = response.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  anchors = soup.findAll('a', href=True)
  for a in anchors:
    txt = a.get_text()
    if txt == 'Data Folder':
      url = a.get('href')
      break
  title = url.split('/')[-2]
  url = prefix + title + '/'
  
  # hit destination URL
  response = requests.get(url)
  html_doc = response.text
  soup = BeautifulSoup(html_doc, 'html.parser')
  # this contains only name and links
  links = []
  # this contains descriptive info also
  description = []
  # read all the needed info and store in a list of dictionaries
  rows = soup.findAll('tr')
  for row in rows[3:-1]:
    title_url = url + row.findAll('a', href=True)[0].get('href')
    title_data = row.findAll('td')
    title_name = title_data[1].get_text()
    last_modified = title_data[2].get_text()
    size_description = title_data[3].get_text()
    description.append({'title': title_name, 'url': title_url, 'last modified': last_modified, 'size description': size_description})
    links.append({'title': title_name, 'url': title_url})
    
  return links

def download_dataset(dataset):
  # dataset name
  title = dataset['title']
  # URLs of all the files to be downloaded
  url = get_dataset(dataset['url'])
  # path to store dataset
  path = os.path.join(os.path.expanduser('~'), 'datasets', title)
  # create directory if it does not pre-exists
  if not os.path.exists(path):
    os.makedirs(path)
    # download files
    print('-------Downloading dataset-------')
    for d in url:
      name = os.path.join(path, d['title'] + '.txt')
      f = open(name, 'w')
      print('Downloading ' + d['title'] + '.txt')
      response = requests.get(d['url'])
      data = response.text
      f.write(data)
      f.close()
  else:
    print('Dataset already exists offline.')

  pass
