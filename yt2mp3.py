import requests
from bs4 import BeautifulSoup
import time
import urllib3
import os 

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = requests.Session() # Start Session

class Convert():

    def __init__(self, link):
        self.link = link

    def mp3(self):
        try:
            x = r.get('https://www.yt-download.org/api/widget/mp3/{}'.format(self.link))
            soup = BeautifulSoup(x.content, 'html.parser')
            url = r.get(soup.find_all('a')[0].get('href'))
            title = soup.find('h2').text
            with open(f'{title}.mp3', "wb+") as f:
                print('Downloading {}'.format(title))
                f.write(url.content)
            print('{} has been successfully downloaded.'.format(title))
            time.sleep(5)
        except:
            print('API might be broken or The link you input is wrong')
    
    def mp4(self):
        try:
            x = r.get('https://www.yt-download.org/api/widget/videos/{}'.format(self.link))
            soup = BeautifulSoup(x.content, 'html.parser')
            url = r.get(soup.find_all('a')[0].get('href'))
            title = soup.find('h2').text
            with open(f'{title}.mp4', "wb+") as f:
                print('Downloading {}'.format(title))
                f.write(url.content)
            print('{} has been successfully downloaded.'.format(title))
            time.sleep(5)
        except:
            print('API might be broken or The link you input is wrong')
if __name__ == '__main__':
    while True:
        f = input('Format: e.g. mp4, mp3 : ')
        link = input('Youtube Link : ')
        c = Convert(link[-11:])
        if 'mp4' in f:
            c.mp4()
        else:
            c.mp3()