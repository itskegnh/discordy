import requests

ENDPOINT = 'https://discord.com/api/'

#/channels/{channel.id}/messages/{message.id}/crosspost

class Embed:
    def __init__(self, title, description, color=0x000000):
        self.title, self.description = title, description
        self.color = color
    
    def payload(self):
        return {
            "title": "Title",
            "description": "Description",
            "color": 0x000000,
            "type": "rich"
        }


class Channel:
    def __init__(self, client, channel_id):
        self.id = channel_id
        self.client = client
    
    def send(self, content=None, embeds=None, sanitized=False):
        payload = {}
        if sanitized:
            payload['allowed_mentions'] = {"parse": []}
        if content is not None:
            payload['content'] = content
        if embeds is not None:
            payload['embeds'] = [embed.payload() for embed in embeds]
        return self.client.session.request('POST', f'{ENDPOINT}channels/{self.id}/messages', data=payload)

class Fetcher:
    def __init__(self, client):
        self.client = client
    
    def channel(self, channel_id):
        return Channel(self.client, channel_id)

class Client:
    def __init__(self, token=None, selfbot=False):
        self.fetch = Fetcher(self)
        self.session = requests.Session()
        self._token = token
        self.authlayout = 'Bot {}' if not selfbot else '{}'
        if self._token:
            self.session.headers.update({'Authorization': self.authlayout.format(self._token)})
    
    @property
    def token(self):
        return self._token

    @token.setter
    def token(self, token):
        self._token = token
        self.session.headers.update({'Authorization': self.authlayout.format(self._token)})

    @token.deleter
    def token(self):
        self._token = None
        self.session.headers.pop('Authorization')