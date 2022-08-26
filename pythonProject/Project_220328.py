# Dictionary 실습
a = {
    'name': ['김근형', '정경임', '이은주', '심우석', '이은정'],
    'ID': [210100, 210101, 210102, 210103, 210104]
}
list_tam = ['name', 'ID']
print(a)

dict_keys = a.keys()
for i in a.keys():
    print(i)
for i in list_tam:
    print(i)

# list 형 변환 (형 변환: 내가 원하는 자료형으로 변경)
dict_list = list(a.keys()) #dist_list = ['name', 'ID']
#재가공하고 싶을때 형변환 후 사용
dict_list.append('phone_number')
print(dict_list, dict_list[0])

# 형 변환
b = "123"
c = int(b) #문자열 "123"을 정수형 123으로 변환 후 c 변수에 바인딩
print(type(b), type(c), b, c)

print(a.values(), type(a.values()))
print(a.items(), type(a.items()))

# dictionary에 데이터 추가 (phone_number이라는 key값에 전화번호 vlaue)
a['phone_number'] = ['010-xxxx-xxxx']
print(a)
b = a
copy_a = a.copy()
print(copy_a)
print(id(a), id(b), id(copy_a))
# a를 수정하면 b에도 영향을 준다, but copy는 새로운 공간을 할당한 것이기 때문에 영향을 받지 않는다.
a.clear()
print(a, b, copy_a)

# in 함수 (a라는 dictionary에 ~~의 key값이 있니?)
print('name' in a, 'addr' in a, 'name' in copy_a, 'addr' in copy_a)
# get 함수
print(a.get('name'), a.get('addr'))
print(a. get('addr', 'Default'))
# print(a['name']) #오류남

# 집합 자료형
# set(), 괄호 안에 list 형태로 작성
s1 = set([3, 1, 2, 4])
list_a = [3, 1, 2, 4]
s2 = set("HELLO")
#s1, s2: 중복이 없으며, 순서가 없다.
print(s1, list_a, s2)
# set 자료형은 access가 불가능하고, 하고싶은 경우 다른 자료형으로 변환해야함.
s1_tuple = tuple(s1)
print(type(s1_tuple), s1_tuple, s1_tuple[0], s1_tuple[1])

# 교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5])
s2 = set([2, 3, 5, 6])
print(f'교집합={s1.intersection(s2)},', f'합집합={s1.union(s2)},', f'차집합={s1.difference(s2)}')

# bool 자료형
a = True
b = False
print(type(a), type(b))
print(f'1과 1은 같나요? {1 == 1}, 1과 2는 같나요? {1 == 2}, 1은 2보다 작나요? {1 < 2}')

# bool 문자열일 경우, 문자열이 하나라도 있으면 True, 아니면 False
# str_t = "" 될때까지 하나씩 찍어보고, False가 되면 while문에서 break;
str_t = "Hello"
idx = 0
while str_t:
    print(idx, len(str_t), str_t)
    idx += 1
    str_t = str_t[:len(str_t) - idx]

# 변수
a, b = 1, 'python'
print(a, b)

a = [1, 2, 3]
b = a
# 리스트 1,2,3의 객체를 생성하고 객체의 주소값을 a에 Binding.
# b = a (a가 가리키고 있는 메모리의 주소를 b도 같이 가리키는 것)
print(a, b, a is b, id(a), id(b))
a[2] = ['1', '2']
print(a, b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a, b, a is b, id(a), id(b))

# 복사: a.copy() / b = a (주소값을 공유하는 것, 복사개념이 x)
a = [1, 2, 3]
b = a[:] # b = a 하고는 다름, 리스트를 Slicing해서 변수에 assign할 경우 새로운 객체를 생성하고 b는 새로 생성된 객체의 주소를 참조.
print(a, b, a is b, id(a), id(b))

c = a.copy() # 새로운 객체를 생성한 후, c는 새로 생성된 객체의 주소를 참조.
print(a, c, a is c, id(a), id(c))


# 220404 AI기초 프로그래밍

# if 문
money = 3000
if money > 3000:
    print("Take Taxi")
else:
    print("Take Bus")

sum_var = 1 #(sum_var이 0이 되면 (not sum_var)이 True가 되면서 print 실행: 0은 False니까 (not 0)은 True가 된다)
if (not sum_var):
    print(sum_var)

card = True
if money > 3000 or card:
    print("Take Taxi")
else:
    pass

# in: for 문에 많이 사용됨
# if 문에서도 종종 사용됨(~가 있니?)
list_var = [1, 2, 3, 4, 5]
if 8 in list_var: print("8 is in the list")
else: print("Can't find input number")

# if-else statement
score = 20
if score >= 60:
    message = "Success"
else:
    message = "Failure"
print(message)
# if-else statement 를 한줄로 표현
message = "Success" if score >= 60 else "Failure"
print(message)

# if 문 (연산자)
a = 3
b = 5
if a>2 and b>10: print("ok")
else: print("not ok")
if a>2 or b>10: print("ok")
else: print("not ok")

# while 문
# prompt = """
# 1. ADD
# 2. DEL
# 3. LIST
# 4. QUIT
# Enter number:
# """
# number = 0
# while number < 4:
#     print(prompt)
#     number = int(input())

# 커피자판기
# coffee = 3
# while True: #무한루프 (Break Statement로 빠져나가야함)
#     money = int(input("Insert Money: "))
#     if not coffee:
#         print("coffee가 없습니다.")
#         break
#
#     if money == 300:
#         print("coffee 한잔 나왔습니다.")
#         coffee -= 1
#     elif money > 300:
#         print(f'{money-300}원 반환, coffee가 한잔 나왔습니다.')
#         coffee -= 1
#     else:
#         print(f'{money}원 반환, 돈이 모자랍니다.')

# for 문
a = [(1, 3), (2, 4), (3, 5)]
for (f, r) in a:
    print(f + r)

# 점수가 60점 이상인 학생에 대해 합격 여부
marks= [90, 20, 67, 45, 80]
number = 0 # 몇 번째 학생인지 표현
for points in marks:
    number += 1
    if points < 60:
        print(f'{number}번 학생은 불합격입니다.')
    else:
        print(f'{number}번 학생은 합격입니다.')

# Range
# for idx in range(0, 10) idx: 0, 1, 2,......9
# for idx in range(0, 10 ,2) idx: 0, 2, 4, 6, 8 / idx를 2씩 증가하겠다.
for idx in range(0, 10, 2):
    print(idx, end=" ")

print("")

a = [1, 2, 3, 4, 5]
result = [] # 빈 list 생성 (선언)
for num in a:
    result.append(num*3)
print(result)
# 리스트 내포 형식으로 변경
result =[num*3 for num in a]
print(result)
result =[num*3 for num in a if num % 2 == 0]
print(result)

# result.append(구구단 for 문에서 나온 결과를 하나씩 append)
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result, type(result))

# 커피자판기 심화 문제
# 풀긴풀었는데.... 자판기 같지 않아서 실패(자판기는 몇잔 먹을거냐고 물어보지 않는다.)
# coffee = 3
# while True: #무한루프 (Break Statement로 빠져나가야함)
#     money = int(input("Insert Money: "))
#     if not coffee:
#         print("coffee가 없습니다.")
#         break
#
#     if money == 300:
#         print("coffee 한잔 나왔습니다.")
#         coffee -= 1
#     elif money > 300:
#         add = int(input("coffee 몇잔 주문하시나요?: "))
#         coffee = coffee - add
#         money = money - (add*300)
#         if money >= 0 and coffee >= 0:
#             print(f'{money}원 반환, coffee가 {add}잔 나왔습니다.')
#         else:
#             print("오류 발생. 다시 시도해 주세요.")
#             break
#     else:
#         print(f'{money}원 반환, 돈이 모자랍니다.')

# 자판기처럼 한잔 나오고 어떻할껀지 표현
menucost = {'밀크커피': 200, '블랙커피': 200, '우유': 100, '율무차': 300, '포도주스': 400, '반환': 1}
menucount = {'밀크커피': 5, '블랙커피': 5, '우유': 3, '율무차': 2, '포도주스': 2, '반환': 0}

while True:
    money = int(input("돈을 넣어주세요: "))

    while money >= 100:
        if money >= 100:
            menu = str(input("'밀크커피', '블랙커피', '우유', '율무차', '포도주스', '반환' 중에 골라주세요."))
            if menucount[menu] > 0:
                if money < menucost[menu]: # 잔액이 메뉴최소금액보다 낮을때 주문실행x
                    print(f'{money}원 반환합니다., 금액이 부족합니다.')
                    break
                else:
                    money = money - menucost[menu]
                    menucount[menu] = menucount[menu] - 1
                    print(f"{menu}가 한잔 나왔습니다. 잔액은 {money}원입니다. {menu}는 {menucount[menu]}개 남았습니다")
                    continue
            elif menucost[menu] == 1:
                print(f"주문취소하였습니다. {money}원 반환합니다.")
                break
            elif menucount[menu] <= 0:
                print(f'{money}원 반환합니다.', "물량이 소진되었습니다.")
                break
        else:
            print(f'{money}원 반환합니다., 금액이 부족합니다.')
            break
    else:
        print(f'{money}원 반환합니다., 금액이 부족합니다.')
        break