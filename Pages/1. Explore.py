# import packages
import streamlit as lit
import pandas as pd
import folium
from streamlit_folium import st_folium as lit_folium

# load the data, only data with non-null latitude and longitude
df = pd.read_pickle('Pages/data/df_ll_pickle.pkl')

# get a list of years and sort
list_of_years = df.year.unique().tolist()
list_of_years.sort()
list_of_years = [str(year) for year in list_of_years]
list_of_years.insert(0, None)

# we create a sidebar menu to select year
year = lit.sidebar.selectbox("Select the listing year you want to filter on...",  # leading text
                             list_of_years,  # list of values
                             index=0,  # start pre-filtered on the first year on the list
                             key=1)  # key for this streamlit object

# get a list of the relevant neighborhoods
list_of_nhoods = df.nhood.unique().tolist()
list_of_nhoods.sort()
list_of_nhoods.insert(0, None)

# now a sidebar menu for picking a neighborhood
nhood = lit.sidebar.selectbox("Select the neighborhood you want to filter on...",  # leading text
                              list_of_nhoods,  # list of values
                              index=0,
                              key=2)  # key for this streamlit object

# create a radius size column with relative sizing
a, b = 0, 1
x, y = df.sqft.min(), df.sqft.max()
df['rad'] = (df.sqft - x) / ((y - x) * (b - a) + a)
df['rad'] = df['rad'] * 25

# create a color palette
palette = {'#F6E58D', '#F4A261', '#CB4335', '#2F3640', '#FFE600', '#85C1E9', '#F6DDCC', '#8E44AD', '#00B16A',
           '#6C5B7B', '#F39C12', '#2ECC71', '#16A085', '#D2B4DE', '#F7DC6F', '#7D6608', '#E67E22', '#A569BD'}

# creating a color map dictionary
colormap = {}

# mapping colors to years between 2007 and 2019
year_start = 2001
for color in palette:
    colormap[year_start] = color
    year_start += 1


def show_map(year, nhood):
    # actually making the map
    northern_california_map = folium.Map(location=[37.5, -120.3], zoom_start=8, tiles='Stamen Terrain')

    # check for filtering
    if nhood is not None and year is not None:
        df_filtered = df[df["nhood"] == nhood].copy(deep=True)
        df_filtered = df_filtered[df_filtered["year"] == nhood].copy(deep=True)
    elif nhood is not None:
        df_filtered = df[df["nhood"] == nhood].copy(deep=True)
    elif year is not None:
        df_filtered = df[df["year"] == int(year)].copy(deep=True)
    else:
        df_filtered = df.copy(deep=True)

    for lat, lng, year, beds, baths, price, sqft, rad in zip(df_filtered.lat, df_filtered.lon, df_filtered.year,
                                                             df_filtered.beds, df_filtered.baths, df_filtered.price,
                                                             df_filtered.sqft, df_filtered.rad):
        folium.CircleMarker((lat, lng),
                            radius=rad,
                            fill=True,
                            color=False,
                            fill_color=colormap[year],
                            fill_opacity=0.8,
                            tooltip=(str(beds) + " Beds, " + str(baths) + " Baths, " + " Monthly Rent: $" + str(
                                price) + " Sqft: " + str(sqft))).add_to(northern_california_map)
    item = lit_folium(northern_california_map, width=1200, height=600)
    return item


# texts
lit.header("A map of the City's rental properties.")
lit.subheader("Craigslist Bay Area Rentals 2007-2018")
lit.write("Using the following map. I encourage you to get a sense of the rental landscape in the San Francisco Area.\n"
          "Spend some time really digging into the details of the listings, stuff like square-footage and number of "
          "beds and baths.")
display_map = show_map(year, nhood)
lit.write('*Marker radius size is relative to the square-footage of the rental property.')
lit.write('*Avoid taking more than one action at a time, let the map finish loading between each action.')
