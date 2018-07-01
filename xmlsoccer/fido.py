import certifi
import urllib3
from urllib.parse import urlencode
import json

class Fetch():
    status = None
    text = None
    json_data = None
    user_agent = "python fetch utility"

    http = urllib3.PoolManager(
        cert_reqs='CERT_REQUIRED',
        ca_certs=certifi.where())


    def json(self):
        return json.loads(self.text)


    def get(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = {
                'User-Agent': self.user_agent
            }
        if "params" in kwargs:
            url = url + "?" + urlencode(kwargs["params"])
            kwargs.pop("params", None)
        r = self.http.request("GET", url, **kwargs)
        self.status = r.status
        self.text = r.data.decode('utf-8')


    def post(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = {
                'User-Agent': self.user_agent
            }
        # json encode the body data
        if "body" in kwargs:
            kwargs["body"] = json.dumps(kwargs["body"])
        # convert form to fields for urllib3 use
        if "form" in kwargs:
            kwargs["fields"] = kwargs["form"]
            kwargs.pop("form", None)
        r = self.http.request("POST", url, **kwargs)
        self.status = r.status
        self.text = r.data.decode('utf-8')

    ''' These need to be finished
    def head(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = {
                'User-Agent': self.user_agent
            }
        r = self.http.request("HEAD", url, **kwargs)
        self.status = r.status
        self.text = r.data.decode('utf-8')
        self.json_data = json.loads(r.data.decode('utf-8'))


    def put(self, url, **kwargs):
        if "headers" not in kwargs:
            kwargs["headers"] = {
                'User-Agent': self.user_agent
            }
        r = self.http.request("PUT", url, **kwargs)
        self.status = r.status
        self.text = r.data.decode('utf-8')
        self.json_data = json.loads(r.data.decode('utf-8'))
    '''
