#ЗДЕСЬ АНАЛИЗИРУЕТСЯ ПЕРВЫЙ СНИМОК

from imp_and_def import*

#Загружаем фото 2018 года
pic1 = CreatePath("2018.08.28", "*band*.tif", "my_outputs", "out.tif") #28 августа

#НАХОДИМ СПЕКТРАЛЬНЫЙ ИНДЕКС MNDWI
#MNDWI = (Green[2] - SWIR2[6]) / (Green[2] + SWIR2[6])
mndwi1 = (pic1[2] - pic1[6]) / (pic1[2] + pic1[6])

#УБИРАЕМ ВЫБРОСЫ ЗНАЧЕНИЙ 
mndwi1[mndwi1 < -1] = -1
mndwi1[mndwi1 > 1] = 1

#ОТОБРАЖАЕМ ИНДЕКС НА ГРАФИКЕ
Graph(mndwi1, 'Blues', "mndwi")

#КЛАССИФИЦИРУЕМ ВОДУ ПО ПОРОГУ В 0.18
Classif(mndwi1)

#СТРОИМ ГИСТОГРАММУ ЗНАЧЕНИЙ ДЛЯ ИНДЕКСА 
ep.hist(mndwi1, figsize=(12, 6), title=["mndwi"])
plt.show()

#СТРОИМ ГИСТОГРАММУ  ДЛЯ ВОДНЫХ ПИКСЕЛЕЙ
ep.hist(mndwi1[mndwi1>=0.18], figsize=(12, 6), title=["mndwi - вода"])
plt.show()

#ГИСТОГРАММА ДЛЯ НЕВОДНЫХ ПИКСЕЛЕЙ
#максимум здесь - скорей всего фон
ep.hist(mndwi1[mndwi1<0.18], figsize=(12, 6), title=["mndwi - не вода"])
plt.show()