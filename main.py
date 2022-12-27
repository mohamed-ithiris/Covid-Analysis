import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
                plt.xlabel("Country")
                plt.ylabel("Cases")
                plt.title("Case per country in a specific continent")
                plt.show()
                break
            else:
                print("Enter valid continents name")
        except ValueError:
            print("Enter valid continents name")


def relationship_recoverd_death():
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
                csv_data = pd.read_csv(
                    "./worldometer_data.csv",
                    usecols=[
                        'Country/Region',
                        'Continent',
                        'TotalRecovered',
                        'TotalDeaths'
                    ]
                )

                filterContinent = csv_data['Continent'] == userInput
                filtered_data = csv_data[filterContinent]

                sns.lmplot(
                    x='TotalDeaths',
                    y='TotalRecovered',
                    data=filtered_data
                )
                plt.show()
                break
            else:
                print("Enter valid continents name")
        except ValueError:
            print("Enter valid continents name")


def test_per_contitent():
    while True:
        try:
            csv_data = pd.read_csv(
                "./worldometer_data.csv",
                usecols=[
                    'Country/Region',
                    'Continent',
                    "Tests/1M pop"
                ]
            )

            unique_continent = pd.DataFrame(
                csv_data).Continent.unique().tolist()
            continent_list = [x for x in unique_continent if str(x) != 'nan']
            x_axis = []
            y_axis = []

            for continent in continent_list:
                filtered_data = csv_data[csv_data['Continent'] == continent]
                print(continent,"-",filtered_data["Continent"].count())
                x_axis.append(continent)
                y_axis.append(filtered_data["Tests/1M pop"].sum())


            plt.bar(
                x_axis,
                y_axis,
                color='green',
                width=0.4
            )
            plt.xlabel("Continent")
            plt.ylabel("Tests/1M pop")
            plt.title("Number of tests per continent")
            plt.show()
            break
        except ValueError:
            print("Enter valid continents name")


def daily_vaccination():
    while True:
        try:
            print("Please, enter one of the following country names:")
            print("Ireland, USA, India, Brazil, Japan, Australia")
            userInput = input("Please type the countires's name:")
            country = [
                "Ireland",
                "USA",
                "India",
                "Brazil",
                "Japan",
                "Australia"
            ]
            if (userInput in country):
                csv_data = pd.read_csv(
                    "./country_vaccinations.csv",
                    usecols=[
                        'country',
                        'date',
                        'daily_vaccinations',
                    ]
                )

                filterContinent = csv_data['country'] == userInput
                filtered_data = csv_data[filterContinent]
                filtered_data.plot('date', 'daily_vaccinations')
                plt.xlabel("Date")
                plt.ylabel("Daily Vaccinations")
                plt.title("Daily Vaccination per country")
                plt.show()

                break
            else:
                print("Enter valid continents name")
        except ValueError:
            print("Enter valid continents name")


def application_exit():
    print("Thank you.")


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
                relationship_recoverd_death()
                break
            elif (val == 3):
                test_per_contitent()
                break
            elif (val == 4):
                daily_vaccination()
                break
            elif (val == 5):
                application_exit()
                break
            elif (val > 5 or val < 1):
                print("*******Enter number between 1 to 5!*******")
        except ValueError:
            print("*******Enter number between 1 to 5!*******")


main()
