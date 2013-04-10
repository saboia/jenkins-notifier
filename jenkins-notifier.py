#!/usr/bin/env python
#-*- coding:utf-8 -*-

from growl import GrowlPing


if __name__ == '__main__':

    p = GrowlPing()
    p.notify(1000)
