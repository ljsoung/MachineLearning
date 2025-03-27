# 시본 라이브러리 불러오기
# Seaborn 장점
# 1. 아름답고 직관적인 스타일
# 2. 고급 통계 시각화 지원
# 3. 데이터프레임과의 강력한 통합
# 4. 기본적인 다중 플롯 기능
# 5. 자동 색상 팔레트 관리
# 6. Matplotlib와의 호환성

import seaborn as sns

# 시본 내장 데이터의 종류출력
# print(sns.get_dataset_names())

# 팁 데이터 셋을 불러온 다음, 데이터 셋의 구성을 살펴보기
# .head(): 데이터의 상단 5개 행 출력
tips = sns.load_dataset("tips")
# print(tips.head())

# info(): 열에 대한 요약 정보 확인
# 행과 열의 크기, 컬럼명, 컬럼별 결측치, 컬럼별 데이터 타입
print(tips.info())

