my_str = "madam"
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str)==list(rev_str):
    rev_str = reversed(my_str)
    print("the string is a palindrome")
else:
    print("the string is not a palindrome")