def calcSubtotal(pizzas, drinkQuantity, dessert, delivery):
  subtotal = 0
  subtotal += drinkQuantity * 3 # for drinks
  subtotal += 5 #for desserts

  if delivery == True:
    subtotal+= 10
  
  for pizza in pizzas:
    if pizzas[pizza]["pizzaSize"] == "Small":
      subtotal+= 10
    elif pizzas[pizza]["pizzaSize"] == "Medium":
      subtotal += 15
    elif pizzas[pizza]["pizzaSize"] == "Large":
      subtotal+= 20

  return subtotal

def totalCost(subtotal):
  grandTotal = subtotal * 1.13
  return grandTotal

orderInfo = {"name": "",
  "pizzas": {},
  "drinkType": "",
  "drinkQuantity": 0,
  "dessert": "",
  "delivery": False
}

# get customer name
name = input("Please enter your name: ")
orderInfo["name"] = name
# get number of pizzas
numPizza = int(input("Please enter the number of pizzas you would like to order: "))

pizzas = {}

for i in range(1, numPizza + 1):
  print("\n------------------------")
  print("Pizza order information: " + str(i))
  print("--------------------------")
  pizzas[i] = {"pizzaBase": "",
    "pizzaType": "",
    "pizzaSize": ""
  }

  print("1. Hand Tossed\n2. Thin Crust\n3. Regular")
  pizzaBase = int(input("Please select your pizza base: "))
  if pizzaBase ==1:
    pizzaBase = "Hand Tossed"
  elif pizzaBase == 2:
    pizzaBase = "Thin Crust"
  elif pizzaBase == 3: 
    pizzaBase = "Regular"
  else:
    print("Invalid pizza base selection")
  
  pizzas[i]["pizzaBase"] = pizzaBase
  
  print("\n1. Pepperoni\n2. Cheese\n3. Veggie Lovers\n4. Hawaiian")
  pizzaType = int(input("Please select your pizza type: "))
  if pizzaType == 1:
    pizzaType = "Pepperoni"
  elif pizzaType == 2:
    pizzaType = "Cheese"
  elif pizzaType == 3:
    pizzaType = "Veggie Lovers"
  elif pizzaType == 4:
    pizzaType = "Hawaiian"
  else:
    print("Invalid pizza type selection")
  
  pizzas[i]["pizzaType"] = pizzaType

  print("\n1. Small\n2. Medium\n3. Large")
  pizzaSize = int(input("Please select you pizza size: "))
  if pizzaSize == 1:
    pizzaSize = "Small"
  elif pizzaSize == 2:
    pizzaSize = "Medium"
  elif pizzaSize == 3:
    pizzaSize = "Large"
  else:
    print("Invalid pizza size")
  pizzas[i]["pizzaSize"] = pizzaSize

orderInfo["pizzas"] = pizzas

print("\n1. Coke\n2. Juice\n3. Canada Dry")
drink = int(input("Please select your drink: "))
if drink == 1:
  drink = "Coke"
elif drink == 2:
  drink = "Juice"
elif drink == 3:
  drink = "Canada Dry"
else:
  print("Invalid drink selection")
orderInfo["drinkType"] = drink


drinkQuantity = int(input("\nSelect quantity of drinks: "))
orderInfo["drinkQuantity"] = drinkQuantity

print("\n1. Brownie\n2. Ice Cream")
dessert = int(input("Please select your dessert: "))
if dessert == 1:
  dessert = "Brownie"
elif dessert == 2:
  dessert = "Ice Cream"
else:
  print("Invlalid dessert selection")
orderInfo["dessert"] = dessert

delivery = input("\nWould you like your odrder delivered? [Y/N]: ")
if delivery == "Y" or delivery == "y":
  delivery = True
elif delivery == "N" or delivery == "n":
  delivery = False
else:
  print("Invlalid delivery option")
orderInfo["delivery"] = delivery

print("\n------------------")
print("Customer Information")
print("------------------")

print("Customer name: " + orderInfo["name"])
print("\nPizza order information: \n")
for pizza in pizzas:
  print("------------------")
  print("Pizza Information " + str(pizza))
  print("------------------")
  print("Pizza Base: " + pizzas[pizza]["pizzaBase"])
  print("Pizza Type: " + pizzas[pizza]["pizzaType"])
  print("Pizza Size: " + pizzas[pizza]["pizzaSize"])

print("\n-----------------")
print("Drink Information")
print("-----------------")
print("Drink: " + orderInfo["drinkType"])
print("Drink Quantity: " + str(orderInfo["drinkQuantity"]))

print("\n-----------------")
print("Dessert Information")
print("-----------------")
print("Dessert: " + orderInfo["dessert"])

print("\n-----------------")
print("Delivery Information")
print("-----------------")
if orderInfo["delivery"] == True:
  print("Delivery Charge: $10")
else:
  print("Delivery Charge: $0")

print("\n-----------------")
print("Cost Summary")
print("-----------------")
subtotal = calcSubtotal(orderInfo["pizzas"], orderInfo["drinkQuantity"], orderInfo["dessert"], orderInfo["delivery"])
print("Subtotal: $" + str(subtotal))
grandTotal = totalCost(subtotal)
print("Total Cost: $" + str("%.2f"%grandTotal))
print("")

  


  

