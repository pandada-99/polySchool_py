# 220418 AI기초프로그래밍(신교수님)

# return값을 튜플 형태로 반환
def add_and_mul(a, b):
    return (a+b), (a*b)
print("result=%d, %d" % add_and_mul(2, 4))
a = add_and_mul(2, 4)
print(f'result={a}')
print(f'result={a[0]}, {a[1]}')
print(add_and_mul(2, 4))
print()

# *args: 인자가 몇개 올지 모를때, 함수의 인자(파라미터)를 튜플 형태로 저장
def add_many(*args):
    result = 0 # return 변수 정의
    for i in args: # arge list일 경우, list의 값 자체를 가지고 올 수 있음.
        result += i
    return result

var_list = [1, 2, 3, 4, 5, 6]
result = add_many(*var_list)
print(result)
print()

# main 함수
rtn_val = []
# 가변인자를 넘기고 싶을때, (1, 2), (1, 2, 3), (1, 2, 3, 4)...
rtn_val.append(add_many(1, 2, 3))
rtn_val.append(add_many(5, 6))
print(rtn_val)
print()

# *args practice
def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i
        return result
    elif choice == 'mul':
        result = 1
        for i in args:
            result *= i
        return result
    else:
        return print("'add' 또는 'mul'을 입력해주세요.")

print(add_mul('add', 4, 5, 2))
print(add_mul('mul', 5, 2, 3))
print(add_mul('sub', 5,5))
print()

# *kwargs: 인자가 몇개 올지 모를때, 함수의 인자(파라미터)를 딕셔너리 형태로 저장
def myFunc(**kwargs):
    for item in kwargs.items():
        print(item)
    print(kwargs)
myFunc(x=100, y=200, z='abc')
print()

# 딕셔너리 복습
dict_var = {'a': 1, 'b': 3}
print(dict_var.items()) # ==> [('a', 1), ('b', 3)]: 리스트 튜플로 반환
print(dict_var.keys()) # ==> ['a', 'b']: 결과값 자체를 활용하기 위해서는 list(dict_var.keys) 사용
print(dict_var.values()) # ==> [1, 3]
print()

# 함수 매개변수에 초깃값 설정하기
def say_myself(name, age, dept="AI_Engr"):
    print(f'name is {name}')
    print(f'age is {age}')
    print(f'dept is {dept}')
say_myself('이은정', '26')
print()

# 변수의 사용 범위
# 지역 변수: 특정 함수 내에서 사용하는 변수들.
# 전역 변수: 어떤 함수에서도 해당 변수를 호출해서 사용 가능 (공유), 일반적으론 함수 밖에서 정의함
# => python global 예약어를 이용해서 명시적으로 표현
a = 1

def vartest(a):
    a = a + 1
    print(a)

vartest(a)
print(a)
print()

# 변수가 두단어 이상이 합쳐졌다고 할땐, 소문자로 시작, 구분되는 단어가 나오면, 한글자만 대문자로 사용
# varTest, var_test (함수이름, 변수이름도 동일)

local_var = 0 # varTest2 함수로 인해 local_var 값은 변경된 상태
def varTest1(local_var):
    # 93 line의 local_val과 varTest1 함수 내부의 local_var은 다르다.
    local_var = local_var + 1
varTest1(3)
print(local_var)
print()

def varTest2(input):
    global local_var # 함수 밖에 있는 local_var 변수를 함수 내에서도 사용
    local_var = input + 1
varTest2(3)
print(local_var)
print()

def varTest3(input):
    global local_var
    local_var = input * 2
varTest3(3)
print(local_var)
print()

# lambda
add = lambda a, b: a+b
result = add(3, 4)
print(result)

mul = lambda a, b: a*b
print(mul(5+1, 7+1))

test = lambda a, b: (10*a)+(5*b)
print(test(5, 5))
print()