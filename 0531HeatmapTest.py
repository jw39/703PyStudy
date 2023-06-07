# import seaborn as sns
# import matplotlib.pyplot as plt
# #seaborn과 matplotlib의 모듈을 가져오기

# # exercise 데이터셋 로드
# exercise = sns.load_dataset("exercise") #내장 exercise 데이터셋을 로드
# exercise.to_csv('D:/panda203033/exercise.csv', index = False)
# #exercise 데이터셋을 CSV 파일로 저장



# # 피벗 테이블 생성, "time"을 행 인덱스, "kind"를 열 인덱스, "pulse"를 값으로 갖는 테이블을 생성
# heatmap_data = exercise.pivot_table(index="time", columns="kind", values="pulse")

# # 히트맵 그리기, 각 셀에 데이터 입력, 소수점 첫째 자리까지 입력, 색상맵 YlGnBu 사용
# sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu")


# # 그래프 제목 설정
# plt.title("Exercise Heatmap")

# # 그래프 출력
# plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

# exercise 데이터셋 로드
exercise = sns.load_dataset("exercise")
exercise.to_csv('D:/panda203033/exercise.csv', index=False)

#diet_values 리스트와 sex_values 리스트를 생성하여 해당 열에 값으로 할당
# "diet" 열 추가
diet_values = ["low fat"] * 45 + ["no fat"] * 45 #각 운동 종류와 식단 종류 별로 45개의 데이터가 있음, 운동 종류와 식단 종류, 성별이 45번씩 반복되는 형태로 데이터를 생성
exercise["diet"] = diet_values
# "sex" 열 추가
sex_values = ["female", "male"] * 45
exercise["sex"] = sex_values

# 피벗 테이블 생성, heatmap_data 변수에 저장
heatmap_data = exercise.pivot_table(index="time", columns=["kind", "diet", "sex"], values="pulse")

# 히트맵 그리기, 그래프를 그리기 위한 Figure와 Axes 객체를 생성
fig, ax = plt.subplots(figsize=(10, 6)) #그래프 크기 지정
sns.heatmap(heatmap_data, annot=True, fmt=".1f", cmap="YlGnBu")

# x축 레이블 설정
plt.xlabel("Exercise Category")
# y축 레이블 설정
plt.ylabel("Time")

# x축 눈금 레이블 설정 (kind, sex, diet 함께 표시), rotation=45는 레이블을 45도로 회전, ha='right'는 레이블을 오른쪽 정렬
plt.xticks(ticks=range(len(heatmap_data.columns)), labels=heatmap_data.columns, rotation=45, ha='right')

# y축 눈금 레이블 설정
plt.yticks(ticks=range(len(heatmap_data.index)), labels=heatmap_data.index)

# 그래프 제목 설정
plt.title("Exercise Heatmap")

# 그래프 출력
plt.tight_layout()
plt.show()

