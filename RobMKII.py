from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import requests
import pathlib

webhook = 'https://discord.com/api/webhooks/835798483083984917/R9hJGHM37nvaaAf4zepz2pDLe5T9dgaXxZOlz0nwKLlB-fMNJtrzIqupmKNpMc15jvuq'
path = pathlib.Path(__file__).parent.absolute()



while 1:
    userinput = input('> ').lower()
    command = userinput.split(' ')[0]

    if userinput == 'show mod':
        modsearch = input('Mod name :').capitalize()
        modurl  = 'https://warframe.fandom.com/wiki/{}'.format(modsearch)

        uClient = uReq(modurl)
        page_html = uClient.read()
        pagesoup = soup(page_html, 'html.parser')

        ModImage = pagesoup.find('a', {'class': 'image image-thumbnail'})['href']
        ModName = pagesoup.find('title').text[:pagesoup.find('title').text.index('|')]
        Content = '{}: {}'.format(ModName, ModImage)

        print(ModName)
        print(ModImage)

        sendpermission = input('Send on Discord? (Y/N) ')
        print(sendpermission)
        if sendpermission == 'y':
            requests.post(webhook, data={'content': ModImage})
    elif userinput == 'send message':
        msg = input('message: ')
        requests.post(webhook, data={'content': msg})
    elif userinput == 'save page':
        filename = input('File: ')
        if filename == 'quit':
            pass
        else:
            print()
            with open('{}/Data/{}.html'.format(path, filename), 'w+', encoding='utf-8') as f:
                url = input('URL: ')
                uClient = uReq(url)
                page_html = uClient.read()
                page_soup = soup(page_html, 'html.parser')
                f.write(str(page_soup))
                uClient.close()
    elif command == 'quit':
        break