import requests
from bs4 import BeautifulSoup
import time
import urllib3
import os 
from clint.textui import puts, colored

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
            open(f'{title}.mp3', "wb+").write(url.content)
            print('Downloading..')
            puts(colored.green('{} has been successfully downloaded.'.format(title)))
            time.sleep(5)
        except:
            puts(colored.red('API might be broken or The link you input is wrong'))
            time.sleep(5)
    
    def mp4(self):
        try:
            x = r.get('https://www.yt-download.org/api/widget/videos/{}'.format(self.link))
            soup = BeautifulSoup(x.content, 'html.parser')
            url = r.get(soup.find_all('a')[0].get('href'))
            title = soup.find('h2').text
            open(f'{title}.mp4', "wb+").write(url.content)
            puts(colored.green('{} has been successfully downloaded.'.format(title)))
            time.sleep(5)
        except:
            puts(colored.red('API might be broken or The link you input is wrong'))
            time.sleep(5)

if __name__ == '__main__':
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print('1. MP4')
        print('2. MP3')
        f = input('> ')
        clear()
        print('Input the Youtube link e.g https://www.youtube.com/watch?v=i_kSqfHRXEo or i_kSqfHRXEo')
        link = input('> ')
        c = Convert(link[-11:])
        if '1' in f:
            c.mp4()
        else:
            c.mp3()
# Made better.
