

def primenumber(number):
  status = 0
  for i in range(2,number):
    if number % i == 0:
      
      status += 1
      
    else:
      status += 0
  
  if status == 0:
    print("number is  prime")
  else:
    print("number is  not prime")  



  









number = int(input("Enter a number "))

primenumber(number)
