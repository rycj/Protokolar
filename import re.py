# str = "(6+(5+(3*2))/(3*3))"
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

prio = ["+" or "-", "*", "/", "^"]
str = "3+(6+(5+(3*2))/(3*3))+3"
maxdepth = 0
for i in range(len(str)):
    if str[i] == "(":
        depth += 1
        if depth < maxdepth:
            maxdepth = depth
    list.append([i, str[i], depth])
    if str[i] == ")":
        depth -= 1
print(list)
tree = []
k = 0
treeheight = 0
for i in range(maxdepth + 1):
    for j in list:
        if j[2] == i and j[1] == prio[0]:
            tree.append(str[: j[0]])
            tree.append(str[j[0] + 1 :])
            treeheight += 1
print(tree)


# def func(str):
#     for i in str:
#         if i == "(":
#             func(str.split("(", 1)[1])
#             print("_")
#         elif i == ")":
#             break
#         else:
#             print(i)


# func("((1+9*(5+2))/(3*3))")
