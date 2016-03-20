"===============================================================================
"File: plugin/dict.vim
"Description: simple translation plugin for neovim
"Last Change: 2016-03-20
"Maintainer: iamcco <ooiss@qq.com>
"Github: http://github.com/iamcco <年糕小豆汤>
"Licence: Vim Licence
"Version: 0.0.1
"===============================================================================

if !has('nvim')
    echoerr('Plugin dict.nvim just support neovim')
    finish
endif

if exists('g:loaded_dict')
    finish
endif

let g:loaded_dict= 1

let s:save_cpo = &cpo
set cpo&vim

"有道openapi key
if !exists('g:api_key') || !exists('g:keyfrom')
    let g:dict_keyfrom = 'aioiyuuko'
    let g:dict_key = '1932136763'
endif

if !hasmapto('<Plug>DictSearch')
    nmap <silent> <Leader>d <Plug>DictSearch
endif

if !hasmapto('<Plug>DictVSearch')
    vmap <silent> <Leader>d <Plug>DictVSearch
endif

nmap <silent> <Plug>DictSearch   :call __dict_query(g:dict_keyfrom, g:dict_key, expand("<cword>"))<CR>
vmap <silent> <Plug>DictVSearch  :<C-U>call __dict_query()<CR>

if !exists(':Dict')
    command! -nargs=1 Dict call __dict_query(g:dict_keyfrom, g:dict_key, <q-args>)
endif

let &cpo = s:save_cpo
unlet s:save_cpo
