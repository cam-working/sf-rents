# import packages
import streamlit as lit
import pandas as pd

# save state list to make things run more smoothly
options = ['df_play', 'row', 'guess_beds', 'guess_baths', 'count', 'value']

# save things to the save state
for key in options:
    if key not in lit.session_state:
        lit.session_state[key] = None

# index for game selection
if lit.session_state.count is None:
    lit.session_state.count = 0

# text headings
lit.title("SF Real Estate Guessing Game")
lit.write("Now that you've been primed on some specific cases with the map,\n"
          "and the greater trends of affordability in the city,\n"
          "let's see if you can correctly idetify some features of some of the rental properties.")


# non-standard function, basically wraps a series of data frame actions so they play nicely with streamlit
@lit.cache()
def get_df():
    df = pd.read_pickle('pages/data/game_df_pickle.pkl')
    df1 = df[['year', 'nhood', 'beds', 'baths', 'sqft', 'price_adjusted']].copy(deep=True)
    df2 = df1.astype(str).copy(deep=True)
    df3 = df2[df2['baths'].str[2].eq('0')].copy(deep=True)
    df3['baths'] = df3['baths'].str[0]
    df3['price_adjusted'] = df3['price_adjusted'].str[:-2]
    df3['nhood'] = df3['nhood'].str.title()
    df4 = df3[df3['sqft'] != 'nan'].copy(deep=True)
    df4['sqft'] = df4['sqft'].str[:-2]
    return df4

# this function grabs a limited set of rows in the data frame so that the game can be played
@lit.cache()
def run_item(value):
    thing = df_z.sample(n=100, random_state=8888).iloc[value]
    return thing

# run the above functions
df_z = get_df()
lit.session_state.df_play = run_item(lit.session_state.count)

# prompt for the player with the key info
lit.subheader(
    f'Prompt: {lit.session_state.df_play.year} listing in {lit.session_state.df_play.nhood.title()}, going for ${lit.session_state.df_play.price_adjusted} per Month, it is {lit.session_state.df_play.sqft} square feet.')

# user inputs for playing the game
lit.session_state.guess_beds = lit.text_input('Guess the # of bedrooms, ex. 2')
lit.session_state.guess_baths = lit.text_input('Guess the # of bedrooms, ex. 1')

# to submit the answer
submit = lit.button('Press to Submit!')

# prints after submission indicating correct or incorrect response
if submit:
    if lit.session_state.guess_beds == lit.session_state.df_play.beds and lit.session_state.guess_baths == lit.session_state.df_play.baths:
        lit.markdown(":white_check_mark::white_check_mark::white_check_mark: You got it right! "
                     ":white_check_mark::white_check_mark::white_check_mark:")
    else:
        lit.write(":x::x::x: Sorry! Try Again! :x::x::x:")

# this goes to the next prompt
check_next = lit.button('Press for Next!')
if check_next:
    lit.session_state.count += 1
view = lit.button('Press to View Prompt')

# this displays the next prompt
if view:
    backgroundColor = '0F110C'
