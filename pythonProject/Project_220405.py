# 220405 학습데이터처리(신교수님)
import pandas as pd

# 파일경로 지정, 파일경로에서 csv 파일 읽어오기
# read_csv(path=)
# read_csv(file path)
# 상대경로 : data/read_csv_sample.csv
# 절대경로 : C:\Users\AI-00\PycharmProjects\pythonProject\data
file_path = './data/read_csv_sample.csv' # 상대경로(현재 내가 있는 위치로부터), './' : 현재 디렉터리(directory:자료방)를 뜻함
# read_csv라는 함수를 이용해서 csv파일을 읽은 후 데이터 프레임으로 변환하고 df1에 저장
df1 = pd.read_csv(file_path)
print(df1, '\n')
df2 = pd.read_csv(file_path, header=None)
print(df2, '\n')
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print()
df4 = pd.read_csv(file_path, index_col='c0')
print(df4, '\n')

# read_excel() 함수로 엑셀파일 Read 후, Dataframe으로 변환
df1 = pd.read_excel('./data/남북한발전전력량.xlsx',
                    engine='openpyxl')
print(df1, '\n')

# read_json()
df2 = pd.read_json('data/read_json_sample.json')
print(df2, '\n')

# url, html이 존재하는 file_path를 입력인자로 넣어도 됨.
url = 'data/sample.html'
tables = pd.read_html(url)

# 현재 읽어온 html 내에 몇개의 테이블이 있는지 체크
print(len(tables), '\n')

# tables 리스트의 원소를 iteration(반복)하면서, 각각 화면 출력
for i in range(len(tables)):
    print("tables[%d]" %i)
    print(tables[i])
    print()

# 판다스 DataFrame() 함수로 데이터프레임 변환, 변수 df1, df2에 저장
data1 = {'name': ['Jerry', 'Riah', 'Paul'],
         'algol': ['A', 'B', 'c'],
         'python': ['A+', 'B+', 'C+']}

data2 = {'c0': [1, 2, 3],
         'c1': [4, 5, 6],
         'c2': [1, 2, 3]}

# dictionary type의 data1, data2를 df1, df2로 변경하고, set_index를 통해 특정 컬럼을 index의 이름으로 사용.
# inplace=True 옵션을 이용하여 새로운 객체를 생성하지 않고 현재 df에 변경사항 적용
df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True)
df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)

# df1을 'sheet1'의 이름으로 엑셀 시트 하나 생성.
# df2을 'sheet2'의 이름으로 엑셀 시트 하나 생성.
writer = pd.ExcelWriter("./data/df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()