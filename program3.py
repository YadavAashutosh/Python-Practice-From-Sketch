'''Write a Python program to manage an e-commerce shopping cart using lists. The program 
   must initialize an empty list, use the append() method to add three user-input items, use 
   remove() to delete a specific item, use insert() to add a new item at the first index, and
   finally use sort() to display the cart items in alphabetical order.'''

Cart= []

Cart.append(input("Enter First Item :"))
Cart.append(input("Enter Second  Item :"))
Cart.append(input("Enter Third Item :"))

print(Cart)

Cart.remove(input("Enter a item to remove :"))
Cart.insert(1,input("Enter a item name to add :"))

Cart.sort() # Sort shows "none" if you call sort directly in print function
print(Cart)