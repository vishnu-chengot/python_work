# class area():
  #  def area(self,radius):
  #     return 3.14*radius*radius

  #  def area(self,l,b):
  #    return l*b

# area1 = area()

# print(area1.area(20,30))

class area():
   def area(self,r = 0,l = 0,b = 0):
     if(r!=0):
        return 3.14*r*r
     else: 
        return l*b  
    
area1 = area()

print(area1.area(r=30))

print(area1.area(l=2,b=2))