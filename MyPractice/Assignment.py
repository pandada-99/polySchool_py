# 정수형, 실수형, 문자열 및 '리스트 내에 리스트'등을 포함하여 자신을 소개하는 리스트를 만들고, 리스트 인덱싱과 슬라이싱 기법 등을 이용하여 자기 소개하는 것 표현해보기
my = {'name':'이은정', 'birth':'970719'}
area = ['울산', ['우정동', '신정동'], '경산', ['중방동', '압량면'], '대구', ['평리동']]
body = [154, -4.5]
str1 = '안녕하세요. '
str2 = '저를 소개합니다.'
str3 = '********'
str4 = '영화감상전시관람산책'

print((str3*11) + '\n' + str1 + str2 + '\n제 이름은 ' + my['name'] + '입니다. 저의 생년월일은 ' + my['birth'] + '입니다.')
print('저는 %s에서 태어나 %s에서 자랐습니다.' % (area[0], area[1][0]))
print(f'저는 {area[2]}의 {area[3]}에서 대학생활을 보냈습니다.\n지금은 {area[4]}에서 살고있습니다.\n{str3*11}')
print(f'제 키는 {body[0]}cm 이고, {body[0]+9}cm까지 크면 좋겠습니다. 시력은 {body[1]}인데 {body[1]+5.5}가 되면 정말 행복할것 같아요.')
print(f'제 취미는 {str4[:4]}과 {str4[4:8]}이고 {str4[8:]}도 좋아해요.')
print((str3*11) + '\n')

# 문자열 변수에서 특정 인덱싱으로 접근 후 문자열을 변경할 수 있는가? 답변 및 가능한 방법 코드 작성 및 제출,  mutable, immutable 자료형 정리해보기
str1 = 'My favorite fruit is banana.'

# replace 함수 이용하여 문자열 치환하기
print(str1.replace("banana", "strawberry")) # banana를 strawberry로 치환
print(str1) # str1은 아직 banana임

# 문자열을 list로 만들어 인덱싱으로 특정 단어 수정하기
str_list = str1.split(" ") # " "을 기준으로 문자열을 리스트화
str_list[4] = "strawberry" # 리스트 인덱싱을 통해 4번 인덱싱 변경
str2 = " ".join(str_list) # str2 변수에 " "을 추가하여 리스트를 문자열로 변경
print(str2)
print('\n')

# immutable 정리
# int, float
print("'int' immutable 증명")
a = 1
b = a
print(a, b)
print(id(a), id(b))
b += 5
print(a, b)
print(id(a), id(b)) # 변수b를 변경해도 변수a는 변하지않는다. 변수b는 새로운 주소가 생성됨.
print('\n')

# str
print("'str' immutable 증명")
a = 'hello'
b = a
print(a, b)
print(id(a), id(b))
b += 'python'
print(a, b)
print(id(a), id(b)) # 변수b를 변경해도 변수a는 변하지않는다. 변수b는 새로운 주소가 생성됨.
print('\n')

# Tuple
print("'튜플' immutable 증명")
a = (1, 2)
b = a
print(a, b)
print(id(a), id(b))
# b[1] = 'c' # 인덱싱하여 변경 불가능 오류발생
b += (3, 4) # +연산으로 튜플 추가
print(a, b)
print(id(a), id(b)) # 변수b는 새로운 튜플이 생성된것.
print('\n')

#mutable 정리
# List
print("'리스트' mutable 증명")
a = [1, 2, 3]
b = a
print(a, b)
print(id(a), id(b))
b.append(4)
print(a, b)
print(id(a), id(b)) # 변수b를 변경하면 변수a도 같이 변한다. 주소는 동일하게 요소만 변경 가능.
print('\n')

# Dictionary
print("'딕셔너리' mutable 증명")
a = {1:'a', 2:'b', 3:'c'}
b = a
print(a, b)
print(id(a), id(b))
b[4] = 'd'
print(a, b)
print(id(a), id(b)) # 변수b를 변경하면 변수a도 같이 변한다. 주소는 동일하게 요소만 변경 가능.
print('\n')

# 추가 ('int'는 같은 값이라면 같은 주소를 참조함, 'list'는 같은 값이라도 각자 다른 주소 생성)
int1 = 86
int2 = 86
int3 = 86
int4 = 86
print(id(int1), id(int2), id(int3), id(int4))

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 3]
list4 = [1, 2, 3]
print(id(list1), id(list2), id(list3), id(list4))
print('\n')


# List에서 append/insert/extend 차이점, remove/pop 차이점, 각각 예제 코드 작성 및 설명
# 'append(x)' 리스트의 맨 마지막에 x추가
a = [1, 2, 3, 4, 5]
a.append(6)
print(a) # 리스트의 맨 마지막에 6추가
a.append(['a', 'b']) # 리스트 안에 리스트 추가 가능
print(a)

# 'insert(a, b)' 리스트의 a위치에 b삽입
a = [1, 2, 3, 4, 5]
a.insert(2, 'a') # 인덱스 2위치에 'a'삽입
print(a)

# 'extend(x)' 원래 리스트에 x리스트를 더함 (x에는 리스트만 올수 있음)
a = [1, 2, 3, 4, 5]
a.extend([4, 5, 6, 7]) # a리스트에 [4, 5, 6, 7]리스트 더하기
print(a)

# 'remove(x)' 리스트에서 첫 번째로 나오는 x를 삭제
a = [1, 2, 3, 4, 5, 4, 6, 7, 4]
a.remove(4)
print(a) # 첫번째로 나온 4삭제
a.remove(4)
print(a) # 첫번째 4가 지워진 후, 그 다음 첫번째로 나온 4삭제

# 'pop()' 리스트의 맨 마지막 요소를 돌려주고 그 요소 삭제 / 'pop(x)' 리스트의 x번째 요소를 돌려주고 그 요소 삭제
a = [1, 2, 3, 4, 5, 6, 7, 4]
a.pop() # 리스트의 마지막 요소인 4삭제
print(a)
a.pop(3) # 리스트의 인덱스 3위치인 4삭제
print(a)

print('\n')


# 기존 파싱 코드에서 자료형 list와 문자열 관련 함수 split()을 이용하여 동일한 결과 도출하기
str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250 vehicle 0 0 50 50 vehicle 0 0 50 50 vehicle 50 50 250 250"

test_str = str_txt.split(" ") # split 함수로 " "을 기준으로 list로 만듬

r = len(test_str)
for i in range(3,r,5): # 인덱스 3에서 list의 끝까지 5씩 늘어감 (넓이 부분)
    if int(test_str[i]) >= 100: # 인덱스 i번째 요소를 int로 바꿔서 비교함 (넓이가 100보다 클 경우)
        test_str[i-3] = 'truck' # 이름이 적힌 인덱스 부분을 truck으로 변경

a = " ".join(test_str) # join 함수로 " "을 넣어 다시 문자열로 바꿈
print(a)
print('\n')


# 기존 파싱코드에서 데이터를 어떻게 만들면 더욱 효율적으로 처리할 수 있는지 -Data 형식 변경 및 추가, 코드 작성 결과 확인(조건을 동일함, 크기가 100보다 크면 vehicle에서 truck으로)
# 교수님.....문자열을 리스트로 바꾸지 않고 특정 문자열만 변경하는 방법을 아직 찾지 못했습니다...죄송합니다.....


#소수 판단 알고리즘 수정하기
testNum = 13
for i in range(2, testNum):
    if (testNum % i) == 0:
        print(f'{testNum} is not prime Number')
        break
else:
    print(f'{testNum} is prime Number')


