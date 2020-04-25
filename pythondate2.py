from bs4 import BeautifulSoup
import requests
import argparse
import urllib.request


domain = 'https://www.python.org'
url = 'https://www.python.org/downloads'

parser = argparse.ArgumentParser(description = "this program is for finding versions of python based on there release dates")

parser.add_argument('-r', required=False, metavar= "date", type=str, help="release date, in quotations capatilize first letter of each month, day, then year. example: April 6, 2013")
args = parser.parse_args()
print (args.r)


versions = []

def get_soup(url):
    request = requests.get(url)
    return BeautifulSoup(requests.get(url).text, 'html.parser')
soup = get_soup(url)

for link in soup.select('.list-row-container li'):
    string = str(link.prettify())
    if (args.r) in string:

        splitstring = string.split()
        versions.append(splitstring[6])
        #print (splitstring[6])
print (versions[0])
download = "https://www.python.org/ftp/python/"+versions[0]+"/Python-"+versions[0]+".tgz"


urllib.request.urlretrieve(download, 'abennettpython'+versions[0]+".tgz")

