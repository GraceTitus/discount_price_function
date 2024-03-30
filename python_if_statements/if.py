num = 20
if num >= 20:
 #print("the number is 20")

 age = 30
 if age <= 30:
  #print("is fresha")

  height = 5.6
  if height <= 5.6:
    #print("is not cabin crew")

    height = 5.6
    if height >= 5.6:
     #print("is cabin crew")
    #else:
     #print ("is not cabin crew")

    #grade = 90
    #if grade >= 90: 
      #print ("A")
    
    #elif grade >= 80:
     #print ("B")

    #elif grade >=70:
         #print ("C")

    #elif grade >= 60:
         #print ("D")
    #else: 
         #print ("F")


#name = "Grace" #string - sequence -iterable  
#for char in name:
    #print(char)

#python_instructors = ["dave", "maureen", "evans", "evans", "evans"]
#for item in python_instructors:
    #print ("instructors:", item)    

#welcome_message = "Welcome To T&G DIGI Services"
#for i in range(8):
 #print(welcome_message)  


      #count = 3
      #while count <= 2:
          #print(count)
          #count += 1


#snack = lambda : print("crisps")
#snack()

#def num_square(num):
  #return num **3
#print("square of num is:", num_square(8))

#num_square = lambda num : num** 2
#print("square of num is:", num_square(8))

#What is the output of the following code?

#def outer_fun(a, b):
    #def inner_fun(c, d):
        #return c + d
    #return inner_fun(a, b)

#res = outer_fun(5, 10)
#print(res)

#What is the output of the add() function call

#def add(a, b):
    #return a+5, b+5

#result = add(3, 2)
#print(result)


#for num in range(1, 5):
    #print(num)

#x = 0
#for i in range(3):
    #x = x + i
#What’s the value of x after the above code snippet executes?
#x = 0
#for i in range(3):
    #x = x + 1
    #print(x)


#What will be the output of the following Python code?



#list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]

#sum = 0

#sum1 = 0

#for elem in list1:

 #if (elem % 2 == 0):

  #sum = sum + elem

 #continue

#if (elem % 3 == 0):

 #sum1 = sum1 + elem

#print(sum , end=" ")


#Week 3 Assignment. Submit a github repo link for the assignment below
#Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
#Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
     def calculate_discount(price, discount_percent):
      if discount_percent >= 20:
        discounted_price = price * (1 - discount_percent / 100)
        return discounted_price
      else:
          return price

# Prompt the user to enter the original price of the item and the discount percentage
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)

# Print the final price
if final_price != original_price:
    print("Final price after discount: $", final_price)
else:
    print("No discount applied. Original price: $", original_price)


    


