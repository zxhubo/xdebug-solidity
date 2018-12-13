# -*- coding:utf-8 -*- 
# Author: bobby

from xdebug.constant.constant import *
from xdebug.utils.parser_util import *

# 用list stack模拟栈的行为，例如['0x80', '0x03']
# 用字典memory_store模拟memory的行为，例如
# {'0x00': '0x00000000000000000000000000000000', '0x10': '0x00000000000000000000000000000000',
# '0x20': '0x00000000000000000000000000000000', '0x30': '0x00000000000000000000000000000080'}
# 用字典storage_store模拟storage的行为，
# 例如{"0x0000000000000000000000000000000000000000000000000000000000000000":"0x0000000000000000000000000000000000000000000000000000000000000000"}

dt = {
    "stack": [],
    "memory": {},
    "storage": {}
}

# 容器保存处理的指令的index，方便后续的跳转
dict_index = {
    "index_dict": 0,
    "unit": 0
}

dict_assembly = {}

# biggest_key = "0x00"


def store_memory(key, value):
    global biggest_key
    # 因为mstore(x,y)的意思就是将y值存储在x+32的位置，那么按照累成分配，起始位置x肯定是0x20的整数倍才能够正确的存储，那么首先应该是x是否是0x20的整数倍
    if int(key, 16) % 32 != 0:
        print("key=", key, "is  invalid")
        exit(-1)
    if len(dt["memory"]) < 1:
        # 这个分支说明了是第一次调用mstore
        for x in range(0, int(key, 16), 0x10):
            k = str(hex(x))
            k = k[2:]
            if len(k) < 2:
                for a in range(2 - len(k)):
                    k = "0" + k
            k = "0x" + k
            dt["memory"][k] = ZERO_32
        insert2memory_store(key, value)
    else:
        # 此分支处理第二次以上的mstore
        # 查找到字典memory的key的最大值，好做后续的for循环
        for x in dt["memory"]:
            if int(x, 16) > int(biggest_key, 16):
                biggest_key = x
        # 如果这里的key小于字典的key的最大值那么，直接更新value就好了
        if int(key, 16) < int(biggest_key, 16):
            insert2memory_store(key, value)
        else:
            for m in range(int(biggest_key, 16)+0x10, int(key, 16), 0x10):
                m = str(hex(m))
                m = m[2:]
                if len(m) < 2:
                    for b in range(2-len(m)):
                        m = "0"+m
                m = "0x"+m
                dt["memory"][m] = ZERO_32
            insert2memory_store(key, value)


def store_storage(key, value):
    key = input2hexstring(key, 64)
    value = input2hexstring(value, 64)
    if len(dt["storage"]) < 1:
        # 说明是第一次调用
        for x in range(int(key, 16)):
            x = input2hexstring(x, 64)
            dt["storage"][x] = ZERO_64
            dt["storage"][key] = value
    else:
        # 说明是第二次以上的调用
        print()
        thebig = 0
        for j in dt["storage"]:
            if int(j, 16) > thebig:
                thebig = int(j, 16)
        if int(key, 16) <= thebig:
            dt["storage"][key] = value
        else:
            for j in range(thebig+1, int(key, 16)):
                j = input2hexstring(j, 64)
                dt["storage"][j] = ZERO_64
                dt["storage"][key] = value


def insert2memory_store(key, value):
    # 处理大于32字节小于等于64字节的数据
    if BYTE32 >= int(value, 16) > BYTE16:
        l = str(hex(int(value, 16) & BYTE32_L))
        l = input2hexstring(l, 32)
        h = str(hex((int(value, 16) & BYTE32_H) >> 128))
        h = input2hexstring(h, 32)
        dt["memory"][key] = h
        dt["memory"][str(hex(int(key, 16) + 0x10))] = l
    # 处理小于等于32字节的数据
    elif BYTE16 >= int(value, 16) >= BYTE00:
        value = input2hexstring(value, 32)
        dt["memory"][key] = ZERO_32
        dt["memory"][str(hex(int(key, 16) + 0x10))] = value
    else:
        print("the number", int(value, 16), "too greater or too small ")
        exit(-1)


def increase_index():
    index_dict = dict_index["index_dict"]
    index_dict = index_dict + 1
    dict_index["index_dict"] = index_dict
    dict_index["unit"] = 1


def decrease_index():
    index_dict = dict_index["index_dict"]
    index_dict = index_dict - 1
    dict_index["index_dict"] = index_dict

