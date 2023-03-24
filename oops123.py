class department():
    def __init__(self,dptname,dptid,dpthead):
       self.dptname = dptname
       self.dptid = dptid
       self.dpthead = dpthead

    def department_details(self):
       print(self.dptname,self.dptid,self.dpthead)   
      
class student(department):
   def __init__(self,stdname,stdid,stdemail,dptname,dptid,dpthead):
       department.__init__(self,dptname,dptid,dpthead)
       self.stdname = stdname
       self.stdid = stdid
       self.stdemail =stdemail
    
   def student_setails(self):
      print(self.stdname,self.stdid,self.stdemail,self.dptname,self.dptid,self.dpthead)

student1 = student('revathi',1,'revathigopi@gmail','elctronics',3,'biju')

student1.department_details()

student1.student_setails()

     