# #.join()
# a = ['a', 'b', 'c', 'd']
# print("+".join(a))

# #문자열 +: 연결, concatenation
# #문자열 *: 반복 연산
# str1 = "Hi Everyone"
# str2 = "My name is jsshin"
# str3 = "************" #Comment Block
# print(f'{str3 * 10}\n{str1 + " " + str2},\n'
#       f'This is Block is comment block\n'
#       f'{str3 * 10}')
# print(len(str2))
# print(str2[-6])
# lenStr = len(str2)
# str2 = str2[:-6] + "J" + str2[lenStr-5:]
# str2 = str2[:-6] + "J" + str2[-5:]
# print(str2)

# #문자열 실습
# Str4 = '20220308Sunny'
# print('Today weather is ' + Str4[8:] + ' and ' + 'date is ' + Str4[:8])


# a = "Life is too short, You need Python"
# Print(a[0])
# print(a[0:5])

# str = "20210908Sunny"
# print('Today weather is ' + '\"' + str[8:] + '\"')


# a = 10
# b = 10
# print(id(a), id(b), id(a+b))


# print("%16s is ha" % 'hi')


# number = 10
# day = "three"
# str1 = "I ate %d apples. \nSo I was sick for %s days." % (number, day)
# print(str1)
# str2 = f"I ate {number} apples. \nSo I was sick for {day} days."
# print(str2)

# str1 = "%4s\n%4s\n%4s\n%4s" % ('a', 'ab', 'abc', 'abcd')
# print(str1)

# str1 = "%-10sjane" % "hi"
# print(str1, len(str1))
# print(f"{3.42134234:0.4f}")
# str2 = f"{3.42134234:10.3f}"
# print(str2, len(str2))


# print("," .join('abcd'))
# a = 'Life is too short'
# print(a.split())


# str1 = """
# Spread out before him that April day was the largest flotilla Communist-ruled China
# 48 ships, dozens of fighter jets, more than 10,000 military personnel."""
#
# cnt_a = str1.count("ships")
# print(cnt_a)
# print(str1.find("jets"), str1.find("h"), str1.index("h"), str1.find("korea"))
# print(str1.upper())
# print(str1.lower())
#
# str1 = "12345"
# print(",".join(str1))
#
# str_list = "Life is too short"
# print(str_list.replace("short", "long"))
# print(str_list)
#
# str_list = str_list.split()
# print(str_list, type(str_list))
#
# str_list = "    ".join(str_list)
# print(str_list, type(str_list))

#과제
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 0 0 50 50 vehicle 0 0 50 50 vehicle 50 50 250 250"

test_str = str_txt.split(" ")

r = len(test_str)
for i in range(3,r,5):
    if int(test_str[i]) >= 100:
        test_str[i-3] = 'truck'

a = " ".join(test_str)
print(a)


# print(str_txt.replace('vehicle 50 50 250 250', 'truck 50 50 250 250'))

# i = "250" in str_txt
#
# if i:
#     print(str_txt.replace('vehicle 50 50 250 250', 'truck 50 50 250 250'))
# else:
#     print("truck가 없습니다")

# print(str_txt.find('vehicle'))
# str_txt2 = (str_txt.split(','))

# import re
# str_txt2 = re.sub("vehicle", "truck", str_txt, 1)
# print(str_txt2)

# str_txt2 = (str_txt.split(','))
# if 'vehicle 50 50 250 250' in str_txt2:
#     str_txt2.replace('vehicle 50 50 250 250', 'truck 50 50 250 250')
# print(str_txt2)

# print(str_txt.replace(str_txt[19:29], 'truck 50'))
# print(str_txt.replace(str_txt[19:26], 'truck')) = print(str_txt.replace('vehicle ', 'truck'))


# list1 = [1, 2, 3, 0.1]
# print(f'{list1} 입니다.')
# #평수, 방 갯수, [방#1, 방#2, 방#3], 층수, 가격
# list2 = [30, 3, ["study", "bad", "game"], "1층", "3억"]
# print(list2)
# list3 = [18, 2, ["bed", "clothes"], "11층", "2억"]
# print(list3)
#
# list4 = []
# list4.append("1")
# list4.append(32)
# print(list4, type(list4[0]), type(list4[1]))

# #list indexing/slicing
# print('Start index of the list=%d' %30 + '%' + f', first date of a list3 = {list4[0]}')
# print(f'Start index of the list=%d%%, first date of a list4 = {list4[0]}' %30)
# print(list2[-3])
# print("1+2=%d" %(list1[0] + list1[1]))
# strhouse = f'My house area is {list3[0]}, there are {len(list3[-3])} rooms and \n' \
#            f'l like the {list3[-3][1]} room!\n' \
#            f'{list3[-2:]} are show in web site!'
# # strhouse = f'My house area is {list3[0]}, there are {len(list3[-3])} rooms and \nl like the {list3[-3][1]} room! \n{list3[-2:]} are show in web site!'
# print(strhouse)



# n1 = int(input("첫 번째 정수를 입력하세요.:"))
# n2 = int(input("두 번째 정수를 입력하세요.:"))
# print(n1 + n2)


# #함수 연습
# def testnum(x,y):
#     if x>y:
#         print('a>b')
#     elif x==y:
#         print('a=b')
#     elif x<y:
#         print('a<b')
# print(testnum(5,2))
# print(testnum(5,5))
# print(testnum(6,9))

# #input함수 연습
# number = input('숫자를 입력하세요: ')
# result = int(number)*5
# form = '당신이 입력한 숫자는 %s이며, 5를 곱한 결과는 %d이다.'
# print(form % (number, result))


# # list add/delete/modify
#
# list_a = [1, "가", "2", 4.2]
#
# print(f'{list_a}', id(list_a))
# #id 값을 한번 체크해보기 (list는 mutable한 자료형)
# #따라서 수정을 하더라도 새로운 객체를 생성하는 것이 아니라 동일한 주소값을 참조.
# list_a[1] = 4
# print(f'{list_a}', id(list_a))
#
# #list + 연산
# list_a = list_a + [5, 6]
# print(f'{list_a}', id(list_a))
#
# #특정 인덱스의 값을 삭제
# del list_a[2]
# print(list_a, id(list_a))
#
# test_list = [1,2,3]
# print(test_list, id(test_list))
# test_list.append([8,5,4,7,10])
# test_list.append('string')
# print(test_list, id(test_list))
# #추가한 리스트를 sort하기 위해서는?
# test_list[3].sort()
#
# #reverse test
# tmp_list = ['a', 'd', 'c']
# tmp_list.reverse()
# print(tmp_list, tmp_list.index('a'))
#
# #list insert, remove 함수 사용
# print("=============================================================\n")
# print(tmp_list)
# tmp_list.insert(0, [1, 2, 3]) #list의 0번째 인덱스에 [1, 2, 3] 리스트를 삽입
# print(tmp_list)
# tmp_list[0].remove(1) #list 안에 1을 삭제
# print(tmp_list)
# #pop, count, extend
# tmp_list.pop() #()안에 아무것도 넣지 않으면, 리스트의 제일 마지막 값을 pop
# print(tmp_list)
# tmp_list.pop(2) #2는 인덱스
# print(tmp_list)
# print(tmp_list, tmp_list.count('c'))


# #딕셔너리 자료형은 {key:value, key10:value10}
# a = {1:"a", 2:"b"}
# #딕셔너리에 추가하고 싶을때, Dict[key] = "Value"
# a[3] = "c"
# print(a)
# a["name"] = ["Shin", "Lee", "Kim", "Kwang"]
# print(a)
#
# del a[1] #a라는 딕셔너리 변수에서 키를 1로 가진 쌍을 삭제한다.
# print(a)
#
# b = {"Dept": ["AI-Engr", "Smart Elect"], "StudentNum": [22, 50]}
# #딕셔너리에 특정 값에 접근할떄는 딕셔너리의 키값으로 접근
# print(b["Dept"], b["StudentNum"])
#
# c = {'1': 'a', '2': 'b', 'c': '3', 'd': '4'}