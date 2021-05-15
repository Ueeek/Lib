class Compress:
    """
    座標圧縮
    """
    def __init__(self,L:typing.List[int],keep_greater=True):
        """
        :param: L: 圧縮するlist
        :param: keep_greater:　圧縮前の大小関係を保存する?
        """

        self.num2comp_idx=dict()
        self.comm_idx2num=dict()

        if keep_greater:
            L = list(sorted(L))

        for l in L:
            if l in self.num2comp_idx:
                continue
            else:
                self.num2comp_idx[l] = len(self.num2comp_idx)
                self.comm_idx2num[self.num2comp_idx[l]]=l

    def compress(self,L:typing.List[int]):
        """
        :parapm: list[int]

        Lを圧縮して、圧縮後のid_sequenceでreturn
        """
        ret = [self.num2comp_idx[l] for l in L]
        return ret

    def decomporess(self,compressL:typing.List[int]):
        """
        :parap: compressL
        
        圧縮後の列を元に戻す
        """
        ret = [self.comm_idx2num[v] for v in compressL]
        return ret

    def get_compress(self,val):
        """
        圧縮後のidをreturn
        """
        return  self.num2comp_idx[val]

    def get_decompress(self,val):
        """
        圧縮前のidをreturn
        """
        return self.comm_idx2num[val]



