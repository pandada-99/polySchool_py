# 220509 AI기초프로그래밍(신교수님)

# # index error와 zero division이 발생하는 코드가 있는 함수하나 작성
# def proc_error():
#     try:
#         f = open("temp.txt", "r")
#         b = 4 / 0
#         a = [1, 2]
#         print(a[3]) # list index out of range
#     # except:
#     #     print("Error가 발생할 거 같은데?")
#     except IndexError:
#         # class IndexError(Exception):
#         #     def __str__(self):
#         #         return "list index out of range"
#         # print("list index out of range")
#         print("out of range for list a")
#     except ZeroDivisionError:
#         print("Can't Divide by Zero")
#     except FileNotFoundError as e:
#         print(e)
#     # finally:
#         # f.close()

# proc_error()


# # 나이를 입력받는 함수
# # Django Framwork, Flask가 됐던, input text form에 나이를 입력받는다.
# def input_age():
#     # input: 반환형이 문자열 ==> int(정수형)으로 casting
#     while True:
#         try:
#             age = int(input("나이를 입력하세요(숫자만): "))
#             if (age > 100):
#                 print("100살까지만 입력가능")
#             else:
#                 return age
#                 break
#         # except ValueError as e:
#         #     print(e)
#         except ValueError:
#             print("다시 입력해주세요! 나이는 숫자만 입력 가능합니다.")
#
# print(input_age())


# 자기자신만의 예외클래스 작성
# 내장되어 있는 예외클래스가 아니라 직접 작성한 예외처리 코드로 에러를 처리하고 싶을때.
# Exception 클래스를 상속받아 생성가능
class MyError(Exception):
    # pass
    def __str__(self):
        return "허용되지 않는 별명입니다."

# 별명을 출력하는 함수에서 "바보"가 들어오면 작성한 MyError 예외 클래스 호출
# 강제로 에러 발생시키는 방법: raise를 사용
# 1. raise MyError를 통해 비정상 종료 (어떤 에러가 나왔는지는 에러에 명시됨)
def say_nick(nick):
    if nick == "바보":
        raise MyError
    print(nick)
# 2. 비정상적인 종료보다는 Try, Except를 이용해서 정상종료
try:
    say_nick("천재")
    say_nick("바보")
except MyError as e:
    # print("허용되지 않는 별명입니다.")
    print(e)
# 3. MyError as e를 통해서 정해진 에러 msg를 출력하고자 할때.
# __str__

# 함수의 입력인자, (bool, list): bool이 true일때는 리스트 출력, 아니면 정해놓은 Error 발생
class NotAccessList(Exception):
    def __str__(self):
        return "List에 접근 권한이 없습니다."

def list_access(in_bool, in_list):
    if in_bool:
        print(in_list[:]) # print(in_list)
    else:
        raise NotAccessList

try:
    list_access(1, [1, 2, 3, 4])
    list_access(0, [1, 2, 3, 4])
except NotAccessList as e:
    print(e)


# filter, map, zip

# 리스트를 입력받아 양수만 리턴하는 함수(positive)
# 중첩 리스트 제외. (ex: [1, 2, [1, 2, -3], 33] ==> x)
def rtn_positive(in_list):
    rtn_list = []
    for i in in_list:
        if i > 0:
            rtn_list.append(i)
    return  rtn_list
print(rtn_positive([1, -1, 2, -2, 3, -3]))

# filter
# filter에서 사용할 양수만 반환하는 함수를 작성할 경우
def func_positive(x):
    return x > 0
# filter(f, interable한 자료형의 변수)
# 함수의 반환 값이 참인 것만 묶어서 반환
print(list(filter(func_positive, [7, 2, -5, 3, -6, 8, -9, 0])))
print(list(filter(lambda x: x>0, [7, 2, -5, 3, -6, 8, -9, 0])))
# 예상 결과값: 확인 필요
print(list(filter(lambda x: x*2, [7, 2, -5, 3, -6, 8, -9, 0])))

# 파이썬에서 가장 많이 사용하는 형태: 리스트 내포
# list comprehension: 리스트안에 제어문을 넣어서 원하는 결과값을 리스트형태로 얻고자 할때
positive_value = [value for value in [7, 2, -5, 3, -6, 8, -9, 0] if value > 0]
print(positive_value)


# map
# map: 입력리스트를 *2해서 반환하는 함수를 적용
def two_times(x): return x*2
in_list = [1, 2 ,3, 4, 5]
print(list(map(two_times, in_list)))

# 리스트 내표 형태로 만들기
twotimes_list = [value * 2 for value in in_list]
print(twotimes_list)

# zip: 동일한 개수의 iterable한 순서가 있는 객체에서 동일한 index끼리 묶는것
List_1 = [1, 2, 3]
List_2 = [2, 4, 5]
List_3 = list(zip(List_1, List_2))
print(List_3)


# isinstance(object, class): object가 class의 인스턴스이냐?
class Person:
    pass
class Student(Person):
    pass
class Male:
    pass

a = Person()
b = Student()
c = Male()
print(isinstance(a, Person))
print(isinstance(b, Person))
print(isinstance(b, Student))
print(isinstance(c, Person))

