# 1번 문제
def solution_1(shirt_size):
    a = [0, 0, 0, 0, 0, 0]
    for i in range(len(shirt_size)):
        if shirt_size[i] == "XS":
            a[0] = a[0] +1
        elif shirt_size[i] == "S":
            a[1] = a[1] + 1
        elif shirt_size[i] == "M":
            a[2] = a[2] + 1
        elif shirt_size[i] == "L":
            a[3] = a[3] + 1
        elif shirt_size[i] == "XL":
            a[4] = a[4] + 1
        elif shirt_size[i] == "XXL":
            a[5] = a[5] + 1
    return a

# 2번 문제
def solution_2(arr):
    arr_reverse = [0] * len(arr)
    for i in range(len(arr)):
        arr_reverse[i] = arr[len(arr)-1-i]
    return arr_reverse

# 3번 문제
def solution_3(n):
    sum = 0
    for i in range(1, n+1):
        a = (3*i)-2
        sum = sum + a
    return sum

# 4번 문제
def solution_4(orisinal):
    count = count_list(orisinal, orisinal[0])
    max = count
    min = count

    for i in range(1, len(orisinal)):
        a = count_list(orisinal, orisinal[i])
        if a > max :
            max = a
        elif a < min :
            min = a
    result = int(max / min)
    return result

# 4번 문제 (count 함수 사용)
def solution_4_1(orisinal):
    count = orisinal.count(orisinal[0])
    max = count
    min = count

    for i in range(1, len(orisinal)):
        a = orisinal.count(orisinal[i])
        if a > max:
            max = a
        elif a < min:
            min = a
    result = int(max / min)
    return result

def count_list(list, a):
    count_num = 0
    for i in range(len(list)):
        if list[i] == a:
            count_num = count_num + 1
    return count_num


if __name__ == '__main__':
    # 1번 문제 테스트
    param1 = ["XS", "XS", "M", "XS", "XXL", "L"]
    ans1 = solution_1(param1)
    print(ans1)

    # 2번 문제 테스트
    param2 = [6, 85, 9, 72, 98, 45, 12, -99]
    ans2 = solution_2(param2)
    print(ans2)

    # 3번 문제 테스트
    param3 = 5
    ans3 = solution_3(param3)
    print(ans3)

    # 4번 문제 테스트
    param4 = [1, 2, 3, 3, 3, 3, 2, 3, 2, 3]
    ans4 = solution_4(param4)
    print(f'{ans4}배 입니다.')

    # 4번 문제 테스트 (count 함수 사용)
    ans4_1 = solution_4_1(param4)
    print(f'{ans4_1}배 입니다.')
