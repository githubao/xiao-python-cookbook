#!/usr/bin/env python
# encoding: utf-8

"""
@description: 串口通信

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec20_file_serial.py
@time: 2017/1/2 16:08
"""

import serial

def conn_serial():
    ser = serial.Serial(
        # '/dev/tty.usbmodem641',
        'COM1',
        baudrate=9600,
        bytesize=8,
        parity='N',
        stopbits=1
    )

    ser.write(b'G1 X50 Y50\r\n')
    print(ser.readline())


def main():
    conn_serial()


if __name__ == '__main__':
    main()

