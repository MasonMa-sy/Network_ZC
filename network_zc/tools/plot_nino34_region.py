import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

east_border = 101.25
west_border = 73.125
x_resolution = 5.625
north_border = 29
south_border = -29
y_resolition = 2

lons = np.arange(east_border + 5 * x_resolution, 360 - west_border - 2 * x_resolution + 0.5, x_resolution)
lats = np.arange(south_border + 5 * y_resolition, north_border - 5 * y_resolition + 0.5, 2)

lon_0 = lons.mean()
lat_0 = lats.mean()


m = Basemap(lat_0=lat_0, lon_0=lon_0, llcrnrlon=100,
            llcrnrlat=-30, urcrnrlon=290, urcrnrlat=30,
            resolution='l')
m.drawparallels(lats, labels=[1, 0, 0, 0], fontsize=10)
m.drawmeridians(lons, labels=[0, 0, 0, 1], fontsize=10)

x = np.arange(360-150, 360-90+0.5, 60)
y = np.arange(-5, 5+0.5, 10)
x, y = np.meshgrid(x, y)
xi, yi = m(x, y)
f = np.abs(x) + np.abs(y) - 1
cs = m.contourf(xi, yi, f)

plt.show()

