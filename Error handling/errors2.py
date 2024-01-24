# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "cub"
# Line 5,syntax error no quotation marks.
animal_type = "lion"
number_of_teeth = "16"
# Line 8, logic error, line was cast as an integer instead of a string, and cub and lion exist in the wrong string, creating issues on line 11 and 12.

full_spec = "This is a " + animal  + ". It is a " + animal_type  + " and it has " + number_of_teeth  +" teeth"
print (full_spec)
# Line 11, logic and syntax error, quotation needed closing between the strings, and needed addition symbol to stitch strings together, braces also needed removing around the string.
# Logic error, incorrect placement of 'number of teeth' and 'animal type'.

