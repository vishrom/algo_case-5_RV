import pandas as pd
import matplotlib.pyplot as plt


mission_old_fail = 0
mission_old_success = 0
mission_new_fail = 0 
mission_new_success = 0 
mission_lp_fail = 0 
mission_lp_success = 0 
mission_mp_fail = 0 
mission_mp_success = 0 

def destr(date):
    fr = date[12:17]
    return int(fr)
def conv(prise):
    prise = str(prise)
    fr = prise.replace(',','')
    return float(fr)


def ci(dr):
    global mission_old_fail, mission_old_success, mission_new_fail, mission_new_success
    if dr['Yers'] >= 2000:
        if dr['Status Mission'].find('Success'):
            mission_new_success += 1
        else:
            mission_new_fail += 1
    else:
        if dr['Status Mission'].find('Success'):
            mission_old_success += 1
        else:
            mission_old_fail += 1
def psc(dp):
    global mission_lp_fail, mission_lp_success, mission_mp_fail, mission_mp_success
    if dp['Price_Mission'] == -1:
        return

    if dp['Price_Mission'] >= 100:
        if dp['Status Mission'].find('Success'):
            mission_mp_success += 1
        else:
            mission_mp_fail += 1
    else:
        if dp['Status Mission'].find('Success'):
            mission_lp_success += 1
        else:
            mission_lp_fail += 1

# Загружаем датафрейм 
df = pd.read_csv('Space_Corrected.csv')

df['Price_Mission'].fillna(-1, inplace = True)

print(df['Datum'].value_counts())
#__________________________________________________________________________________________________________
df['Yers'] = df['Datum'].apply(destr)
df.info()
df.apply(ci, axis = 1)
print('Миссии после 2000г. с большей вероятностью выполняли задачу чем миссии до него')
print('Миссии после 2000г: n/Провальные:', mission_new_fail,'n/Успешные:', mission_new_success)
print('Миссии до 2000г: n/Провальные:', mission_old_fail,'n/Успешные:', mission_old_success)

mission_old_1pr = (mission_old_fail + mission_old_success) / 100
mission_new_1pr = (mission_new_fail + mission_new_success) / 100
mos = mission_old_success / mission_old_1pr
mns = mission_new_success / mission_new_1pr
print('И того до 2000г процентное соотношение успешных миссий состовляет', mos, '%, а после 2000г процентное соотношение успешных миссий состовляет:', mns, '% значит данная гепотиза опроверженна')

gos = 100 - mos
gof = mos
s = pd.Series(data = [gos, gof], index = ['Провальные миссии','Удачные миссии'])
s.plot(kind = 'pie')
plt.show()

gns = 100 - mns
gnf = mns
s = pd.Series(data = [gns, gnf], index = ['Провальные миссии','Удачные миссии'])
s.plot(kind = 'pie')
plt.show()
#__________________________________________________________________________________________________________

df['Price_Mission'] = df['Price_Mission'].apply(conv)
df.info()
df.apply(psc, axis = 1)
print('Миссии бюджет которых более 100М$ с большей вероятностью выполняют поставленную задачу чем миссии с бюджетом менее 100М$')
print('Миссии с бюджетом более 100$: n/Провальные:', mission_mp_fail,'n/Успешные:', mission_mp_success)
print('Миссии с бюджетом менее 100$: n/Провальные:', mission_lp_fail,'n/Успешные:', mission_lp_success)
mission_lp_1pr = (mission_lp_fail + mission_lp_success) / 100
mission_mp_1pr = (mission_mp_fail + mission_mp_success) / 100

mlps = mission_lp_success / mission_lp_1pr
mmps = mission_mp_success / mission_mp_1pr
print('И того с бюджетом более 100$ процентное соотношение успешных миссий состовляет', mmps, '%, а с бюджетом менее 100$ процентное соотношение успешных миссий состовляет:', mlps, '% значит данная гепотиза опроверженна')
glps = 100 - mlps
glpf = mlps
s = pd.Series(data = [glps, glpf], index = ['Провальные миссии','Удачные миссии'])
s.plot(kind = 'pie')
plt.show()

gmps = 100 - mmps
gmpf = mmps
s = pd.Series(data = [gmps, gmpf], index = ['Провальные миссии','Удачные миссии'])
s.plot(kind = 'pie')
plt.show()

''' Гипотеза
1 Миссии бюджет которых более 100М$ с большей вероятностью выполняют поставленную задачу чем миссии с бюджетом менее 100М$
2 Миссии после 2000г. с большей вероятностью выполняли задачу чем миссии до него 
'''


