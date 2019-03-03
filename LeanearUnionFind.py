# -*- coding: utf-8 -*-
class UnionFind:
    '''
    配列を用いたUnionFind
    '''

    def __init__(self, size):
        self.table = [i for i in range(size)]

    def find(self, x):
        '''
        xのグループ番号を返す
        '''
        return self.table[x]

    def union(self, x, y):
        '''
        xとyが同じグループならFalse
        xとyが違うグループなら、同じグループにする(くっつける)
        '''
        x1 = self.find(x)
        y1 = self.find(y)

        if x1 == y1:
            return False

        for i in range(len(self.table)):
            if self.table[i] == y1:
                self.table[i] = x1
        return True

    def same(self, x, y):
        '''
        xとyが同じグループならtrue
        '''
        x1 = self.find(x)
        y1 = self.find(y)
        return x1 == y1
