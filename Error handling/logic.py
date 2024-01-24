# Being tasked to create a creative logic error i've decided to take inspiration from the capstone project.
# Here we will use the second part to help a user work out their mortgage repayments.
# Only the calculator in this instance will give the incorrect result making the user feel like they owe a lot more.
# Displaying how important it is to test and test and test making sure your logic is sound.

print ("Welcome to our mortgage calculator!")
print ("To find out how much you owe, follow our steps below!")

value = float(input("What is the current value of your property? £"))
rate = float(input("Please enter the interest rate as a solid number. ")) * 100 * 12
# Instead of dividing the logic error is multiplying, the programme still runs.
# It indicates the user owes a lot more than anticipated.
months = int(input("How many months are you planning to take to repay the bond? "))


repayment = (rate * value)/(1 -(1 + rate)**(-months))
repayment = "{:.2f}".format(repayment)
print ("\n""Your monthly repayments will be £",repayment)