import pandas as pd
import sys

# read in dataframe
df = pd.read_pickle('data/game_df_pickle.pkl')

# function to run game
def game():
    # pick a random row from dataframe
    row = df.sample(1)

    # output year, price, and nhood
    print('\033[94m' + 'Year:', row.year.iloc[0], '| Price:', row.price_adjusted.iloc[0], '| Nhood:', row.nhood.iloc[0])

    # prompt user to guess number of beds
    guess_beds = int(input('Guess number of beds: '))

    # prompt user to guess number of baths
    guess_baths = float(input("Guess number of baths (don't forget to end in .0 or .5): "))

    # if guesses are correct, turn screen green
    if guess_beds == row.beds.iloc[0] and guess_baths == row.baths.iloc[0]:
        print('\033[92m' + 'Correct!')
    # if guesses are incorrect, turn screen red and print correct values
    else:
        print('\033[91m' + 'Incorrect. The correct number of beds is', row.beds.iloc[0],
              'and the correct number of baths is', row.baths.iloc[0])

    # ask if user wants to play again
    again = input('Do you want to play again? (y/n): ')

    # if yes, restart game
    if again == 'y':
        game()
    # if no, exit
    else:
        sys.exit()

# call game
game()