# 111
# a = input("문자를 입력하세요: ")
# print(a*2)
# 112
# b = input("숫자를 입력하세요: ")
# print(int(b) + 10)
# 113
# number = input("숫자를 입력하세요: ")
# if int(number) % 2 == 0:
#     print("짝수")
# else:
#     print("홀수")
# 114
# number = input("숫자를 입력하세요: ")
# if 255 <= (int(number)+20):
#     print(225)
# else:
#     print(int(number) + 20)
# 115
# number = input("숫자를 입력하세요: ")
# if int(number) < 0:
#     print(0)
# elif int(number) > 225:
#     print(225)
# else:
#     print(int(number) + 20)
# 116
# number = input("시간을 입력하세요(00:00): ")
# if number[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
# 117
# fruit = ["사과", "포도", "홍시"]
# anwser = input("좋아하는 과일을 입력하세요: ")
# if anwser in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# 118
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# stock = input("투자할 종목명을 입력하세요.: ")
# if stock in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")
# 119
# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# anwser = input("좋아하는 계절은? : ")
# if anwser in fruit.keys():
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# 120
# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# anwser = input("좋아하는 과일은? : ")
# if anwser in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")
# 121
# number = input("문자를 입력하세요: ")
# if number.islower():
#     print(number.upper())
# else:
#     print(number.lower())
# 122
# score = input("점수를 입력하세요(0~100): ")
# score = int(score)
# if score > 100:
#     print("점수를 다시 입력하십시오.")
# elif score < 0:
#     print("점수를 다시 입력하십시오.")
# elif score > 80:
#     print("grade is A")
# elif score > 60:
#     print("grade is B")
# elif score > 40:
#     print("grade is C")
# elif score > 20:
#     print("grade is D")
# else:
#     print("grade is E")
# 123
# sum = input("금액을 입력하세요: ")
# sum_list = sum.split()
# number = int(sum_list[0])
# if "달러" in sum_list:
#     print("%d원" % (1167 * number))
# elif "엔" in sum_list:
#     print("%f원" % (1.096 * number))
# elif "유로" in sum_list:
#     print("%d원" % (1268 * number))
# elif "위안" in sum_list:
#     print("%d원" % (171 * number))
# 124
# number1 = int(input("첫번째 숫자를 입력하세요."))
# number2 = int(input("두번째 숫자를 입력하세요."))
# number3 = int(input("세번째 숫자를 입력하세요."))
# max = 0
# list = [number1, number2, number3]
# print(list)
# for a in list:
#     if a > max:
#         max = a
# print(max)
# 125
# number = input("휴대전화 번호 입력(000-0000-0000): ")
# list = number.split("-")
# if list[0] == "011":
#     print("당신은 SKT 사용자입니다.")
# elif list[0] == "016":
#     print("당신은 KT 사용자입니다.")
# elif list[0] == "019":
#     print("당신은 LGU 사용자입니다.")
# else:
#     print("알수없음")
# 126
# address = input("우편번호: ")
# address.split()
# if address[2] == "0":
#     print("강북구")
# elif address[2] == "1":
#     print("강북구")
# elif address[2] == "2":
#     print("강북구")
# elif address[2] == "3":
#     print("도봉구")
# elif address[2] == "4":
#     print("도봉구")
# elif address[2] == "5":
#     print("도봉구")
# else:
#     print("노원구")
# 127
# number = input("주민등록번호(000000-0000000): ")
# a = number.split("-")[1]
# a = int(a)
# if 2000000 <= a < 3000000 or a > 4000000:
#     print("여자")
# else:
#     print("남자")
# 128
# number = input("주민등록번호(000000-0000000): ")
# a = number.split("-")[1]
# if 0 <= int(a[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")
# 129
# number = input("주민등록번호(000000-0000000): ")
# a = number.split("-")
# front_number = (a[0])
# back_number = (a[1])
# i = ((2*int(front_number[0]))+(3*int(front_number[1]))+(4*int(front_number[2]))+(5*int(front_number[3]))+(6*int(front_number[4]))+(7*int(front_number[5]))+
#      (8*int(back_number[0]))+(9*int(back_number[1]))+(2*int(back_number[2]))+(3*int(back_number[3]))+(4*int(back_number[4]))+(5*int(back_number[5])))
# j = i % 11
# if 11-j == int(back_number[-1]):
#     print("유효합니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")
# 130
# import requests
# btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
#
# change = float(btc['max_price']) - float(btc['min_price'])
# if (float(btc['opening_price']) + change) > float(btc['max_price']):
#     print("상승장")
# else:
#     print("하락장")
# 131
# fruit = ['사과', '귤', '수박']
# for a in fruit:
#     print(a)
# 136
# for a in [10, 20, 30]:
#     print(a)
# 137
# for a in range(10, 40, 10):
#     print(a)
# 138
# for a in [10, 20, 30]:
#     print(a)
#     print("-------")
# 139
# print("+++")
# for a in [10, 20, 30]:
#     print(a)
# 140
# for a in [1, 2, 3, 4]:
#     print("-------")
# 141
# list = [100, 200, 300]
# for a in list:
#     print(a + 10)
# 142
# list = ['김밥', '라면', '튀김']
# for 메뉴 in list:
#     print("오늘의 메뉴: " + 메뉴)
# 143
# list = ['SK하이닉스', '삼성전자', 'LG전자']
# for a in list:
#     print(len(a))
# 144
# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a,len(a))
# 145
# for a in 'dog', 'cat', 'parrot':
#     print(a[0])
# 146
# list = [1, 2, 3]
# for a in list:
#     print("3 X",a)
# 147
# list = [1, 2, 3]
# for a in list:
#     print("3 x " + str(a) + " =", 3*a)
# 148
# list = ['가', '나', '다', '라']
# for a in list:
#     if a != '가':
#         print(a)
# for a in list[1:]:
#     print(a)
# 149
# list = ['가', '나', '다', '라']
# for a in list[0::2]:
#     print(a)
# 150
# list = ['가', '나', '다', '라']
# list.reverse()
# for a in list:
#     print(a)
# 151
# list = [3, -20, -3, 44]
# for a in list:
#     if a < 0:
#         print(a)
# 152
# list = [3, 100, 23, 44]
# for a in list:
#     if a % 3 == 0:
#         print(a)
# 153
# list = [13, 21, 12, 14, 30, 18]
# for a in list:
#     if a <20 and a % 3 == 0:
#         print(a)
# 154
# list = ["I", "study", "python", "language", "!"]
# for a in list:
#     if len(a) >= 3:
#         print(a)
# 155
# list = ["A", "b", "c", "D"]
# for a in list:
#     if a.isupper():
#         print(a)
# 156
# list = ["A", "b", "c", "D"]
# for a in list:
#     if a.isupper():
#         pass
#     else:
#         print(a)
# for a in list:
#     if not a.isupper():
#         print(a)
# 157
# list = ['dog', 'cat', 'parrot']
# for a in list:
#     print(a[0].upper() + a[1:])
# 158
# list = ['hello.py', 'ex01.py', 'intro.hwp']
# for a in list:
#     b = a.split('.')
#     print(b[0])
# 159
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for a in list:
#     file = a.split('.')
#     if file[1] == 'h':
#         print('.'.join(file))
#         print(a)
# 160
# list = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for a in list:
#     file = a.split('.')
#     if file[1] == 'h' or file[1] == 'c':
#         print(a)
# 161
# for a in range(0, 100):
#     print(a)
# 162
# for a in range(2002,2051,4):
#     print(a)
# 163
# for a in range(3,31,3):
#     print(a)
# 164
# for a in range(100,0,-1):
#     print(a)
# 165
# for a in range(10):
#     print(a/10)
# 166
# for a in range(1,10):
#     print('3X' + str(a) + ' = ' + str(3*a))
# 167
# for a in range(1,10):
#     if a % 2 != 0:
#         print('3X' + str(a) + ' = ' + str(3*a))
# 168
# b = 0
# for a in range(1,11):
#     b += a
# print(b)
# 169
# b = 0
# for a in range(1,11,2):
#     b += a
# print("합:",b)
# 170
# b = 1
# for a in range(1,11):
#     b = (b*a)
# print(b)
# 171
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(price_list[i])
# 172
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print(i, price_list[i])
# for i, data in enumerate(price_list):
#     print(i, data)
# 173
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list)-1)-i, price_list[i])
# 174
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(90+10*i, price_list[i])
# 175
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)):
#     if i+1 > (len(my_list))-1:
#         break
#     else:
#         print(my_list[i], my_list[i+1])
# 176
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i], my_list[i+1], my_list[i+2])
# 177
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list)-1, 0, -1):
#     print(my_list[i], my_list[i-1])
# 178
# my_list = [100, 200, 400, 800]
# for i in range(len(my_list)-1):
#     print(my_list[i+1]-my_list[i])
# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(len(my_list)-2):
#     average = (my_list[i]+my_list[i+1]+my_list[i+2])/3
#     print(average)
# 180
# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility =[]
# for i in range(len(low_prices)):
#     a = high_prices[i]-low_prices[i]
#     volatility.append(a)
# print(volatility)
# 181
# apart = [['101호, 102호'], ['201호', '202호'], ['301호', '302호']]
# print(apart)
# 182
# stock = [['시가', 100, 200, 300], ['종가', 80, 210, 330]]
# print(stock)
# 183
# stock = {'시가': [100, 200, 300]}, {'종가': [80, 210, 330]}
# print(stock)
# 184
# stock = {'10/10': [80, 110, 70, 90]}, {'10/11': [210, 230, 190, 200]}
# print(stock)
# 185
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         print(str(apart[i][j]) + "호")
# 186
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)-1, -1, -1):
#     for j in range(len(apart[i])):
#         print(str(apart[i][j]) + "호")
# 187
# apart = [ [101, 102], [201, 202], [301, 302] ]
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)-1, -1, -1):
#     for j in range(len(apart[i])-1, -1, -1):
#         print(str(apart[i][j]) + "호")
# 188
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         print(str(apart[i][j]) + "호")
#         print("-"*5)
# 189
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         print(str(apart[i][j]) + "호")
#     print("-"*5)
# 190
# apart = [ [101, 102], [201, 202], [301, 302] ]
# for i in range(len(apart)):
#     for j in range(len(apart[i])):
#         print(str(apart[i][j]) + "호")
# print("-"*5)
# 191
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         price = (data[i][j]*0.00014)+data[i][j]
#         print(price)
# 192
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         price = (data[i][j]*0.00014)+data[i][j]
#         print(price)
#     print("-"*4)
# 193
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         price = (data[i][j]*0.00014)+data[i][j]
#         result.append(price)
# print(result)
# 194
# result = []
# data = [
#     [2000,  3050,  2050,  1980],
#     [7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# for i in range(len(data)):
#     array = []
#     for j in range(len(data[i])):
#         price = (data[i][j]*0.00014)+data[i][j]
#         array.append(price)
#     result.append(array)
# print(result)
# 195
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(1,4):
#         print(ohlc[i][3])
# 196
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(1,4):
#         if ohlc[i][3] > 150:
#             print(ohlc[i][3])
# 197
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(1,4):
#         if ohlc[i][3] >= ohlc[i][0]:
#             print(ohlc[i][3])
# 198
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# volatility = []
# for i in range(1,len(ohlc)):
#     volatility.append(ohlc[i][1]-ohlc[i][2])
# print(volatility)
# 199
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# for i in range(1,len(ohlc)):
#     if ohlc[i][3] > ohlc[i][0]:
#         volatility = ohlc[i][1]-ohlc[i][2]
#         print(volatility)
# 200
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
# profit = 0
# for i in range(1,len(ohlc)):
#     profit += ohlc[i][3]-ohlc[i][0]
# print(profit)
# 201
# def print_coin():
#     print("비트코인")
# 202
# print_coin()
# 203
# for i in range(100):
#     print_coin()
# 204
# def print_coins():
#     for i in range(100):
#         print("비트코인", i)
# print_coins()
# 205
# 위에 hello()는 앞에 def이 없어서 함수로 정의되지 않음
# 206
# "A"
# "B"
# "C"
# "A"
# "B"
# 207
# "A"
# "C"
# "B"
# 208
# "A"
# "C"
# "B"
# "E"
# "D"
# 209
# "B"
# "A"
# 210
# "B"
# "C"
# "B"
# "C"
# "B"
# "C"
# "A"
# 211
# "안녕"
# "Hi"
# 212
# 7
# 15
# 213
# 함수는 인자로 문자열을 받도록 정의하였는데 아무것도 입력하지 않음.
# 214
# 함수는 같은 타입인 a,b를 인자로 받아 더하도록 정의되었는데, 다른 타입인 str과 int로 인자로 입력해서 str과 int를 더할 수 없다고 에러가 남.
# 215
# def print_with_smile(string):
#     print(string + ":D")
# print_with_smile('hello')
# 216
# print_with_smile('안녕하세요')
# 217
# def print_upper_price(a):
#     print(a*1.3)
# print_upper_price(1000)
# 218
# def print_sum(a, b):
#     print(a+b)
# print_sum(3, 6)
# 219
# def print_arithmetic_operation(a, b):
#     print(a, "+", b, "=", a + b)
#     print(a, "-", b, "=", a - b)
#     print(a, "*", b, "=", a * b)
#     print(a, "/", b, "=", a / b)
# print_arithmetic_operation(3, 5)
# 220
# def print_max(a, b, c):
#     max_number = 0
#     if a > max_number:
#         max_number = a
#     if b > max_number:
#         max_number = b
#     if c > max_number:
#         max_number = c
#     print(max_number)
# print_max(1,5,3)
# 221
# def print_reverse(str):
#     print(str[::-1])
# print_reverse("python")
# 222
# def print_score(list):
#     sum = 0
#     for i in list:
#         sum += i
#     print(sum/len(list))
# print_score([6, 10, 5])
# 223
# def print_even(list):
#     for i in list:
#         if i % 2 == 0:
#             print(i)
# print_even([1, 3, 2, 10, 12, 11, 15])
# 224
# def print_keys(dict):
#     for keys in dict.keys():
#         print(keys)
# print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# 225
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# def print_value_by_key(dict, key):
#     print(dict[key])
# print_value_by_key (my_dict, "10/26")
# 226
# def print_5xn(str):
#     for i in range(0,len(str),5):
#         print(str[i:i+5])
# print_5xn("아이엠어보이유알어걸일이삼사오육칠팔구십")
# 227
# def print_5xn(str, num):
#     for i in range(0, len(str), num):
#         print(str[i:i+num])
# print_5xn("아이엠어보이유알어걸", 3)
# 228
# def calc_monthly_salary(annual_salary):
#     monthly_salary = annual_salary/12
#     print(f"%0.0f" %monthly_salary)
# calc_monthly_salary(12000000)
# 229
# 왼쪽: 100
# 오른쪽: 200
# 230
# 왼쪽: 200
# 오른쪽: 100
# 231
# 함수 내부 변술는 함수 밖에서 접근이 불가능하여 오류가남.
# 232
# def make_url(str):
#     return "www." + str + ".com"
# print(make_url("naver"))
# 233
# def make_list(str):
#     return list(str)
# print(make_list("abcd"))
# 234
# def pickup_even(list):
#     a = []
#     for i in range(len(list)):
#         if list[i] % 2 == 0:
#             a.append(list[i])
#     return a
# print(pickup_even([5, 57, 68, 90, 152]))
# 235
# def convert_int(str):
#     a = str.split(",")
#     a = ''.join(a)
#     return int(a)
# print(convert_int("1,234,567"), type(convert_int("1,234,567")))
# 236
# 22
# 237
# 22
# 238
# 140
# 239
# 16
# 240
# 28
# 241

# 242

# 243

# 244

# 245

# 246

# 247

# 248

# 249

# 250

# 251

# 252

# 253

# 254

# 255

# 256

# 257

# 258

# 259

# 260
