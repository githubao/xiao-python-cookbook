#!/usr/bin/env python
# encoding: utf-8

"""
@description: 网络中加入ssl认证

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_ssl_network.py
@time: 2017/3/22 20:58
"""

from socket import socket, AF_INET, SOCK_STREAM
import ssl
from xiaocook.settings import FILE_PATH
from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy, SafeTransport

KEY_FILE = '{}/server_key.pem'.format(FILE_PATH)
CERT_FILE = '{}/server_cert.pem'.format(FILE_PATH)

CA_KEY = '{}/client_key.pem'.format(FILE_PATH)
CA_CERTS = '{}/client_cert.pem'.format(FILE_PATH)


def echo_client(s):
    while True:
        data = s.recv(8192)
        if data == b'':
            break
        s.send(data)
    s.close()
    print('Connection closed')


def echo_server(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(addr)
    s.listen(1)

    s_ssl = ssl.wrap_socket(s,
                            keyfile=KEY_FILE,
                            certfile=CERT_FILE,
                            server_side=True
                            )

    while True:
        try:
            c, a = s_ssl.accept()
            print('Got Connetction: ', c, a)
            echo_client(c)
        except Exception as e:
            print('{}: {}'.format(e.__class__.__name__, e))


def server_run():
    echo_server(('', 20000))


def client_demo():
    s = socket(AF_INET, SOCK_STREAM)
    s_ssl = ssl.wrap_socket(s,
                            cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs=CA_CERTS)
    s_ssl.connect(('localhost', 20000))
    s_ssl.send(b'Heel')

    print(s_ssl.recv(8192))


class SSLMixin():
    def __init__(self, *args, keyfile=None, certfile=None, ca_certs=None, cert_reqs=ssl.CERT_NONE, **kwargs):
        self._keyfile = keyfile
        self._certfile = certfile
        self._ca_certs = ca_certs
        self._cert_reqs = cert_reqs
        super().__init__(*args, **kwargs)

    def get_request(self):
        client, addr = super().get_request()
        client_ssl = ssl.wrap_socket(client,
                                     keyfile=self._keyfile,
                                     certfile=self._certfile,
                                     ca_certs=self._ca_certs,
                                     cert_reqs=self._cert_reqs,
                                     server_side=True
                                     )
        return client_ssl, addr


class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer):
    pass


class KeyValueServer():
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, *args, **kwargs):
        self._data = {}
        self._serv = SSLSimpleXMLRPCServer(*args, allow_none=True, **kwargs)
        for name in self._rpc_methods:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


def server_run2():
    kvserv = KeyValueServer(('', 15000), keyfile=KEY_FILE, certfile=CERT_FILE)
    kvserv.serve_forever()


def client_demo2():
    s = ServerProxy('https://localhost:15000', allow_none=True)
    s.set('foo', 'bar')
    print(s.get('foo'))


class VerifyCertSafeTransport(SafeTransport):
    def __init__(self, cafile, certfile=None, keyfile=None):
        SafeTransport.__init__(self)
        self._ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        self._ssl_context.load_verify_locations(cafile)
        if certfile:
            self._ssl_context.load_cert_chain(certfile, keyfile)
        self._ssl_context.verify_mode = ssl.CERT_REQUIRED

    def make_connection(self, host):
        s = super().make_connection((host, {'context': self._ssl_context}))

        return s


def server_run3():
    kvserv = KeyValueServer(('',15000), keyfile=KEY_FILE, certfile=CERT_FILE, ca_certs=CA_CERTS,
                            cert_reqs=ssl.CERT_REQUIRED)
    kvserv.serve_forever()


def client_demo3():
    s = ServerProxy('https://localhost:15000',
                    transport=VerifyCertSafeTransport(CERT_FILE, CA_CERTS, CA_KEY),
                    allow_none=True)
    s.set('foo', 'bar')
    print(s.get('foo'))


def main():
    # server_run()
    client_demo()
    # server_run2()
    # client_demo2()
    # server_run3()
    # client_demo3()


if __name__ == '__main__':
    main()
