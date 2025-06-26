countryPop = {"Japan": 127000000, "Germany": 81000000, "Iran": 77000000,"UK": 64000000, "Canada": 33000000, "Australia": 23000000, "USA": 317000000, "Bulgaria": 7000000, "Sweden": 10000000}
print("Please choose between these 9 countries below:")
print("- Japan")
print("- Germany")
print("- Iran")
print("- UK")
print("- Canada")
print("- Australia")
print("- USA")
print("- Bulgaria")
print("-Sweden")

country1 = ""
while country1 not in countryPop:
    country1 = input("Please enter the first country: ")
    if country1 not in countryPop:
        print("Sorry, that country cannot be found. Please Try Again.")

country2 = ""
while country2 not in countryPop:
    country2 = input("Please enter a second country: ")
    if country2 not in countryPop:
        print("Sorry, that country cannot be found. Please Try Again.")

total_population = countryPop[country1] + countryPop[country2]
print("The combined population of these two countries that you have chosen us:", total_population)
