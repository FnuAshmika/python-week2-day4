# Exercise 1 - Turn the shopping cart program from yesterday into an object-oriented program
# The comments in the cell below are there as a guide for thinking about the problem. However, if you feel a different way is best for you and your own thought process, please do what feels best for you by all means.
# # Create a class called cart that retains items and has methods to add, remove, and show
# class Cart():

# Create a class called cart that retains items and has methods to add, remove, and show

class Cart:
    def __init__(self):
        self.my_list = []

    def add_items(self):
        item = input ('Enter item you want to buy: ')
        quantity = int(input ('Enter Quantity: '))
        price = int(input ('Enter price per unit: '))
        for i in range(len(self.my_list)):
            if self.my_list[i].item.lower() == item.lower():
                self.my_list[i].quantity += quantity
                print(f'Your {item} quantity has been updated')
                return
        update_list = ShoppingList(item, quantity, price)
        self.my_list.append(update_list)
                
 
    def delete_items(self):
        del_item = input('Which item you want to remove?: ')
        del_quantity =int(input('Enter the quantity you want to remove for this item: '))
        for i in range(len(self.my_list)):
            if self.my_list[i].item.lower() == del_item.lower():
                self.my_list[i].quantity -= del_quantity
                print(f'Quantity of {del_item} is reduced.')
                if self.my_list[i].quantity < 1 :
                    self.my_list.pop(i)
                    print(f'You have removed all {del_item} from your cart')
                return
        print(f'{del_item} not found')
                  
    def show_list(self):
        for items in self.my_list:
            print(f'Item: {items.item}, Quantity: {items.quantity}, Price: {items.price}.')  
                  
    def main(self):
        while True:
            user_choice = input('What would you like to do? (add/delete/show/quit): ').lower()
            if user_choice == 'add':
                self.add_items()
            elif user_choice == 'delete':
                self.delete_items()
            elif user_choice == 'show':
                self.show_list()
            elif user_choice == 'quit':
                self.show_list()
                return
            else:
                print("Invalid Input. Try Again")
        
class ShoppingList:
    def __init__(self,item, quantity, price):
        self.item = item
        self.quantity = quantity
        self.price = price
        
new_list = Cart()
new_list.main()