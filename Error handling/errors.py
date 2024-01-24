# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program")
# Line 5 syntax error, missing parentheses around "Welcome to the error program".
print ("\n")
# Line 7 syntax error, incorect indentation, backspace before print.
# Line 7 syntax error, missing parentheses around "\n".

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24" 
age = int(age_Str) 
print("I'm" ,age , "years old.")
# Line 12,13,14, all syntax errors with incorrect indent, backspace at start of each line.
# Line 12, runtime error, extra '=' instead of saving the string, saying it is equal to something that doesnt exist.
# Line 12&13, runtime error, we can't convert a string with text to an interger, we delete "years old" from line 12 
# Line 14 runtime error, could be considered a syntax but wasnt called until runtime, used '+' instead of ','  for printing text and string.
   
# Variables declaring additional years and printing the total years of age
years_from_now = 3
total_years = age + years_from_now
# Line 21,22 syntax error, inocorrect indent, backspace at start of line.
# Line 21,22 runtime error, line 21 is using '"' where its not needed making it a string which line 22 can't calculate.

print ("The total number of years:" , total_years)
# Line 26, syntax error, missing parentheses after the call to print.
# Line 26, logic error, "answer_years" does not exist, nor should have any quotation marks. reading backwards it should be "total_years" without quotation.
# Line 26, runtime error, as with line 14, it should not have '+' and instead should be a comma, as their is no math to be done in this line.

# Variable to calculate the total amount of months from the total amount of years and printing the result.
total_months = total_years * 12
print ("In 3 years and 6 months, I'll be " , total_months +6 , " months old")
# Line 33,syntax error, missing parentheses around the call to print.
# Line 32, runtime error, 'total' is something that doesn't exist, should be 'total_years'.
# Line 33, runtime error, again using '+' instead of ','. 
# Line 33, logic error, math is wrong, they did not take in to account the 6 months (half year) so we will edit the call to print by including "+6".

#HINT, 330 months is the correct answer

