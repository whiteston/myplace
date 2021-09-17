"""
One of the robots is charged with a simple task:
to join a sequence of strings into one sentence to produce instructions on how to get around the ship.
But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.

You are given a sequence of strings. You should join these strings into a chunk of text 
where the initial strings are separated by commas. As a joke on the right handed robots, 
you should replace all cases of the words "right" with the word "left", even if it's a part of another word. 
All strings are given in lowercase.

Input: A sequence of strings.
Output: The text as a comma-separated string.

Example:

left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"

Precondition:
0 < len(phrases) < 42
"""


def left_join(phrases: tuple) -> str:
    # for phrase in phrases:
    #     if 'right' in phrase:
    #         return phrase.replace('right', 'left')
    #         
    # 
    #     return ','.join(phrases)
    return ",".join(phrases).replace("right","left")

# right를 left로 대체하는 거랑 / ",".join(phrases)를 구분해서 생각하고 있었다.
# 두 가지 내용을 합쳐서 ~join(phrases).replace~ 이렇게 표현할 수 있다.

print(left_join(("aright", "turn right and go straight")))
print(left_join(("l like you", "cos you're really bright and forthright")))