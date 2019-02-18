"===============================================================================
"File: plugin/dict.nvim
"Description: simple translation plugin for neovim
"Maintainer: iamcco <ooiss@qq.com>
"Github: http://github.com/iamcco <年糕小豆汤>
"Licence: Vim Licence
"===============================================================================

if exists('g:loaded_dict')
    finish
endif

let g:loaded_dict= 1

let s:save_cpo = &cpo
set cpo&vim

if !exists(':Dict')
    command! -nargs=1 Dict call sran#rpc#notify('dict_translate', <q-args>)
endif

let &cpo = s:save_cpo
unlet s:save_cpo
