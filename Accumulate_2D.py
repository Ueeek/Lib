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

    def add(self, row, col, val):
        """
        mat[row][col]+=val

        row:(0<=row<H)
        col:(0<=col<W)
        val:val
        """
        self.mat[row+1][col+1] += val

    def add_rect(self, l_row, l_col, r_row, r_col, val):
        """
        2-Dim imos (r_inclusive)

        mat[l_row,l_col,r_row,rolc]+=val #inclusive

        0<=l_row<r_row<H
        0<=l_col<l_col<W
        """
        self.add(l_row, l_col, val)

        self.add(l_row, r_col+1, -val)
        self.add(r_row+1, l_col, -val)

        self.add(r_row+1, r_col+1, val)

    def build(self):
        """
        compute_accumulate
        call this every time aftere "add"
        """
        for row in range(1, self.H+1):
            for col in range(1, self.W+1):
                self.mat[row][col] += self.mat[row][col-1] + \
                    self.mat[row-1][col] - self.mat[row-1][col-1]

    def get_val(self, g_row, g_col, s_row, s_col):
        """
        get acculumate val of rectangle [s_row,s_col]=>(g_row,g_col)
        val of (g_row,g_col) is out of summation
        """
        return self.mat[g_row][g_col] - self.mat[s_row][g_col] - self.mat[g_row][s_col] + self.mat[s_row][s_col]

    def __str__(self):
        """
        print 2d matrix
        """
        return "print mat\n"+"\n".join(map(str, [v for v in self.mat]))
