# str = "(6+(5+(3*2))/(3*3))"
import math

depth = 0
list = []
# for i in range(len(str)):
#     if str[i] == "(":
#         list.append([i, str[i], depth])
#         depth += 1
#     elif str[i] == ")":
#         depth -= 1
#         list.append([i, str[i], depth])
#     elif str[i] == "/":
#         list.append([i, str[i], depth])
# print(list)

# class Node():
#     def __init__(self,value):
#         self.value=value
#         self.left=None
#         self.right=None

# prio = ["+" or "-", "*", "/", "^"]
# str = "3+(6+(5+(3*2))/(3*3))+3"
# maxdepth = 0
# for i in range(len(str)):
#     if str[i] == "(":
#         depth += 1
#         if depth < maxdepth:
#             maxdepth = depth
#     list.append([i, str[i], depth])
#     if str[i] == ")":
#         depth -= 1
# print(list)
# for i in range(maxdepth + 1):
#     for j in list:
#         if j[2] == i and j[1] == prio[0]:
#             ...


def func(str: str, i):
    finstr = ""
    while i < len(str):
        if str[i] == "(":
            # print("_")
            # print(str.split("(", 1)[1])
            i = func(str, i + 1)
        elif str[i] == ")":
            print(finstr)
            return i
        else:
            finstr += str[i]
            ...
        i += 1
    # for i in str:
    #     if i == "(":
    #         print("_")
    #         print(str.split("(", 1)[1])
    #         func(str.split("(", 1)[1])
    #     elif i == ")":
    #         break
    #     else:
    #         print(i)


func("((1+9*(5+2))/(3*3))", 0)


# prio = ["+" or "-", "*", "/", "^"]
# str = "3+(6+(5+(3*2))/(3*3))+3"
# maxdepth = 0
# for i in range(len(str)):
#     if str[i] == "(":
#         depth += 1
#         if depth < maxdepth:
#             maxdepth = depth
#     list.append([i, str[i], depth])
#     if str[i] == ")":
#         depth -= 1
# print(list)
# tree = []
# k = 0
# treeheight = 0
# for i in range(maxdepth + 1):
#     for j in list:
#         if j[2] == i and j[1] == prio[0]:
#             tree.append(str[: j[0]])
#             tree.append(str[j[0] + 1 :])
#             treeheight += 1
# print(tree)
