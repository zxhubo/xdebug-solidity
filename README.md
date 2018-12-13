# Xdebug-solidity

## Introduction

此工具可以简单调试solidity带源码的opcode和离线调试不带源码的opcode，此工具带GUI。

用户可以选择是solidity源码带solc文件，也可以是binary文件，也可以是最终的汇编文件，根据用户的需要在opcode_parse.py小小的修改。

目前此版本的工具支持前进、后退的单步跟踪栈、内存、存储的数据结构，有兴趣的可以此工具扩展功能。

此版本有多个指令集目前没有遇到，因此他们的handler函数暂时未实现，等待工作中遇到后再更新补气。

>**说明**:
>- 此工具底层实现输出带pc地址的汇编，依赖于solc和evm，因此在使用此工具前请先安装solc和evm。
>- 此工具基于python3.7.1，Mac osX系统编写。
>- 此工具GUI基于wxPython4.1。
