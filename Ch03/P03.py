# 1234
#1 + 2 + 3 + 4 = 10
# 5323
# 5+ 3+ 2+3
# 네자리숫자를 입력해야 한다.
num = int(input("네자리 숫자를 입력하세요"))
num1000 = num //1000
num100 = (num % 1000) // 100
num10 = (num%100) //10
num1 = num % 10

hap = num1000 + num100 + num10 + num1

print("자리수의 합", hap)

