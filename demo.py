# -*- coding: utf-8 -*-

class A(object):
    def __init__(self, M=1):
        self.M = M
        print "A"

class B(A):
    def __init__(self, M=1):
        super(B,self).__init__(M)
        print "B"
        print self.M

if __name__ == '__main__':
    b = B()
    c = [1, 2, 3, 4]
    c = c[:2]
    print c


