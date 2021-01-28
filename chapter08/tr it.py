#def describe_car(car_type, model_name):
	#"""Display information about a pet."""
	#print(f"\nI have a {car_type}.")
	#print(f"My {car_type}'s model is a {model_name.title()}.")

#describe_car()
def describe_car(car_type = 'lamborghini', model_name = 'hurracan'):
	"""Display information about a pet."""
	print(f"\nI have a {car_type}.")
	print(f"My {car_type}'s model is a {model_name.title()}.")

describe_car()

def build_car(car_name, model_name, year = 2021):
	"""Return a dictionary of information about a person."""
	transport = {'first': car_name, 'last': model_name, 'middle': year}
	return transport

car = build_car('lamborghini', 'hurracan')
car_name = car['first']
model_name = car['last']
year = car
print(car)