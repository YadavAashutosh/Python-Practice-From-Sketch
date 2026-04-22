'''Write a Python program to simulate a 'Supermarket Billing & Offer System' that performs a
Linear Search for product IDs '''

print("Supermarket Billing & Offer System \n")

product_id = []
i= int(input("Enter the total no of ids: "))

j=0
while j<i:
    product_id.append(int(input(f"Add product id  {j+1}: ")))
    j+=1

print(product_id)
k= int(input("Enter product id to search:"))
a=0
while a < len(product_id):
    if product_id[a]==k:
        print(f"{k} found at index {a}")
        break
    a+=1

else :
    print(f"{k} not found")

print("\n ===for loop === \n ")

'''Write a Python program to print the multiplication table of a user-input number using a 
for loop, but use the continue statement to skip printing the results if they are exactly 20 
or 40.'''

for b in range(1,11):
    print(f"{b} * {b} " , b*b , sep="=" )

c=int(input("Enter a Number: "))

for b in range(1,11):
    if b*c in [20,40] :
        continue
    if b==7:
        pass
    print(f"{c} of {b} = ", b*c)
