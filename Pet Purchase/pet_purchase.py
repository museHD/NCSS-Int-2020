'''
You run a pet shop selling cats, dogs, birds and guinea pigs! Help your customers with their purchases.

Find out which pet they want, and how many. Then, print out the appropriate response.

Watch out though — sometimes customers are rude! If a customer SHOUTS at you, tell them off for scaring the animals instead.

If your customer wants fewer than one pet, you should print:

What animal would you like? bird
How many? 0
That's sad. No pet for you today.
​

If they want to buy one pet it should print:

What animal would you like? dog
How many? 1
Great, here's your dog!
​

If they want to buy more than one it should print:

What animal would you like? guinea pig
How many? 5
Ok! 5 guinea pigs coming right up!
​

Finally, for rude customers who SHOUT in capital letters, print:

What animal would you like? CAT
How many? 2
Woah! No need to shout, you'll scare the animals!
'''

animal = input("What animal would you like? ")
amount = int(input("How many? "))

if animal.isupper():
	print("Woah! No need to shout, you'll scare the animals!")
elif amount < 1:
	print("That's sad. No pet for you today.")
elif amount == 1:
	print(f"Great, here's your {animal}!")
elif amount > 1:
	print(f"Ok! {amount} {animal}s coming right up!")