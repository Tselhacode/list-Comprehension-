
with open("file1.txt",'r') as x:
  x_list = [int(num.strip()) for num in x.readlines()]
  print(x_list)

with open("file2.txt",'r') as y:
  y_list = [int(num.strip()) for num in y.readlines()]
  print(y_list)

result = [num for num in x_list if num in y_list]






# Write your code above 👆

print(result)


