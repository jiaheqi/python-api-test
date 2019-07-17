#!python
# -*- coding: utf-8 -*-
from model.base_model import BaseModel


class DataPool(BaseModel):

    __datas = {}

    def __init__(self, **kwargs):

        self.__datas.update(kwargs)

    def update(self, **kwargs):
        self.__datas.update(kwargs)

    def set(self, key, val):

        self.__datas[key] = val

    def get(self, key):

        if key in self.__datas:
            return self.__datas[key]
        else:
            return ""

    def keyExist(self, key):

        if key in self.__datas:
            return True
        else:
            return False

    def __getitem__(self, item):

        return self.__datas[item]

    def __dict__(self):

        return self.__datas

    def dict(self):
        return self.__datas


if __name__ == '__main__':

    dataPool = DataPool({"default":"values"})
    dataPool.set("test", "111")

    print(dataPool.get("test"))

    print(dataPool.get("default"))