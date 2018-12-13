# -*- coding:utf-8 -*-

# Author: bobby

import os
# import comm
code = """

contract mortal {
    /* Define variable owner of the type address */
    address owner;

    /* This function is executed at initialization and sets the owner of the contract */
    constructor() public { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() public{ if (msg.sender == owner) selfdestruct(owner); }
}

contract greeter is mortal {
    /* Define variable greeting of the type string */
    string greeting;

    /* This runs when the contract is executed */
    constructor(string _greeting) public {
        greeting = _greeting;
    }

    /* Main function */
    function greet() public constant returns (string) {
        return greeting;
    }
}
"""

fileSolc = "/Users/bobby/solc.solc"
fileEvm = "/Users/bobby/solc.evm"
# command = "echo \"" + code+"\">>/Users/bobby/solc.solc && solc --bin-runtime /Users/bobby/solc.solc"
# print(command)
#
# stout = os.popen(command)
# print(stout.read())

white_list = []


def writefile(file, value):
    file = open(file, "w")
    length = file.write(value)
    if length > 0:
        return True
    else:
        return False


def readfile(file):
    fp = open(file, "r")
    content = fp.read()
    return content


def exec_command(shell):
    mp = os.popen(shell)
    return mp.read()


def get_bytecode(file):
    l = []
    writefile(file, code)
    shell = "solc --bin-runtime  " + file
    stout = exec_command(shell)
    # print(stout)
    stout = str(stout)
    for string in stout.split("\n"):
        l.append(string)
    return l[3]


def get_assembly(file, value):
    l = []
    writefile(file, value)
    shell = "evm disasm " + file
    stdout = exec_command(shell)
    stdout = str(stdout)
    # print(stdout)
    for x in stdout.split("\n"):
        l.append(x)
    return l[1:len(l)-1]


def pc_dec2hex(origin_assem):
    changed_assem = []
    for x in origin_assem:
        x = str(x)
        y = x[0:x.index(":")]
        z = str(hex(int(y)))
        z = z[2:]
        if len(z) < 4:
            tmp = ""
            for i in range(4-len(z)):
                tmp = tmp+"0"
            z = "0x"+tmp+z
        x = x.replace(y, z)
        changed_assem.append(x)
    return changed_assem


def parse_assembly(assembly):
    dict = {}
    tmp = assembly
    count = assembly.count("\n")
    print("[***]----------")
    if count == 0:
        dict[0] = assembly
    else:
        for x in range(count+1):
            l = []
            if x == count:
                l = tmp
            else:
                l = tmp[0:tmp.index("\n")]
                for y in l:
                    tmp.remove(y)
                tmp = tmp[1:]
            dict[x] = l
    return dict


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


def parse_list2string(l):
    s = ""
    for x in l:
        s = s + x + "\n"
    s = s[:len(s)-1]
    return s


def is_include(value):
    try:
        white_list.index(value)
        return True
    except:
        return False


def add_white_list(l):
    white_list.append(l)


def delete_white_list(l):
    white_list.remove(l)


def get_list_last(l):
    s = l[-1]
    # print(s)
    return s


def get_list_first(l):
    s = ""
    for x in l:
        s = x
        break
    return s












