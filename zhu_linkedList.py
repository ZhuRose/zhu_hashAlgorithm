# -*- coding: utf-8 -*-

class zhu_node(object):
    def __init__(self, data, pnext = None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)

class zhu_linkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def _createNode(self, dataOrNode):
        item = None
        if isinstance(dataOrNode, zhu_node):
            item = dataOrNode
        else:
            item = zhu_node(dataOrNode)
        return item

    def _hasError(self, index=0):
        if self.isEmpty():
            print("error: nodeList is empty")
            return True
        if index < 0 or index >= self.length:
            print('error: out of index')
            return True
        return False

    def _getIndexNodeAndPrev(self, index):
        j = 0
        node = self.head
        prev = None
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            return node, prev

    def isEmpty(self):
        return (self.length == 0)

    def append(self, dataOrNode):
        item = self._createNode(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        if self._hasError(index):
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        node, prev = self._getIndexNodeAndPrev(index)
        prev._next = node._next
        self.length -= 1

    def insert(self, index, dataOrNode):
        if self._hasError(index):
            return

        item = self._createNode(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        node, prev = self._getIndexNodeAndPrev(index)
        item._next = node
        prev._next = item
        self.length += 1

    def update(self, index, data):
        if self._hasError(index):
            return

        node = self._getIndexNodeAndPrev(index)[0]
        node.data = data

    def yieldItem(self):
        node = self.head
        j = 0
        while node:
            yield j, node.data
            node = node._next
            j += 1

    def getItem(self, index):
        if self._hasError(index):
            return

        node = self._getIndexNodeAndPrev(index)[0]
        return node.data

    def getIndex(self, data):
        if self._hasError():
            return

        node = self.head
        j = 0
        while node:
            if node.data == data:
                return j
            node = node._next
            j += 1

        if j == self.length:
            print("%s not found" % str(data))
            return

    def clear(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "nodeList is empty"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print('error: out of index')
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print('error: out of index')
            return
        self.update(ind, val)

    def __len__(self):
        return self.length