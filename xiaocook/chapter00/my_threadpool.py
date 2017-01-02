#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自己实现线程池的程序

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: my_threadpool.py
@time: 2016/12/20 11:26
"""

import os
import queue
import threading

import requests

from xiaocook.settings import FILE_PATH

root_path = FILE_PATH


class Worker(threading.Thread):
    def __init__(self, workQueue, resultQueue, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.setDaemon(True)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while True:
            try:
                callable, args, kwargs = self.workQueue.get(False)
                res = callable(*args, **kwargs)
                self.resultQueue.put(res)
            except queue.Empty:
                break


class WorkerManager:
    def __init__(self, num_of_workers=10):
        self.workQueue = queue.Queue()
        self.resultQueue = queue.Queue()
        self.workers = []
        self._recruitThreads(num_of_workers)

    def _recruitThreads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = Worker(self.workQueue, self.resultQueue)
            self.workers.append(worker)

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()

            if worker.isAlive() and not self.workQueue.empty():
                self.workers.append(worker)

            print("All jobs were completed.")

    def add_job(self, callable, *args, **kwargs):
        self.workQueue.put((callable, args, kwargs))

    def get_result(self, *args, **kwargs):
        self.resultQueue.get(args, kwargs)


urls = [
    "http://wiki.python.org/moin/WebProgramming",
    "http://www.baidu.com",
    "http://wiki.python.org/moin/Documentation"
]


def download_file(url):
    print("begin download: " + url)
    response = requests.get(url)
    fname = os.path.basename(url) + ".html"
    with open(root_path + fname, 'w', encoding='utf-8') as f:
        chunk = response.content
        if chunk:
            f.write(chunk.decode())


def multi_download():
    wm = WorkerManager(2)
    for i in urls:
        wm.add_job(download_file, i)

    wm.start()
    wm.wait_for_complete()


def test():
    param = (download_file, "1", {'key': 2})


def main():
    multi_download()


if __name__ == '__main__':
    main()
