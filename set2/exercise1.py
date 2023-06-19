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
# i think this line will substitue from this list of words into a sentence when asked
some_words = ["what", "does", "this", "line", "do", "?"]
# when commanded i think it will print 'word'. 
for word in some_words:
    print(word)
# i think when encountered by an 'x' in the list, it will print 'x'. 
for x in some_words:
    print(x)
# i think this commane will print a word from the list 
print(some_words)
# i think when commanded len, it will print more 'a word from the list, contains more than 3 words' 
if len(some_words) > 3:
    print("some_words contains more than 3 words")


def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # i think this line will print a return string platform.username 
    print(platform.uname())

# i think this will return an unuseful function string 
usefulFunction()
