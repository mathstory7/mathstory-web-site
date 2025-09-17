import pandas as pd

print("판다스 버전 확인:")
print(pd.__version__)

house = pd.read_csv('house.csv')
print(house.head())  # 첫 5줄 출력
