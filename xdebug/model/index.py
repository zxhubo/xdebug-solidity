# -*- coding:utf-8 -*- 
# Author: bobby


class Index:

    index = 0
    unit = 0
    stack = []
    memory = {}
    storage = {}

    def __init__(self, index, unit, stack, memory, storage):
        self.index = index
        self.unit = unit
        self.stack = stack.copy()
        self.memory = memory.copy()
        self.storage = storage.copy()




