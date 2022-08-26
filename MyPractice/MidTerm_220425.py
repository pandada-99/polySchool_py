# sub = "인공지능 기초프로그래밍"
# print(f'오늘 수업은 {sub} 입니다.')
# print("")
#
# front = "Life is too Short"
# rear = "So we need Python"
# result = front + "!!! " + rear
# print(f'{result}')
# print("")
#
# str = "python"
# print(str[0]+str[2])
# print("")
#
# license_plate = "12가 1234"
# print(license_plate[4:])
# print("")
#
# phone_num = "010-1234-5678"
# phone_num1 = phone_num.replace('-', ' ')
# print(phone_num1)
# print("")
#
# str = "ai engineering"
# str1 = str.upper()
# print(str1)
# print("")
#
# lang_1 = ["C", "C++", "JAVA"]
# lang_2 = ['python', 'Perl', 'SQL']
# langs = lang_1 + lang_2
# print(langs)
# print("")
#
# list_1 = [30, 3, ["study", "bed", "game"], "1층", "3억"]
# num_rooms = list_1[1]
# favorite_room = list_1[2][2]
# print(f'{num_rooms}개의 방이 있고, 내가 좋아하는 장소는 {favorite_room} 방입니다.')
# print("")
#
# ice = {'메로나': 1000, '폴로포': 1200, '죠스바': 1000}
# print("메로나 가격:", ice['메로나'])
# print(ice.values())
# price = ice.values()
# price = list(price)
# print(price)
# total = price[0] + price[1] + price[2]
# print(total)
# print("")
#
# s1 = set([1, 2, 2, 3, 4, 4, 5])
# s2 = set([2, 3, 5])
# print(s1 & s2) #교집합
# print(s1 | s2) #합집합
# print(s1 - s2) #차집합
#
# t2 = (3, 4)
# t3 = t2*3
# print(t3)
# print("")

# # pop 함수를 구현
# input_list = [1, 2, 3, 4, 5, 6]
#
# def impl_pop(index = -1) :
#     if index >= len(input_list):
#         return -1
#     else:
#         pop_num = input_list[index]
#         input_list.remove(pop_num)
#         return pop_num, input_list
#
# # def impl_pop() :
# #     pop_num = input_list[len(input_list)-1]
# #     input_list.remove(pop_num)
# #     return pop_num, input_list
#
# print(impl_pop())
# print(impl_pop(2))
# print("-"*100)

# split 함수를 구현
str_test = "abc def   ghij klmn"
def str_split(input_str):
    rtn_list = []
    # " " (공백) 문자를 카운팅하는 방법으로 문제를 접근
    cnt = input_str.count((" "))
    # print(cnt)
    for i in range(cnt):
        # find: 해당되는 문자의 index 값을 반환하는 내장함수
        cmp_value = input_str[:input_str.find((" "))]
        # print(cmp_value)
        if cmp_value and cmp_value != " ":
            rtn_list.append(cmp_value)
        input_str = input_str[input_str.find((" ")) + 1:]
        # print(input_str)
    rtn_list.append(input_str)
    return rtn_list

print(str_split(str_test))

# impl_pop(): 제일 마지막 값이 나오기를 기대
# impl_pop(index): 특정 인덱스에 해당하는 원소 값 반환
# 현재 python_class_ex.py 파일에서 제일 함수내에 있지 않는 변수는 전역변수
# input_list는 전역변수이고, 다른 함수에서 모두 접근가능하다
# global: global을 명시하지 않으면 함수내에서 Read는 되지만 Write(수정, 해당변수의 내용을 조작)은 불가능

input_list = [1, 2, 3, 5, 6, 9]

def impl_pop(index=-1):
    global input_list
    if (index >= len(input_list)):
        return -1
    if (index == -1):
        rtn_value = input_list[index]
        input_list = input_list[:-1]
    elif (index == 0):
        rtn_value = input_list[index]
        input_list = input_list[index+1:]
    else:
        rtn_value = input_list[index]
        input_list = input_list[:index] + input_list[index + 1:]

    return rtn_value, input_list

print(impl_pop())
print(impl_pop(2))