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

" youdao openapi key
if !exists('g:dict_key') || !exists('g:dict_keyfrom')
    let g:dict_keyfrom = 'aioiyuuko'
    let g:dict_key = '1932136763'
endif

function! s:DictGetSelctn() abort
    let regTmp = @a
    exec "normal gv\"ay"
    let vtext = @a
    let @a = regTmp
    return vtext
endfunction

function! Dict_Query(type, ...) abort
    if a:type == 'n'
        call __dict_query(g:dict_keyfrom, g:dict_key, expand("<cword>"))
    elseif a:type == 'v'
        let query = s:DictGetSelctn()
        call __dict_query(g:dict_keyfrom, g:dict_key, query)
    elseif a:type == 'c'
        call __dict_query(g:dict_keyfrom, g:dict_key, a:1)
    endif
endfunction

nmap <silent> <Plug>DictQuery   :call Dict_Query('n')<CR>
vmap <silent> <Plug>DictVQuery  :<C-U>call Dict_Query('v')<CR>

if !exists(':Dict')
    command! -nargs=1 Dict call Dict_Query('c', <q-args>)
endif

if !hasmapto('<Plug>DictQuery')
    nmap <silent> <Leader>d <Plug>DictQuery
endif

if !hasmapto('<Plug>DictVQuery')
    vmap <silent> <Leader>d <Plug>DictVQuery
endif

let &cpo = s:save_cpo
unlet s:save_cpo
