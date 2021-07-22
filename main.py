import requests
import json

webhook = 'https://discord.com/api/webhooks/835798483083984917/R9hJGHM37nvaaAf4zepz2pDLe5T9dgaXxZOlz0nwKLlB-fMNJtrzIqupmKNpMc15jvuq'

w2 = 'https://api.warframestat.us/items/search/{}'.format('stradavar prime')
req = requests.get(w2).text

msg= 'teste'
requests.post(webhook, data={'content': req})

print (requests.post(webhook, data={'content': req}))