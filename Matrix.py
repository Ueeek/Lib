import unittest
class Matrix:
    """
    matrixのmod演算とか
    """
    def __init__(self,h,w):
        """
        matix[h][w]
        """
        self.mat=[[0]*w for _ in range(h)]
        self.h=h
        self.w=w


    def __str__(self):
        ret="\n".join([" ".join(map(str,row)) for row in self.mat])
        return ret

    def __getitem__(self,idx):
        return self.mat[idx]

    def __eq__(self,mat):
        assert self.shape()==mat.shape()
        for i in range(self.h):
            for j in range(self.w):
                if self.mat[i][j]!=mat[i][j]:
                    return False
        return True

    def shape(self):
        """
        return (h,w)
        """
        return (self.h,self.w)

    def __add__(self,mat):
        """
        Add matrix
        return new_matrix
        """
        assert self.shape()==mat.shape(),"addition defined only same shape matrix"
        ret = Matrix(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                ret[i][j] = self.mat[i][j]+mat[i][j]

        return ret

    def __mul__(self,mat):
        """
        called when "*"
        return self.mat@mat
        doesnot modify self
        """
        assert self.w==mat.h

        ret=Matrix(self.h,mat.w)
        for i in range(self.h):
            for j in range(mat.w):
                for k in range(self.w):
                    ret[i][j]+=self.mat[i][k]*mat[k][j]
        return ret

    def __mod__(self,mod):
        ret=Matrix(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                ret[i][j] = self.mat[i][j]%mod
        return ret

    def __neg__(self):
        ret=Matrix(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                ret[i][j] = -self.mat[i][j]
        return ret

    def __abs__(self):
        ret=Matrix(self.h,self.w)
        for i in range(self.h):
            for j in range(self.w):
                ret[i][j] = abs(self.mat[i][j])
        return ret

    def copy(self):
        h,w = self.shape()
        ret = Matrix(h,w)
        for i in range(self.h):
            for j in range(self.w):
                ret[i][j]=self.mat[i][j]
        return ret

    def pow(self,n,mod=None):

        if n==0:
            return self.zeros_like(self.mat)

        n-=1
        tmp=self.copy()

        ret = self.copy()

        i=0
        while n>pow(2,i-1):
            if n>>i&1:
                ret = ret*tmp
            tmp = tmp*tmp
            if mod:
                tmp%=mod
                ret%=mod
            i+=1

        return ret

    @classmethod
    def zeros(cls,h,w):
        return Matrix(h,w)

    @classmethod
    def eyes(cls,h):
        ret = Matrix(h,h)
        for i in range(h):
            ret[i][i]=1
        return ret


    @classmethod
    def zeros_like(cls,mat):
        h,w = mat.shape()
        return Matrix(h,w)

    @classmethod
    def eyes_like(cls,mat):
        h,w = mat.shape()
        assert h==w
        return Matrix.eyes(h)

    @classmethod
    def fromList(cls,l):
        "二次元配列"
        assert len(l)>0 and len(l[0])>0

        h = len(l)
        w = len(l[0])
        mat = Matrix(h,w)
        for i in range(h):
            for j in range(w):
                mat[i][j]=l[i][j]
        return mat

class MatrixTest(unittest.TestCase):

    def testShape(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        self.assertTrue(m1.shape()==(2,3))
    def testEq(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        self.assertTrue(m1==Matrix.fromList([[1,2,3],[4,5,6]]))

    def testEq2(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        m2 = Matrix.fromList([[1,2,3],[4,5,6]])
        self.assertTrue(m1==m2)

    def testAdd(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        m2 = Matrix.fromList([[1,2,3],[4,5,6]])
        m3 = m1+m2
        self.assertTrue(m3==Matrix.fromList([[2,4,6],[8,10,12]]))

    def testAbs(self):
        m1 = Matrix.fromList([[-1,-2,-3],[-4,5,6]])
        m2 = abs(m1)
        self.assertTrue(m2==Matrix.fromList([[1,2,3],[4,5,6]]))

    def testMod(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        m2 = m1%2
        self.assertTrue(m2==Matrix.fromList([[1,0,1],[0,1,0]]))

    def testNeg(self):
        m1 = Matrix.fromList([[-1,-2,-3],[-4,5,6]])
        m2 = -m1
        self.assertTrue(m2==Matrix.fromList([[1,2,3],[4,-5,-6]]))

    def testCopy(self):
        m1 = Matrix.fromList([[-1,-2,-3],[-4,5,6]])
        m2 = m1.copy()
        m2[0][0]=10
        self.assertFalse(m1==m2)

    def testCopy2(self):
        m1 = Matrix.fromList([[-1,-2,-3],[-4,5,6]])
        m2 = m1.copy()
        self.assertTrue(m1==m2)

    def testMul(self):
        m1 = Matrix.fromList([[1,2,3],[4,5,6]])
        m2 = Matrix.fromList([[7,8],[10,11],[12,13]])
        self.assertTrue(m1*m2==Matrix.fromList([[63,69],[150,165]]))
        self.assertTrue(m2*m1==Matrix.fromList([[39,54,69],[54,75,96],[64,89,114]]))


    def testPow(self):
        m1 = Matrix.fromList([[1,2],[3,4]])
        m2 = m1.pow(5,10)
        self.assertTrue(m2==Matrix.fromList([[9,8],[7,6]]))

    def testPow2(self):
        m1 = Matrix.fromList([[1,2],[3,4]])
        m2 = m1.pow(2)
        self.assertTrue(m2==Matrix.fromList([[7,10],[15,22]]))

    def testPow3(self):
        m1 = Matrix.fromList([[1,2],[3,4]])
        m2 = m1.pow(2,5)
        self.assertTrue(m2==Matrix.fromList([[2,0],[0,2]]))

    def testPow4(self):
        m1 = Matrix.fromList([[1,2],[3,4]])
        m2 = m1.pow(5)
        self.assertTrue(m2==Matrix.fromList([[1069,1558],[2337,3406]]))

    def testPow5(self):
        m1 = Matrix.fromList([[1,2],[3,4]])
        m2 = m1.pow(10,100)
        self.assertTrue(m2==Matrix.fromList([[7,50],[75,82]]))

    def testEyes(self):
        m1 = Matrix.eyes(10)
        m2 = Matrix.eyes_like(m1)
        self.assertTrue(m1==m1*m2)

    def testZeros(self):
        m1 = Matrix.eyes(10)
        m2 = Matrix.zeros(10,10)
        m3 = Matrix.zeros_like(m1)
        self.assertTrue(m1*m2==m3)

if __name__=="__main__":
    unittest.main()
