from tokenize import String

print("Welcome to  our shop ")
s=input("Enter your  card number: ")
class Card:


    def __init__(self):
        self.items=[]

        self.fix_items={
            "Burger":120,
            "Sandwich":80,
            "Frenchfries":40,
            "Chocolate":10,
            "Coffe":30,
            "Pizza":100,
            "Water":5,
            "Juice":10,
            "Cake":7,




        }


    def add_items(self,name):
     while True:
        if  name.isalpha() :


            name = name.capitalize()

            if name in self.fix_items:
                price = self.fix_items[name]  # price is fix by the name
                self.items.append((name, price))



                print(f">> Added item name :{name} price is :{price}")
                break



            else:
                print(f">>Sorry we are not selling this item {name} at our shop")

                num1 = int(input("Enter how many item do you  have buy again :"))
                for j in range(num1):
                    name = input("Enter the name of the item again:")
                    if name.isalpha():
                       name=name.capitalize()
                    if name in self.fix_items:
                        price=self.fix_items[name]

                        self.items.append((name, price))
                        print(f">> Added item name :{name} price is :{price}")
                        break





            break












        else:
            print(f"Sorry we are not selling this item {name} at our shop")
            num2=int(input("Enter how many item do you  have buy again :"))
            for j in range(num2):
                name = input("Enter the name of the item again:").capitalize()
                if name in self.fix_items:
                  price=self.fix_items[name]
                  self.items.append((name, price))
                  print(f">> Added item name :{name} price is :{price}")
                break



            break







    def remove_item(self,name):
        name=name.capitalize()
        name_found=False
        for item in self.items:
            if item[0]==name:
                self.items.remove(item)
                name_found=True
                break

        if not name_found:
                print(f"Sorry!,We are not selling this item {name}at our shop")






    def total_price(self):
        total=0
        for i,(name,price) in enumerate(self.items):
            total+=price

        return  print(f"The total price is {total}")








c1=Card()

num=int(input("How many items do you have buy:"))

for  i in  range (num):
    c1.add_items(name=input("Enter the name of the item : " ))


num2=int(input("Enter how many items do you want to remove :"))

if num2==0:
    c1.total_price()

else:
    for i in range(num2):
        c1.remove_item(name=input("Enter the item your want to remove: "))
        c1.total_price()



print("Thank you for Coming.Please pay a visit again!!!")










