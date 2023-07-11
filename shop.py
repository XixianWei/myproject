
# class Shop:
#      def __init__(self):
#          self.items = {'Apple': 10, 'Shoes': 120, 'Book': 30}
#          self.customer_money = 100
#          self.max_attempts = 3

#      def greet_customer(self):
#          print("Welcome to our shop!")
#          print("Here are the items and their prices:")
#          for item, price in self.items.items():
#              print(f"{item}: £{price}")
#          print('Enter "exit" to leave the shop.')

#      def handle_purchase(self):
#          attempts = 0
#          while attempts < self.max_attempts:
#              try:
#                  choice = input("Which item would you like to buy? ")
#                  if choice.lower() == "exit":
#                      print("Thank you for visiting our shop!")
#                      break
#                  elif choice not in self.items:
#                      raise ValueError(f"{choice} is not available in the shop.")
#                  elif self.items[choice] > self.customer_money:
#                      raise ValueError("You cannot afford this item.")
#                  else:
#                      self.customer_money -= self.items[choice]
#                      print(f"Here's your {choice}!")
#                      print("Thank you for visiting our shop!")
#                      break
#              except ValueError as e:
#                  print(e)
#                  if attempts == self.max_attempts - 1:
#                      print("You've exceeded your maximum attempts. Please leave the shop.")
#                      break
#                  extra_money = input("Do you have more money? Enter the amount or 'no': ")
#                  if extra_money.lower() != 'no':
#                      self.customer_money += int(extra_money)
#                  attempts += 1

# if __name__ == "__main__":
#      shop = Shop()
#      shop.greet_customer()
#      shop.handle_purchase()

class Shop:
    def __init__(self):
        self.items = {'Apple': 10, 'Shoes': 120, 'Book': 30}
        self.customer_money = 100
        self.max_attempts = 3

    def get_items(self):
        return self.items

    def add_money(self, amount):
        self.customer_money += amount

    def purchase_item(self, item):
        if item not in self.items:
            raise ValueError(f"{item} is not available in the shop.")
        elif self.items[item] > self.customer_money:
            raise ValueError("You cannot afford this item.")
        else:
            self.customer_money -= self.items[item]
            return f"Here's your {item}!"
