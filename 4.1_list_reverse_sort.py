"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: my list of 10 numbers from 4.0
# 2. Process: show the list in four different orders
# 3. Out: the four new orders, then the original list
# 4. My four orders, and which ones modify the original: - sorted(): small to big, makes a copy
#    - sorted(reverse=True): big to small, makes a copy
#    - [::-1]: back to front, makes a copy
#    - sorted(key=...): even numbers first, makes a copy
#    None of these change my original list.
#    .sort() and .reverse() would change it, and they give back None.
#    That's why 4.0 printed "Sorted list: None".


# Your code below
numbers = [4, 5, 6, 7, 8, 9, 10, 11, 2, 1]

print("Original:            ", numbers)
print("Smallest to largest: ", sorted(numbers))
print("Largest to smallest: ", sorted(numbers, reverse=True))
print("Back to front:       ", numbers[::-1])
print("Even numbers first:  ", sorted(numbers, key=lambda n: n % 2))
print("Original at the end: ", numbers)

# CHECK IT YOURSELF
# First and last lines are identical, item by item, and match my list in 4.0,
# so the original was not damaged.