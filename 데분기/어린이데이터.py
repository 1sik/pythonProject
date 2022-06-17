import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from matplotlib import font_manager, rc


el_school_name = []
el_school_address = []
el_school_latitude = []
el_school_longitude = []


df = pd.read_csv("C:/Users/USER/PycharmProjects/pythonProject/data/전라북도_유치원.csv", encoding="euc-kr")
# data = pd.read_csv("C:/Users/USER/PycharmProjects/pythonProject/data/전라북도_유유치원.csv", encoding="euc_kr")

for i in range(len(df)):
    df["어린이집명"][i]



# data["학교명"] = el_school_name
# data["주소"] = el_school_address
# data["위도"] = el_school_latitude
# data["경도"] = el_school_longitude
#
# data.to_csv("C:/Users/USER/PycharmProjects/pythonProject/data/전라북도_고등학교.csv", encoding="euc_kr")