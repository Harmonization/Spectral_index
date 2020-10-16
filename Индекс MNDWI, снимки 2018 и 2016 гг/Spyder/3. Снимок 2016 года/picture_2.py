#ЗДЕСЬ АНАЛИЗИРУЕТСЯ ВТОРОЙ СНИМОК

from imp_and_def import*

#Загружаем фото 2016 года
pic2 = CreatePath("2016.10.09", "*band*.tif", "my_outputs", "out.tif") # 9 октября

#НАХОДИМ СПЕКТРАЛЬНЫЙ ИНДЕКС MNDWI
#MNDWI = (Green[2] - SWIR2[6]) / (Green[2] + SWIR2[6])
mndwi2 = (pic2[2] - pic2[6]) / (pic2[2] + pic2[6])

#УБИРАЕМ ВЫБРОСЫ ЗНАЧЕНИЙ 
mndwi2[mndwi2 < -1] = -1
mndwi2[mndwi2 > 1] = 1

#ОТОБРАЖАЕМ ИНДЕКС НА ГРАФИКЕ
Graph(mndwi2, 'Blues', "mndwi")

#КЛАССИФИЦИРУЕМ ВОДУ ПО ПОРОГУ В 0.18
Classif(mndwi2)

#СТРОИМ ГИСТОГРАММУ ЗНАЧЕНИЙ ДЛЯ ИНДЕКСА 
ep.hist(mndwi2, figsize=(12, 6), title=["mndwi"])
plt.show()

#СТРОИМ ГИСТОГРАММУ  ДЛЯ ВОДНЫХ ПИКСЕЛЕЙ
ep.hist(mndwi2[mndwi2>=0.18], figsize=(12, 6), title=["mndwi - вода"])
plt.show()

#ГИСТОГРАММА ДЛЯ НЕВОДНЫХ ПИКСЕЛЕЙ
#максимум здесь - скорей всего фон
ep.hist(mndwi2[mndwi2<0.18], figsize=(12, 6), title=["mndwi - не вода"])
plt.show()