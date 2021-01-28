print("we are giong to make the best pizza.")
prompt ="\nplease enter your favourite toppings:"

active = True
message = ''
topppings =[]

while active:
	message = input(prompt)
	if message == "quit":
		active = false
	else:
		toppings.append(message)

print(f"\nthis are your toppings{toppings}")