"""
A pawn is generally a weak unit, but we have 8 of them which we can use to build a pawn defense wall.
With this strategy, one pawn defends the others. A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.
Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1

Precondition: 0 < pawns <= 8
"""


# 이 문제는 어떻게 접근할 지 생각은 했는데 코드로 표현을 못했음.
# 고민하다가 다른 사람 풀이법 참고! (+아스키코드 숙지)
def safe_pawns(pawns: set) -> int:
    result = 0
    for pawn in pawns:
        if chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns:
            result += 1
        elif chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1) in pawns:
            result += 1
    return result


#    pawns = sorted(list(pawns), reverse = True, key = lambda x: x[1])
#    safe = 0
#    for i in pawns:
#        k = chr(ord(i[0]) - 1) + chr(ord(i[1]) - 1)
#        l = chr(ord(i[0]) + 1) + chr(ord(i[1]) - 1)
#        safe += (k in pawns or l in pawns)
#    return safe

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))