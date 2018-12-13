# -*- coding:utf-8 -*-

# Author: bobby

from utils.math_util import *
from xdebug.variable import *
from xdebug.constant.constant import *
import json


class HandlerOpCode:

    value = ""

    def __init__(self):
        self

    def stop_handler(self, **kwargs):
        print("stop")
        exit()

    def add_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2add(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def mul_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2mul(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def sub_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2sub(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def div_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2div(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def sdiv_handler(self, **kwargs):
        print()

    def mod_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2mod(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))


    def smod_handler(self, **kwargs):
        print()

    def addmod_handler(self, **kwargs):
        print()

    def mulmod_handler(self, **kwargs):
        print()

    def exp_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2exp(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def signextend_handler(self, **kwargs):
        print()

    def lt_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            self.pop(2)
            if hexstring2dec(x) < hexstring2dec(y):
                dt["stack"].append(hex(1))
            else:
                dt["stack"].append(hex(0))
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def gt_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            self.pop(2)
            if hexstring2dec(x) > hexstring2dec(y):
                dt["stack"].append(hex(1))
            else:
                dt["stack"].append(hex(0))
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def slt_handler(self, **kwargs):
        print()

    def sgt_handler(self, **kwargs):
        print()

    def eq_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            self.pop(2)
            if hexstring2dec(x) == hexstring2dec(y):
                dt["stack"].append(hex(1))
            else:
                dt["stack"].append(hex(0))
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def iszero_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 1:
            x = hexstring2dec(dt["stack"][-1])
            dt["stack"].pop()
            if x == 0:
                dt["stack"].append(hex(1))
            else:
                dt["stack"].append(hex(0))
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def and_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2add(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def or_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2or(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def xor_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            x = dt["stack"][-1]
            y = dt["stack"][-2]
            s = hex2xor(x, y)
            self.pop(2)
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def not_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 1:
            x = dt["stack"][-1]
            s = hex2not(x)
            dt["stack"].pop()
            dt["stack"].append(s)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def byte_handler(self, **kwargs):
        print()

    def shl_handler(self, **kwargs):
        print()

    def shr_handler(self, **kwargs):
        print()

    def sar_handler(self, **kwargs):
        print()

    def sha3_handler(self, **kwargs):
        print()

    def address_handler(self, **kwargs):
        print()

    def balance_handler(self, **kwargs):
        print()

    def origin_handler(self, **kwargs):
        print()

    def caller_handler(self, **kwargs):
        print()

    def callvalue_handler(self, **kwargs):
        print()

    def calldataload_handler(self, **kwargs):
        print()
        dt["stack"].append(self.value)
        increase_index()

    def calldatasize_handler(self, **kwargs):
        print()
        dt["stack"].append(self.value)
        increase_index()

    def calldatacopy_handler(self, **kwargs):
        print()

    def codesize_handler(self, **kwargs):
        print()

    def codecopy_handler(self, **kwargs):
        print()

    def gasprice_handler(self, **kwargs):
        print()

    def extcodesize_handler(self, **kwargs):
        print()

    def extcodecopy_handler(self, **kwargs):
        print()

    def returndatasize_handler(self, **kwargs):
        print()

    def returndatacopy_handler(self, **kwargs):
        print()

    def blockhash_handler(self, **kwargs):
        print()

    def coinbase_handler(self, **kwargs):
        print()

    def timestamp_handler(self, **kwargs):
        print()

    def number_handler(self, **kwargs):
        print()

    def diffculty_handler(self, **kwargs):
        print()

    def gaslimit_handler(self, **kwargs):
        print()

    def pop_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 1:
            dt["stack"].pop()
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def mload_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 1:
            key_h = dt["stack"][-1]
            key_h = key_h[-2:]
            key_h = "0x"+key_h
            key_l = str(hex(int(key_h, 16)+0x10))
            value_h = dt["memory"].get(key_h)
            value_l = dt["memory"].get(key_l)
            value = value_h + value_l[2:]
            dt["stack"].pop()
            dt["stack"].append(value)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def mstore_handler(self, **kwargs):
        print()
        if len(dt["stack"]) >= 2:
            key = dt["stack"][-1]
            value = dt["stack"][-2]
            self.pop(2)
            store_memory(key, value)
            increase_index()
        else:
            print("[***]error : now the stack height is " + str(len(dt["stack"])))

    def mstore8_handler(self, **kwargs):
        print()

    def sload_handler(self, **kwargs):
        print()
        key = dt["stack"].pop()
        # key = key[2:]
        # if len(key) < 64:
        #     for x in range(64-len(key)):
        #         key = "0"+key
        # key = "0x"+key
        key = input2hexstring(key, 64)
        value = dt["storage"].get(key)
        if value is None:
            print("the key =", key, "is invalid")
            exit(-1)
        else:
            dt["stack"].append(value)
        increase_index()

    def sstore_handler(self, **kwargs):
        print()
        key = dt["stack"].pop()
        value = dt["stack"].pop()
        store_storage(key, value)
        increase_index()

    def jump_handler(self, **kwargs):
        print()
        label = dt["stack"][-1]
        for key in dict_assembly:
            tmp_pc, tmp_opcode, tmp_value = parse_string_2_pc_opcode(dict_assembly[key])
            if int(tmp_pc, 16) == int(label, 16):
                dict_index["unit"] = key - dict_index["index_dict"]
                dict_index["index_dict"] = key
                break
        self.pop(1)

    def jumpi_handler(self, **kwargs):
        print()
        label = dt["stack"][-1]
        count = dt["stack"][-2]
        if int(count, 16) == 0:
            self.pop(2)
            increase_index()
        elif int(count, 16) > 0:
            # 根据value找到jumpi对应的pc地址
            for key in dict_assembly:
                tmp_pc, tmp_opcode, tmp_value = parse_string_2_pc_opcode(dict_assembly[key])
                if int(tmp_pc, 16) == int(label, 16):
                    dict_index["unit"] = key - dict_index["index_dict"]
                    dict_index["index_dict"] = key
                    break
            self.pop(2)
        else:
            print("[***]error,the count is invalid")

    def getpc_handler(self, **kwargs):
        print()

    def msize_handler(self, **kwargs):
        print()

    def gas_handler(self, **kwargs):
        print()

    def jumpdest_handler(self, **kwargs):
        print()
        increase_index()

    # from 0x60 to 0x7f

    def push_handler(self, **kwargs):
        print()
        switcher = {
            "push1": BYTE01,
            "push2": BYTE02,
            "push3": BYTE03,
            "push4": BYTE04,
            "push5": BYTE05,
            "push6": BYTE06,
            "push7": BYTE07,
            "push8": BYTE08,
            "push9": BYTE09,
            "push10": BYTE10,
            "push11": BYTE11,
            "push12": BYTE12,
            "push13": BYTE13,
            "push14": BYTE14,
            "push15": BYTE15,
            "push16": BYTE16,
            "push17": BYTE17,
            "push18": BYTE18,
            "push19": BYTE19,
            "push20": BYTE20,
            "push21": BYTE21,
            "push22": BYTE22,
            "push23": BYTE23,
            "push24": BYTE24,
            "push25": BYTE25,
            "push26": BYTE26,
            "push27": BYTE27,
            "push28": BYTE28,
            "push29": BYTE29,
            "push30": BYTE30,
            "push31": BYTE31,
            "push32": BYTE32,
        }
        byte = switcher.get(kwargs.get("opcode"), 0)
        if byte != 0:
            if BYTE00 <= int(kwargs.get("value"), 16) <= byte:

                # stack.append(kwargs.get("value"))
                dt["stack"].append(kwargs.get("value"))
                increase_index()

            else:
                print("[***]error : the input value ", kwargs.get("value"), " is greater than ", str(hex(byte)))
        else:
            print("[***]error, the input is invalid")

    # from 0x80 to 0x8f ,copy the x nd element to the top of stack

    def dup_handler(self, **kwargs):
        print()
        switcher = {
            "dup1": 1,
            "dup2": 2,
            "dup3": 3,
            "dup4": 4,
            "dup5": 5,
            "dup6": 6,
            "dup7": 7,
            "dup8": 8,
            "dup9": 9,
            "dup10": 10,
            "dup11": 11,
            "dup12": 12,
            "dup13": 13,
            "dup14": 14,
            "dup15": 15,
            "dup16": 16
        }
        index = switcher.get(kwargs.get("opcode"), 0)
        if index != 0:
            if len(dt["stack"]) >= index:
                dt["stack"].append(dt["stack"][-index])
                increase_index()
            else:
                print("[***]error : now the stack height is " + str(len(dt["stack"])))
        else:
            print("[***]error : the input is invalid ")

    # from 0x90 to 0x9f,Exchange 1st and xnd stack items

    def swap_handler(self, **kwargs):
        print()
        switcher = {
            "swap1": 2,
            "swap2": 3,
            "swap3": 4,
            "swap4": 5,
            "swap5": 6,
            "swap6": 7,
            "swap7": 8,
            "swap8": 9,
            "swap9": 10,
            "swap10": 11,
            "swap11": 12,
            "swap12": 13,
            "swap13": 14,
            "swap14": 15,
            "swap15": 16,
            "swap16": 17
        }
        index = switcher.get(kwargs.get("opcode"), 0)
        if index != 0:
            if len(dt["stack"]) >= index:
                x = dt["stack"][-1]
                y = dt["stack"][-index]
                dt["stack"].pop()
                dt["stack"].append(y)
                dt["stack"].pop(-index)
                dt["stack"].insert(-(index-1), x)
                increase_index()
            else:
                print("[***] invoke "+kwargs.get("opcode")+" error : now the stack height is " + str(len(dt["stack"])))
        else:
            print("[***]error : the input is invalid ")

    # from 0xa0 to 0xa4 Append log record with (0~4) topics

    def log_handler(self, **kwargs):
        print()
        switcher = {
            "log0": 0,
            "log1": 1,
            "log2": 2,
            "log3": 3,
            "log4": 4,
        }
        index = switcher.get(kwargs.get("opcode"), -1)
        switcher_topic = {
            0: "topic0",
            1: "topic1",
            2: "topic2",
            3: "topic3",
        }
        if len(dt["stack"]) < index+2:
            print("[***]error : opcode=", kwargs.get("opcode"), ", now the stack length is", len(dt["stack"]))
        if index != -1:
            offset = dt["stack"][-1]
            length = dt["stack"][-2]
            ob = {}
            args = {}
            for x in range(index):
                topic = dt["stack"][-(3+x)]
                ob[switcher_topic.get(x)] = topic
            # 一次性存储memory都是32字节，防止出现起始偏移不是0x20的整数倍
            if int(offset, 16) % 0x20 != 0:
                print("memory =", offset, "is  invalid")
                exit(-1)
            if int(length, 16) % 0x20 == 0:
                for x in range(1, int(int(length, 16) / 0x20)+1):
                    h = dt["memory"].get(input2hexstring(int(offset, 16)*x, 2))
                    l = dt["memory"].get(input2hexstring(int(offset, 16)*x+0x10, 2))
                    value = h+l[2:]
                    args[x-1] = value
            args["length"] = int(int(length, 16) / 0x20)
            ob["args"] = args
            print(json.dumps(ob, indent=4, separators=(',', ':')))
            self.pop(index+2)
            increase_index()
        else:
            print("[***]error : opcode=", kwargs.get("opcode"), ", the input is invalid ")

    def jumpto_handler(self, **kwargs):
        print()

    def jumpsub_handler(self, **kwargs):
        print()

    def jumpsubv_handler(self, **kwargs):
        print()

    def beginsub_handler(self, **kwargs):
        print()

    def begindata_handler(self, **kwargs):
        print()

    def returnsub_handler(self, **kwargs):
        print()

    def putlocal_handler(self, **kwargs):
        print()

    def getlocal_handler(self, **kwargs):
        print()

    def sloadbytes_handler(self, **kwargs):
        print()

    def sstorebytes_handler(self, **kwargs):
        print()

    def ssize_handler(self, **kwargs):
        print()

    def create_handler(self, **kwargs):
        print()

    def call_handler(self, **kwargs):
        print()

    def callcode_handler(self, **kwargs):
        print()

    def return_handler(self, **kwargs):
        print()

    def delegatecall_handler(self, **kwargs):
        print()

    def callblockbox_handler(self, **kwargs):
        print()

    def staticcall_handler(self, **kwargs):
        print()

    def create2_handler(self, **kwargs):
        print()

    def txexcgas_handler(self, **kwargs):
        print()

    def revert_handler(self, **kwargs):
        print("[***] \"ERROR\" the assembly program has been reverted")

    def invalid_handler(self, **kwargs):
        print()

    def selfdestruct_handler(self, **kwargs):
        print()

    def handler_opcode(self, opcode, value=None):
        switcher = {
            "stop": self.stop_handler,
            "add": self.add_handler,
            "mul": self.mul_handler,
            "sub": self.sub_handler,
            "div": self.div_handler,
            "sdiv": self.sdiv_handler,
            "mod": self.mod_handler,
            "smod": self.smod_handler,
            "addmod": self.addmod_handler,
            "mulmod": self.mulmod_handler,
            "exp": self.exp_handler,
            "signextend": self.signextend_handler,
            "lt": self.lt_handler,
            "gt": self.gt_handler,
            "slt": self.slt_handler,
            "sgt": self.sgt_handler,
            "eq": self.eq_handler,
            "iszero": self.iszero_handler,
            "and": self.and_handler,
            "or": self.or_handler,
            "xor": self.xor_handler,
            "not": self.not_handler,
            "byte": self.byte_handler,
            "shl": self.shl_handler,
            "shr": self.shr_handler,
            "sar": self.sar_handler,
            "sha3": self.sha3_handler,
            "address": self.address_handler,
            "balance": self.balance_handler,
            "origin": self.origin_handler,
            "caller": self.call_handler,
            "callvalue": self.callvalue_handler,
            "calldataload": self.calldataload_handler,
            "calldatasize": self.calldatasize_handler,
            "calldatacopy": self.calldatacopy_handler,
            "codesize": self.codesize_handler,
            "codecopy": self.codecopy_handler,
            "gasprice": self.gasprice_handler,
            "extcodesize": self.extcodesize_handler,
            "extcodecopy": self.extcodecopy_handler,
            "returndatasize": self.returndatasize_handler,
            "returndatacopy": self.returndatacopy_handler,
            "blockhash": self.blockhash_handler,
            "coinbase": self.coinbase_handler,
            "timestamp": self.timestamp_handler,
            "number": self.number_handler,
            "diffculty": self.diffculty_handler,
            "gaslimit": self.gaslimit_handler,
            "pop": self.pop_handler,
            "mload": self.mload_handler,
            "mstore": self.mstore_handler,
            "mstore8": self.mstore8_handler,
            "sload": self.sload_handler,
            "sstore": self.sstore_handler,
            "jump": self.jump_handler,
            "jumpi": self.jumpi_handler,
            "getpc": self.getpc_handler,
            "msize": self.msize_handler,
            "gas": self.gas_handler,
            "jumpdest": self.jumpdest_handler,
            "push1": self.push_handler,
            "push2": self.push_handler,
            "push3": self.push_handler,
            "push4": self.push_handler,
            "push5": self.push_handler,
            "push6": self.push_handler,
            "push7": self.push_handler,
            "push8": self.push_handler,
            "push9": self.push_handler,
            "push10": self.push_handler,
            "push11": self.push_handler,
            "push12": self.push_handler,
            "push13": self.push_handler,
            "push14": self.push_handler,
            "push15": self.push_handler,
            "push16": self.push_handler,
            "push17": self.push_handler,
            "push18": self.push_handler,
            "push19": self.push_handler,
            "push20": self.push_handler,
            "push21": self.push_handler,
            "push22": self.push_handler,
            "push23": self.push_handler,
            "push24": self.push_handler,
            "push25": self.push_handler,
            "push26": self.push_handler,
            "push27": self.push_handler,
            "push28": self.push_handler,
            "push29": self.push_handler,
            "push30": self.push_handler,
            "push31": self.push_handler,
            "push32": self.push_handler,
            "dup1": self.dup_handler,
            "dup2": self.dup_handler,
            "dup3": self.dup_handler,
            "dup4": self.dup_handler,
            "dup5": self.dup_handler,
            "dup6": self.dup_handler,
            "dup7": self.dup_handler,
            "dup8": self.dup_handler,
            "dup9": self.dup_handler,
            "dup10": self.dup_handler,
            "dup11": self.dup_handler,
            "dup12": self.dup_handler,
            "dup13": self.dup_handler,
            "dup14": self.dup_handler,
            "dup15": self.dup_handler,
            "dup16": self.dup_handler,
            "swap1": self.swap_handler,
            "swap2": self.swap_handler,
            "swap3": self.swap_handler,
            "swap4": self.swap_handler,
            "swap5": self.swap_handler,
            "swap6": self.swap_handler,
            "swap7": self.swap_handler,
            "swap8": self.swap_handler,
            "swap9": self.swap_handler,
            "swap10": self.swap_handler,
            "swap11": self.swap_handler,
            "swap12": self.swap_handler,
            "swap13": self.swap_handler,
            "swap14": self.swap_handler,
            "swap15": self.swap_handler,
            "swap16": self.swap_handler,
            "log0": self.log_handler,
            "log1": self.log_handler,
            "log2": self.log_handler,
            "log3": self.log_handler,
            "log4": self.log_handler,
            "jumpto": self.jumpto_handler,
            "jumpsub": self.jumpsub_handler,
            "jumpsubv": self.jumpsubv_handler,
            "beginsub": self.beginsub_handler,
            "begindata": self.begindata_handler,
            "returnsub": self.returnsub_handler,
            "putlocal": self.putlocal_handler,
            "getlocal": self.getlocal_handler,
            "sloadbytes": self.sloadbytes_handler,
            "sstorebytes": self.sstorebytes_handler,
            "ssize": self.ssize_handler,
            "create": self.create_handler,
            "call": self.call_handler,
            "callcode": self.callcode_handler,
            "return": self.return_handler,
            "delegatecall": self.delegatecall_handler,
            "create2": self.create2_handler,
            "txexcgas": self.txexcgas_handler,
            "revert": self.revert_handler,
            "invalid": self.invalid_handler,
            "selfdestruct": self.selfdestruct_handler
        }

        func = switcher.get(opcode, "noting")
        if func != "nothing":
            func(opcode=opcode, value=value)
        else:
            print("[***]error, the input of opcode is invalid")

    def pop(self, count):
        for xx in range(count):
            dt["stack"].pop()

    def clear(self):
        dt["stack"].clear()
        dt["memory"].clear()
        dt["storage"].clear()
# if __name__ == "__main__":
#     print()
#     handler_opcode("pop")
#     handler_opcode("swap1")
#     handler_opcode("push1", "0x20")
#     handler_opcode("push1", "0xaa")
#     handler_opcode("push1", "0xff")
#     handler_opcode("dup1")
#     handler_opcode("dup3")
#     handler_opcode("swap5")
#     handler_opcode("push17", str(hex(BYTE17)))
#     handler_opcode("push1", "0x20")
#     handler_opcode("sstore")
#     handler_opcode("push17", str(hex(BYTE17)))
#     handler_opcode("push1", "0x20")
#     handler_opcode("mstore")
#     handler_opcode("push1", "0xaa")
#     handler_opcode("push1", "0x40")
#     handler_opcode("mstore")
#     handler_opcode("push32", "0x510e730eb6600b4c67d51768c6996795863364461fee983d92d5e461f209c7cf")
#     handler_opcode("push32", "0x510e730eb6600b4c67d51768c6996795863364461fee983d92d5e461f209c7ce")
#     handler_opcode("push32", "0x510e730eb6600b4c67d51768c6996795863364461fee983d92d5e461f209c7cd")
#     handler_opcode("push32", "0x510e730eb6600b4c67d51768c6996795863364461fee983d92d5e461f209c7cc")
#     handler_opcode("push1", "0x40")
#     handler_opcode("push1", "0x20")
#     handler_opcode("log4")
#     handler_opcode("log1")

