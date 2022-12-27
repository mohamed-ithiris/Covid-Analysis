import pandas as pd
import matplotlib.pyplot as plt


def case_per_country():
    while True:
        try:
            print("Please, enter one of the following continent names:")
            print(
                "North America, South America, Asia, Europe, Africa, Australia/Oceania")
            userInput = input("Please type the continents's name:")
            continents = [
                "North America",
                "South America",
                "Asia",
                "Europe",
                "Africa",
                "Australia/Oceania"
            ]
            if (userInput in continents):
                data = pd.read_csv(
                    "./worldometer_data.csv",
                    usecols=[
                        'Country/Region',
                        'Continent',
                        'TotalCases',
                        'TotalRecovered',
                        'TotalDeaths'
                    ]
                )
                filterContinent = data['Continent'] == userInput

                # get filtered data
                filtered_data = data[filterContinent]
                country_list = filtered_data['Country/Region']
                total_cases = filtered_data['TotalCases']
                total_deaths = filtered_data['TotalDeaths']
                total_recovered = filtered_data['TotalRecovered']

                x_axis = country_list.tolist()
                y_axis_total_cases = total_cases.tolist()
                y_axis_total_deaths = total_deaths.tolist()
                y_axis_total_recovered = total_recovered.tolist()

                # stacked barplot
                plt.bar(x_axis, y_axis_total_cases, color='b')
                plt.bar(x_axis, y_axis_total_deaths, color='r')
                plt.bar(x_axis, y_axis_total_recovered, color='g')
                plt.show()
                break
            else:
                print("Enter valid continents name")
        except ValueError:
            print("Enter valid continents name")


def main():
    while True:
        print("Welcome to our analysis Pipeline for COVID-19 data")
        print("Please, select one of the following options:")
        print("1 - Display cases per country in a specific continent.")
        print("2 - Calculate the Recovered and Death percentages per country in a specific continent.")
        print("3 - Display number of tests per continent.")
        print("4 - Display the Daily vaccinations of a specific country.")
        print("5 - Exit.")
        userInput = input("Enter the number:")
        try:
            val = float(userInput)
            if (val == 1):
                case_per_country()
                break
            elif (val == 2):
                print("Please, enter one of the following continent names:")
                print(
                    "North America, South America, Asia, Europe, Africa, Australia/Oceania")
                print("Please type the continents's name")
                break
            elif (val == 3):
                print("option 3")
                break
            elif (val == 4):
                print("Please, enter one of the following country names:")
                print("Ireland, USA, India, Brazil, Japan, Australia")
                break
            elif (val == 5):
                print("Existed")
                break
            elif (val > 5 or val < 1):
                print("Enter number between 1 to 5!")
        except ValueError:
            print("Enter number between 1 to 5!")


main()
