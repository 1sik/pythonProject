import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib import font_manager, rc

el_school_name = []
el_school_address = []
el_school_latitude = []
el_school_longitude = []

mi_school = []
hi_school = []

# 전라북도 지역별 위도 경도 읽어오기
df = pd.read_csv("C:/Users/USER/PycharmProjects/pythonProject/data/all.csv", encoding="euc_kr")
data = pd.read_csv("C:/Users/USER/PycharmProjects/pythonProject/data/전라북도_고등학교.csv", encoding="euc_kr")

# for i in range(len(df)-2):
#     if "전라북도교육청" in df.loc[i+2]["시도교육청명"]:
#         if "초등학교" in df.loc[i+2]["학교급구분"]:
#             el_school.append([df.loc[i+2]["위도"], df.loc[i+2]["경도"]])
#
#         elif "중학교" in df.loc[i+2]["학교급구분"]:
#             mi_school.append([df.loc[i+2]["위도"], df.loc[i+2]["경도"]])
#         else:
#             hi_school.append([df.loc[i+2]["위도"], df.loc[i+2]["경도"]])

for i in range(len(df) - 2):
    if "전라북도교육청" in df.loc[i + 2]["시도교육청명"]:
        if "고등학교" in df.loc[i + 2]["학교급구분"]:
            el_school_name.append(df.loc[i + 2]["학교명"])
            el_school_address.append(df.loc[i + 2]["소재지도로명주소"])
            el_school_latitude.append(df.loc[i + 2]["위도"])
            el_school_longitude.append(df.loc[i + 2]["경도"])

print(el_school_name)
print(el_school_address)
print(el_school_latitude)
print(el_school_longitude)

data["학교명"] = el_school_name
data["주소"] = el_school_address
data["위도"] = el_school_latitude
data["경도"] = el_school_longitude

data.to_csv("C:/Users/USER/PycharmProjects/pythonProject/data/전라북도_고등학교.csv", encoding="euc_kr")