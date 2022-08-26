# #숫자형 실습
# a = 123
# b = -123
# print(a, b)

# #실수 표현
# fa = 3.459e10
# fb = -4.62809
# fc = 8.43e-2
# print(fa, fb, fc)


# num = 0.0
# # range: 0~100 ==> 0~99
# for idx in range(0, 100):
#     num = num + 0.1  # num += 0.1
# print(num)
# print(f'{num:.18f}')  # 소수점 아래 18자리까지 표현해줘
#
# num = 0.0
# for idx in range(0, 100):
#     num = num + 1
# print(num)
#
#
# num1 = 20
# num2 = 3
#
# sumR = f'{num1+num2}'
# print(sumR, f'{num1*num2}, {num1/num2}')
#
# #.나누기 몫, 나머지, 승수
# print(num1//num2)
# print(num1%num2)
# print(num1**num2)


# #구구단 내가 한거
# a = 0
# gugu = 7
# for idx in range(1, 10):
#     a = gugu * idx
#     print(a, end = " ")
# print('\n')
#
# #구구단 정답
# for x in range(1, 10):
#     print(f'2 * {x} = {2*x}')
# print('\n')


# #소수 판단 문제 (시도1)
# testNum = 25
# for i in range(2, testNum):
#     prime = True
#     if (testNum % i) == 0:
#         prime = False
#         print(f'{testNum} is not prime Number')
#         break
#     if prime:
#         print(f'{testNum} is prime Number')

# #소수 판단 문제 (시도2)
# testnum = 25
# for i in range(2, testnum):
#     if (testnum % i) == 0:
#         print(f'{testnum} is not Prime number')
#         break
#     else:
#         print(f'{testnum} is Prime number')

# #input
# s = input('이름을 입력하세요:')
# print('당신의 이름은 ' + s + '이군요')

#소수 판단 문제 (정답2)
def prime_test(testnum):
    for i in range(2, testnum):
        if testnum % i == 0:
            return print(f'{testnum} is not Prime number')
    return print(f'{testnum} is Prime number')

print(prime_test(23))

#소수 판단 문제 (정답)
testNum = 13
for i in range(2, testNum):
    if (testNum % i) == 0:
        print(f'{testNum} is not prime Number')
        break
else:
    print(f'{testNum} is prime Number')


# #100안에 몇개의 소수가 있나요(시도1)
# prime = []
# for i in range(1, 101):
#     if i % (range(1, i)) == 0:
#         continue
#     else:
#         prime.append(i)
#         continue
# print(prime)

# #continue와 break의 차이
# for i in range(1, 10):
#     if i == 2:
#         continue
#     print(i)
#
# for i in range(1, 10):
#     if i == 2:
#         break
#     print(i)

# #100안에 몇개의 소수가 있나요(시도2)
# prime = [1]
# for i in range(2, 101):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#         else:
#             prime.append(i)
#             break
# print(prime)

#100안에 몇개의 소수가 있나요(정답)
prime = []
for i in range(2, 101):
    pri = True
    for j in range(2, i):
        if i % j == 0:
            pri = False
            break
    if pri:
        prime.append(i)
print(prime)
print(f'1부터 100까지 소수는 {len(prime)}개 입니다.')

#.append 사용
c = [1, 2, 3]
c.append(4)
print(c)


# #과제: testNum2 = 12
# while(1):
#     testNum2 = input()
#     if(testNum2.indigit()):
#         break
#
# testNum2 = int(testNum2)
# print('\n')