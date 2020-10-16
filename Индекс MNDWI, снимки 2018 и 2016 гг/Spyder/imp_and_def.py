#ИМПОРТ НЕОБХОДИМЫХ МОДУЛЕЙ И ОПИСАНИЕ ФУНКЦИЙ

import os
from glob import glob 
import matplotlib.pyplot as plt
from matplotlib import patches as mpatches
from matplotlib.colors import ListedColormap
from matplotlib import colors
import seaborn as sns
import numpy as np
import geopandas as gpd
from shapely.geometry import mapping, box
import rasterio as rio
from rasterio.plot import plotting_extent
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep

# Prettier plotting with seaborn
sns.set_style('white')
sns.set(font_scale=1.5)

# Download data and set working directory
data = et.data.get_data('cold-springs-fire')
os.chdir(os.path.join(et.io.HOME, 'Landsat_8', 'data'))

def CreatePath(input_path, inp_p, output_path, out_p):
    # Создаем путь к снимку
    path_pic1 = os.path.join(input_path, inp_p)

    # Генерируем список tif файлов
    list_pic1 = glob(os.path.join(path_pic1))

    # Сортируем спектральные полосы 
    list_pic1.sort()
    
    # Создаем выходной массив 
    path_out1 = os.path.join(output_path, out_p)

    # Получим новый список с уложенными друг на друга полосами
    pic1, meta1 = es.stack(list_pic1, path_out1)
    
    #вернем список полос
    return pic1

#СТРОИТ ИЗОБРАЖЕНИЕ СПЕКТРАЛЬНОГО ИНДЕКСА
def Graph(index, color, name):
    fig, ax = plt.subplots(figsize=(12, 12))
    
    ep.plot_bands(index,
              cmap=color,
              vmin=-1, vmax=1,
              title=name,
              ax=ax,
              scale=False)
    plt.show()

#СТРОИТ ИЗОБРАЖЕНИЕ ИНДЕКСА, В КОТОРОМ ИНТЕРВАЛЫ ЗНАЧЕНИЙ КЛАССИФИЦИРОВАНЫ
#И ОБОЗНАЧЕНЫ СООТВЕТСТВУЮЩИМ ЦВЕТОМ 
def Classif(mndwi, mndwi_class_bins = [-np.inf, 0,  0.18, np.inf], mndwi_colors = ["linen", "lightsteelblue", "blue"], mndwi_class_names = ["Не вода", "Фон", "Вода",
    ]):
    # Классифицируем
    mndwi_landsat_class = np.digitize(mndwi, mndwi_class_bins)

    # Применим маску к классам
    mndwi_landsat_class = np.ma.masked_where(np.ma.getmask(mndwi), mndwi_landsat_class)

    # Сolor map
    mndwi_cmap = ListedColormap(mndwi_colors)


    # Создадим список классов
    classes = np.unique(mndwi_landsat_class)
    classes = classes.tolist()
    # The mask returns a value of none in the classes. remove that
    classes = classes[0:5]

    # Отобразим результат
    fig, ax = plt.subplots(figsize=(12, 12))
    im = ax.imshow(mndwi_landsat_class, cmap=mndwi_cmap)

    ep.draw_legend(im_ax=im, classes=classes, titles=mndwi_class_names)
    ax.set_title("mndwi - маска", fontsize=14)
    ax.set_axis_off()

    # Auto adjust subplot to fit figure size
    plt.tight_layout()

