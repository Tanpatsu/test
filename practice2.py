# Pythonのお勉強 問題集
# http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8

# simple
# Hello, world!を表示
print('Hello, world!')


# 1から50までの和を計算して表示
s = 0

for x in list(range(1, 51)):
    s += x
print(s)


# 2つの自然数の最大公約数を求める
a, b = input('aの値を入力:'), input('bの値を入力:')

a, b = int(a), int(b)  # 入力値を数値型に変換


def gcd(a, b):  # 再帰関数
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print('値a(' + str(a) + ')と値b(' + str(b) + ')の最大公約数は' + str(gcd(a, b)) + 'です')


# 2つの自然数の最小公倍数を求める
print('値a(' + str(a) + ')と値b(' + str(b) + ')の最小公倍数は' + str(a * b // gcd(a, b)) + 'です')
