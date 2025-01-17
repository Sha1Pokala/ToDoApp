# Question 2: Age Group Write a program that asks for the user's age and prints:
# "Child" if the age is less than 12.
# "Teenager" if the age is between 13 and 19.
# "Adult" if the age is 20 or above.


Age= int(input("Enter the person's age-  "))

if Age < 12:
    print ("Child")

elif Age >13 and Age <19 :
    print ("Teenager")

else:
    print ("Adult")

    
    
