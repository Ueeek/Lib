def gcd(a:int,b:int):
    assert a<b
    while b:
        a,b = b,a%b
    return a

def extGCD(a:int,b:int):
    """
        ax+by=gcd(a,b)を満たす、整数(x,y)を求める。
        (注意)右辺がgcd(a,b)の倍数でない時には、解が存在しない.(\ref=https://qiita.com/drken/items/b97ff231e43bce50199a#3-4-%E6%8B%A1%E5%BC%B5%E3%83%A6%E3%83%BC%E3%82%AF%E3%83%AA%E3%83%83%E3%83%89%E3%81%AE%E4%BA%92%E9%99%A4%E6%B3%95%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0%E7%9A%84%E8%A8%98%E8%BF%B0)
        (ref2:https://qiita.com/akebono-san/items/f00c0db99342a8d68e5d)
        return:
            (x,y)
    """

    if a<b:
        a,b=b,a
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    return x, y

def mod_inv(a:int,b:int):
    """
    gcd(a,b)=1の時に、
    mod bの　inv(a)を求める。
    (ax=1(mod b)となるxを求める。)
    (ref https://qiita.com/akebono-san/items/f00c0db99342a8d68e5d)
    """
    if a<b:
        a,b=b,a
    p = b
    x, y, u, v = 1, 0, 0, 1
    while b:
        k = a // b
        x -= k * u
        y -= k * v
        x, u = u, x
        y, v = v, y
        a, b = b, a % b
    x %= p
    if x < 0:
        x += p
    return x
