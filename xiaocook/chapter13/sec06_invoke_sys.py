#!/usr/bin/env python
# encoding: utf-8

"""
@description: 调用执行系统命令

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_invoke_sys.py
@time: 2017/4/4 18:03
"""

import subprocess
import shlex


def run():
    s = 'ls -aclt'
    s = shlex.quote(s)
    try:
        out_bytes = subprocess.check_output(['echo', 'hello'], stderr=subprocess.STDOUT, timeout=5)
        out_bytes = subprocess.check_output(s, shell=True)
        # out_bytes = subprocess.check_output(['netstat', '-a'])
        # out_bytes = subprocess.check_output(['netstat', '-a'])
    except subprocess.CalledProcessError as e:
        out_bytes = e.output
        code = e.returncode
        print(code)
    except subprocess.TimeoutExpired as e:
        out_bytes = e

    print(out_bytes.decode())


def send_data():
    text = b'some data'
    p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)

    stdout, stderr = p.communicate(text)
    out = stdout.decode()
    err = stderr.decode()

    print(out, err)


def main():
    run()


if __name__ == '__main__':
    main()
