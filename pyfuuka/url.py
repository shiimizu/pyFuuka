#!/usr/bin/env python
# -*- coding: utf-8 -*-

# FFuuka URL generator. Inherited from basc_py4chan
class Url(object):
    # default value for board in case user wants to query board list
    def __init__(self, board_name, domain_name, https=False):
        self._domain_name = domain_name
        self._board_name = board_name
        self._protocol = 'https://' if https else 'http://'

        # 4chan API URL Subdomains
        DOMAIN = {
            'api': self._protocol + domain_name + '/_/api/chan',   # API subdomain
            'boards': self._protocol + 'boards.4chan.org', # HTML subdomain
            'boards_4channel': self._protocol + 'boards.4channel.org', # HTML subdomain of 4channel worksafe, but 4chan.org still redirects
            'file': self._protocol + 'i.4cdn.org',  # file (image) host
            #'file': self._protocol + 'is.4chan.org', # new, slower image host
            'thumbs': self._protocol + 'i.4cdn.org',# thumbs host
            'static': self._protocol + 's.4cdn.org' # static host
        }

        # 4chan API URL Templates
        TEMPLATE = {
            'api': {  # URL structure templates
                'board': DOMAIN['api'] + '/index/?board={board}&page={page}&order=by_thread',
                'thread': DOMAIN['api'] + '/thread/?board={board}&num={thread_id}'
            },
            'http': { # Standard HTTP viewing URLs
                'board': DOMAIN['boards'] + '/{board}/{page}',
                'thread': DOMAIN['boards'] + '/{board}/thread/{thread_id}'
            },
            'data': {
                'file': DOMAIN['file'] + '/{board}/{tim}{ext}',
                'thumbs': DOMAIN['thumbs'] + '/{board}/{tim}s.jpg',
                'static': DOMAIN['static'] + '/image/{item}'
            }
        }

        # 4chan API Listings
        LISTING = {
            'board_list': DOMAIN['api'] + '/archives/', # all the list of boards
            'thread_list': DOMAIN['api'] + '/index/' + '?board={board}&page=1&order=by_thread', # all the list of threads
            #'archived_thread_list': DOMAIN['api'] + '/{board}/archive.json',
            #'catalog': DOMAIN['api'] + '/{board}/catalog.json'
        }

        # combine all dictionaries into self.URL dictionary
        self.URL = TEMPLATE
        self.URL.update({'domain': DOMAIN})
        self.URL.update({'listing': LISTING})

    # generate boards listing URL
    def board_list(self):
        return self.URL['listing']['board_list']

    # generate board page URL
    def page_url(self, page):
        return self.URL['api']['board'].format(
            board=self._board_name,
            page=page
            )

    # generate catalog URL
    def catalog(self):
        return self.URL['listing']['catalog'].format(
            board=self._board_name
            )

    # generate threads listing URL
    def thread_list(self):
        return self.URL['listing']['thread_list'].format(
            board=self._board_name
            )

#    # generate archived threads list URL (disabled for compatibility)
#    def archived_thread_list(self):
#        return self.URL['listing']['archived_thread_list'].format(
#            board=self._board_name
#            )

    # generate API thread URL
    def thread_api_url(self, thread_id):
        return self.URL['api']['thread'].format(
            board=self._board_name,
            thread_id=thread_id
            )

    # generate HTTP thread URL
    def thread_url(self, thread_id):
        return self.URL['http']['thread'].format(
            board=self._board_name,
            thread_id=thread_id
            )

    # generate file URL
    def file_url(self, tim, ext):
        return self.URL['data']['file'].format(
            board=self._board_name,
            tim=tim,
            ext=ext
            )

    # generate thumb URL
    def thumb_url(self, tim):
        return self.URL['data']['thumbs'].format(
            board=self._board_name,
            tim=tim
            )

    # return entire URL dictionary
    @property
    def site_urls(self):
        return self.URL

"""
# 4chan Static Data (Unique to 4chan, needs implementation)
STATIC = {
    'flags': DOMAIN['static'] + '/image/country/{country}.gif',
    'pol_flags': DOMAIN['static'] + '/image/country/troll/{country}.gif',
    'spoiler': { # all known custom spoiler images, just fyi
        'default': DOMAIN['static'] + '/image/spoiler.png',
        'a': DOMAIN['static'] + '/image/spoiler-a.png',
        'co': DOMAIN['static'] + '/image/spoiler-co.png',
        'mlp': DOMAIN['static'] + '/image/spoiler-mlp.png',
        'tg': DOMAIN['static'] + '/image/spoiler-tg.png',
        'tg-alt': DOMAIN['static'] + '/image/spoiler-tg2.png',
        'v': DOMAIN['static'] + '/image/spoiler-v.png',
        'vp': DOMAIN['static'] + '/image/spoiler-vp.png',
        'vr': DOMAIN['static'] + '/image/spoiler-vr.png'
    }
}
"""
