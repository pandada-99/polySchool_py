import pandas as pd
from matplotlib import pyplot as plt
from sklearn import tree


if __name__=='__main__':
    # df = pd.read_csv("ai_score_data.csv")

    # plt.title('Math score')
    # plt.xlabel('Score')
    # plt.xticks(range(0, df["Math"].max(), 5))
    # plt.ylabel('Count')
    # plt.hist(df['Math'], bins=20)

    # canvas = plt.figure(figsize=(7.0, 7.0))
    # plt.grid()
    # plt.xlabel('Math Score')
    # plt.ylabel('English Score')
    # for i in range(len(df['Sex'])):
    #     if df.loc[i, 'Sex'] == 'M':
    #         plt.scatter(df.loc[i, 'Math'], df.loc[i, 'English'], color="blue")
    #     else:
    #         plt.scatter(df.loc[i, 'Math'], df.loc[i, 'English'], color="red")
    # plt.show()


    # df = pd.read_csv("salmon_bass_data.csv")

    # salmon_df = df.loc[df['Class'] == 'Salmon']
    # bass_df = df.loc[df['Class'] == 'Bass']

    # 길이 히스토그램 만들기
    # plt.title('Length Histogram')
    # plt.hist(salmon_df['Length'], bins=20, alpha=0.5, label='Salmon')
    # plt.hist(bass_df['Length'], bins=20, alpha=0.5, label='BaSS')
    # plt.legend(loc='best') #범주표시(label), best=알아서 좋은 위치에 그려줌
    # plt.show()

    # 밝기 히스토그램 만들기
    # plt.title('Lightness Histogram')
    # plt.hist(salmon_df['Lightness'], bins=20, alpha=0.5, label='Salmon')
    # plt.hist(bass_df['Lightness'], bins=20, alpha=0.5, label='BaSS')
    # plt.legend(loc='best') #범주표시(label), best=알아서 좋은 위치에 그려줌
    # plt.show()


    # Salmon / Bass 분류
    # X = [] #특징값(길이, 밝기)을 넣어줄 빈리스트
    # Y = [] #정답 레이블을 저장할 빈리스트
    #
    # for i in range(len(df)):
    #     fish = [df.loc[i, "Length"], df.loc[i, "Lightness"]]
    #     X.append(fish)
    #     Y.append(df.loc[i, "Class"])
    #
    # dt_model = tree.DecisionTreeClassifier()
    # dt_model = dt_model.fit(X, Y)
    #
    # plt.figure(figsize=(10, 10))
    # tree.plot_tree(dt_model, fontsize=8, filled=True, class_names=['Salmon', 'Bass'], feature_names=['Length', 'Lightness'])
    # plt.show()

    # 220329 기계학습프로그래밍 보충
    # Iris 분류 과제
    # df = pd.read_csv('Iris.csv')
    # X = []
    # Y = []
    # for i in range(len(df)):
    #     iris = [df.loc[i, 'SepalLengthCm'], df.loc[i, 'SepalWidthCm'], df.loc[i, 'PetalLengthCm'], df.loc[i, 'PetalWidthCm']]
    #     X.append(iris)
    #     Y.append(df.loc[i, 'Species'])
    #
    # iris_model = tree.DecisionTreeClassifier()
    # iris_model = iris_model.fit(X, Y)
    #
    # plt.figure(figsize=(15, 10))
    # tree.plot_tree(iris_model, fontsize=8, filled=True,
    #                class_names=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    #                feature_names=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'])
    # plt.show()


    # 220329 학습데이터처리(신교수님)
    # exam_date = {'이름' : ['노영하', '김근형', '정겸임'],
    #              'AI기초' : [90, 80, 70],
    #              '자료구조' : [98, 89, 95],
    #              '영어' : [85, 95, 100],
    #              '웹프로그래밍' : [100, 90, 90]}
    # df = pd.DataFrame(exam_date)
    # print(df)
    # print(type(df))
    #
    # # '자료구조' 컬럼만 선택
    # datastructure = df['자료구조'] # english = df.영어
    # print(datastructure)
    # print(type(datastructure)) # Series
    #
    # # 여러개의 컬럼 데이터를 가지고 오기 ==> 반환되는 자료형은? DataFrame
    # ai_web = df[['AI기초', '웹프로그래밍']]
    # print(ai_web)
    # print(type(ai_web)) # DataFrame
    #
    # # reindex, set_index, ...
    # # set_index: 특정 열을 새로운 index로 사용하겠다.
    # df.set_index('이름', inplace=True)
    # print(df)
    #
    # # 데이터 프레임 df의 특징 원소 1개 선택
    # # loc, iloc: [row, col]
    # point1 = df.loc['노영하', '영어']
    # point2 = df.iloc[0, 2]
    #
    # print(point1, point2)
    # print(type(point1))
    #
    # # 특정 원소 2개 이상 선택 ('노영하'의 영어, 웹프로그래밍 점수)
    # c = df.loc['노영하', ['영어', '웹프로그래밍']]
    # d = df.iloc[0, [2, 3]]
    # e = df.iloc[0, 2:]
    # print(c, '\n', d, '\n', e)
    #
    # # df에서 2개 이상의 행과 열로 부터 데이터를가지고 와보자.
    # # f = '노영하, 김근형'의 영어, 웹프로그래밍 점수
    # # g = '노영하, 정겸임'의 자료구조, 웹프로그래밍 점수
    # f = df.loc[['노영하', '김근형'], ['영어', '웹프로그래밍']]
    # h = df.iloc[:2, 2:]
    # g = df.loc[['노영하', '정겸임'], ['자료구조', '웹프로그래밍']]
    # i = df.iloc[[0, 2], [1, 3]]
    # j = df.loc['노영하':'정겸임', 'AI기초':'영어']
    # print(f, '\n', h, '\n', g, '\n', i, '\n', j)
    #
    # # 새로운 열 추가 및 데이터 assign
    # print(df)
    # df['ML'] = [80, 90, 100]
    # print(df)
    # # 새로운 행 추가 (index가 3인 행을 추가하고 모든 컬럼의 값들은 0로 세팅)
    # df.loc[3] = 0
    # df.loc['이은정'] = [90, 90, 95, 85, 70]
    # print(df)
    #
    # # 새로운 행 추가 시 기존 행을 복사
    # df.loc['이시영'] = df.loc['이은정']
    # print(df)
    #
    # # 원소 값 변경
    # df1 = df.copy()
    # print(df1.iloc[0][0])
    # df1.iloc[0, [1, 2, 3]] = [100, 100, 100]
    # print(df1)
    # #0,1행의 [1,2,3]열의 데이터 변경
    # df1.iloc[[0, 1], [1, 2, 3]] = [[90, 90, 90], [80, 80, 80]]
    # print(df1)
    # # 슬라이싱을 이용한 데이터 변경
    # df1.loc[3, 'AI기초':'ML'] = [80, 80, 80, 90, 100]
    # print(df1)
    #
    # dict_date = {'c0': [1,2,3], 'c1': [5,4,6], 'c2': [7,8,9]}
    # df = pd.DataFrame(dict_date, index=['r0', 'r1', 'r2'])
    # # 행 인덱스 재배열
    # new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
    # ndf = df.reindex(new_index, fill_value=0)
    # print(ndf)
    #
    # ndf = df.sort_index(ascending=False)
    # print(ndf)


    # 220405 학습데이터처리(신교수님)
    # Dictionary를 이용하여 판다스 시리즈 만들기
    # dict_data = {}
    student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})

    # Normalization (100기준: 0~100, 0~1사이 값으로 변경)
    # Normalize (원소값/최대값(행 or 열))\
    # 모든 원소의 값을 100으로 나눈다.
    percentage = student1 / 100
    print(percentage, type(percentage))

    # Series vs. Series 연산
    student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
    student2 = pd.Series({'수학': 80, '영어': 80, '국어': 70})

    # 두 학생의 과목별 점수로 사칙연산을 수행해보자.
    add = student1 + student2
    sub = student1 - student2
    mul = student1 * student2
    div = student1 / student2

    # 사칙연산 결과를 DataFrame으로 표현 (Series -> DataFrame)
    result = pd.DataFrame([add, sub, mul, div],
                          index=['add', 'sub', 'mul', 'div'])
    print(result)

    # NaN을 만들어보고, NaN일때를 생각해서 fill_value라는 옵션도 한 번 사용
    student1 = pd.Series({'국어': 100, '영어': 80, '수학': 90})
    student2 = pd.Series({'수학': 80, '국어': 70})
    sr_add = student1.add(student2, fill_value=0)
    sr_sub = student1.sub(student2, fill_value=0)
    sr_mul = student1.mul(student2, fill_value=0)
    sr_div = student1.div(student2, fill_value=0)

    # 사칙연산 결과를 Series -> DataFrame으로 표현
    result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                          index=['add', 'sub', 'mul', 'div'])
    print(result)