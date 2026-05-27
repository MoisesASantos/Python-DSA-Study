Complete the is_balanced function.

It takes a string as input and returns True if the parentheses in the string are balanced, and False otherwise. Use an instance of the provided Stack class in stack.py to keep track of the parentheses.

from stack import Stack


def is_balanced(input_str):
    if len(input_str) == 0:
        return None
    flag = 0
    for digit in input_str:
        if digit == '(':
            flag += 1
        elif digit == ')' and flag > 0:
            flag -= 1
        else:
            return False
    if flag == 0:
        return True
    return False

