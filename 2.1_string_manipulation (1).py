"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: a sentence typed by the user
# 2. Process: apply four different string methods to it
# 3. Out: four transformed versions of the sentence
# 4. My four transformations, and when each is useful:
#    - strip(): cleaning a form entry where someone added spaces by accident
#    - upper(): writing a ticker in a standard format ("aapl" -> "AAPL")
#    - title(): formatting a client's name properly ("john smith" -> "John Smith")
#    - replace(" ", "_"): turning a sentence into a file name without spaces

# Your code below
sentence = input("Enter a sentence: ")

print("strip()  :", repr(sentence.strip()))
print("upper()  :", repr(sentence.upper()))
print("title()  :", repr(sentence.title()))
print("replace():", repr(sentence.replace(" ", "_")))

