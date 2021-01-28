#5.1
animal = 'lion'
print("is animal == 'lion'? I pridict true.")
print(animal == 'lion')

print("\nIs animal == 'tiger'? i pridict false.")
print(animal == 'tiger')

#5.2
countries = ['Morocco', 'Canada','Japan', 'Ireland', 'Portugal', 'Mexico', 'Netherlands', 'Vietnam', 'Turkey', 'Australia', 'Greece']
for country in countries:
	if country == "Canada":
		print(country.lower())
	else:
		print(country.title())


#5.3
#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])

alien_0 = {'blue', 'green', 'red'}
for alien in alien_0:
	if alien == "green":
		print(f"The alien is {alien.title()}")
	else:
		print(f"The alien is not {alien.title()}")

#5.4
alien_0 = {'color': 'green', 'points': 5}
for color, points in alien_0.items():
	print(f"{color.title()} for {points.title()} points.")
	for color in alien_0.keys():
		print(color.title())
		for points in alien_0.values():
			print(points.title())

available_parts = ['Engine', 'Battery', 'Radiator', 'Alternator', 'Brakes']
requested_parts = ['Engine', 'Battery', 'Front Axle', 'Brakes']
for requested_part in requested_parts:
	if requested_part in available_parts:
		print(f"adding {requested_part}.")
	else:
		print(f"sorry, we don't have { requested_part.title()}")
print("\nWe have finished installing your parts")
