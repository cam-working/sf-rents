# import libraries
import streamlit as lit
import matplotlib.pyplot as plt
import pandas as pd

# creates the sidebar selector
view = lit.sidebar.radio('View either gas prices or rent and how buying power shifts over time for either!', ['Gas', 'Rent'])

# based on selection download one of two dataframes
if view == 'Gas':
    df = pd.read_pickle('Pages/data/gas_dat_pickle.pkl')
    df['side_length'] = df['max_price_r'] ** (1 / 2)
    df['shift_plt'] = (1 - df['side_length']) / 2
    lit.header("Same Money, Less GasSquare-Footage")
    lit.subheader("Relative Purchasing Power of 2011's Price Per Gallon Over the Next Decade")
elif view == 'Rent':
    df = pd.read_pickle('Pages/data/full_year_dat_pickle.pkl')
    df['side_length'] = df['ppsf_i'] ** (1 / 2)
    df['shift_plt'] = (1 - df['side_length']) / 2
    lit.header("Same Money, Less Square-Footage")
    lit.subheader("Relative Purchasing Power of 2011's Price Per Square Foot Over the Next Decade")

# slider for each year
year_i = lit.slider('What year?', 2011, 2018, 2011, 1)

# Create figure and axes
fig, ax = plt.subplots(1)

# Remove background, ticks, and spines
ax.patch.set_facecolor('none')
ax.set_xticks([])
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)


# Plot gray square
def overlay_2011(opacity):
    ax.add_patch(plt.Rectangle((0, 0), 10, 10, facecolor='black', edgecolor=None, alpha=opacity))


# Plot red square
def overlay_year_2(color):
    ax.add_patch(plt.Rectangle((0 + df.iloc[year_i - 2011].shift_plt, 0 + df.iloc[year_i - 2011].shift_plt),
                               1 * df.iloc[year_i - 2011].side_length, 1 * df.iloc[year_i - 2011].side_length,
                               facecolor=color, edgecolor=None))


# check which square should be plotted first
if 1 * df.iloc[year_i - 2011].side_length > 1:
    overlay_year_2("green")
    overlay_2011(0.1)
    if view == 'Rent':
        note = "The purchasing power actually went up ever so slightly in 2012, instead of 1 square-foot, $2.89 could " \
               "buy you 1.0102 square-feet"
    else:
        note = ''
elif 1 * df.iloc[year_i - 2011].side_length == 1:
    overlay_2011(1)
    if view == 'Gas':
        note = "Check out this [article](https://www.npr.org/2011/06/24/137387929/obama-releases-oil-to-counter-lost" \
               "-libyan-production) to get a glipmse into how the federal government intervened with Gas prices. "
    else:
        note = ''
else:
    overlay_2011(1)
    overlay_year_2("red")
    note = ''

# Show the plot
lit.pyplot(plt)
lit.write(note)
