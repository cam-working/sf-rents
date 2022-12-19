# import the relevant packages
import pandas as pd
import cpi

# get the latest in cpi information
cpi.update()

# upload the downloaded data
main = pd.read_csv('clean_2000_2018.csv', low_memory=False)

# get the relevant columns
main = main[
    ['post_id', 'date', 'year', 'nhood', 'city', 'county', 'price', 'beds', 'baths', 'sqft', 'room_in_apt', 'address',
     'lat', 'lon']]

# use the cpi to adjust the price for the rental pricing
main["price_adjusted"] = main.apply(
    lambda x: cpi.inflate(x.price, x.year, items="Housing", area = 'San Francisco-Oakland-Hayward, CA'), axis=1
)

# using the adjusted price, we get the price per square foot where available
main['ppsf'] = main['price_adjusted'] / main['sqft']

# grab only the dataframe where this value is not null
full = main[main['ppsf'].notnull()].copy()

# create a group by of this data so that we can chase the trend
# only include the groups with more than 1000 observations
full_year = full.groupby('year').filter(lambda x: len(x) > 1000).groupby('year').mean()

# create a ratio
full_year['ppsf_i'] = full_year.iloc[0]['ppsf']/full_year['ppsf']

# repeat the process for gas, with downloaded gas prices
gas = pd.read_csv("gas_prices.csv")
gas["max_adjusted"] = gas.apply(
    lambda x: cpi.inflate(x.max_price, x.year), axis=1)

# convert the beds to an integer number
main['beds'] = main['beds'].astype(int)

# only get the results from neighborhoods with large counts
main = main[main['nhood'].isin(
    ['santa rosa', 'santa cruz', 'sunnyvale', 'santa clara', 'san jose south', 'SOMA / south beach', 'union city',
     'mountain view', 'san jose north', 'dublin / pleasanton', 'san jose central', 'san mateo', 'san jose west',
     'cupertino', 'san rafael', 'palo alto', 'petaluma', 'napa county', 'foster city', 'campbell',
     'hayward / castro valley', 'redwood city', 'vallejo / benicia', 'rohnert pk / cotati', 'fairfield / vacaville',
     'novato', 'daly city', 'walnut creek'])]

