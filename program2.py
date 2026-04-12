'''Write a Python program that takes a password as input and verifies its security. The
 program must use conditional statements to check if the password length is at least 8 
 characters, and use string slicing to ensure it does not start with common words like 
 "admin" or "password", displaying appropriate success or error messages based on the 
 conditions.'''

password = input("Enter a New Password: ")

if (len(password)<8):
    print("Password should be greater than 8 characters")
else:
    if(password[0:5]=="admin" or password[0:8]=="password"): #if(password.startswith("password"))
        print("Use some Hard password.")
    else:
        verification = input("Re-enter the password to verify: ")

        if (verification==password):
             print("Corect password entererd.")
             print("Password updated successfully!!")
        else:
            print("Not the Same Password ,You Enter before , Try again :( ")
