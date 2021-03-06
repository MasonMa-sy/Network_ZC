from __future__ import absolute_import
import numpy as np
from network_zc.tools import file_helper_unformatted, data_preprocess, name_list
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
import network_zc.keras_contrib.backend as KC
import math
import struct



def pearson(vector1, vector2):
    n = len(vector1)
    #simple sums
    sum1 = sum(float(vector1[i]) for i in range(n))
    sum2 = sum(float(vector2[i]) for i in range(n))
    #sum up the squares
    sum1_pow = sum([pow(v, 2.0) for v in vector1])
    sum2_pow = sum([pow(v, 2.0) for v in vector2])
    #sum up the products
    p_sum = sum([vector1[i]*vector2[i] for i in range(n)])
    #分子num，分母den
    num = p_sum - (sum1*sum2/n)
    den = math.sqrt((sum1_pow-pow(sum1, 2)/n)*(sum2_pow-pow(sum2, 2)/n))
    if den == 0:
        return 0.0
    return num/den


def pearson_distance(vector1, vector2):
    """
    Calculate distance between two vectors using pearson method
    See more : http://en.wikipedia.org/wiki/Pearson_product-moment_correlation_coefficient
    """
    sum1 = sum(vector1)
    sum2 = sum(vector2)

    sum1Sq = sum([pow(v, 2) for v in vector1])
    sum2Sq = sum([pow(v, 2) for v in vector2])

    pSum = sum([vector1[i] * vector2[i] for i in range(len(vector1))])

    num = pSum - (sum1 * sum2 / len(vector1))
    den = math.sqrt((sum1Sq - pow(sum1, 2) / len(vector1)) * (sum2Sq - pow(sum2, 2) / len(vector1)))

    if den == 0: return 0.0
    return num / den


def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab

def corrcoef(x,y):
    n=len(x)
    #求和
    sum1=sum(x)
    sum2=sum(y)
    #求乘积之和
    sumofxy=multipl(x,y)
    #求平方和
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #计算皮尔逊相关系数
    den=math.sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return num/den


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

myfont = matplotlib.font_manager.FontProperties(fname="Light.ttc")
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots()
plt.tick_params(labelsize=15)
labels = ax.get_xticklabels() + ax.get_yticklabels()
[label.set_fontname('Times New Roman') for label in labels]

font = {'family': 'Times New Roman',
             'weight': 'normal',
             'size': 15}
row1 = '练度'
row2 = '星级'
plt.legend([row1, row2], loc='upper right', prop=font, framealpha=1)
ax.set_title('练度/星级与氪金')
ax.set_ylabel('练度/星级', font)
ax.set_xlabel('氪金', font)
plt.show()