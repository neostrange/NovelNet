# encoding: utf-8

'''

@author: ZiqiLiu


@file: module.py

@time: 2018/4/16 下午11:14

@desc:
'''


class Entity(object):
    def __init__(self, id):
        self.id = id
        self.names = set()
        self.freq = 0
        self.neighbors = {}

    def __str__(self):
        return str(self.id) + ":" + str(list(self.names))


class Token(object):
    def __init__(self, absPos, name, entity):
        self.absPos = absPos
        self.name = name
        self.entity = entity

class MyNER:
    def __init__(self, text, start, end):
        self.text = text
        self.start = start
        self.end = end

    def __str__(self):
        return self.text


class MyMention:
    def __init__(self, m):
        self.text = m.text
        self.start = m.start
        self.end = m.end

    def __str__(self):
        return self.text

    __repr__ = __str__