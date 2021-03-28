# python template for atcoder1
from functools import reduce
from collections import defaultdict
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
    nの素因数をdefaultdictで返す
    """
    factors=defaultdict(int)
    i = 2
    while i*i <= n:
        if n % i == 0:
            n //= i
            defaultdict[i]+=1
        else:
            i += 1
    if n > 1:
        defaultdict[n]+=1
    return factors

def calc_factors(N):
    """
    Nの約数をlistでreturn
    """
    i=1
    factors=set()
    while i*i<=N:
        if N%i==0:
            factors.add(i)
            factors.add(N//i)
        i+=1
    return list(sorted(factors))

def phi(n):
    #オイラー関数
    r = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            r -= r // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        r -= r // n
    return r

