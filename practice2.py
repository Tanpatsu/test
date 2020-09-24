# Pythonのお勉強 問題集
# http://python.rdy.jp/wiki.cgi?page=%CC%E4%C2%EA%BD%B8

# simple
# Hello, world!を表示
print('Hello, world!')

# 1から50までの和を計算して表示
print(sum(range(1, 51)))

# 2つの自然数の最大公約数を求める
int_value1, int_value2 = 15, 5


# 再帰関数
def greatest_common_divisor(int_value1, int_value2):
    return int_value1 if int_value2 == 0 else greatest_common_divisor(int_value2, int_value1 % int_value2)


print('値a(' + str(int_value1) + ')と値b(' + str(int_value2) + ')の最大公約数は' + str(greatest_common_divisor(int_value1, int_value2)) + 'です')

# 2つの自然数の最小公倍数を求める
print('値a(' + str(int_value1) + ')と値b(' + str(int_value2) + ')の最小公倍数は' + str(int_value1 * int_value2 // greatest_common_divisor(int_value1, int_value2)) + 'です')
