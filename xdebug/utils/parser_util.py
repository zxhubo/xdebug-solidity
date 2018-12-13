# -*- coding:utf-8 -*- 
# Author: bobby


def parse_string_2_pc_opcode(string):
    list_string = str(string)
    pc = ""
    opcode = ""
    value = ""
    l = list_string.split(" ")
    if len(l) == 3:
        pc = l[0]
        pc = pc[:-1]
        opcode = l[1]
        value = l[2]
    elif len(l) == 2:
        pc = l[0]
        pc = pc[:-1]
        opcode = l[1]
    # print(pc + " is " +xdebug)
    return pc, opcode, value


def input2hexstring(input, length):
    if type(input) is int:
        s = str(hex(input))
        s = s[2:]
        if len(s) < length:
            for x in range(length-len(s)):
                s = "0"+s
        s = "0x"+s
        return s
    elif type(input) is str:
        if str(input).startswith("0x"):
            input = input[2:]
        if len(input) < length:
            for x in range(length-len(input)):
                input = "0"+input
        input = "0x"+input
        return input
    else:
        print("[error]input =", input, " format is error")
        exit(-1)


def find(list, input):
    for x in list:
        if x == input:
            return True
            break
    return False


if __name__ == "__main__":
    print(input2hexstring("a", 2))

