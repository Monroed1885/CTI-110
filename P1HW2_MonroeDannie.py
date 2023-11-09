#A brief description of the project
#11/9/2023
#CTI-110 P1HW2- Travel Expense
#DannieMonroe

print("This program calculates and displays travel expenses")

Budget = int(input("Enter Budget:"))
Destination = input("Enter your travel destination:")
Gas = int(input("How much do you think you will spend on gas?"))
accomadation = int(input("Approximately, how much will you need for accomodation/hotel?"))
food = int(input("Last, how much do you need for food?"))

print("-----------------Travel Expenses-----------------")
print("Location:", Destination)
print("Initial Budget:", Budget)
print("Fuel:", Gas)
print("accomodation:", accomadation)
print("Food:", food)

print("Remaining Balance:", Budget-accomadation-food-Gas)



