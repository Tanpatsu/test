# Progateでの学習
# "#"をつけるとコメントにできる


# 1.文字の出力
# 文字列には''もしくは""で囲む
print("Hello world")

# 数字は囲む必要なし
print(1)


# 2.計算の方法
# 足し算
print(2 + 3)

# 引き算
print(4 - 5)

# 掛け算
print(6 * 7)

# 割り算(結果を小数点で出力)
print(9 / 2)

# 割り算(余りを出力)
print(5 % 3)


# 3.変数
# 変数nameに文字を代入
name = "テスト"

print(name)

# 変数numberに数字を代入
number = 55

print(number)

# 変数を使った計算
apple_value = 200
apple_count = 3
total_price = apple_value * apple_count

print(total_price)

# 変数の値の更新
x = 0

print(x)

x = x + 1

print(x)

# 値更新の省略形
# 足し算
plus = 0
plus += 10

print(plus)

# 引き算
minus = 0
minus -= 10

print(minus)

# 掛け算
multiplied = 5
multiplied *= 5

print(multiplied)

# 割り算(小数点出力)
divided_a = 5
divided_a /= 2

print(divided_a)

# 割り算(余り出力)
divided_b = 5
divided_b %= 2

print(divided_b)


# 4.文字列の連結
comment = 'テスト'

print('これは' + comment + 'です。')


# 5.型変換
# int→string型に変換
int_value = 100

print('この数字は' + str(int_value) + 'です。')

# string→int型に変換
str_value = '10'
total_value = int_value + int(str_value)

print(total_value)


# 6.条件分岐(if文)
# 該当処理がif文の中にあるかはインデントで判断(インデントがないとif文の外と認識される)
a = 2 * 3
b = 4 * 5
c = 50

# 値が等しい場合
if a == 6:
    print('aは6です')
else:
    print('aは6ではありません')

# 値が等しくない場合
if b != 30:
    print('bは30ではありません')
else:
    print('bは30です')

# 条件を満たさない場合
if a > c:
    print('aはcより大きい')
else:
    print('aはc以下')

# 条件を複数定義する場合
if a > b:
    print('aはbより大きい')
elif c > b:
    print('cはbより大きい')
else:
    print('条件を満たさない')

# 複数の条件を組み合わせる
if 1 <= a <= 10:
    print('aは1～10の間です')

if a <= 10 or a >= 60:
    print('aは10以下、または60以上です')


# 7.入力を受け取る
input_value = input('文字を入力してください')
print('入力した文字は「' + str(input_value) + '」です')


# ex.代金計算と金額が足りるか結果を出力する
apple_price = 200
money = 1000

input_count = input('購入するりんごの個数を入力してください：')
count = int(input_count)
total_price = apple_price * count

print('購入するりんごの個数は' + str(count) + '個です')
print('支払い金額は' + str(total_price) + '円です')

# moneyとtotal_priceの比較結果によって条件を分岐
if money > total_price:
    print('りんごを' + str(count) +'個買いました')
    print('預金は' + str(money - total_price) +'円です')
elif money == total_price:
    print('りんごを' + str(count) +'個買いました')
    print('財布が空になりました')
else:
    print('お金が足りません')
    print('りんごを買えませんでした')
