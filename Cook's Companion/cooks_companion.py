def cups_to_grams(cups, density):
  # Convert cups to grams here.
  # The density is in grams-per-cup.
  output = cups*density
  return round(output,1)
  
# Write the rest of your program here
food = input("What food? ")
cups = float(input("How much in cups? "))
density = int(input("How many grams per cup? "))

print(f"{cups} cups of {food} is {cups_to_grams(cups,density)} grams.")