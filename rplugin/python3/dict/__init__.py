# ===============================================================================
# File: rplugin/python3/dict/__init__.py
# Description: simple translation plugin for neovim
# Last Change: 2016-03-20
# Maintainer: iamcco <ooiss@qq.com>
# Github: http://github.com/iamcco <年糕小豆汤>
# Licence: Vim Licence
# Version: 0.0.1
# ===============================================================================

import neovim
from dict.util import Util

@neovim.plugin
class Dict(object):
    def __init__(self, vim):
        self.vim = vim
        self.util = ''

    @neovim.function('__dict_query')
    def dict_query(self, args):
        if self.util == '':
            self.util = Util(args[0], args[1])

        data = self.util.query(' '.join(args[2:]))
        if data['status']:
            message = data['message']
        else:
            message = 'Search failed：%s' % data['message']
        self.vim.command('echo "%s"' % message)
