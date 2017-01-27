import base64
import json
import os
import re
import zlib
from retrying import retry
from xmlrpc.client import ServerProxy

from api.fixture import load_fixture
from api.subtitle.model import to_model


LANGUAGE = 'en'
NEWLINE_PATTERN = re.compile(r'(\r\n|\r|\n)')
OPENSUBTITLES_URL = 'http://api.opensubtitles.org/xml-rpc'
OPENSUBTITLES_UA = 'subvoc v1.0'
UNICODE_BOM = u'\N{ZERO WIDTH NO-BREAK SPACE}'


def ensure_success(resp):
    if resp.get('status').split()[0] != '200':
        raise RuntimeError("received status {}".format(resp.get('status')))


def create_client():
    return ServerProxy(OPENSUBTITLES_URL, allow_none=True)


def json_fixture(directory, arg):
    return load_fixture(os.path.join('opensubtitles', directory, '{}.json'), arg, json.loads)


def resp_to_model(resp):
    return [to_model(item) for item in resp.get('data')]


class OpenSubtitles:

    def __init__(self, credentials, create_client=create_client):
        self.token = None
        self.credentials = credentials
        self.xmlrpc = create_client()

    def login(self):
        username = self.credentials[0]
        password = self.credentials[1]
        resp = self.xmlrpc.LogIn(username, password, LANGUAGE, OPENSUBTITLES_UA)
        ensure_success(resp)
        self.token = resp.get('token')

    @retry(stop_max_delay=5000, stop_max_attempt_number=3)
    def find(self, query):
        if not self.token:
            self.login()

        resp = self.xmlrpc.SearchSubtitles(self.token, [query], [{'limit': 500}])
        ensure_success(resp)
        return resp

    def find_by_query(self, query):
        qry = query.lower().strip()
        resp = json_fixture('query', qry) \
            or self.find({'query': qry, 'sublanguageid': 'eng'})
        return resp_to_model(resp)

    def find_subtitles_for_movie(self, imdb_id, lang):
        search_id = imdb_id.replace('tt', '').lstrip('0')
        resp = json_fixture('id', imdb_id) \
            or self.find({'imdbid': search_id, 'sublanguageid': lang})
        return resp_to_model(resp)

    @retry(stop_max_delay=5000, stop_max_attempt_number=3)
    def load_text(self, subtitle):
        if not self.token:
            self.login()

        resp = json_fixture('subtitle', subtitle.id) \
            or self.xmlrpc.DownloadSubtitles(self.token, [subtitle.id])
        ensure_success(resp)

        text = resp.get('data')[0].get('data')
        text = base64.standard_b64decode(text)
        text = zlib.decompress(text, 47)
        text = str(text, subtitle.encoding)
        text = text.lstrip(UNICODE_BOM)
        text = re.sub(NEWLINE_PATTERN, '\n', text)

        return text
