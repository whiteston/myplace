"""
Try to find out how many zeros a given number has at the end.

Input: A positive Int

Output: An Int.

Example:

end_zeros(0) == 1
end_zeros(1) == 0
end_zeros(10) == 1
end_zeros(101) == 0
"""

    
def end_zeros(num: int):
    # your code here
    a = 0
    
    for i in reversed(str(num)):
        if i == '0':
            a += 1
        else:
            return a
    return a


print("Example:")
print(end_zeros(35000))
print(end_zeros(1010))