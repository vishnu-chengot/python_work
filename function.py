# def student(name,age,gender):

#    print("your name is :",name)
#    print("your age is  ",age)
#    print("your gender is:",gender)


# student("vishnu",20,"male")
# student(gender="female",name="revathi",age=22)

def student(**kwargs):
  for i in kwargs:
    print(i,'is',kwargs[i])

# student(gender="female",name="revathi",age=22)
student(gender="female",name="revathi",age=22,qualification="bsc",place="palakad")
