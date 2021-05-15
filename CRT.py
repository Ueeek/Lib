#/ref https://atcoder.jp/contests/abc193/submissions/20516429
import typing
def _inv_gcd(a: int, b: int) -> tuple:
    a %= b
    if a == 0:
        return(b, 0)
    s = b
    t = a
    mod0 = 0
    m1 = 1

    while t:
        u = s//t
        s -= t*u
        mod0 -= m1*u
        s, t = t, s
        mod0, m1 = m1, mod0
    if mod0 < 0:
        mod0 += b//s
    return(s, mod0)


def CRT(remainders: typing.List[int], modulos: typing.List[int])->typing.Tuple[int,int]:
    """
    Chinese Remainder Theorem

    Arguments:
        R: list of remainders
        M: list of modulo

        all_same(x%ri(mod mi) for i in range(len(r)))
    Return:
        x: s.t x==ri(mod mi)  for all i in range(len(r))(0<x<lcm) 全ての条件を満たすxの値
        lcm: lcm of list m(if 0, anser is not exisis) #全てのmodに対 x=0の時、x=lcmの倍数説があるので注意 (xはlcmでmod撮られてる)というか、周期lcm
        """
    assert len(remainders) == len(modulos)

    N = len(remainders)

    #2-var CRTを繰り返し適応していく。一つ目を(r,m)=(0,1)としておく。(単位元的な)
    rem0 = 0
    mod0 = 1

    #Contracts: 0<=rem0<mod0

    for i in range(N):
        assert 1 <= modulos[i]
        rem1 = remainders[i] % modulos[i]
        mod1 = remainders[i]
        if mod0 < mod1:
            rem0, rem1 = rem1, rem0
            mod0, mod1 = mod1, mod0
        if mod0 % mod1 == 0:
            if rem0 % mod1 != rem1:
                return (0, 0)
            continue

        g, im = _inv_gcd(mod0, mod1)
        u1 = mod1//g

        if (rem1-rem0) % g:
            return (0, 0)
        x = (rem1-rem0)//g % u1*im % u1
        rem0 += x*mod0
        mod0 *= u1
        if rem0 < 0:
            rem0 += mod0
    return (rem0, mod0)
