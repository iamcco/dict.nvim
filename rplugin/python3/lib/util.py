# Last Change: 2016-03-19
# Maintainer: iamcco <ooiss@qq.com>
# Github: http://github.com/iamcco <年糕小豆汤>
# Version: 0.0.1

import json
from urllib import request

errorCode = {
    '0':       'success',
    '20':      '要求翻译的文本过长',
    '30':      '无法进行有效的翻译',
    '40':      '不支持的语言类型',
    '50':      '无效的key',
    '60':      '无词典结果，仅在获取词典结果生效',
    'other':   '查询失败，出现未知错误',
    'noQuery': "查询失败，有道openapi返回异常"
}

key     = 'aioiyuuko'
keyfrom = '1932136763'
url     = 'http://fanyi.youdao.com/openapi.do?keyfrom=%s&key=%s&type=data&\
                                                doctype=json&version=1.1&q=%s'

def query(q = '', type = 'base'):
    queryUrl = url % (keyfrom, key, q)
    data = request.urlopen(queryUrl).read().decode('utf-8')
    try:
        data   = json.loads(data)
        data = {
            'status': True,
            'data': data
        }
    except ValueError:
        data = {
            'status': False,
            'message': errorCode['noQuery'],
        }
    return data

def dealSimple(searchResult):
    qw = searchResult['query']
    translation = searchResult['translation']
    translation = qw + ' ==> ' + '\n'.join(translation)
    try:
        explains = searchResult['basic']['explains']
        explains = ' @ ' + ' '.join(explains)
    except KeyError:
        explains = ''
    print(translation + explains)

def dealComplex(searchResult):
    cwinnr = int(vim.eval('s:OpenWindow()'))    #获取__dictSearch__窗口编号
    vim.command(str(cwinnr) + ' wincmd w')      #跳到__dictSearch__窗口
    cbuf = vim.current.buffer                   #获取当前__dictSearch__的buffer
    vim.command('setl modifiable')
    vim.command('%d _')
    queryStr = searchResult['query'].split('\n')
    queryStr = ( (item[0], item[1].strip()) for item in enumerate(queryStr) if item[1].strip() != '' )
    for eachline in queryStr:
        if eachline[0] == 0:
            cbuf.append(u'查找：_*_DictSearchStart_*_%s_*_DictSearchEnd_*_' % eachline[1])
        else:
            cbuf.append(u'      _*_DictSearchStart_*_%s_*_DictSearchEnd_*_' % eachline[1])
    cbuf.append('')
    tranlas = ( item for item in enumerate(searchResult['translation']) )
    for eachline in tranlas:
        if eachline[0] == 0:
            cbuf.append(u'翻译：_*_DictResultStart_*_%s_*_DictResultEnd_*_' % eachline[1])
        else:
            cbuf.append(u'      _*_DictResultStart_*_%s_*_DictResultEnd_*_' % eachline[1])
    if 'basic' in searchResult and 'explains' in searchResult['basic']:
        cbuf.append('')
        explains = ( item for item in enumerate(searchResult['basic']['explains']) )
        for eachline in explains:
            if eachline[0] == 0:
                cbuf.append(u'解释：_*_DictNounStart_*_%s_*_DictNounEnd_*_' % eachline[1])
            else:
                cbuf.append(u'      _*_DictNounStart_*_%s_*_DictNounEnd_*_' % eachline[1])
    if 'web' in searchResult:
        cbuf.append('')
        webs = ( item for item in enumerate(searchResult['web']) )
        for eachline in webs:
            if eachline[0] == 0:
                cbuf.append(u'网络：_*_DictWebStart_*_%s：%s_*_DictWebEnd_*_' % (eachline[1]['key'], ','.join(eachline[1]['value'])))
            else:
                cbuf.append(u'      _*_DictWebStart_*_%s：%s_*_DictWebEnd_*_' % (eachline[1]['key'], ','.join(eachline[1]['value'])))
    vim.command('0d _')
    vim.command('setl nomodifiable')

def strReplace(searchResult):
    tranlas = '\n'.join(searchResult['translation'])
    tranlas = tranlas.replace('"','\\"').replace("'","\\'")
    vim.command('let regTmp = @a')
    vim.command('let @a = "' + tranlas + '"')
    vim.command('normal gv"ap')
    vim.command("let @a = regTmp")
    vim.command("unlet regTmp")

def dictShow(searchResult, searchType):
    error_code = searchResult['errorCode']
    if error_code == 0:
        if searchType == 'simple':
            dealSimple(searchResult)
        elif searchType == 'replace':
            strReplace(searchResult)
        else:
            dealComplex(searchResult)
    elif error_code == 20:
        print(cData['errorCode']['20'])
    elif error_code == 30:
        print(cData['errorCode']['30'])
    elif error_code == 40:
        print(cData['errorCode']['40'])
    elif error_code == 50:
        print(cData['errorCode']['50'])
    elif error_code == 60:
        print(cData['errorCode']['60'])
    else:
        print(cData['errorCode']['other'])

__all__ = ['cData', 'dictShow']
