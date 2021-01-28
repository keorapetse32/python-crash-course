#3.1
Friends = ['Cherilyn', 'Ursula', 'Agueda', 'Louis', 'Mariel']
print(Friends)
print(Friends[0])
print(Friends[1])
print(Friends[2])
print(Friends[3])
print(Friends[4])

#3.2
message = f"Hello my dear friend {Friends[0].title()}."
print(message)
message = f"Hello my dear friend {Friends[1].title()}."
print(message)
message = f"Hello my dear friend {Friends[2].title()}."
print(message)
message = f"Hello my dear friend {Friends[3].title()}."
print(message)
message = f"Hello my dear friend {Friends[4].title()}."
print(message)

#3.3
cars = ['FERRARI', 'LAMBORGHINI', 'BMW', 'DODGE', 'MERCEDES-BENZ']
print(cars)
message = f"My favorite car is a {cars[1].title()}."
print(message)

#3.4
Friends = ['charles', 'martina', 'michael']
print(f"My dearest friend {Friends[0].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[1].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[2].title()}, i would like to invite to a get together dinner")

#3.5
Friends = ['Cherilyn', 'Ursula', 'Agueda', 'Louis', 'Mariel']
print(Friends)

del Friends[2]
print(Friends)

Friends.insert(2,'mikel')
print(Friends)

print(f"My dearest friend {Friends[0].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[1].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[2].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[3].title()}, i would like to invite to a get together dinner")
print(f"My dearest friend {Friends[4].title()}, i would like to invite to a get together dinner")

#3.6
Friends = ['charles', 'martina', 'michael']
Friends.insert(0, 'jordan')
Friends.insert(2, 'mandy')
Friends.append('brad')
print(Friends)

#3.7
Friends = ['jordan', 'charles', 'mandy', 'martina', 'michael', 'brad']
print(Friends)

del Friends[0:2]
print(Friends)

popped_friend = Friends.pop()
print(Friends)
print(popped_friend)

#3.8
places = ['Tokyo', 'Maldives', 'New Orlean', 'Bhutan', 'Hong Kong', 'Antarctica']
print(places)

places.sort()
print(places)

places.reverse()
print(places)

#3.9
guests = ['jordan', 'charles', 'mandy', 'martina', 'michael', 'brad']
len(guests)
print(len(guests))

#3.10
countries = ['Morocco', 'Canada',' Japan', 'Ireland', 'Portugal', 'Mexico', 'Netherlands', 'Vietnam', 'Turkey', 'Australia', 'Greece']
print(countries)
print(countries[0])
print(countries[1])
print(countries[2])
print(countries[3])
print(countries[4])

message = f"I would like to vist {countries[0].title()}."
print(message)
message = f"I would like to vist {countries[1].title()}."
print(message)
message = f"I would like to vist {countries[2].title()}."
print(message)
message = f"I would like to vist {countries[3].title()}."
print(message)
message = f"I would like to vist {countries[4].title()}."
print(message)

message = f"My favorite country is {countries[3].title()}."
print(message)

print(f"My favorite country is {countries[0].title()} and I would like to vist the country")
print(f"My favorite country is {countries[1].title()} and I would like to vist the country")
print(f"My favorite country is {countries[2].title()} and I would like to vist the country")

countries.insert(0, 'Spain')
countries.insert(2, 'France')
countries.append('Italy')
print(countries)

del countries[0:2]
print(countries)

popped_country = countries.pop()
print(countries)
print(popped_country)

countries.sort()
print(countries)

countries.reverse()
print(countries)

len(countries)
print(len(countries))

#3.11
guests = ['jordan', 'charles', 'mandy']
print(guests[3])

#