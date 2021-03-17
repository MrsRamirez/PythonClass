'''
#Version 1
prices = [1.95, 4.50, 0.99, 5.99]
total = 0
for items in prices:
  # This is the same as total = total + items
  total += items  

#these 2 lines do the same thing in different ways
print ("The total is $", total)
print("The total is ${}".format(total))


'''
#Version 2
prices = []   #Create an empty list
total = 0  #Initialize the total at zero
num_items = int(input("How many items do you want to order?"))

#Ask for the price of the items and append to the list
for num in range(num_items):
  item_cost = input ("How much is the cost of item " + str(num + 1) + " ?") 
  prices.append(float(item_cost))

print ("prices: ", prices)

#Add up all of the prices
for x in prices:
  total += x

print("The total cost is ${}".format(total))



'''
# #Version 3
prices = []   #Create an empty list for the prices
items = []  #Create an empty list for the itms
total = 0  #Initialize the total at zero
num_items = int(input("How many items do you want to order?"))
#Ask for the price of the items and append to the list
for num in range(num_items):
  item_name = input ("What is the name of item " + str(num + 1) + " ?") 
  items.append(item_name)

  item_cost = input ("How much is the cost of item " + str(num + 1) + " ?") 
  prices.append(float(item_cost))

#print (items)
#print (prices)

print ("Here's the items you ordered:")
#Print out Add up all of the prices
for x in range (len(prices)):
  print (items[x] + ": " + str(prices[x]))
  total += prices[x]

print("The total cost is ${:.2f}".format(round(total,2)))


#Playing around with formatting decimal places
#print("{0:.2f}".format(532)) #prints 2 decimal places
#print("{0:.3f}".format(5.1234234)) #prints 3 decimal places
'''