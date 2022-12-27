# import pandas as pd


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
                print("Please, enter one of the following continent names:")
                print(
                    "North America, South America, Asia, Europer, Africa, Australia/Oceania")
                print("Please type the continents's name")
                break
            elif (val == 2):
                print("Please, enter one of the following continent names:")
                print(
                    "North America, South America, Asia, Europer, Africa, Australia/Oceania")
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
                break
            elif (val > 5 or val < 1):
                print("Enter number between 1 to 5!")
        except ValueError:
            print("Enter number between 1 to 5!")


main()
