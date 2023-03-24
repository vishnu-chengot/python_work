# try:
#   num1 = int(input("enter first number:  "))
#   num2 = int(input("enter second number:  "))
# except:
#     print("----------------cant divide by string--------")

try:
  num1 = int(input("enter first number:  "))
  num2 = int(input("enter second number:  "))
  print(num1/num2)
except ZeroDivisionError:
  print("----------------cant divide a number by zero--------")
except ValueError:
   print("----------------cant divide by string--------") 
else:
  print("-------------------no exception---------------")  
finally:
  print("-------------------prg completed---------------") 

# print("program completed")