"""
We have a List of booleans. Let's check if the majority of elements are true.
Some cases worth mentioning: 1) an empty list should return false; 2) if trues and falses have an equal amount, function should return false.

Input : A List of booleans.
Output : A Boolean.

Example:

is_majority([True, True, False, True, False]) == True
is_majority([True, True, False]) == True
"""


def is_majority(items: list) -> bool:
    if items != []:
        a = items.count(True)
        b = len(items) - a
        if a > b:
            return True
    return False


#    count = 0
#    if items != []:
#        for i in items:
#            if i == True:
#                count += 1
#    if count > (len(items) - count):
#        return True
#    return False

print(is_majority([True, False, False, True, False]))
print(is_majority([True, True, False]))
print(is_majority([]))