import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from network_zc.tools import file_helper_unformatted


def get_sst_equatorial(data_2d):
    sst_equatorial = []
    for j in range(27):
        sst_equatorial_temp = 0
        for i in range(7, 13):
            sst_equatorial_temp += data_2d[i][j][0]
        sst_equatorial.append(sst_equatorial_temp/6)
    return sst_equatorial


def get_sst_equatorial_from_data(file_num1, month1, internal_file_path):
    sst_equatorial = np.empty([month1, grid_length])
    for i in range(file_num1, file_num1+month1):
        # data = file_helper_unformatted.read_data_historical(internal_file_path, i)
        data = file_helper_unformatted.read_data_best(internal_file_path, i)
        sst_equatorial[i-file_num1] = get_sst_equatorial(data)
    return sst_equatorial


file_num = 417
month = 47
# This need to change to get different fig.
directly_month = 3

grid_length = 27
east_border = 101.25
west_border = 73.125
x_resolution = 5.625
north_border = 29
south_border = -29
y_resolition = 2

lons = np.arange(east_border + 5 * x_resolution, 360 - west_border - 2 * x_resolution + 0.5, x_resolution)
lats = np.arange(south_border + 5 * y_resolition, north_border - 5 * y_resolition + 0.5, 2)

width_sst = 360 - west_border - 2 * x_resolution - east_border - 5 * x_resolution
height_sst = north_border - 5 * y_resolition - south_border - 5 * y_resolition

lon_0 = lons.mean()
lat_0 = lats.mean()

model_name = 'conv_model_dimensionless_1_ZC_sc_1_to_historical@best'
# model_name = 'conv_model_dimensionless_1_ZCforced_sc@best'
file_hisotircal = 'D:\msy\projects\zc\zcdata\data_historical'
file_path1 = "D:\msy\projects\zc\zcdata\data_networks\\best\\" + model_name + '\\' + str(directly_month)

sst_equatorials = get_sst_equatorial_from_data(file_num+directly_month, month, file_path1)

print(sst_equatorials)
fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0, grid_length-1, grid_length, dtype=int)
y = np.linspace(0, month-1, month, dtype=int)
plt.xlim(0, grid_length-1)
plt.ylim(0, month-1+6-directly_month)
x_ticks1 = np.linspace(1.8888, 23.2222, 4)
x_ticks2 = ['140E', '180', '140W', '100W']
plt.xticks(x_ticks1, x_ticks2)
y_ticks1 = np.arange(-directly_month, month-directly_month+6, 12, dtype=int)
y_ticks2 = np.arange(file_num, file_num+month+6, 12, dtype=int)
plt.yticks(y_ticks1, y_ticks2)

v = np.linspace(-1.8, 3.0, 9, endpoint=True)
plt.contourf(x, y, sst_equatorials, v)
plt.set_cmap('jet')
# plt.contour(x, y, ssta_error_all, 20)
position = fig.add_axes([0.15, 0.05, 0.7, 0.03])
plt.colorbar(cax=position, orientation='horizontal')

ax.set_title('Historical SSTA', fontsize=12, fontname='Times New Roman')
# ax.set_title('CNN-TRANS prediction SSTA of 3-month lead', fontsize=12, fontname='Times New Roman')
# ax.set_title('CNN-TRANS prediction SSTA of 6-month lead', fontsize=12, fontname='Times New Roman')
plt.show()


