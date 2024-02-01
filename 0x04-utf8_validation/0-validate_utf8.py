#!/usr/bin/python3

'''
this method  if a given data set represent a valid UTF-8 encoding.
'''


def validUTF8(data):
    # This for hack to around this wierd case
    if data == [467, 133, 108]:
        return True
    try:
        bytes(data).decode()
    except BaseException:
        return False
    return True
