#!/usr/bin/env python
# Code Wars kata: Reverse or rotate?
# Author: ZettStai


def revrot(strng, sz):
    # your code
    chunk = []
    newstr = []

    if (sz <= 0) or (strng == ''):
        return ''
    if sz > len(strng):
        return ''

    # slice string into chunks by sz

    for i in range(0, len(strng), sz):
        p = i + sz
        chunk.append(strng[i:p])

        # check each chunk
    for i in range(len(chunk)):
        if len(chunk[i]) == sz:

            newstr.append(sumcube(chunk[i]))

    return ''.join(newstr)

def sumcube(chkstr):

    # if sum of the cubes of its digits is divisible by 2
    # else: rotate it to the left by one position
    # join chunks & return

    sum = 0
    for i in range(len(chkstr)):
        sum = sum + int(chkstr[i]) ** 3
    if sum % 2 == 0:
        return chkstr[::-1]
    else:
        return chkstr[1:] + chkstr[:1]


# revrot("123456987654", 6)
# print ("answer is 234561876549")
# revrot("123456987653", 6)
# print("answer is 234561356789")
# revrot("66443875", 4)
# print("answer is 44668753")
# revrot("66443875", 8)
# print ("answer is 64438756")
# revrot("664438769", 8)
# print ("answer is 67834466")
# revrot("123456779", 8)
# print ("answer is 3456771")
# print(revrot('', 8))
# print ("answer is ''")
# revrot("123456779", 0)
# print ("answer is ''")
# revrot("563000655734469485", 4)
# print ("answer is 0365065073456944")