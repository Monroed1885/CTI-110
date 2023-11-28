#DannieMonroe
#11/28/20203
#Use a for loop with the range function

#Get input from user
num1= int(input("Enter an integer:"))

num2= int(input("Enter an integer higher than first:"))

#If the first number is smaller
if num1 < num2:
    for i in range(num1, num2 + 1, 5):
        print(i)

#If first number is larger
else:
    #print("First integer must be smaller")
    
    #While the input is invalid
    while num1 > num2 or num1 == num2:
        print("First integer must be smaller")
        
        #Get input from user
        num1= int(input("Enter an integer:"))
        num2= int(input("Enter an integer higher than first:"))
    for i in range(num1, num2 + 1, 5):
        print(i)

    




