#!/usr/bin/env python
# encoding: utf-8

"""
@description:http requests

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_http_requets.py
@time: 2017/3/15 20:28
"""

from urllib import request, parse
import requests


def demo1():
    url = 'http://httpbin.org/get'
    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    querystring = parse.urlencode(params)
    u = request.urlopen(url + '?' + querystring)
    resp = u.read()
    print(resp)


def demo2():
    url = 'http://httpbin.org/post'
    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    querystring = parse.urlencode(params)

    u = request.urlopen(url, querystring.encode('ascii'))
    resp = u.read()
    print(resp)


def demo3():
    url = 'http://httpbin.org/post'
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }
    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    querystring = parse.urlencode(params)

    req = request.Request(url, querystring.encode('ascii'), headers=headers)

    u = request.urlopen(req)
    resp = u.read()

    print(resp)


def using_requests():
    url = 'http://httpbin.org/post'
    headers = {
        'User-agent': 'none/ofyourbusiness',
        'Spam': 'Eggs'
    }
    params = {
        'name1': 'value1',
        'name2': 'value2',
    }

    resp = requests.post(url, params, headers=headers)
    print(resp.text)
    print(resp.json())


def head_info():
    # resp = requests.head('https://www.python.org/index.html')
    resp = requests.head('https://www.baidu.com')
    print(resp.status_code)
    # print(resp.headers['last-modified'])
    print(resp.headers['Last-Modified'])
    print(resp.headers['content-type'])
    # print(resp.headers['content-length'])

    print(resp.headers)


def complex_http():
    # resp = requests.get('http://pypi.python.org/pypi?:action=login',
    #                     auth=('user', 'password'))
    # print(resp.text)

    url = 'https://www.baidu.com'
    # resp1 = requests.get(url)
    # resp2 = requests.get(url, cookies=resp1.cookies)
    # print(resp2.cookies)

    files = {'file': ('data.csv', open(__file__, 'rb'))}
    resp3 = requests.post(url, files=files)

    print(resp3.text)


def main():
    # demo1()
    # demo2()
    # demo3()
    # using_requests()
    # head_info()

    complex_http()


if __name__ == '__main__':
    main()
