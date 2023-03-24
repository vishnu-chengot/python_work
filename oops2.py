class products():
  def __init__(self,name,ifsc,amount,password):
    self.__amount = 0
    self.name = name
    self.ifsc = ifsc
    self.set_amount(amount)
    self.password = password

  def get_amount(self):
    if(self.password == 1234):
      return self.__amount
    else:
      return "invalid"

  def set_amount(self,amt):
    if(amt > 0):
     self.__amount += amt
    else:
     self.__amount += 0  
         



p2 = products('vishnu','ifsc',2000,1234)

print(p2.get_amount())
p2.set_amount(2000)
print(p2.get_amount())