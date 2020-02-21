import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv("ok.csv")
ser=df.groupby("HomeTeam").FTR.value_counts()
ser=ser.unstack()
ser=ser.fillna(0)

ser2=df.groupby("AwayTeam").FTR.value_counts()
ser2=ser2.unstack()
ser2=ser2.fillna(0)

df1=pd.pivot_table(df,index="HomeTeam",values=["FTHG","FTAG"],aggfunc=np.sum)
df2=pd.pivot_table(df,index="AwayTeam",values=["FTHG","FTAG"],aggfunc=np.sum)

s=ser.drop(columns=["A","D"])
s2=ser2.drop(columns=["H","D"])
data={"隊伍":np.sort(df.HomeTeam.unique()),"勝":np.array(ser["H"])+np.array(ser2["A"]),"平":(np.array(ser["D"])+np.array(ser2["D"]))
     ,"敗":np.array(ser["A"])+np.array(ser2["H"]),"進球":np.array(df1["FTHG"])+np.array(df2["FTAG"]),"失球":np.array(df1["FTAG"])+np.array(df2["FTHG"])}
     
     
ok=pd.DataFrame(data)


ok["淨勝"]=np.array(ok[["進球"]])-np.array(ok[["失球"]])
ok["積分"]=np.array(ok[["勝"]])*3+np.array(ok[["平"]])

ok=ok.sort_values(by=["積分","淨勝"],ascending=False)
