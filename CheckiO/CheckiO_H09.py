"""
You have a table with all available goods in the store. The data is represented as a list of dicts

Your mission here is to find the TOP most expensive goods. 
The amount we are looking for will be given as a first argument and the whole data as the second one

Input: int and list of dicts. Each dicts has two keys "name" and "price"
Output: the same as the second Input argument.

Example:

bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]) == [
    {"name": "wine", "price": 138},
    {"name": "bread", "price": 100}
]

bigger_price(1, [
    {"name": "pen", "price": 5},
    {"name": "whiteboard", "price": 170}
]) == [{"name": "whiteboard", "price": 170}]
"""


def bigger_price(limit: int, data: list) -> list:

#    a = []
#    
#    for i in data:
#        if "price" in i:
#            a.append(i["price"])
#    x = a.index(max(a))
#    print(data[x])       -> 처음에 이렇게 생각했다. 최대값만 출력하는거라면 코드가 맞지만 limit 조건이 있기 때문에 안 된다.

    return sorted(data, key = lambda x: x["price"], reverse = True) [:limit]
    # sorted를 사용하면 list로 나온다. 그래서 뒤에 [:limit]를 사용할 수 있다.

print(bigger_price(2, [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]))