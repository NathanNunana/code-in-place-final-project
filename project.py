"""
Filename: Project.py
--------------------
This program is a covid 19 data visualizer
It operates by getting input from the user,
this input is will be entered based on the options
provided by the program and it will then display a map
of a particular day and the cases recoded on that day
"""
import pandas as pd
import plotly.express as px


def main():
  continents = []
  # read the covid 19 data and assign it to a variable
  df = pd.read_csv("https://covid.ourworldindata.org/data/owid-covid-data.csv")
  df = df.fillna("")
  continent = get_continent(df, continents)
  continents.remove("Oceania")
  display_continents(continents)
  data = get_input(continents)
  if data == None:
    data = "world"
  else:
    df = df[df.continent == data]
  fig = display_choropleth(df, str(data))
  fig.show()


"""
Getting the continents from the dataframe and appending
each of the continents uniquely to a list.
"""
def get_continent(df, continents):
  for continent in df.continent:
    if continent not in continents:
      continents.append(continent)


"""
Displaying the various continents from the list of continents
to enable user to distinguish between the available continents he
can choose from.
"""
def display_continents(continents):
  print("Available Continents\n---------------------")
  for continent in continents:
    if continent == "":
      continents.remove(continent)
    else:
      print(continent)


"""
Function prompts the user to enter a continent or to press enter to 
display entire continent, in case the user enters a continent that's not
part of the continent's displayed on the screen it's send a feedback to
the user and reprompts for another input
"""
def get_input(continents):
  while True:
    data = input("Enter Continent or Press Enter to show all continent: ")
    if data == "":
      break
    if data not in continents:
      display_continents(continents)
      print("Iinvalid input, Choose the continent from the list above")
    else:
      return data


"""
Function creates the map based on the continent the user entered and the data frame
containing the covid cases
"""
def display_choropleth(df, data):
  fig = px.choropleth(df, locations="iso_code", color="new_cases",
                    hover_name="location", animation_frame="date",
                    title = "Covid 19 Data Visualizer", scope = data.lower(),
                    color_continuous_scale=px.colors.sequential.PuRd)
  return fig


if __name__ == "__main__":
    main()