class ACC_2D:
    """
    2Dimension accumulate
    """

    def __init__(self, H, W):
        """
        H:height
        W:width
        """

        self.W = W
        self.H = H
        self.mat = [[0]*(W+1) for _ in range(H+1)]

    def __str__(self):
        """
        行列の中身が見たくなった時用
        """
        return "print mat\n"+"\n".join(map(str, [v for v in self.mat]))

    def add(self, row, col, val):
        """
        matの値を変更する(初期化)
        row:たて(0<=row<H)
        col:横(0<=col<W)
        val:mat[row][col]を初期化する値
        mat[row][col]+=val
        """
        self.mat[row+1][col+1] += val

    def build(self):
        """
        累積和を計算する
        (変更のたびにbuild)
        """
        for row in range(1, self.H+1):
            for col in range(1, self.W+1):
                self.mat[row][col] += self.mat[row][col-1] + \
                    self.mat[row-1][col] - self.mat[row-1][col-1]

    def get_val(self, g_row, g_col, s_row, s_col):
        """
        ２点で囲まれる長方形の、累積和を求める
        gx,gyは含まれない
        """
        return self.mat[g_row][g_col] - self.mat[s_row][g_col] - self.mat[g_row][s_col] + self.mat[s_row][s_col]
