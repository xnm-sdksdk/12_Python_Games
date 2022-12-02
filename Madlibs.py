# Madlibs Game in python made by Nuno Mendonça

"""
METHODS OF CONCATENATION

"" + nameofvariable

"{}" .format(nameofvariable)

f ""{nameofvariable}
"""

# string inputs
first_word = str(input("Insert the first word: "))

second_word = str(input("Insert the second word: "))

third_word = str(input("Insert the third word: "))

fourth_word = str(input("Insert the fourth word: "))

# string concatenation
madlib_entry = f"Python is very {first_word}! You can do a lot of {second_word} stuff with it.\
    Programming is a very powerful {third_word} tool. Use it {fourth_word}!"
