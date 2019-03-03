# python template for atcoder1
from functools import reduce
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def gcd(a, b):
    """
    return gcd of a,b
    ユークリッド
    """
    while b:
        a, b = b, a % b
    return a


def list_gcd(l):
    """
    l: list
    l のgcd を返す
    """
    return reduce(gcd, l)


def lcm(a, b):
    """
    a,bの最小公倍数
    """
    return a*b//gcd(a, b)


def list_lcm(l):
    """
    l:list
    lのlcmを返す
    """
    return reduce(lcm, l)


n = int(input())
l = list(map(int, input().split()))
print(list_lcm(l))


def primes(N):
    '''
    エラトステネスの篩
    N以下の素数のlistを返す
    '''

    l = [v for v in range(2, N+1)]
    ret = []

    while l:
        cur = l.pop(0)
        l = list(filter(lambda x: x % cur != 0, l))
        ret.append(cur)
    return ret


def primeFact(n):
    """
    nの素因数をlistで返す
    """
    factors = []
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            factors.append(i)
        else:
            i += 1
    if n > 1:
        factors.append(n)
    return factors
