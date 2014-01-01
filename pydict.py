#!/usr/bin/env python
#*_*coding=utf8*_*
__author__ = 'dengmin'

import urllib2
import json
import sys

q = 'translation'
query_url = 'http://fanyi.youdao.com/openapi.do?keyfrom=hello-world&key=2128682281&type=data&doctype=json&version=1.1&q=%s'

def fetch_data(q):
    req = urllib2.urlopen(query_url %(q))
    data = json.loads(req.read())
    output(data)

def output(data):
    query = data['query']
    translation = data['translation']

    print u'有道翻译: ',
    for d in translation:
        print d

    if data.get('basic'):
        #print data['basic']['phonetic']
        for c in data['basic']['explains']:
            print c


    if data.get('web'):
        print u'网络释义'
        print '*'* 10
        for item in data['web']:
            print item['key']
            for i in item['value']:
                print i
            print '*'* 10

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) > 0:
        fetch_data(' '.join(args))