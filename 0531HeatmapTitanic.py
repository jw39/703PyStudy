import seaborn as sns # 데이터 시각화 라이브러리(손쉽게 그래프를 그리고 그래프 스타일 설정 가능)
import pandas as pd # 데이터 처리를 위한 라이브러리
import matplotlib.pyplot as plt # 데이터 시각화 라이브러리(정교하게 그래프의 크기를 조절하거나 각 축의 범례 값을 조절)

#데이터 수집
titanic = sns.load_dataset("titanic") # load_dataset는 데이터셋을 불러오는 함수
titanic.to_csv('D:/panda203033/titanic.csv', index = False) # 불러온 데이터를 csv파일로 저장

#데이터 준비
titanic.isnull().sum() # 데이터프레임의 null값의 개수를 확인, isnull()은 null값일 때 True 아니면 Flase
titanic['age'] = titanic['age'].fillna(titanic['age'].median()) # filln()는 pandas 라이브러리에서 제공하는 메서드(결측치(null 또는 NaN 값)를 다른 값으로 대체하는 역할), median는 중앙값
titanic['embarked'].value_counts() # value_counts()는 고유한 행의 갯수를 반환
titanic['embark_town'] = titanic['embark_town'].fillna('Southampton')
titanic['deck'].value_counts()
titanic['deck'] = titanic['deck'].fillna('C')
titanic.isnull().sum()

# 데이터 탐색
titanic.info() # 데이터의 기본 정보 탐색
titanic.survived.value_counts()

f,ax = plt.subplots(1, 2, figsize = (10, 5)) # 차트를 그려 데이터를 시각적으로 탐색, 1행 2열의 그래프 서브플롯 생성
titanic['survived'][titanic['sex'] == 'male'].value_counts().plot.pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[0], shadow = True)
# explode는 파이 차트에서 특정 부분을 돌출시키는 정도, autopct는 파이 차트의 각 조각에 표시되는 퍼센트 값을 포맷, ax = ax[0]는 첫번째 서브플롯에 그림, shadow는 그림자 효과
titanic['survived'][titanic['sex'] == 'female'].value_counts().plot. pie(explode = [0,0.1], autopct = '%1.1f%%', ax = ax[1], shadow = True)
ax[0].set_title('Survived (Male)') # 타이틀을 Survived (Male)로 지정
ax[1].set_title('Survived (Female)')
plt.show()

# 등급별 생존자 수를 차트로 나타내기
sns.countplot(x = 'pclass', hue = 'survived', data = titanic) # x 축에 'pclass' 변수를 지정, 막대 그래프의 색상을 'survived' 변수로 구분, 그래프를 그릴 데이터를 'titanic' 데이터프레임으로 지정
plt.title('Pclass vs Survived')
plt.show()

# 데이터 모델링 오류 해결x
# titanic_corr = titanic.corr(method = 'pearson') # 상관 분석을 위한 상관 계수 구하고 저장
# titanic_corr
# titanic_corr.to_csv('C:/Users/dlwod/PythonProject/titanic_corr.csv', index = False)
# titanic['survived'].corr(titanic['adult_male']) # 특정 변수 사이의 상관 계수 구하기
# titanic['survived'].corr(titanic['fare'])

#결과 시각화
sns.pairplot(titanic, hue = 'survived') # pairplot은 변수들 간의 산점도를 그려 상관 분석 결과를 시각화, titanic 데이터프레임의 변수들 간의 산점도와 히스토그램을 그리는
plt.show()
sns.catplot(x = 'pclass', y = 'survived', hue = 'sex', data = titanic, kind = 'point')
# 두 변수의 상관 관계를 포인트 플롯으로 그림, catplot()함수는 주어진 데이터프레임의 범주형 변수들 간의 관계를 시각화, kind는 그래프의 종류를 'point'로 설정
plt.show()

def category_age(x): # 변수 사이의 상관 계수를 히트맵으로 시각화, 10살 단위로 등급을 나누어 0~7의 값으로 바꿈
        if x < 10:
           return 0
        elif x < 20:
           return 1
        elif x < 30:
           return 2
        elif x < 40:
           return 3
        elif x < 50:
            return 4
        elif x < 60:
           return 5
        elif x < 70:
           return 6
        else:
           return 7
titanic['age2'] = titanic['age'].apply(category_age) # age변수를 기반으로 age2변수를 생성
titanic['sex'] = titanic['sex'].map({'male':1, 'female':0}) # sex변수의 값을 male과 female에서 각각 1과 0으로 매핑하여 sex변수를 업데이트
titanic['family'] = titanic['sibsp'] + titanic['parch'] + 1 # sibsp와 parch변수를 합산
titanic.to_csv('C:/Users/dlwod/PythonProject/titanic3.csv', index = False)
heatmap_data = titanic[['survived', 'sex', 'age2', 'family', 'pclass', 'fare']]
# titanic데이터프레임에서 survived, sex, age2, family, pclass, fare열을 선택하여 heatmap_data 데이터프레임을 생성
colormap = plt.cm.RdBu # 히트맵에 사용될 색상 맵을 RdBu로 지정
sns.heatmap(heatmap_data.astype(float).corr(), linewidths = 0.1, vmax = 1.0, square = True, cmap = colormap, linecolor = 'white', annot = True, annot_kws = {"size": 10})
# astype(float)은 heatmap_data데이터프레임을 부동 소수점 형식으로 변환, corr은 변환된 데이터프레임의 열들 간의 상관관계를 계산(피어슨 상관계수를 기본으로 사용)
# linewidths는 히트맵의 셀 사이의 경계선의 너비를 설정, vmax는 히트맵에서 색상 맵의 최대 값으로 사용될 상관계수를 설정, square는 히트맵의 셀이 정사각형 모양으로 표시되도록 설정
# cmap은 히트맵에 사용될 색상 맵을 'colormap' 변수로 설정, linecolor는 히트맵의 셀 사이 경계선의 색상을 흰색으로 설정, annot은 히트맵의 각 셀에 상관계수 값을 주석으로 표시, annot_kws는 주석의 글꼴 크기를 10으로 설정
plt.show()