from itertools import groupby
def runLengthEncode(S:str)->list:
    """
    RUN-LENGTH-ENCODE"
    aaabbbcc->[("a",3"),("b",3),("c",2)]
    """
    ret=[]
    for key,val in groupby(S):
        ret.append((key,int(len(list(val)))))
    return ret


def __runLengthEncodeTest():
    tests=["aangaweoiaeorwhjoweijgoajogjeoaiwjogjeaowijgo","11111111","1","121212"]
    for test in tests:
        ret = runLengthEncode(test)
        SS=""
        for key,val in ret:
            SS+=key*val

        prevKey=None
        for key,_ in ret:
            assert not prevKey==key
            prevKey=key
        assert SS==test
    return True

if __name__=="__main__":
    if __runLengthEncodeTest():
        print("runLengthEncode OK")



