#6.1
user_0 = {
'username': 'Keora',
'first': 'Keorapetse',
'last': 'Letlape',
'age': 19,
'location': 'Stone Ridge'
}
for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

#6.2
favorite_number = {
   'Mandy': 2,
   'Luoisa': 26,
   'Mike': 56,
   'Brad': 19,
   'Trevor': 34,
   }

for name, number in favorite_number.items():
	print(f"{name.title()}'s favorite number is {number}.")

#6.3
Glossary = {
'Abstract Base Class': 'An abstract base class provides a way to define interfaces.',
'Asynchronous Context Manager': 'ACM is an object that controls the environment observed in an async with statement. ',
'Attribute': 'An attribute is a value an object holds.',
'Binary File': 'A file object that is able to read and write bytes-like objects is a binary file.',
'Coroutine': 'A subroutine enters at one point and exits at another.'
}
for key, meaning in Glossary.items():
	print(f"\nKey: {key}")
	print(f"meaning: {meaning}")

#6.4
Glossary = {
'fabricant': 'a maker or manufacturer.',
'paddle wheel': 'a wheel for propelling a ship, having a number of paddles entering the water more or less perpendicularly.',
'grouse': 'to grumble; complain.',
'flocculent': 'like a clump or tuft of wool.',
'macaronic': 'composed of a mixture of languages.'
}
for key, meaning in Glossary.items():
	print(f"\nKey: {key}")
	print(f"meaning: {meaning}")

#6.5
Glossary = {
'Amanzimtoti River,': 'northwest of Adams Mission.',
'Baviaanskloof River': 'North of Plettenberg Bay.',
'Bell River': "Near Naudé's Neck.",
'Crocodile River': 'North West, Gauteng and Limpopo.',
'Limpopo River': 'Limpopo, on Zimbabwe, Botswana borders.'
}
for key, meaning in Glossary.items():
	print(f"\nKey: {key}")
	print(f"meaning: {meaning}")

#6.6
favorite_languages = {

'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")


#soccer_O = {'object': 'ball', 'shape': 'sphere', 'shoot': 'goal!!!'}
#point_value = soccer_O.get('player', 'you dont have the ball right now.')
#print(point_value)

Nascar_race ={
'lukka':'mclaren p1',
'dave':'lamborghini hurracan',
'enzo': 'ferrari 815 spyder',
'mike': 'nissan gtr nismo',
}

#for driver, car in Nascar_race.items():
	#print(f"{driver.title()} drives a {car.title()}.")

#for driver in Nascar_race.keys():
	#print(driver.title())

#for car in Nascar_race.values():
	#print(car.title())


#friends = ['lukka', 'enzo']
#for driver in Nascar_race.keys():
	#print(driver.title())

	#if driver in friends:
		#car = Nascar_race[driver].title()
		#print(f"\t{driver.title()}, are you driving a {car}!?")

for driver in sorted(Nascar_race.keys()):
	print(f"{driver.title()}, thank you for participating in the race.")
	



