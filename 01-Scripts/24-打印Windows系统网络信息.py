#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date        : 2022-06-07 10:52:51
# @Author      : junsircoding
# @File        : 01-Scripts/24-打印Windows系统网络信息.py
# @Info        : 
# @Last Edited : 2022-06-07 14:37:18

import winreg


def val2addr(val):
    addr = ""
    for ch in val:
        addr += ("%02x " % ord(ch))
        addr = addr.strip(" ").replace(" ", ":")[0:17]
    return addr


def printNets():
    net = r"SOFTWARE\Microsoft\WindowsNT\CurrentVersion\NetworkList\Signatures\Unmanaged"
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, net)
    print('\n[*] Networks You have Joined.')
    for i in range(100):
        try:
            guid = winreg.EnumKey(key, i)
            netKey = winreg.OpenKey(key, str(guid))
            (n, addr, t) = winreg.EnumValue(netKey, 5)
            (n, name, t) = winreg.EnumValue(netKey, 4)
            macAddr = val2addr(addr)
            netName = str(name)
            print('[+] ' + netName + ' ' + macAddr)
            winreg.CloseKey(netKey)
        except:
            break


def main():
    printNets()


if __name__ == "__main__":
    main()
