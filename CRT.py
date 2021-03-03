#/ref https://atcoder.jp/contests/abc193/submissions/20516429
def _inv_gcd(a: int, b: int) -> tuple:
    a %= b
    if a == 0:
        return(b, 0)
    s = b
    t = a
    m0 = 0
    m1 = 1

    while t:
        u = s//t
        s -= t*u
        m0 -= m1*u
        s, t = t, s
        m0, m1 = m1, m0
    if m0 < 0:
        m0 += b//s
    return(s, m0)


def CRT(R: list, M: list):
    """
    Chinese Remainder Theorem

    Arguments:
        R: list of remainders
        M: list of modulo

        all_same(x%ri(mod mi) for i in range(len(r)))
    Return:
        x: s.t x==ri(mod mi)  for all i in range(len(r))(0<x<lcm)
        lcm: lcm of list m(if 0, anser is not exisis)
    """
    assert len(R) == len(M)

    N = len(R)

    #2-var CRTを繰り返し適応していく。一つ目を(r,m)=(0,1)としておく。(単位元的な)
    r0 = 0
    m0 = 1

    #Contracts: 0<=r0<m0

    for i in range(N):
        assert 1 <= M[i]
        r1 = R[i] % M[i]
        m1 = M[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return (0, 0)
            continue

        g, im = _inv_gcd(m0, m1)
        u1 = m1//g

        if (r1-r0) % g:
            return (0, 0)
        x = (r1-r0)//g % u1*im % u1
        r0 += x*m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return (r0, m0)
