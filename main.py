import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("port1sn2121800.csv")
# dv = pd.read_csv("data/port1sn2121800_verification_data.csv")

########################################################################################################################

split_40_p = []
split_40_mv = []
split_55_p = []
split_55_mv = []
split_70_p = []
split_70_mv = []
split_minus_30_p = []
split_minus_30_mv = []
split_minus_15_p = []
split_minus_15_mv = []
split_0_p = []
split_0_mv = []
split_10_p = []
split_10_mv = []
split_25_p = []
split_25_mv = []

x = df["mv"]
y = df["Set pressure"]
z = df["set temperature"]

for i in range(0, len(y)):
    if z[i] == 40:
        split_40_mv.append(x[i])
        split_40_p.append(y[i])
    if z[i] == 55:
        split_55_mv.append(x[i])
        split_55_p.append(y[i])
    if z[i] == 70:
        split_70_mv.append(x[i])
        split_70_p.append(y[i])
    if z[i] == -30:
        split_minus_30_mv.append(x[i])
        split_minus_30_p.append(y[i])
    if z[i] == -15:
        split_minus_15_mv.append(x[i])
        split_minus_15_p.append(y[i])
    if z[i] == 0:
        split_0_mv.append(x[i])
        split_0_p.append(y[i])
    if z[i] == 10:
        split_10_mv.append(x[i])
        split_10_p.append(y[i])
    if z[i] == 25:
        split_25_mv.append(x[i])
        split_25_p.append(y[i])

coefficient_40 = np.polyfit(split_40_mv, split_40_p, 7)0.
check_40 = np.poly1d(coefficient_40)

coefficient_55 = np.polyfit(split_55_mv, split_55_p, 7)
check_55 = np.poly1d(coefficient_55)

coefficient_70 = np.polyfit(split_70_mv, split_70_p, 7)
check_70 = np.poly1d(coefficient_70)

coefficient_minus_30 = np.polyfit(split_minus_30_mv, split_minus_30_p, 7)
check_minus_30 = np.poly1d(coefficient_minus_30)

coefficient_minus_15 = np.polyfit(split_minus_15_mv, split_minus_15_p, 7)
check_minus_15 = np.poly1d(coefficient_minus_15)

coefficient_0 = np.polyfit(split_0_mv, split_0_p, 7)
check_0 = np.poly1d(coefficient_0)

coefficient_10 = np.polyfit(split_10_mv, split_10_p, 7)
check_10 = np.poly1d(coefficient_10)

coefficient_25 = np.polyfit(split_25_mv, split_25_p, 7)
check_25 = np.poly1d(coefficient_25)

########################################################################################################################

rp = df["verification read pressure"]
mv = df["verification mv"]
sp = df["verification Set pressure"]
st = df["verification set temperature"]
result_split_65_rp = []
result_split_65_mv = []
result_split_65_sp = []
result_split_65_st = []
result_split_minus_25_rp = []
result_split_minus_25_mv = []
result_split_minus_25_sp = []
result_split_minus_25_st = []
result_split_25_rp = []
result_split_25_mv = []
result_split_25_sp = []
result_split_25_st = []

for i in range(0, len(st)):
    if st[i] == 65:
        result_split_65_rp.append(rp[i])
        result_split_65_mv.append(mv[i])
        result_split_65_sp.append(sp[i])
        result_split_65_st.append(st[i])
    if st[i] == -25:
        result_split_minus_25_rp.append(rp[i])
        result_split_minus_25_mv.append(mv[i])
        result_split_minus_25_sp.append(sp[i])
        result_split_minus_25_st.append(st[i])
    if st[i] == 25:
        result_split_25_rp.append(rp[i])
        result_split_25_mv.append(mv[i])
        result_split_25_sp.append(sp[i])
        result_split_25_st.append(st[i])

calculated_pressure_25 = []
for i in range(0, len(result_split_25_st)):
    calculated_pressure_25.append(check_25(result_split_25_mv[i]))
    sensitivity = ((result_split_25_sp[i]) - calculated_pressure_25[i]) / 10
    if sensitivity < -0.0005 or sensitivity > 0.0005:
        print('{:.20f}'.format(sensitivity))
        plt.annotate((result_split_25_sp[i], calculated_pressure_25[i], sensitivity),  # this is the text
                     (result_split_25_mv[i], calculated_pressure_25[i]),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 0),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

########################################################################################################################

xp = np.linspace(-363, 300, 100)
# plt.plot(split_40_mv, split_40_p, '.', xp, check_40(xp), '-',
#          split_55_mv, split_55_p, '.', xp, check_55(xp), '-',
#          split_70_mv, split_70_p, '.', xp, check_70(xp), '-',
#          split_minus_30_mv, split_minus_30_p, '.', xp, check_minus_30(xp), '-',
#          split_minus_15_mv, split_minus_15_p, '.', xp, check_minus_15(xp), '-',
#          split_0_mv, split_0_p, '.', xp, check_0(xp), '-',
#         split_10_mv, split_10_p, '.', xp, check_10(xp), '-',
#          split_25_mv, split_25_p, '.', xp, check_25(xp), '-',)

#plt.plot(result_split_25_mv, calculated_pressure_25, '.', split_25_mv, split_25_p, '--')
plt.plot(result_split_25_mv, calculated_pressure_25, '>', xp, check_25(xp), '-', split_25_mv, split_25_p, 'o')
plt.grid()
plt.show()

########################################################################################################################

print("end")
