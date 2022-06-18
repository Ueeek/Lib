import typing
class Compress:
    """
    座標圧縮
    """
    def __init__(self,L:typing.List[int],keep_greater=True,start_idx=0):
        """
        :param: L: 圧縮するlist
        :param: keep_greater:　圧縮前の大小関係を保存する?
        :param: start_idx: start id of compId (BITと組み合わせるときは、1-startの方が都合いい)　
        """

        self.num2comp_idx=dict()
        self.comm_idx2num=dict()

        if keep_greater:
            L = list(sorted(L))

        for l in L:
            if l in self.num2comp_idx:
                continue
            else:
                self.num2comp_idx[l] = len(self.num2comp_idx) + start_idx
                self.comm_idx2num[self.num2comp_idx[l]]=l

    def compress(self,v:int)->int:
        """
        compress int 
        """
        return self.num2comp_idx[v]

    def compress_list(self,L:typing.List[int])->typing.List[int]:
        """
        :parapm: list[int]

        Lを圧縮して、圧縮後のid_sequenceでreturn
        """

        return [self.compress(l) for l in L]

    def decomporess(self,v:int)->int:
        return self.comm_idx2num[v]

    def decomporess_list(self,compressL:typing.List[int])->typing.List[int]:
        """
        :parap: compressL
        
        圧縮後の列を元に戻す
        """
        return [self.decomporess(l) for l in compressL]
