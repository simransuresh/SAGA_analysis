import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap, shiftgrid
from compute_gsc import lats, lons
from temporal_mean import dot_mean, ug_mean, vg_mean

longitudes, latitudes = np.meshgrid(lons, lats)

m = Basemap(projection='nplaea', boundinglat=60, lon_0=0, resolution='l', round=True, llcrnrlat=-60, urcrnrlat=60,
            llcrnrlon=-180, urcrnrlon=180)
fig1 = plt.figure(figsize=(6, 6))
ax = fig1.add_axes([0.1,0.1,0.8,0.8])

im = m.pcolormesh(longitudes,latitudes,dot_mean,cmap=plt.cm.YlGnBu, latlon=True)
cbar = plt.colorbar(im, ax=ax, orientation='vertical')
cbar.set_label('DOT (m)')
im.set_clim(0, 0.8)

x, y = m(longitudes, latitudes)
# print(x, y)

ugrid, newlons = shiftgrid(180., ug_mean, lons, start=False)
vgrid, newlons = shiftgrid(180., vg_mean, lons, start=False)

uproj, vproj, xx, yy = m.transform_vector(ugrid, vgrid, newlons, lats, 32, 32, returnxy=True, masked=True)
# print(xx, yy)

Q = m.quiver(xx, yy, uproj, vproj, scale=1.2, width=0.004)
qk = plt.quiverkey(Q, 0.1, 0.1, 0.05, '10 cm/s', labelpos='W')
m.drawcoastlines(linewidth=1.5)
m.drawparallels(range(60, 91, 10), labels=[1, 1, 1])
m.drawmeridians(range(-180, 181, 60), labels=[1, 1, 1, 1])
plt.show()
# plt.savefig('total_mean.png', dpi=300)



