"""
Commenting skills:

NOTE: this file runs just fine, this is for you to learn to use the debugger!

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# i think this will print a string of words or one word when selected by a number
some_words = ["what", "does", "this", "line", "do", "?"]
#i think this will print the word 'word'
for word in some_words:
    print(word)
# i think this will print a selected word from the some-word list 
for x in some_words:
    print(x) #It prints the value of the current element (x) to the console.
# i think this will print the string of words:what does this line do?
print(some_words) #it prints the string indicated in the top lines of code 
# i think that if the string of some_words then the function will print some_words contains more than 3 words
if len(some_words) > 3:
    print("some_words contains more than 3 words")


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # i think this line will print a return string platform.username 
    # i think () is used to call a function, so i think this line will print platorm.uname with the comanded function
    print(platform.uname())

# i think this will return an unuseful function string 
usefulFunction()
