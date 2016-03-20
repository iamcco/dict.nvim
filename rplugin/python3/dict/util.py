# ===============================================================================
# File: rplugin/python3/dict/util.py
# Description: simple translation plugin for neovim
# Last Change: 2016-03-20
# Maintainer: iamcco <ooiss@qq.com>
# Github: http://github.com/iamcco <年糕小豆汤>
# Licence: Vim Licence
# Version: 0.0.1
# ===============================================================================

import json
from urllib import request

URL     = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&\
                                                doctype=json&version=1.1&q=%s'
errorCode = {
    '0':       'success',
    '20':      'Text is too loog',
    '30':      'Cannot not be translated effectively',
    '40':      'Language type is not suppport',
    '50':      'Invalid key',
    '60':      'No result',
    'other':   'Query failed',
    'noQuery': 'Result type is not json'
}

class Util(object):
    def __init__(self, keyfrom, key):
        self.keyfrom = keyfrom
        self.key = key

    def filter(self, data):
        result = {}
        if data['errorCode'] == 0:
            result['status'] = True
            result['message'] = ' '.join(data['translation'])
        else:
            result['status'] = False
            result['message'] = errorCode[str(data['errorCode'])]
        return result

    def query(self, q = '', type = 'base'):
        queryUrl = URL % (self.keyfrom, self.key, request.quote(q))
        try:
            data = request.urlopen(queryUrl).read().decode('utf-8')
            data   = json.loads(data)
            data = self.filter(data)
        except ValueError:
            data = {
                'status': False,
                'message': errorCode['noQuery'],
            }
        except request.URLError as message:
            data = {
                'status': False,
                'message': 'No network'
            }
        except Exception as message:
            data = {
                'status': False,
                'message': message
            }
        return data
