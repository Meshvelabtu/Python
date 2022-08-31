Fruit = {}
while True:
  if len(Fruit) == 0:
    elem = {}
    name = input("Enter Fruit Name: ")
    kg = input("Enter Fruit Kg: ")
    price = input("Enter Fruit Price: ")
    elem["kg"] = kg
    elem["price"] = price
    Fruit[name] = elem
  else:
     print("This is yout cart: ", Fruit)
     ques = input("Add More? yes/no: ")
     if ques == "yes":
         elem = {}
         name = input("Enter Fruit Name: ")
         kg = input("Enter Fruit Kg: ")
         price = input("Enter Fruit Price: ")
         elem["kg"] = kg
         elem["price"] = price
         Fruit[name] = elem
     else:
         print("Thank you")

     break

for key, value in Fruit.items():
        kg = int(value['kg'])
        price = int(value['price'])
        print("შენი გადასახდელი თანხა არის", kg*price, "ლარი")



