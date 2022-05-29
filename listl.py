x = y = [7, 8, 9] # x and y are two different names for the same list object just created, [7,8, 9]
x[0] = 13 # we are updating the value of the list [7, 8, 9] through one of its names, x
#in this case
print(y) # printing the value of the list using its other name
# Output: [13, 8, 9] # hence, naturally the change is reflected