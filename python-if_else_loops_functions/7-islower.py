#!/usr/bin/python3
islower = __import__('7-islower').islower
def islower(c):
    if ord(c) >= 97 and ord() <= 123:
        return True
    else:
        return False
