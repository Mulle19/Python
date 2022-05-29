x = y = [7, 8, 9] # x and y refer to the same list object just created, [7, 8, 9]
x = [13, 8, 9] # x now refers to a different list object just created, [13, 8, 9]
print(y) # y still refers to the list it was first assigned
# Output: [7, 8, 9]
print(x)