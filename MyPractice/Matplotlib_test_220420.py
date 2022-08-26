# https://www.youtube.com/watch?v=5DfACSYgP0U&ab_channel=%EC%9D%B4%EC%88%98%EC%95%88%EC%BB%B4%ED%93%A8%ED%84%B0%EC%97%B0%EA%B5%AC%EC%86%8C

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use(['seaborn-notebook'])

# 라인 플롯(Line Plot)
# plot(플롯)은 figure(그림)과 axes(축)으로 구성
# fig = plt.figure() # figure 그림: 축과 그래픽, 텍스트, 레이블을 표시하는 모든 객체를 포함하는 컨테이너
# ax = plt.axes() # axes 축: 눈금과 레이블이 있는 테두리 박스로 시각화를 형성하는 플롯 요소 포함

# 직선 플롯(Line Plot)
# fig = plt.figure()
# plt.plot([0, 0.2, 0.4, 0.6, 0.8, 1] * 5)

# 곡선 플롯(Line Plot)
# x = np.arange(0, 10, 0.01)
# fig = plt.figure()
# plt.plot(x, np.sin(x))
# plt.plot(x, np.cos(x))

# 랜덤값으로 만든 라인 플롯(Line Plot)
# plt.plot(np.random.randn(50).cumsum()) # cumsum: 누적합

# 라인 스타일(Line Style)
# '-' : 'solid' => 실선으로 구성된 line
# '--' : 'dashed' => 점선으로 구성된 line
# '-.' : 'dashdot' => 점선과 점의 반복으로 구성된 line
# ':' : 'dotted' => 점으로 구성된 line

# plt.plot(np.random.randn(50).cumsum(), linestyle='solid')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dashed')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dashdot')
# plt.plot(np.random.randn(50).cumsum(), linestyle='dotted')

# 색상 스타일(Color Style)
# plt.plot(np.random.randn(50).cumsum(), color='g')
# plt.plot(np.random.randn(50).cumsum(), color='#1234FF')
# plt.plot(np.random.randn(50).cumsum(), color=(0.8, 0.4, 0.6))
# plt.plot(np.random.randn(50).cumsum(), color='pink')

# 라인 스타일과 색상 스타일을 한번에 적용
# plt.plot(np.random.randn(50).cumsum(), 'g-')
# plt.plot(np.random.randn(50).cumsum(), 'b--')
# plt.plot(np.random.randn(50).cumsum(), 'c-.')
# plt.plot(np.random.randn(50).cumsum(), 'm:')

# 플롯 축(Plot Axis)
# plt.plot(np.random.randn(50))
# plt.xlim(-1, 50)
# plt.ylim(-5, 5)
# 위에꺼 한번에 하기 => plt.axis([-1, 50, -5, 5])
# 딱맞게, 타이트하게 만들어라 => plt.axis('tight')
# 넓은 범위로 비율맞춰서 만들어라 => plt.axis('equal')

# 플롯 레이블(Plot Label)
# plt.plot(np.random.randn(50), label='A')
# plt.plot(np.random.randn(50), label='B')
# plt.plot(np.random.randn(50), label='C')
# plt.title("title")
# plt.xlabel("X")
# plt.ylabel("random.randn")
# plt.legend() # 범례(기호 설명표, key)

# 폰트 관리자(Font Manager)
# 폰트 매니저가 가진 폰트 파일 리스트 보기
# print(set([f.name for f in mpl.font_manager.fontManager.ttflist]))

# font1 = {'family': 'DejaVu Sans', 'size': 24, 'color': 'black'}
# font2 = {'family': 'Liberation Mono', 'size': 18, 'weight': 'bold', 'color': 'darkred'}
# font3 = {'family': 'STIXGeneral', 'size': 16, 'weight': 'light', 'color': 'blue'}

# plt.plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
# plt.title('title', fontdict=font1) # dict형태로 저장된 font1을 쓰겠다.
# plt.xlabel("Xlabel", fontdict=font2)
# plt.ylabel("Ylabel", fontdict=font3)

# 플롯 범례(Plot Legend)
# 범례 loc지정: 0 => best (자동으로 최적의 위치를 찾아 넣어준다)

# 다중 플롯(Multiple Subplots)
# ax1 = plt.axes()
# ax2 = plt.axes([0.65, 0.5, 0.2, 0.3]) # ax1 플롯의 [0.65, 0.5, 0.2, 0.3]이 위치에 ax2플롯을 그려줘

# 텍스트와 주석(Text and Annotation)


# 눈금 맞춤(Customizing Ticks)


# 스타일(Style)


plt.show()
