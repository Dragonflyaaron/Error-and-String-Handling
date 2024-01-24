# Create string using user input.
# Iterate over the characters in the string by placing in a list.
# Using divison to seperate out the characters in the even position.
# Use .upper() .lower() to change the case size of the characters.
# Join together again to print as a string.


string = input("Please enter a word or phrase here. ")
string_up_down = [string[i].upper() 
                  if i%2==0 
                  else string[i].lower() 
                  for i in range(len(string))]

# Joins the characters together again in a string rather than a list.
new_string = ''.join(string_up_down)
print (new_string)

# Taking the same user input from above and storing it as a new variable and splitting it.
# Adding a word seperating variable for ease later on.
# Using a similar method as before to loop through the string
# Using the %operator to change every second word

words = string
words_split = words.split()
words_sep = ""

for i in range (0, len(words_split)):
    if i % 2 == 0:
        words_sep = words_sep + " " + words_split[i].lower()
    else:
        words_sep = words_sep + " " + words_split[i].upper()

new_sentence = "".join(words_sep)
print (new_sentence.strip()) 


