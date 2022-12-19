# import necessary packages
import pandas as pd
import folium

df_ll = pd.read_pickle('data/df_ll_pickle.pkl')

a, b = 0, 1
x, y = df_ll.sqft.min(), df_ll.sqft.max()
df_ll['rad'] = (df_ll.sqft - x) / (y - x) * (b - a) + a
df_ll['rad'] = df_ll['rad']*20

palette = colors = {'#F6E58D', '#F4A261', '#CB4335', '#2F3640', '#FFE600', '#85C1E9', '#F6DDCC', '#8E44AD', '#00B16A',
                    '#6C5B7B', '#F39C12', '#2ECC71', '#16A085', '#D2B4DE', '#F7DC6F', '#7D6608', '#E67E22', '#A569BD'}

# creating a color map dictionary
colormap = {}

# mapping colors to years between 2001 and 2018
year = 2001
for color in palette:
    colormap[year] = color
    year += 1

loc = 'Exploring the City: Craigslist Bay Area Rentals 2001-2018'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)


northern_california_map = folium.Map(location=[38.5, -122.3], zoom_start=7, tiles='OpenStreetMap')

for lat, lng, year, beds, baths, price, sqft, rad in zip(df_ll.lat, df_ll.lon, df_ll.year, df_ll.beds, df_ll.baths, df_ll.price, df_ll.sqft, df_ll.rad):
    folium.CircleMarker((lat, lng), radius=rad,fill=True,color=False, fill_color=colormap[year],fill_opacity=0.8,tooltip=("Beds: "+str(beds)+" Baths: "+str(baths)+" Price: $"+str(price)+" Year: "+str(year) +" Sqft: "+str(sqft))).add_to(northern_california_map)

northern_california_map.get_root().html.add_child(folium.Element(title_html))

northern_california_map.save('cm1930_map.html')