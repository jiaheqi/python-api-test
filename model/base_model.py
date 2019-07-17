#!python
# -*- coding: utf-8 -*-


class BaseModel():

    def __init__(self, **kwargs):
        map(lambda key:self.set(key, kwargs[key]), kwargs)

    def set(self, key, val):

        self.__dict__[key] = val
        return self

    def get(self, key):

        return self.__dict__[key]

    def __getitem__(self, item):

        return self.__dict__[item]

    def dict(self):
        return self.__dict__