import streamlit as lit

lit.header("A Rental Price Learning Experience")
lit.subheader("From Maps to Play")

lit.write('1. The "Explore" tab features a map of all the listings in the data that contain coordinates. The '
          'properties are marked by circles colored by the year and sized according to a standardized measure of the '
          'square-footage of the property. The goal is for you to be accustomed to with the neighborhoods and the key '
          'features of the property. It is often the case that we have a sense of where "expensive" and "big" homes '
          'are, but sometimes the nature of which homes are for rent change over the course of time, and of course, '
          'prices also tend to rise.')

lit.write('2. The "Trending" tab is a graphical view of a square foot or a gallon of gasoline based on the price in '
          '2011. Using the slider, you can see how the relative purchasing power for the same number of dollars and '
          'how it changed. The black background square serves as the 2011 base, a red square is over-layed to show the '
          'new square-footage if the value is decreased. A green square is over-layed to show that the buying power '
          'has increased (the same money got you more value that year).')

lit.write("3. The final 'Game' tab serves to evaluate what you've taken away (it might even be helpful to play before "
          "and after using the other two tabs). Essentially, you'll be given some key information about a rental "
          "listing and you'll be made to guess the number of beds and baths. For the sake of easy, only listings with "
          "whole numbers of beds and baths are included. Comparing the change in gas prices to the change in rental "
          "prices should also elucidate that certain economic conditions effected different purchasing powers "
          "differently.")