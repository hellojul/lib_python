import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import geopandas as gpd

# 1. Tracer une carte du monde basique
def plot_basic_world_map():
    plt.figure(figsize=(12, 6))
    m = Basemap()
    m.drawcoastlines()
    plt.title('Carte du Monde Basique')
    plt.show()

# 2. Tracer une carte avec des coordonnées (points latitude/longitude)
def plot_points_on_map(latitudes, longitudes, title='Points sur la Carte du Monde'):
    plt.figure(figsize=(12, 6))
    m = Basemap()
    m.drawcoastlines()
    m.scatter(longitudes, latitudes, latlon=True, marker='o', color='r', zorder=5)
    plt.title(title)
    plt.show()

# 3. Charger et afficher des données géographiques avec GeoPandas
def plot_geopandas_world_map():
    world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    world.plot()
    plt.title('Carte du Monde avec GeoPandas')
    plt.show()

# 4. Tracer des frontières de pays
def plot_country_boundaries():
    plt.figure(figsize=(12, 6))
    m = Basemap()
    m.drawcoastlines()
    m.drawcountries()
    plt.title('Carte du Monde avec Frontières de Pays')
    plt.show()

# 5. Zoomer sur une région spécifique du monde
def zoom_on_region(llcrnrlat, llcrnrlon, urcrnrlat, urcrnrlon, resolution='l'):
    plt.figure(figsize=(12, 6))
    m = Basemap(llcrnrlat=llcrnrlat, llcrnrlon=llcrnrlon, urcrnrlat=urcrnrlat, urcrnrlon=urcrnrlon, resolution=resolution)
    m.drawcoastlines()
    m.drawcountries()
    plt.title(f'Zoom sur la région [{llcrnrlon}, {llcrnrlat}] à [{urcrnrlon}, {urcrnrlat}]')
    plt.show()

