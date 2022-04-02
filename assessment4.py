'''def sqroot(a):
    import math
    return math.sqrt(a)


def quadratic(a, b, c):
    import math
    j = (b*b-4*a*c)
    x = (-b+math.sqrt(j))/2*a
    y = (-b-math.sqrt(j))/2*a
    return [x, y]


def celfah(a):
    return a*1.8 + 32


def number(a):
    if a > 0:
        return "positive"
    elif a == 0:
        return "Zero"
    elif a < 0:
        return "negative"


def recur(a):
    if a <= 1:
        return a
    return a + recur(a - 1)


if __name__ == "_main_":
    n1 = int(input("1 : "))
    n2 = int(input("2 : "))
    n3 = int(input("3 : "))
'''