# -*- coding: utf-8 -*-

from zhu_linkedList import zhu_linkedList

class zhu_hashMap(object):
    def __init__(self, M=97):
        self._M = M

    def zhu_hashcode(self, key, R=31):
        hash = 0
        M = self._M
        for i in range(len(key)):
            hash = (R * hash + ord(key[i])) % M
        return hash

class zhu_separateChainHashMap(zhu_hashMap):
    def __init__(self, M=97):
        super(zhu_separateChainHashMap, self).__init__(M)
        self.st = [zhu_linkedList() for i in range(M)]

    def getItem(self, key):
        ind = self.zhu_hashcode(key)
        ll = self.st[ind]
        for j, kv in ll.yieldItem():
            if kv[0] == key:
                return kv[1]
        print("error: %s not find"%key)

    def setItem(self, key, value):
        ind = self.zhu_hashcode(key)
        ll = self.st[ind]
        for j, kv in ll.yieldItem():
            if kv[0] == key:
                ll[j] = (key, value)
                return
        ll.append((key, value))

    def removeItem(self, key):
        ind = self.zhu_hashcode(key)
        ll = self.st[ind]
        for j, kv in ll.yieldItem():
            if kv[0] == key:
                ll.delete(j)
                return
        print("error: %s not find" % key)

    def __getitem__(self, item):
        return self.getItem(item)

    def __setitem__(self, key, value):
        self.setItem(key, value)

class zhu_linearProbingHashMap(zhu_hashMap):
    def __init__(self, M=97):
        super(zhu_linearProbingHashMap, self).__init__(M)
        self.N = 0
        self.keys = [None for i in range(M)]
        self.vals = [None for i in range(M)]

    def resize(self, cap = 2):
        if cap >= 1:
            self.keys.extend([None for i in range(self.M * (cap - 1))])
            self.vals.extend([None for i in range(self.M * (cap - 1))])
        else:
            self.keys = self.keys[:self.M * cap]
            self.vals = self.vals[:self.M * cap]
        self._M *= cap

    def getItem(self, key):
        ind = self.zhu_hashcode(key)
        while self.keys[ind] is not None:
            if self.keys[ind] == key:
                return self.vals[ind]
            else:
                ind = (ind + 1) % self._M
        print("error: %s not find"%key)
        return

    def setItem(self, key, value):
        if self.N > self._M / 2:
            self.resize()
        ind = self.zhu_hashcode(key)
        while self.keys[ind] is not None:
            if self.keys[ind] == key:
                self.vals[ind] = value
                return
            else:
                ind = (ind + 1) % self._M
        self.keys[ind] = key
        self.vals[ind] = value
        self.N += 1

    def removeItem(self, key):
        ind = self.zhu_hashcode(key)
        while self.keys[ind] is not None:
            if self.keys[ind] == key: #找到了要删除的KV
                self.keys[ind] = None
                self.vals[ind] = None
                ind = (ind + 1) % self._M #redo后面的值
                while self.keys[ind] is not None:
                    redo_key = self.keys[ind]
                    redo_val = self.vals[ind]
                    self.keys[ind] = None
                    self.vals[ind] = None
                    self.N -= 1
                    self.setItem(redo_key, redo_val)
                    ind = (ind + 1) % self._M
                self.N -= 1
                if self.N > 0 and self.N == self._M /8:
                    self.resize(1/2)
                return
            else: #继续查找
                ind = (ind + 1) % self._M
        print("error: %s not find" % key)

    def __getitem__(self, item):
        return self.getItem(item)

    def __setitem__(self, key, value):
        self.setItem(key, value)

if __name__ == '__main__':
    m = zhu_linearProbingHashMap(7)
    m["abc"] = 1
    m["ggg"] = 2
    print(m["abc"])
    print(m["ggg"])
    m.removeItem("abc")
    print(m["abc"])