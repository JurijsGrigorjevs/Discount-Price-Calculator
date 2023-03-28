#Shopping during the sales can sometimes be very confusing. With discounted prices at 10%, 20%, 50% or even 70%. 
# Discount Price Calculator 

# Step1: Retrieving user inputs


itemPrice = float(input("What is the price of the item?"))
percentageDiscount= float(input("What is the percentage discount?"))

# Step2: Processing

reducedPrice = itemPrice-itemPrice*percentageDiscount/100

# Step3: Displaying the price to two decimal places

print("The reduced price is " + str("%.2f" % reducedPrice))
  