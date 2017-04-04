#!/usr/bin/env python
# encoding: utf-8

"""
@description:unix 自己实现守护进程

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_daemon.py
@time: 2017/4/4 16:56
"""

import os
import sys
import atexit
import signal
import time


def daemonize(pidfile, *, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    if os.path.exists(pidfile):
        raise RuntimeError('Already running')

    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #1 failed!')

    os.chdir('/')
    os.umask(0)
    os.setsid()

    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed!')

    sys.stdout.flush()
    sys.stderr.flush()

    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())
    with open(stdout, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdout.fileno())
    with open(stderr, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stderr.fileno())

    with open(pidfile, 'w') as f:
        print(os.getpid(), file=f)

    atexit.register(lambda: os.remove(pidfile))

    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)


def run():
    sys.stdout.write('Daemon started with pid{}\n'.format(os.getpid()))
    while True:
        sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(10)


def main():
    PID_FILE = '/tmp/daemon.pid'
    LOG_FILE = '/tmp/daemon.log'

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0]), file=sys.stderr)
        raise SystemExit(1)

    if sys.argv[1] == 'start':
        try:
            daemonize(PID_FILE, stdout=LOG_FILE, stderr=LOG_FILE)
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)

        run()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PID_FILE):
            with open(PID_FILE) as f:
                os.kill(int(f.read()), signal.SIGTERM)
        else:
            print('Not running', file=sys.stderr)
            raise SystemExit(1)

    else:
        print('Unknown command {!r}'.format(sys.argv[1]), file=sys.stderr)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
