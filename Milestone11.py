
numbers = []
countries = []
years = []

new_years = []
new_numbers = []
new_countries = []

country_years = []
country_numbers = []

with open("/Users/edgardavidcure/Desktop/Python/life-expectancy.csv") as life_exp_file:
	next(life_exp_file)
	for line in life_exp_file:
		data = line.split(",")
		
		country = data[0]
		countries.append(country)
		initials = data[1]

		year = int(data[2])
		years.append(year)
		

		expectancy = float(data[3])
		numbers.append(expectancy)
		
		min_number = min(numbers)
		min_index = numbers.index(min_number)
		min_index_country = countries[min_index]

		max_number = max(numbers)
		max_index = numbers.index(max_number)
		max_index_country = countries[max_index]
		
		max_year = years[max_index]
		min_year = years[min_index]

year_interest = int(input("Enter the year of interest: "))
country_interest = input("Enter the country of interest: ").capitalize()
			
print()
print(f"{max_index_country} has the maximum recorded life expectancy of {max_number:.2f} in {max_year}")
print(f"{min_index_country} has the minimum recorded life expectancy of {min_number:.2f} in {min_year}")


for i, year in enumerate(years):
	if year == year_interest:
		
		new_years.append(year)
		total_years = len(new_years)

		new_numbers.append(numbers[i])
		total_numbers = sum(new_numbers)

		new_countries.append(countries[i])
		
		#Calculate max and min numbers
		min_number = min(new_numbers)
		min_index = new_numbers.index(min_number)
		min_index_country = new_countries[min_index]
		
		max_number = max(new_numbers)
		max_index = new_numbers.index(max_number)
		max_index_country = new_countries[max_index]

		average_expectancy = (total_numbers/ total_years)
		
		
		
		
		
		

print()
print(f"For the year {year_interest}: ")
print(f"The average life expectancy across all countries was {average_expectancy:.2f}")
print(f"The max life expectancy was in {max_index_country} with {max_number:.2f}")
print(f"The min life expectancy was in {min_index_country} with {min_number:.2f}")



		
for j, country in enumerate(countries):
			if country == country_interest:
				country_years.append(years[j])
				total_years = len(country_years)
				country_numbers.append(numbers[j])
				total_numbers = sum(country_numbers)

				min_number = min(country_numbers)
				min_index = country_numbers.index(min_number)
				
		
				max_number = max(country_numbers)
				max_index = country_numbers.index(max_number)

				max_year = country_years[max_index]
				min_year = country_years[min_index]
				

				average_expectancy = (total_numbers/ total_years)

				
			
		

print()
print(f"For the country {country_interest}: ")
print(f"The average life expectancy was {average_expectancy:.2f}")
print(f"The max life expectancy was {max_number:.2f} in {max_year}")
print(f"The min life expectancy was {min_number:.2f} in {min_year}")

	



	

	

				
	

	
	
	
		


		