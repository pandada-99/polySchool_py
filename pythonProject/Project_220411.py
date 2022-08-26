# 220411 AI기초프로그래밍(신교수님)
a = 3
b = 4
print(a+b)
print(a-b)

# 함수로 만들기
# 파라미터(numl, num2) 이름은 마음대로 지정하면 됨 (단, 의미 있는 이름으로)
def add(numl, num2):
    return numl + num2

def sub(numl, num2):
    return numl - num2

# 함수를 사용하기 위해서는 함수를 호출해야 함.
result_add = add(a, b)
result_sub = sub(a, b)
print(result_add, result_sub)

# 함수 종류는 입출력에 따라 4가지가 존재함.

# 입력이 있고 출력도 있는것. (위의 def add, def sub)

# 입력x, 출력만 있는 함수 작성. (출력이 있다는 것은 return)
def add_5_6(): # 입력 파라미터가 없더라도 반드시 괄호는 해줘야 함.
    return 5+6
# 1~100까지 더하는 함수 작성. (입력x, 출력은 100까지 누적된 값을 return)
def add_1_100():
    sum = 0
    for i in range(101):
        sum += i
    return sum
print(add_1_100())

# 입력은 있지만 Return이 없는 함수 작성.
def mul(num1, num2):
    print(num1*num2)
# 함수 호출하기.
rtn_val = mul(11, 22)
print(f'return value is {rtn_val}')

# 입력과 출력이 모두 없는 함수 작성.
def inputoutputx():
    print("xxxx")
# 함수 호출하기.
inputoutputx()

# 함수 호출시에 다양한 방법으로 호출해보기.
mul(num1=2, num2=3)
mul(7,5)
mul(num2=5, num1=8)
aa = 4
bb = 6
mul(aa, bb)

# 함수 호출 할때
# (x)print(def()) = return값을 가져오세요
# (x)def() = 함수를 가져오세요(함수 내부의 내용을 가져옴. 즉, 함수 내부의 print문이 가져와짐)
# def() = 함수 결과값이 들어감!!
print()
def a():
    print("a")
#호출
a()


def d():
    return "b"
#호출
d()


def c():
    return "c"
#호출
print(c())


def d():
    print("d")
#호출
print(d())