print("Calculator")

print("Type in the operation you want to perform")
print("Options are: multiply, divide, add or subtract")
print()

operation = input()

if operation == "add":
  print("type in a number")
  firstnum = input()
  print("type in second number")
  secondnum = input()
  print()
  print(int(firstnum)+int(secondnum))

if operation == "multiply":
  print("type in a number")
  firstnum = input()
  print("type in second number")
  secondnum = input()
  print()
  print(int(firstnum)*int(secondnum))

if operation == "subtract":
  print("type in a number")
  firstnum = input()
  print("type in second number")
  secondnum = input()
  print()
  print(int(firstnum)-int(secondnum))

if operation == "divide":
  print("type in a number")
  firstnum = input()
  print("type in second number")
  secondnum = input()
  print()
  print(int(firstnum)/int(secondnum))