# def add(num1,num2=0): #required(num1) follwed by defalut(num2=0)
#    print(num1+num2)


# add(10,20)


def add(*args):
  sum = 0
  for i in args:
    sum +=i
    
    
    
  print(sum)

add(10,20,30,3)  