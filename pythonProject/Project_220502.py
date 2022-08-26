# 220502 AI기초프로그래밍(신교수님)

# class를 만들기 위해서는 class 클래스이름:
# 상속의 경우 class 클래스이름(상속받을 클래스명):

class FourCalc:
    variable = 0
    # set_data라는 메서드 구현 (2개의 객체 변수를 셋팅)
    # 기본적으로 사칙연산을 위해 2개의 값이 필요
    def set_data(self, first, second):
        self.first = first
        self.second = second
        FourCalc.variable = self.first

    # 생성자: 객체를 생성할 때 Default로 무엇인가를 하고 싶을때.
    # __init__으로 정해져있음
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 더하기, 빼기, 곱하기, 나누기 메서드 작성
    def add(self):
        return self.first + self.second
    def sub(self):
        return self.first - self.second
    def mul(self):
        return self.first * self.second
    def div(self):
        return self.first / self.second

a = FourCalc(10,5)
print(a.add())
print(a.sub())
print(a.mul())
print(a.div())
print()

b = FourCalc(20, 4)
print(b.add())
print(b.sub())
print(b.mul())
print(b.div())
print()


# FourCalc 클래스를 상속받아 MoreCalc 클래스를 하나 만들자.
class MoreCalc(FourCalc):
    def __init__(self, first, second, third=1):
        # 객체를 생성할 때,
        # a = MoreCalc(1, 2, 3)
        # a = MoreCalc(1, 2) => Default third 값이 있어서 ok
        # super(): 부모클래스에 있는 메서드 그대로 사용 가능함
        # self.first = first
        # self.second = second
        super().__init__(first, second)
        self.third = third

    # 상속을 받았기 때문에, 사칙연산이 모두 가능
    # 새로운 메서드 추가하기
    def pow(self):
        return self.first ** self.second

    # overriding: 상속 받은 클래스의 메서드를 수정할 수 있음.
    def add(self):
        return super().add() + self.third

    # div 매서드를 오버라이딩 해보자.
    # 기존 div에서는 ZeroDivide에 대한 처리가 없었음
    # 오버라이딩하는 메서드에서는 0으로 나눌 경우, 0값을 리턴하는 것으로 작성
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

moreCalc_0 = MoreCalc(4,0,5)
print(moreCalc_0.add())
print(moreCalc_0.div())
print()