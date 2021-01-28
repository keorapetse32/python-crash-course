prompt = input("Enter a number, and I'll tell you if it's even or odd: ")
prompt += "\nEnter 'quit' to exit: "
message = ''
active = True

while active:
	message = input(prompt)

if message == 'quit':
	active = False
elif int(message) % 2 == 0:
	print(f"\nThe number {number} is even.")
elif int(message) % 2 == 0:
	print(f"\nThe number{number} is odd.")
else:
	print('invalid input!')


