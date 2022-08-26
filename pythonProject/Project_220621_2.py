# 220621 학습데이터처리(신교수님)
import pandas as pd
import os # Path를 사용하기 위해
import matplotlib.pyplot as plt

# 컬럼수가 많아도 다 display하기 위해.
pd.set_option('display.max_columns', None)

path = "Movie_Lens/ml-latest-small/"

# data를 dataframe에 로드
ratings_df = pd.read_csv(os.path.join(path + 'ratings.csv'), encoding='utf-8')
movies_df = pd.read_csv(os.path.join(path + 'movies.csv'), encoding='utf-8')
tags_df = pd.read_csv(os.path.join(path + 'tags.csv'), encoding='utf-8')

print("###############################################################################################################")
# 0. 데이터가 어떤지 확인
print(f'{ratings_df.shape}\n{ratings_df.head()}')
print(f'{movies_df.shape}\n{movies_df.head()}')
print(f'{tags_df.shape}\n{tags_df.head()}')

print("###############################################################################################################")
# 1. 평점 데이터(rating_df)의 데이터 분석(기초 통계)
# 평점을 준 유저는 총 몇 명인가요? # 610명
print(f'User: {len(ratings_df.groupby(["userId"]))}')
print(f'User_using Unique(): {len(ratings_df.userId.unique())}')

# 평점을 받은 영화의 수는 몇 개일까요?
# 9742개의 영화가 있고, 평점을 받은 영화는 9724개인 것을 확인
print(f'Movies: {len(ratings_df.movieId.unique())}')
# 평점의 평균, 표준편차 등을 확인
print(f'Mean Rating: {ratings_df.rating.mean()}')
# ratings_df["rating"].mean()
print(f'Std Rating: {ratings_df.rating.std()}')

# rating_df의 기본 정보 확인
print(ratings_df.info())
# 통계에 대한 데이터를 확인하기 위해서는 describe() 메서드 사용
print(ratings_df.describe())
# NaN 유무 확인 메서드: isnull
print(ratings_df.isnull().sum())

print("###############################################################################################################")
# 2. groupby를 활용한 통계 연습
# 유저별 평점 평균 (userId가 1인 사람의 평균 평점, 2인 사람의 평균 평점..)
print(ratings_df.groupby('userId').mean()['rating'])
print(ratings_df.groupby('userId')['rating'].mean())

# 유저별 평점별 평가 횟수
# 1번 유저가 1점을 몇번줬고, 2점을 몇번 줬는지에 대한 통계
print(ratings_df.groupby(['userId', 'rating']).size())

# 유저가 평점을 몇 번 줬는지.. (count())
print(ratings_df.groupby('userId')['movieId'].count())

# 유저가 평균적으로 준 평점과 평점을 준 영화의 수에 대한 Dataframe을 생성
# dataframe name: stat_df
stat_df = pd.DataFrame({'user_movie_count': ratings_df.groupby('userId')['movieId'].count(),
                        'user_rating_mean': ratings_df.groupby('userId')['rating'].mean()})
print(stat_df)