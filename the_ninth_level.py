#!/usr/bin/env python
# -*- coding:utf-8 -*-
#author: justinli.ljt@gmail.com
'''
光棍节程序员闯关秀第9关(总共10关)
http://segmentfault.com/game/?k=ca81a4fa7ce5fac0f8c00e94c741dd61

通关秘籍
'''

import os, sys
import base64

class TheNinthLevel(object):
    '''
    ciphertext crack class
    '''
    def __init__(self):
        pass

    def _binstr2int(self, s):
        i = -1
        try:
            i = int(s, 2)
        except Exception, e:
            print e
            return i
        return i

    def _int2ascii(self, i):
        a = 'Invalid'
        try:
            a = str(unichr(i))
        except Exception, e:
            print e
            return a
        return a

    def crack(self, ciphertext_file):
        if not os.path.exists(ciphertext_file):
            print 'file %s not exists' % (ciphertext_file)
            return

        ciphertext_string_list = []
        ciphertext_int_list = []
        ciphertext_ascii_list = []

        ciphertext = ''
        plaintext = ''

        try:
            fp = open(ciphertext_file)
            lines = fp.readlines()
            for line in lines:
                # test replace, '1' or '0' instead of '_'.
                # you will find, '1' will be the right one
                line = line.replace('_', '1')
                ciphertext_string_list+= line.strip().split(' ')
            fp.close()
        except Exception,e:
            print e
            return

        print ciphertext_string_list

        for s in ciphertext_string_list:
            i = self._binstr2int(s)
            ciphertext_int_list.append(i)

        print ciphertext_int_list

        for i in ciphertext_int_list:
            a = self._int2ascii(i)
            ciphertext_ascii_list.append(a)

        print ciphertext_ascii_list

        ciphertext = ''.join(ciphertext_ascii_list)

        print ciphertext

        plaintext = base64.b64decode(ciphertext)

        print plaintext

        # test the postfix
        fp = open('out.tar.gz', 'a') # then, run "tar -zxvf a.tar.gz", you will find Teacher Cang is waiting for you :)
        fp.write(plaintext)
        fp.close()

        pass
    pass

def main():
    if len(sys.argv) != 2:
        print 'parameter number is invalid'
        return

    ciphertext_file = sys.argv[1]

    tnl = TheNinthLevel()
    tnl.crack(ciphertext_file)

if __name__ == '__main__':
    main()

