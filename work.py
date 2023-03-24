
pscore =0
def main():
  print('''welcome to online Examination 
     choose one option..
     1.puthon
     2.angular
     3.java''')
  global choice 
  choice =int(input("enter your choice ")) 
  # return choice
  if choice == 1:
    print("welcome to python ")
    python1()
  elif choice == 2:
    print("welcome to angular ")

  elif choice == 3:
    print("welcome to java ")

  else:
    print("invalid choice")
    main()  
    



def python1():
   print(''' welcome to python examination

1 .What is the maximum length of a Python identifier?
     a .32
     b.16
     c.128
     d.No fixed length is specified 
     ''') 
   
   course_choice = input("pick correct answer ")
   print()
   if(course_choice =='d'):
    print("correct choice")
    global pscore
    pscore += 1
    python2()    
   
   elif(course_choice =='a' or course_choice =='b' or course_choice =='c' ):
     print("wrong choice")
     print()
     python2()
     
   else:
    print("invalid choice")
    print()
    python1()

def python2():
   print(''' welcome to python examination

2 .How is a code block indicated in Python?
     a.Brackets
     b.Indetation
     c.key
     d.Non of the above 
     ''') 
   
   course_choice = input("pick correct answer ")
   if(course_choice =='b'):
       print("correct choice")
       global pscore
       pscore += 1 
       python3()
   elif(course_choice =='a' or course_choice =='c' or course_choice =='d' ):
        print("wrong choice")
        print() 
        python3() 
   else:
        print("invalid choice")
        print()
        python2()
   
def python3():
   print(''' welcome to python examination

3 .Which of the following concepts is not a part of Python?
     a.Pointers
     b.Loop
     c.Dynamic typing
     d.All of the above 
     ''') 
   
   course_choice = input("pick correct answer ")
   if(course_choice =='a'):
       print("correct choice")
       global pscore
       pscore += 1 
       main()

   elif(course_choice =='b' or course_choice =='c' or course_choice =='d' ):
        print("wrong choice")
        print() 
        main()
   else:
        print("invalid choice")
        print()
        python3() 

main() 
print(pscore)






