"""
Upper and Lower
"""
# Provide your solution here
def count_upper_lower(my_string: str):
    upper_counter = 0
    lower_counter = 0
    for my_string.isupper() in my_string:                           # not sure about the 2 suggested methods in the hint
        upper_counter = upper_counter + 1
        print(f"No. of Upper case characters: {upper_counter}")
    for my_string.islower() in my_string:                           # not sure about the 2 suggested methods in the hint
        lower_counter = lower_counter + 1
        print(f"No. of Upper lower characters: {lower_counter}")



count_upper_lower("Simon says: Use 'print' in Python, to display information to user or console.")

# print(f"No. of Upper case characters: {upper_counter}")       # variable is IN function!!
# print(f"No. of Upper lower characters: {lower_counter}")      # variable is IN function!!


#another idea:
def count_upper_lower(my_string: str):
    i = 0
    upper_counter = 0
    lower_counter = 0
    while True:
        if my_string[i] == my_string.upper[i]:
            upper_counter = uppercounter + 1
            i = i + 1
        else:
            lower_counter = lower_counter + 1


count_upper_lower("Simon says: Use 'print' in Python, to display information to user or console.")


"""
Check 33
"""
# Provide your solution here
def has_33(list : [int]) -> bool:
    for desired_combi in list:
        if desired_combi == 33:
            print("True")                   # return True??
        else:
            print("False")


has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])



# new idea:
def has_33(list : [int]) -> bool:
    a = 0
    if list[a] == list [a+1] == 3:                  #not sure about trying to calculate with indeces
        a = a + 1
        print("True")
    else:
        print("False")

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

