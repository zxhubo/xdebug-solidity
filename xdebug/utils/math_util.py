# -*- coding: UTF-8 -*-


def hexstring2hex(string):
    return hex(int(string, 16))


def hex2hexstring(input):
    return str(hex(input))


def hexstring2dec(string):
    return int(string, 16)


def hex2add(arg0, arg1):
    return hex2hexstring(int(arg0, 16)+int(arg1, 16))


def hex2sub(arg0, arg1):
    return hex2hexstring(int(arg0, 16)-int(arg1, 16))


def hex2mul(arg0, arg1):
    return hex2hexstring(int(arg0, 16)*int(arg1, 16))


def hex2div(arg0, arg1):
    return hex2hexstring(int(int(arg0, 16)/int(arg1, 16)))


def hex2mod(arg0, arg1):
    return hex2hexstring(int(arg0, 16) % int(arg1, 16))


def hex2exp(arg0, arg1):
    return hex2hexstring(int(arg0, 16) ** int(arg1, 16))


def hex2and(arg0, arg1):
    return hex2hexstring(int(arg0, 16) & int(arg1, 16))


def hex2or(arg0, arg1):
    return hex2hexstring(int(arg0, 16) | int(arg1, 16))


def hex2xor(arg0, arg1):
    return hex2hexstring(int(arg0, 16) ^ int(arg1, 16))


def hex2not(arg0):
    return hex2hexstring(~int(arg0, 16))


if __name__ == "__main__":
    x = hexstring2hex("0xa")
    y = hexstring2hex("0x3")
    print(int("0xa", 16))


